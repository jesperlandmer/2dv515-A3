import operator

from db import db

class score:
    def __init__(self, link=None, score=0.0, content={}, location={}, pageRank={}):
        self.link = link
        self.score = score
        self.content = content
        self.location = location
        self.pageRank = pageRank

class searchEngine:
    def __init__(self, db=db()):
        self.db = db

    def searchQuery(self, query):
        query = query.lower()
        words = query.split(' ')
        wordIds = [self.getIdForWord(w) for w in words]
        result = {}
        totscore = score(content={}, location={}, pageRank={})

        totscore.content = self.db.getFrequencyScore(wordIds)
        totscore.location = self.db.getLocationScore(wordIds)
        totscore.pageRank = dict(self.db.getPageLinks())
        con1 = totscore.content['/wiki/Charles_Babbage']
        loc1 = totscore.location['/wiki/Charles_Babbage']
        pag1 = totscore.pageRank['/wiki/Charles_Babbage']

        self.normalizeScore(totscore.content, False)
        self.normalizeScore(totscore.location, True)
        self.normalizeScore(totscore.pageRank, False)

        con2 = totscore.content['/wiki/Charles_Babbage']
        loc2 = totscore.location['/wiki/Charles_Babbage']
        pag2 = totscore.pageRank['/wiki/Charles_Babbage']

        for link in totscore.content:
            calcScore = totscore.content[link] + (0.8 * totscore.location[link]) + (0.5 * totscore.pageRank[link])
            result[link] = score(link=link,
                                 score=calcScore,
                                 content=totscore.content[link],
                                 location=0.8*totscore.location[link],
                                 pageRank=0.5*totscore.pageRank[link])

        # Sort list from top down highest score
        sortedList = []
        for page in (sorted(result.values(), key=operator.attrgetter('score'), reverse=True)):
            sortedList.append(page)

        return sortedList

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
        vsmall = 0.00001
        if smallIsBetter:
            vmin = min(scores.values())
            for key in scores:
                score = scores[key]
                scores[key] = float(vmin) / max(vsmall, score)
        else:
            vmax = max(scores.values())
            if vmax == 0: vmax = vsmall
            for key in scores:
                score = scores[key]
                scores[key] = score / vmax


def getTopFive(result):
        # Sort list from top down highest score
    sortedList = []
    for score in result[:5]:
        sortedList.append({
            'link': score.link,
            'score': score.score,
            'location': score.location,
            'frequency': score.content,
            'pageRank': score.pageRank
        })

    test = sortedList[:5]
    return sortedList
