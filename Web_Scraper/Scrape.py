import requests

from bs4 import BeautifulSoup


def scrape(url):
    response = requests.get(url)
    parse = BeautifulSoup(response.content, 'html.parser')
    # extract info
    movies = []

    
    














