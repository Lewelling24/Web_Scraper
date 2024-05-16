import requests

from bs4 import BeautifulSoup

import pandas as pd

import time

url = "https://www.imdb.com/chart/top"

response = requests.get(url)

print (response)

parse = BeautifulSoup(response.content, 'html.parser')

print(parse)

# extract info
movies = []

for row in parse.select('tbody.lister-list tr'):
    title = row.find('td', class_='titleColumn').find('a').get_text()
    year = row.find('td', class_='titleColumn').find('span', class_='secondaryInfo').get_text()[1:-1]
    rating = row.find('td', class_='ratingColumn imdbRating').find('strong').get_text()
    movies.append([title, year, rating])

print(movies)
