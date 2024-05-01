import requests
from bs4 import BeautifulSoup

search_query = 'Samsung S2'
url = 'https://www.ebay.com/{search_query}'
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    listings = soup.find_all('div', class_='s-item')

    for listing in listings:
        title_element = listing.find('h3', class_='s-item__title')
        if title_element:
            title = title_element.text.strip()
            print('Title:', title)

        price_element = listing.find('span', class_='s-item__price')
        if price_element:
            price = price_element.text.strip()
            print('Price:', price)

        link_element = listing.find('a', class_='s-item__link')
        if link_element:
            link = link_element['href']
            print('Link:', link)

        print('---')
else:
    print('Failed to retrieve eBay search results.')
