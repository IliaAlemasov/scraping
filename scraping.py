import time

import requests
from bs4 import BeautifulSoup
import lxml

for count in range(1,8):

    time.sleep(0.15)

    url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'

    responce = requests.get(url)

    soup = BeautifulSoup(responce.text, "lxml")

    data = soup.find_all('div', class_ = 'col-lg-4 col-md-6 mb-4')

    for card in data:

        name = card.find('h4', class_ ='card-title').text.replace('\n', '')

        price = card.find('h5').text

        url_img = 'https://scrapingclub.com' + card.find('img', class_ = 'card-img-top img-fluid').get('src')

        print(name + "\n" + price + '\n' + url_img)

        time.sleep(.3)





