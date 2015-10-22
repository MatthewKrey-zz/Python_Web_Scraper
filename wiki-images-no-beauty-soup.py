# This experiment will explore web scraping images via reference links
# from a Wikipedia page Notes section w/o BeautifulSoup & w/ Regular Expressions

import urllib2
from urllib2 import urlopen
import re
import cookielib, urllib2
from cookielib import CookieJar
import datetime

global wiki_references
wiki_references = [
"http://www.who.int/mediacentre/factsheets/fs297/en/",
"http://www.cancer.gov/cancertopics/cancerlibrary/what-is-cancer",
"http://www.nhs.uk/Conditions/Cancer/Pages/Symptoms.aspx",
"http://www.cancer.gov/about-cancer/causes-prevention/risk/obesity/obesity-fact-sheet#q3",
"http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2515569",
                ]


cj = CookieJar() # in case site requires storage of cookies
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent'), 'Mozilla/5.0'] # do not visit as robot

for reference in wiki_references:


#
# def main():
#     try:
#         page = "https://en.wikipedia.org/wiki/Cancer"
#         sourceCode = opener.open(page).read()
#
#         try:
#
#         except Exception, e:
#             print str(e)
#
#     except Exception, e:
#         print str(e)
#
# main()
