# This experiment will explore the use of:
# BeautifulSoup & lxml libraries for HTML/XML Parsing
# urllib for making HTTP Requests
import wikipedia
import re
from collections import Counter

class WikiScrape(object):
    def __init__(self, page_title):
        self.content = wikipedia.page(page_title).references

    def get_references(self):
        return self.references

    def get_words(self):
        return re.findall("[a-zA-Z]+", self.content)

    def get_word_count(self):
        content_word_list = self.get_words()
        return Counter(content_word_list)

print WikiScrape("Cancer")
