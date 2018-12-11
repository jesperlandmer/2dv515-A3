from db import db

from searchEngine import searchEngine

class pageRankGenerator:
    def __init__(self, wordList={}, db=db()):
        self.db = db
        self.search = searchEngine(db=self.db)

    def calculatePageRank(self, max_iterations=20):
        pages = self.db.getPages()
        for i in range(max_iterations):
            for page in pages:
                self.iteratePR(page)
    
    def iteratePR(self, page):
        pr = 0.0
        
