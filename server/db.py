import sqlite3
conn = sqlite3.connect('page.db')
c = conn.cursor()

def saveToDb(page):
    url = page.link
    words = page.words

    c.execute(f"INSERT OR REPLACE INTO pages (url) VALUES ('{url}');")

    for id in words:
        # words[id] = words[id].replace("'", "\\'") # replace comma for db insertion
        c.execute(f"INSERT OR REPLACE INTO words (url, id, word) VALUES (?, ?, ?);", (url, id, words[id],))

    conn.commit()

def closeDb():
    conn.close()