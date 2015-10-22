# This solution will explore a quick & dirty wiki page scrape
# with the Wikipedia Python library & regular expressions

import wikipedia
import re
from collections import Counter

class WikiScrape(object):
    def __init__(self, page_title):
        self.content = wikipedia.page(page_title).content

    def get_content(self):
        return self.content

    def get_words(self):
        return re.findall("[a-zA-Z]+", self.content)

    def get_word_count(self):
        content_word_list = self.get_words()
        return Counter(content_word_list)

print WikiScrape("Cancer").get_word_count()
