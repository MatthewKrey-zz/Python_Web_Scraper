# This solution will explore the use of:
# BeautifulSoup & lxml libraries for HTML/XML Parsing
# urllib for making HTTP Requests

from bs4 import BeautifulSoup
from urllib import urlopen

# make this WikiImageScraper class for scaling to scrape other wiki pages

BASE_URL = "https://en.wikipedia.org/wiki/Cancer"

def make_soup(url):
    html = urlopen(url.read())
    return BeautifulSoup(html, "lxml")

def get_notes_images(section_url):
    html = urlopen(section_url).read()
    soup = make_soup(section_url)
    notes_images = soup.find("div", {"id": "bodyContent"}) # need to identify anchor tags for each external text
    # pseudo code placeholder for assigning notes_image_links
    # notes_image_links = [ BASE_URL + {li.a["rel"], class="external text", a.["href"]} ]
    return notes_image_links

# get_notes_images(section_url)
