import operator

from db import db

class score:
    def __init__(self, page=None, score=0.0, content={}, location={}, pageRank={}):
        self.page = page
        self.score = score
        self.content = content
        self.location = location
        self.pageRank = pageRank

class searchEngine:
    def __init__(self, db=db()):
        self.db = db

    def searchQuery(self, query):
        result = {}
        totscore = score(content={}, location={}, pageRank={})
        pages = self.db.getPages()
        id = self.getIdForWord(query)

        [self.setScores(totscore, pages[p], id) for p in pages]

        self.normalizeScore(totscore.content, False)
        self.normalizeScore(totscore.location, True)
        self.normalizeScore(totscore.pageRank, False)

        for p in pages.values():
            calcScore = totscore.content[p.link] + (0.8 * totscore.location[p.link]) + (0.5 * totscore.pageRank[p.link])
            result[p.link] = score(page=p, score=calcScore)

        # Sort list from top down highest score
        sortedList = []
        for page in (sorted(result.values(), key=operator.attrgetter('score'), reverse=True)):
            sortedList.append(page)

        return sortedList, totscore

    def getIdForWord(self, word):
        wordid = self.db.getWordId(word)
        if (wordid != None):
            return wordid[0]
        else:
            wordid = self.db.getMaxId()[0]
            if wordid == None: wordid = 0
            self.db.saveWord(wordid, word)
            return wordid


    def setScores(self, totscore, p, id):
        if id in p.wordlocations:
            totscore.content[p.link] = self.db.getFrequencyScore(p, id)
            totscore.location[p.link] = self.db.getLocationScore(p, id) + 1
        else: 
            totscore.content[p.link] = 0
            totscore.location[p.link] = 100000
        totscore.pageRank[p.link] = p.pageRank

    def normalizeScore(self, scores, smallIsBetter):
        if smallIsBetter:
            vsmall = 0.00001
            vmin = min(scores.values())
            for key in scores:
                score = scores[key]
                scores[key] = float(vmin) / max(vsmall, score)
        else:
            vmax = max(scores.values())
            for key in scores:
                score = scores[key]
                scores[key] = score / vmax


def getTopFive(result, totscore):
        # Sort list from top down highest score
    sortedList = []
    for score in result[:5]:
        p = score.page
        sortedList.append({
            'link': p.link,
            'score': score.score,
            'location': totscore.location[p.link] * 0.8,
            'frequency': totscore.content[p.link],
            'pageRank': totscore.pageRank[p.link] * 0.5
        })

    test = sortedList[:5]
    return sortedList