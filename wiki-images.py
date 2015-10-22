# This experiment will explore the use of:
# BeautifulSoup & lxml libraries for HTML/XML Parsing
# urllib for making HTTP Requests

from bs4 import BeautifulSoup
from urllib import urlopen
import wikipedia
import re
# <div class="reflist columns references-column-count references-column-count-2">
#
# class WikiScrape(object):
#     def __init__(self, page_title):
#         self.content = wikipedia.page(page_title).content
#
#     def get_content(self):
#         return self.content
#
#     def get_words(self):
#         return re.findall("[a-zA-Z]+", self.content)
#
# print WikiScrape("Cancer").get_word_count()


# BASE_URL = "https://en.wikipedia.org/wiki/Cancer"
#
# def make_soup(url):
#     html = urlopen(url.read())
#     return BeautifulSoup(html, "lxml")
#
# def get_notes_images(section_url):
#     html = urlopen(section_url).read()
#     soup = make_soup(section_url)
#     notes_images = soup.find # need to identify anchor tags for each external text
#     # pseudo code placeholder for assigning notes_image_links
#     # notes_image_links = [ BASE_URL + {li.a["rel"], class="external text", a.["href"]} ]
#     return notes_image_links
