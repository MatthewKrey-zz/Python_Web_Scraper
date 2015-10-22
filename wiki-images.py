# This experiment will explores the use of a page spider algorithm

import urlparse
import urllib
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Cancer"

urls = [url] # stack of urls to scrape
visited = [url] # "historic" record of urls

def make_soup(BASE_URL):
    html = urllib.urlopen(BASE_URL).read()
    return BeautifulSoup(html, "lxml")

while len(urls) > 0:
    try:
        htmltext = urllib.urlopen(urls[0].read())
    except:
        print urls[0]
    soup = make_soup(url)

    urls.pop(0)
    print len(urls)

    for tag in soup.findAll('a', href=True):
        tag['href'] = urlparse.urljoin(url, tag['href'])
        if url in tag['href'] and tag['href'] not in visited:
            urls.append(tag['href'])
            visited.append(tag['href'])

print visited
