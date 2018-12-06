import ssl
import urllib.request as urllib
from bs4 import BeautifulSoup as bs
import re
import os

from db import saveToDb, closeDb

WIKI_URL = 'https://en.wikipedia.org'
WIKI_URI = '/wiki/'

class page:
    def __init__(self, link, words={}):
        self.link = link
        self.words = words

    def getIdForWord(self, word):
        if (self.containsWord(word)):
            return list(self.words.keys())[list(self.words.values()).index(word)]
        else:
            id = len(self.words)
            self.words[id] = word
            return id

    def containsWord(self, word):
        return word in self.words.values()

class crawler:
    def __init__(self, pageList=[]):
        self.pageList = pageList

    def setPages(self, dirs=[]):
        filenames = []
        for dirName in dirs:
            linkNames = self.getAllFiles(dir=dirName)

            if linkNames != None:
                filenames = filenames + linkNames

        for filename in filenames:
            with open(filename) as f:
                link = WIKI_URI + filename
                p = page(link, words={})
                for words in f:
                    words = words.split(' ')
                    for word in words:
                        p.getIdForWord(word)
                
                saveToDb(p)

        closeDb()

    def getAllFiles(self, dir=''):
        dirs = os.listdir(dir)
        for i in range(len(dirs)):
            dirs[i] = dir + '/' + dirs[i]
        return dirs


    # Method for crawling new links
    def crawl(self, filename):
        with open(filename) as f:
            for link in f:
                try:
                    url = WIKI_URL + link
                    p = page(url, words={})

                    # Temp solution to avoid SSL errors
                    req = urllib.Request(url, headers={'X-Mashape-Key': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'})
                    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
                    c = urllib.urlopen(url, context=gcontext).read()
                    soup = bs(c, 'html.parser')

                    text = getTextOnly(soup)
                    words = separateWords(text)

                    for word in words:
                        p.getIdForWord(word)

                    saveToDb(p)
                except:
                    print('Url fetching error')
                    continue


def getTextOnly(soup):
    el = soup.string
    if el == None:
        content = soup.contents
        result = ''
        for text in content:
            subtext = getTextOnly(text)
            result += subtext + '\n'
        return result
    else:
        return el.strip()

def separateWords(text):
    splitter = re.compile('\\W+')
    return [s.lower() for s in splitter.split(text) if s!= '' and isDigitNotYear(s) == False]

# To ignore digits, but accept years (yyyy)
def isDigitNotYear(val):
    if (val.isdigit()):
        # Check if year 1 - 3000
        match = re.match(r'([1-2][0-9]{3}|3000)\b', val)
        if match: return False
        else: return True
    else:
        return False

crawler().setPages(dirs=['wikipedia/Words/Games','wikipedia/Words/Programming'])
