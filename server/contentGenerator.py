import ssl
import urllib.request as urllib
from bs4 import BeautifulSoup as bs
import re
import os

from db import db
from searchEngine import searchEngine

WIKI_URL = 'https://en.wikipedia.org'
WIKI_URI = '/wiki/'

class page:
    def __init__(self, link, words=[]):
        self.link = link
        self.words = words

class crawler:
    def __init__(self, wordList={}, db=db()):
        self.wordList = wordList
        self.db = db
        self.search = searchEngine(db=self.db)

    def indexPages(self, dirs=[]):
        filenames = []
        for dirName in dirs:
            linkNames = self.getAllFiles(dir=dirName)

            if linkNames != None:
                filenames = filenames + linkNames

        for filename in filenames:
            with open(filename) as f:
                # TODO: fix this link name issue, get only filename not path
                link = WIKI_URI + filename
                p = page(link, words=[])
                self.db.begin()
                self.db.savePage(p)

                for words in f:
                    words = words.split(' ')
                    for i in range(len(words)):
                        wordid = self.search.getIdForWord(words[i])
                        self.db.saveLocation(p, wordid, i)
                
                self.db.commit()
        
        self.db.closeDb()

    def updatePagesWithPageRank(self, dirs=[], max_iterations=20):
        pages = self.db.getPages()
        filenames = []
        for dirName in dirs:
            linkNames = self.getAllFiles(dir=dirName)

            if linkNames != None:
                filenames = filenames + linkNames

        for filename in filenames:
            filenameKey = filename.split('/')[3]
            filenameKey = WIKI_URI + filenameKey
            page = pages[filenameKey]
            page.links = []

            with open(filename) as f:
                for link in f:
                    page.links.append(link.rstrip())

        for i in range(max_iterations):
            self.db.begin()

            for link in pages:
                p = pages[link]
                self.iteratePR(p, pages)
                self.db.updatePageRank(p)

            self.db.commit()

        self.db.closeDb()

        return pages

                # self.db.commit()

        # self.db.closeDb()

    def iteratePR(self, p, pages):
        pr = 0.0
        for link in pages:
            po = pages[link]
            if (po.hasLinkTo(p.link)):
                pr += po.pageRank / len(po.links)
        p.pageRank = 0.85 * pr + 0.15


    def getAllFiles(self, dir=''):
        dirs = os.listdir(dir)
        for i in range(len(dirs)):
            dirs[i] = dir + '/' + dirs[i]
        return dirs





    # Method for crawling new links
    # Not currently used
    # def crawl(self, filename):
    #     with open(filename) as f:
    #         for link in f:
    #             try:
    #                 url = WIKI_URL + link
    #                 p = page(url, words={})

    #                 # Temp solution to avoid SSL errors
    #                 req = urllib.Request(url, headers={'X-Mashape-Key': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'})
    #                 gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    #                 c = urllib.urlopen(url, context=gcontext).read()
    #                 soup = bs(c, 'html.parser')

    #                 text = getTextOnly(soup)
    #                 words = separateWords(text)

    #                 for word in words:
    #                     p.getIdForWord(word)

    #                 saveToDb(p)
    #             except:
    #                 print('Url fetching error')
    #                 continue


# Not used soup and word extractors
# def getTextOnly(soup):
#     el = soup.string
#     if el == None:
#         content = soup.contents
#         result = ''
#         for text in content:
#             subtext = getTextOnly(text)
#             result += subtext + '\n'
#         return result
#     else:
#         return el.strip()

# def separateWords(text):
#     splitter = re.compile('\\W+')
#     return [s.lower() for s in splitter.split(text) if s!= '' and isDigitNotYear(s) == False]

# # To ignore digits, but accept years (yyyy)
# def isDigitNotYear(val):
#     if (val.isdigit()):
#         # Check if year 1 - 3000
#         match = re.match(r'([1-2][0-9]{3}|3000)\b', val)
#         if match: return False
#         else: return True
#     else:
#         return False

# crawler().indexPages(dirs=['wikipedia/Words/Games','wikipedia/Words/Programming'])
crawler().updatePagesWithPageRank(dirs=['wikipedia/Links/Games','wikipedia/Links/Programming'])
