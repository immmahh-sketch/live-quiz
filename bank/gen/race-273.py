# Bank session 19 Oct 2026: 1 children's TV race -> bank/race-273.json (Byker Grove, for the Newcastle crowd).
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

race("Byker Grove - name it", "Television", "medium", ["Byker Grove", "children's TV", "North East", "BBC"], [
 ("The city it's set in", "Newcastle", ["Sunderland", "Durham", "Middlesbrough"]),
 ("What Byker Grove is", "A youth club", ["A school", "A football club", "A hospital"]),
 ("The Newcastle area where it was actually filmed", "Benwell", ["Byker", "Heaton", "Jesmond"]),
 ("Its creator", "Adele Rose", ["Adele Silva", "Anne Rose", "Adele Roberts"]),
 ("The youth leader", "Geoff", ["Graham", "Gordon", "Gavin"]),
 ("What Spuggie's nickname means in Geordie", "Sparrow", ["Robin", "Pigeon", "Seagull"]),
 ("Ant's character", "PJ", ["AJ", "PK", "TJ"]),
 ("Dec's character", "Duncan", ["Dougie", "Darren", "Dean"]),
 ("What happened to PJ", "Blinded in a paintball accident", ["Hit by a car", "Fell off a roof", "Caught in a fire"]),
 ("Their 1994 hit as PJ & Duncan", "Let's Get Ready to Rhumble", ["Shout", "Do the Bartman", "Rhythm Is a Dancer"]),
 ("Where that song got to when it came back in 2013", "Number one", ["Number 5", "Number 10", "Number 40"]),
 ("Their Saturday-morning show after the Grove", "SMTV Live", ["Live & Kicking", "Going Live!", "Saturday Superstore"]),
 ("Their Saturday-night show", "Saturday Night Takeaway", ["Noel's House Party", "Saturday Night Live", "Gladiators"]),
 ("Their jungle show", "I'm a Celebrity", ["Love Island", "Big Brother", "Survivor"]),
 ("The future EastEnders star who was in it", "Jill Halfpenny", ["Jill Scott", "Jill Gascoine", "Jill Dando"]),
 ("The future presenter who played Charlie", "Donna Air", ["Donna Ewin", "Donna Edmonds", "Donna Allen"]),
 ("Its 1994 first for children's TV", "A kiss between two boys", ["A royal visit", "A live episode", "A wedding"]),
 ("The channel", "BBC One", ["ITV", "BBC Two", "Channel 4"]),
 ("The year it began", "1989", ["1985", "1993", "1997"]),
 ("The year it ended", "2006", ["2001", "2009", "2012"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-273.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
