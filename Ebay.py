from bs4 import BeautifulSoup
import requests

search_query = 'Samsung S21'
url = "https://www.ebay.com/{search_query}"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    listings = soup.find_all('div', class_= 's-item' )
    
    for listings in soup.find_all("article"):
        print(listings.text.strip())
        

    
    
