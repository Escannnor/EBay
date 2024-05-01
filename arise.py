import requests
from bs4 import BeautifulSoup

base = 'https://www.arise.tv/category/sports/page/'
n = range(1, 4)
for num in n:
    url = f'{base}{num}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for data in soup.find_all('article'):
        print(data.text.strip())
        head = data.find('h3')
        print(head)
        image = data.find('img')
        if image:
            img = image.get('src')
            print(img)
        href = data.find('a')
        if href:
            url = href.get('href')
            print(url)
    
        print('\n')