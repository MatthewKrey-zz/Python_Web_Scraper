# This experiment will explore the use of:
# BeautifulSoup & lxml libraries for HTML/XML Parsing
# urllib for making HTTP Requests
from os import path
from sys import stdout
import codecs
from bs4 import BeautifulSoup
import requests
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

streamWriter = codecs.lookup('utf-8')[-1]
stdout = streamWriter(stdout)

cj = CookieJar() # in case site requires storage of cookies
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent'), 'Mozilla/5.0'] # do not visit as robot

def main():
    try:
        for reference in wiki_references:
            page = reference
            sourceCode = opener.open(page).read()
            print sourceCode

    #     try:
    #         titles = re.findall(r'',sourceCode)
    #         links = re.findall(r'(.*?)',sourceCode)
    #
    #         for link in links:
    #             print link
    #     except Exception, e:
    #         print str(e)
    #
    except Exception,e:
        print str(e)
        pass

main()
