from urllib.request import urlopen

# just getting started
url = urlopen("https://www.imdb.com")

html_bytes = url.read()

html = html_bytes.decode("utf-8")

print(html)