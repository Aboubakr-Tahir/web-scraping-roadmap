import os
import requests
from urllib.parse import urlparse, urljoin 
from bs4 import BeautifulSoup

downloadDirectory = 'images'
baseUrl = 'https://en.wikipedia.org/wiki/Kevin_Bacon'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

def getAbsoluteURL(baseUrl, source):
    """
    Construit une URL absolue et propre.
    Ne télécharge que les fichiers du même domaine.
    """
    url = urljoin(baseUrl, source)
    
    parsed_url = urlparse(url)
    base_domain = urlparse(baseUrl).netloc
    
    if parsed_url.netloc != base_domain:
        return None
    return url

def getSafeDownloadPath(downloadDirectory, fileUrl):
    """
    Crée un chemin de sauvegarde "plat" et sécurisé.
    Empêche les attaques de "directory traversal".
    """
    path = urlparse(fileUrl).path
    
    filename = os.path.basename(path)

    if not os.path.exists(downloadDirectory):
        os.makedirs(downloadDirectory)
    
    return os.path.join(downloadDirectory, filename)

try:
    response = requests.get(baseUrl, headers=headers, timeout=10)
    response.raise_for_status()
    bs = BeautifulSoup(response.text, 'lxml')

    downloadList = bs.find_all('img')

    print(f"Trouvé {len(downloadList)} images...")

    for download in downloadList:
        source = download.get('src')
        if not source:
            continue  

        fileUrl = getAbsoluteURL(baseUrl, source)
        
        if fileUrl is not None:
            print(f"Téléchargement de : {fileUrl}")
            
            try:
                image_response = requests.get(fileUrl, headers=headers, timeout=10)
                image_response.raise_for_status()
                
                savePath = getSafeDownloadPath(downloadDirectory, fileUrl)
                
               
                with open(savePath, 'wb') as f:
                    f.write(image_response.content)
            
            except requests.exceptions.RequestException as e:
                print(f"  -> Échec du téléchargement : {e}")

    print("Téléchargement terminé.")

except requests.exceptions.RequestException as e:
    print(f"Erreur : Impossible de charger la page de base {baseUrl}. {e}")