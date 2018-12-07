import sqlite3
conn = sqlite3.connect('page.db')
c = conn.cursor()

class page:
    def __init__(self, link, wordlocations=[]):
        self.link = link
        self.wordlocations = wordlocations

class db:
    def __init__(self, db='page.db'):
        self.conn = sqlite3.connect('page.db')
        self.cursor = self.conn.cursor()

    def begin(self):
        self.cursor.execute('BEGIN TRANSACTION') 

    def getWordId(self, word):
        self.cursor.execute('SELECT wordid FROM words where word = ?', (word,))
        return self.cursor.fetchone()

    def getMaxId(self):
        self.cursor.execute('SELECT COUNT(*) FROM words')
        result = self.cursor.fetchone()
        return result

    def getPages(self):
        self.cursor.execute('SELECT * from (SELECT p.url,w.wordid,w.location FROM pages AS p JOIN wordlocation AS w ON w.url = p.url)')
        pages = self.cursor.fetchone()
        return pages

    def getFrequencyScore(self, page, wordid):
        self.cursor.execute('SELECT count(*) FROM wordlocation where url = ? AND wordid = ?', (page.link,wordid))
        return self.cursor.fetchone()

    def getLocationScore(self, page, wordid):
        self.cursor.execute('SELECT MIN(location) FROM wordlocation where url = ? AND wordid = ?', (page.link,wordid))
        return self.cursor.fetchone()

    def saveWord(self, wordid, word):
        self.cursor.execute('INSERT OR REPLACE INTO words (wordid, word) VALUES (?, ?);', (wordid, word))

    def savePage(self, page):
        url = page.link
        self.cursor.execute(f"INSERT OR REPLACE INTO pages (url) VALUES ('{url}');")

    def saveLocation(self, page, wordid, location):
        url = page.link
        self.cursor.execute(f"INSERT INTO wordlocation (url, wordid, location) VALUES (?, ?, ?)", (url, wordid, location))

    def commit(self):
        self.cursor.execute('COMMIT') 

    def closeDb(self):
        self.conn.close()