# This solution will explore a quick & dirty wiki page scrape w/ the Wikipedia Python library

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


#WikiScrape("Cancer").get_content()
#Counter(WikiScrape("Cancer").get_words())
print WikiScrape("Cancer").get_word_count()
