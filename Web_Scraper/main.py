import requests

from bs4 import BeautifulSoup

import pandas as pd

import time

url = "https://www.imdb.com/chart/top"

response = requests.get(url)

parse = BeautifulSoup(response.content, 'html.parser')

# extract info
movies = []

for row in parse.select('tbody.lister-list tr'):
    title = row.find('td', class_='titleColumn').find('a').get_text()
print(parse)
