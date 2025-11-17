import csv 
import requests 
from bs4 import BeautifulSoup 

url = "https://en.wikipedia.org/wiki/Comparison_of_text_editors"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

try: 
    response = requests.get(url , headers=headers) 
    response.raise_for_status() 
    bs = BeautifulSoup(response.text , "lxml")
    
    table = bs.find("table" , class_="wikitable")
    
    rows = table.find_all("tr") 

    with open("editors.csv", "w", encoding="utf-8", newline='') as csvFile:
        writer = csv.writer(csvFile)
        
        for row in rows: 
            csvRow = []
            
            
            for cell in row.find_all(['th', 'td']): 
                
               
                csvRow.append(cell.get_text(strip=True))
            
            
            writer.writerow(csvRow)
            
    print("Succès ! Le fichier 'editors.csv' a été créé.")
    
   

except requests.exceptions.HTTPError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Une erreur est survenue : {e}")