import pymysql 
import requests 
import re 
import time 
from bs4 import BeautifulSoup
import sys 

headers = {'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 9; VIA_P3 Build/PPR1.180610.011)'}
pages = set()
timeout= 30
start = time.time()
conn = pymysql.connect(host='127.0.0.1',
user='root', passwd="my-secret-pw", db='scraping' ,  charset='utf8')
cur = conn.cursor()


def store(title , content) : 
    cur.execute("INSERT INTO pages (title , content) VALUES (%s , %s)" , (title , content))
    cur.connection.commit()
    print("commited succefully")
    
    
def getLinks(Url) : 
  try : 
    global pages
    global start
    global timeout
    if time.time() - start > timeout : 
      print("force script Stopping.")
      sys.exit()
    full_Url="https://en.wikipedia.org{}".format(Url)
    response = requests.get(full_Url , headers=headers) 
    bs = BeautifulSoup(response.text , "lxml") 
    title = bs.h1.get_text() 
    paragraphs = bs.find("div",{"id":"mw-content-text"}).find_all("p")
    for p in paragraphs : 
      if p.attrs.get("class") != ["mw-empty-elt"] : 
        content = p.get_text()
        store(title=title , content=content)
        break   
    print("-"*20)   
    for link in bs.find('div',{'id':'bodyContent'}).find_all("a",{"href":re.compile(r"^(/wiki/)[^\:]*$")}) : 
      if link.attrs.get('href') is not None : 
        if link.attrs.get('href') not in pages : 
          newLink = link.attrs.get('href') 
          print(f"new link found : {newLink}") 
          pages.add(newLink) 
          getLinks(newLink) 
    return pages      
  except requests.exceptions.HTTPError as e:
    print(f"Error: {e}")   
    
try : 
    links = getLinks('/wiki/Kevin_Bacon')
finally :     
    cur.close()
    conn.close()