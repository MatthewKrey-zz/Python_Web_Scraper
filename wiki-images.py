# This experiment will explore the use of:
# BeautifulSoup & lxml libraries for HTML/XML Parsing
# urllib for making HTTP Requests

import urlparse
import urllib
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Cancer"

urls = [url] # stack of urls to scrape
visited = [url] # "historic" record of urls

while len(urls) > 0:
    try:
        htmltext = urllib.urlopen(urls[0].read())
    except:
        print urls[0]
    soup = BeautifulSoup(url)

    urls.pop(0)

    print soup.findAll('a', href=True)
