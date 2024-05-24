import requests

from bs4 import BeautifulSoup

import pandas as pd

import time

url = "https://www.imdb.com/chart/top"

#transfer into function

def scrape(url):
    response = requests.get(url)
    parse = BeautifulSoup(response.content, 'html.parser')
    # extract info
    movies = []

    for row in parse.select('tbody.lister-list tr'):
        title = row.find('td', class_='titleColumn').find('a').get_text()
        year = row.find('td', class_='titleColumn').find('span', class_='secondaryInfo').get_text()[1:-1]
        rating = row.find('td', class_='ratingColumn imdbRating').find('strong').get_text()
        movies.append([title, year, rating])

    
    return movies    
    # Add a delay between requests to avoid overwhelming the website with requests
    


def store(movies):
# Store the information in a pandas dataframe
    df = pd.DataFrame(movies, columns=['Title', 'Year', 'Rating'])
    df.to_csv('top-rated-movies.csv', index=False)

    
time.sleep(1)









