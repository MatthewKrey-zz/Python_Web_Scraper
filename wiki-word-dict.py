# This solution will explore a quick & dirty Wiki page scrape
# with the Wikipedia Python library, regular expressions & Pandas

import wikipedia
import re
from collections import Counter
import pandas as pd
from pandas import DataFrame
import csv


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


class WikiDataFrame(object):
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def dict_to_dataframe(self):
        df = pd.DataFrame(self.dictionary.items(), columns=['Word', 'Word_Count'])
        wiki_words_df = df.sort(columns="Word_Count", ascending=False)
        return wiki_words_df


wiki_word_dictionary = WikiScrape("Cancer").get_word_count()
print WikiDataFrame(wiki_word_dictionary).dict_to_dataframe().to_csv('wiki_word_dictionary.csv', sep=':', index=False, index_label=None)
