# This solution will explore the use of:
# BeautifulSoup & lxml libraries for HTML/XML Parsing
# urllib for making HTTP Requests
# bleach for HTML validation & removing unnecessary elements

# make this a WikiScraper class for scaling to scrape other wiki pages

from bs4 import BeautifulSoup
from urllib import urlopen
#import bleach   # ipynb explodes here


BASE_URL = "https://en.wikipedia.org/wiki/Cancer"

def make_soup(BASE_URL):
    html = urlopen(BASE_URL).read()
    return BeautifulSoup(html, "lxml")

def get_body_content(BASE_URL):
    soup = make_soup(BASE_URL)
    body_content = soup.find_all("div", {"id": "bodyContent"}) # returns collection of HTML tag objects
    body_content_words = {}
    for word in body_content_words:
        print body_content_words[word.get_text()]

#def _bleach_html(BASE_URL)

get_body_content(BASE_URL)
