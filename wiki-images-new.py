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

for reference in wiki_references:

    # a place to store the links we find
    links = []

    r = requests.get(reference)
    soup = BeautifulSoup(page)
    for link in soup.findAll('a', href=True):
        # skip useless links
        if link['href'] == '' or link['href'].startswith('#'):
            continue
        # initialize the link
        thisLink = {
            'url': link['href'],
            'title': link.string,
            'image': '',
        }
        # see if the link contains an image
        img = link.find('img', src=True)
        if img:
            thisLink['image'] = img['src']
            if thisLink['title'] is None:
                # look for a title here if none exists
                if 'title' in img:
                    thisLink['title'] = img['title']
                elif 'alt' in img:
                    thisLink['title'] = img['alt']
                else:
                    thisLink['title'] = path.basename(img['src'])

        if thisLink['title'] is None:
            # check for text inside the link
            if len(link.contents):
                thisLink['title'] = ' '.join(link.stripped_strings)
        if thisLink['title'] is None:
            # if there's *still* no title (empty tag), skip it
            continue
        # convert to something immutable for storage
        hashableLink = (thisLink['url'].strip(),
                        thisLink['title'].strip(),
                        thisLink['image'].strip())
        # store the result
        if hashableLink not in links:
            links.append(hashableLink)

    # print the results
    for link in links:
        stdout.write('\t'.join(link) + '\n')
