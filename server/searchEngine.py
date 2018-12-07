from db import db

class score:
    def __init__(self, page=None, score=0.0, content=[], location=[]):
        self.page = page
        self.content = content
        self.location = location

class searchEngine:
    def __init__(self, db=db()):
        self.db = db

    def searchQuery(self, query):
        result = {}
        totscore = score(content=[], location=[])
        pages = self.db.getPages()

        for i in range(len(pages)):
            p = pages[i]
            totscore.content[i] = self.db.getFrequencyScore(p, query)
            totscore.location[i] = self.db.getFrequencyScore(p, query)

        self.normalizeScore(totscore.content, False)
        self.normalizeScore(totscore.location, True)

        for i in range(len(pages)):
            p = pages[i]
            calcScore = 1.0 * totscore.content[i] + 0.5 * totscore.location[i]
            result[p.link] = score(page=p, score=calcScore)




    def getIdForWord(self, word):
        wordid = self.db.getWordId(word)
        if (wordid != None):
            return wordid[0]
        else:
            wordid = self.db.getMaxId()[0]
            if wordid == None: wordid = 0
            self.db.saveWord(wordid, word)
            return wordid

    def normalizeScore(self, scores, smallIsBetter):
        if smallIsBetter:
            vmin = min(scores)
            for i in range(len(scores)):
                scores[i] = vmin / max(scores, 0.00001)
        else:
            vmax = max(scores)
            for i in range(len(scores)):
                scores[i] = scores[i] / max

