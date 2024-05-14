import requests

from bs4 import BeautifulSoup

import pandas as pd

import time

url = "https://imbd.com"

response = requests.get(url)

parse = BeautifulSoup(response.content, 'html.parser')

print(parse)
