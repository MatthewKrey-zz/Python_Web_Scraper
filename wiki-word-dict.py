# This solution will explore the use of:
# BeautifulSoup & lxml libraries for HTML/XML Parsing
# urllib & requests for making HTTP Requests
# bleach for HTML validation & removing unwanted elements

# make this a WikiScraper class for scaling to scrape other wiki pages

from bs4 import BeautifulSoup
from urllib import urlopen
import bleach


BASE_URL = "https://en.wikipedia.org/wiki/Cancer"

def make_soup(BASE_URL):
    html = urlopen(BASE_URL).read()
    return BeautifulSoup(html, "lxml")

def get_body_content(BASE_URL):
    soup = make_soup(BASE_URL)
    body_content = soup.find("div", {"id": "bodyContent"})
    return body_content

get_body_content(BASE_URL)
