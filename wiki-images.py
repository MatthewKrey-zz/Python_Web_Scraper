# This experiment will explore the use of:
# BeautifulSoup & lxml libraries for HTML/XML Parsing
# urllib for making HTTP Requests

from bs4 import BeautifulSoup
import requests
import urllib2
from urllib2 import urlopen
import re
import cookielib, urllib2
from cookielib import CookieJar
import datetime

BASE_URL = "https://en.wikipedia.org/wiki/Cancer"

def make_soup(BASE_URL):
    html = urlopen(BASE_URL).read()
    return BeautifulSoup(html, "lxml")

def get_notes_images(BASE_URL):
    soup = make_soup(BASE_URL)
    references = soup.findAll("ol", "references")
    return references

def main():
    try:
        page = get_notes_images(BASE_URL)

        try:
            links = re.findall(r'<a.*?href="(.*?)"', s, page)
            for link in links:
                print link

        except Exception, e:
            print str(e)

    except Exception, e:
        print str(e)

main()
