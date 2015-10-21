# This experiment will explore scraping the words from a Wikipedia article's
# content section without BeautifulSoup & using Regular Expressions

# make this a WikiScraper class for scaling to scrape other wiki pages

import urllib2
from urllib2 import urlopen
import re
import cookielib, urllib2           # if site requires us to store cookies 
from cookielib import CookieJar
import datetime
