# This solution will explore the use of:
# BeautifulSoup & lxml libraries for HTML/XML Parsing
# urllib for making HTTP Requests

from bs4 import BeautifulSoup
from urllib import urlopen

# make this WikiScraper class for scaling to scrape other wiki pages

BASE_URL = "https://en.wikipedia.org/wiki/Cancer"

def get_body_content(section_url):
    html = urlopen(section_url).read()
    soup = BeautifulSoup(html, "lxml")
    body_content = soup.find("div", {"id": "bodyContent"})
    #category_links = [BASE_URL + ]
