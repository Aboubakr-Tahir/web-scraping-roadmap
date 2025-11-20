import requests
import json
import time


URL = 'https://21ogkm5th5-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.17.0)%3B%20Browser'


HEADERS = {
    
    'x-algolia-api-key': 'dc91173a4a5d669a3eef474e5836e94f',
    'x-algolia-application-id': '21OGKM5TH5',
    
    
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    
    
    'Origin': 'https://www.sunglasshut.com',
    'Referer': 'https://www.sunglasshut.com/',
}

PAYLOAD_JSON = {
    "requests": [
        {
            "hitsPerPage": 25,
            "indexName": "prod_live_sgh_en-us__ungrouped",
            "facetFilters": ["x_groupkey: RB2140 Original Wayfarer Classic_RB2140_SUN_"],
            "numericFilters": [[], []],
            "ruleContexts": ["SAFEBRANDSEARCH", "SAFEBRANDSEARCH"],
            "clickAnalytics": True,
            "query": "Ray-Ban",
            "explain": True,
            "userToken": "anonymous-25b17421-d1f2-49dc-b617-2cb0c905c1ab",
            "params": ""
        }
    ]
}



try:
    print("Envoi de la requête API Algolia...")
    
   
    response = requests.post(URL, headers=HEADERS, json=PAYLOAD_JSON, timeout=30)
    
   
    response.raise_for_status() 
    
    
    data = response.json() 
    
    
    output_filename = 'sunglass_data.json'
    with open(output_filename, 'w', encoding='utf-8') as f:
        
        json.dump(data, f, ensure_ascii=False, indent=4)
        
    print("Succès ! La requête a fonctionné.")
    print(f"Données stockées dans {output_filename}")
    
    
    first_hit = data['results'][0]['hits'][0]
    print(f"Vérification : Produit trouvé = {first_hit['parentProductId']}")
    print(f"Prix : {first_hit['prices']['LISTPRICE']['offerPrice']} {first_hit['prices']['LISTPRICE']['currency']}")
    
except requests.exceptions.RequestException as e:
    print(f"Erreur fatale lors de la requête : {e}")