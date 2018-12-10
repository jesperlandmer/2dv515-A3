import operator

from db import db

class score:
    def __init__(self, page=None, score=0.0, content={}, location={}):
        self.page = page
        self.score = score
        self.content = content
        self.location = location

class searchEngine:
    def __init__(self, db=db()):
        self.db = db

    def searchQuery(self, query):
        result = {}
        totscore = score(content={}, location={})
        pages = self.db.getPages()

        for link in pages:
            p = pages[link]
            id = self.getIdForWord(query)

            if id in p.wordlocations:
                totscore.content[p.link] = self.db.getFrequencyScore(p, id)
                totscore.location[p.link] = self.db.getLocationScore(p, id) + 1
            else: 
                totscore.content[p.link] = 0
                totscore.location[p.link] = 100000

        self.normalizeScore(totscore.content, False)
        self.normalizeScore(totscore.location, True)

        for link in pages:
            p = pages[link]
            calcScore = 1.0 * totscore.content[p.link] + 0.5 * totscore.location[p.link]
            result[p.link] = score(page=p, score=calcScore)

        # Sort list from top down highest score
        sortedList = []
        for page in (sorted(result.values(), key=operator.attrgetter('score'), reverse=True)):
            sortedList.append(page)
            
        # Return top 5
        return sortedList[:5]


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
            vmin = min(scores.values())
            for key in scores:
                score = scores[key]
                scores[key] = float(vmin) / max(score, 0.00001)
        else:
            vmax = max(scores.values())
            for key in scores:
                score = scores[key]
                scores[key] = score / vmax

# print(searchEngine().searchQuery('nintendo'))