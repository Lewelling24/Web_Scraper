#make use of scrape.py
from Scrape import *
import time


url = "https://www.imdb.com/chart/top"

store_var = scrape(url)

print(store_var)