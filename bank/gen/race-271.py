# Bank session 19 Oct 2026: 1 sitcom race -> bank/race-271.json (Ever Decreasing Circles). A Just Good Friends race was drafted but had too few solid rows.
# Checked against every race in stock with lqsql/audit/race-overlap.py before importing.
# raceOk: 20 rows, 20 different right answers, no right answer among another row's options, no wrong option on 3+ rows.
import json, os
from collections import Counter
R = []
def race(title, cat, diff, tags, rows):
    rights = {r[1] for r in rows}
    assert len(rows) == 20, (title, len(rows))
    assert len(rights) == 20, (title, 'duplicate right answers')
    bad = [(q, w) for q, right, wrong in rows for w in wrong if w in rights]
    assert not bad, (title, 'recycled', bad)
    for q, right, wrong in rows:
        assert len(wrong) == 3 and len(set(wrong)) == 3 and right not in wrong, (title, q)
    over = [w for w, n in Counter(w for _, _, wrong in rows for w in wrong).items() if n > 2]
    assert not over, (title, 'wrong option on 3+ rows', over)
    R.append({"type": "race", "text": "The Race: " + title, "target": 10, "category": cat, "tags": tags, "difficulty": diff,
              "bank": [{"q": q, "right": right, "wrong": wrong} for q, right, wrong in rows]})

race("Ever Decreasing Circles - name it", "Television", "medium", ["Ever Decreasing Circles", "sitcoms", "BBC"], [
 ("The fussy hero", "Martin Bryce", ["Martin Bryant", "Michael Bryce", "Martin Bryson"]),
 ("The actor who played him", "Richard Briers", ["Richard Wilson", "Richard Beckinsale", "Richard O'Sullivan"]),
 ("That actor's role in The Good Life", "Tom Good", ["Jerry Leadbetter", "Tom Goodman", "Ted Good"]),
 ("The honour he received in 2003", "Knighthood", ["OBE", "MBE", "Peerage"]),
 ("Martin's obsession", "Running local clubs and committees", ["Fishing", "Gardening", "Football"]),
 ("His wife", "Ann", ["Angela", "Alice", "Amy"]),
 ("The actress who played her", "Penelope Wilton", ["Penelope Keith", "Penelope Cruz", "Penelope Tree"]),
 ("Her later Downton Abbey role", "Isobel Crawley", ["Violet Crawley", "Cora Crawley", "Mrs Hughes"]),
 ("The smooth new neighbour", "Paul Ryman", ["Paul Rider", "Peter Ryman", "Paul Ryan"]),
 ("The actor who played him", "Peter Egan", ["Peter Davison", "Peter Bowles", "Peter Kay"]),
 ("Paul's business", "A hair salon", ["A garage", "A restaurant", "An estate agency"]),
 ("The couple in matching jumpers", "Howard and Hilda", ["Harold and Hilda", "Howard and Holly", "Henry and Hilda"]),
 ("The actor who played Howard", "Stanley Lebor", ["Stanley Baxter", "Stanley Tucci", "Stanley Holloway"]),
 ("The street they live on", "The Close", ["The Crescent", "The Avenue", "The Grove"]),
 ("The writers", "Esmonde and Larbey", ["Galton and Simpson", "Croft and Perry", "Marks and Gran"]),
 ("Their earlier hit", "The Good Life", ["Porridge", "Butterflies", "Rising Damp"]),
 ("The channel", "BBC One", ["ITV", "BBC Two", "Channel 4"]),
 ("The year it began", "1984", ["1980", "1988", "1992"]),
 ("The year it ended", "1989", ["1986", "1991", "1995"]),
 ("Series made", "4", ["2", "3", "6"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-271.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
