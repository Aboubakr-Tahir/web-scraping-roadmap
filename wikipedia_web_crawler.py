import requests
from bs4 import BeautifulSoup
import re 
import time 
import sys 
headers = {'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 9; VIA_P3 Build/PPR1.180610.011)'}
pages = set()
timeout= 30
start = time.time()
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
    print(f"title of this link : {title}")
    paragraphs = bs.find("div",{"id":"mw-content-text"}).find_all("p")
    for p in paragraphs : 
      if p.attrs.get("class") != ["mw-empty-elt"] : 
        print(f"paragraph of this link : {p.get_text()}")
        break  
    try : 
      edit_link=bs.find("a", {"id": "ca-edit"}).attrs.get("href")
      print(f"edit link found : {edit_link}")
    except AttributeError as e:
      print("no edit link found")   
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
links = getLinks("/wiki/Main_Page")
print(links)