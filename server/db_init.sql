CREATE TABLE pages ( url TEXT NOT NULL PRIMARY KEY, pr_score REAL);
CREATE TABLE words(wordid INT NOT NULL PRIMARY KEY, word TEXT);
CREATE TABLE wordlocation ( url TEXT, wordid INT, location INT);

CREATE TABLE concat_values AS SELECT url, wordid, GROUP_CONCAT(location), pr_score AS locations from (SELECT p.url,p.pr_score,w.wordid,w.location FROM pages AS p JOIN wordlocation AS w ON w.url = p.url) GROUP BY url,wordid;

CREATE TEMPORARY TABLE frequency_score AS SELECT url, COUNT(*) AS frequency FROM wordlocation WHERE wordid = ? GROUP BY url UNION SELECT url, 0 AS frequency FROM wordlocation WHERE url NOT IN (SELECT DISTINCT url FROM wordlocation WHERE wordid = ?) GROUP BY url;