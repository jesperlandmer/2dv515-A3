import sqlite3

class page:
    def __init__(self, link, links=[], wordlocations={}, pageRank=1.0):
        self.link = link
        self.links = links
        self.wordlocations = wordlocations
        self.pageRank = pageRank

    def hasLinkTo(self, url):
        return url in self.links

class db:
    def __init__(self, conn=sqlite3.connect('page.db', check_same_thread=False), db='page.db'):
        self.conn = conn
        self.cursor = self.conn.cursor()
        
    def start(self):
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
        result = {}
        self.cursor.execute('SELECT * FROM concat_values;')
        pages = self.cursor.fetchall()

        # Row: url | wordid | locations | pagerank
        for row in pages:
            p = None
            if (row[0] not in result):
                p = page(row[0], wordlocations={}, pageRank=row[3])
                result[row[0]] = p
            else: p = result[row[0]]

            p.wordlocations[row[1]] = [int(x) for x in row[2].split(',')]
        return result

    def getFrequencyScore(self, page, wordid):
        self.cursor.execute('SELECT count(*) FROM wordlocation where url = ? AND wordid = ?', (page.link,wordid))
        result = self.cursor.fetchone()
        return result[0]

    def getLocationScore(self, page, wordid):
        self.cursor.execute('SELECT MIN(location) FROM wordlocation where url = ? AND wordid = ?', (page.link,wordid))
        result = self.cursor.fetchone()
        return result[0]

    def updatePageRank(self, page):
        self.cursor.execute('UPDATE pages SET pr_score = ? WHERE url = ?', (page.pageRank,page.link))

    def saveWord(self, wordid, word):
        self.cursor.execute('INSERT INTO words (wordid, word) VALUES (?, ?)', (wordid, word))

    def savePage(self, page):
        url = page.link
        self.cursor.execute('INSERT INTO pages (url) VALUES (?)', (url))

    def saveLocation(self, page, wordid, location):
        url = page.link
        self.cursor.execute('INSERT INTO wordlocation (url, wordid, location) VALUES (?, ?, ?)', (url, wordid, location))

    def commit(self):
        self.cursor.execute('COMMIT') 

    def closeDb(self):
        self.conn.close()