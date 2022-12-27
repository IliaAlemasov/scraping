import requests
from bs4 import BeautifulSoup
import lxml

url = 'https://scrapingclub.com/exercise/list_basic/?page=1'

responce = requests.get(url)

soup = BeautifulSoup(responce.text, "lxml")

data = soup.find('div', class_ = 'col-lg-4 col-md-6 mb-4')

name = data.find('h4', class_ = 'card-title').text.replace('\n', '')

price = 





