# This experiment will explores the use of a page spider algorithm

import urlparse
import urllib
import re
from bs4 import BeautifulSoup
from IPython import embed

BASE_URL = "http://www.surfline.com/home/index.cfm"

def make_soup(BASE_URL):
    html = urllib.urlopen(BASE_URL).read()
    return BeautifulSoup(html, "lxml")

def get_image_links(BASE_URL):
    soup = make_soup(BASE_URL)
    anchor_tags = soup.select('a[href^="http"]')
    hrefs = []
    for link in anchor_tags:
        hrefs.append(link.get("href"))
    external_images = []
    i = 0
    for site in hrefs:
        try:
            external_soup = make_soup(site)
            external_image = external_soup.img.get('src')
            urllib.urlretrieve(site + external_image, "Output/downloaded_image" + str(i) + re.findall('\.jpg$|\.jpeg$|\.png$|\.gif$', external_image)[0])
            external_images.append(external_image)
            i += 1
        except(IOError, AttributeError, TypeError, IndexError):
            continue
    return external_images

print get_image_links(BASE_URL)
