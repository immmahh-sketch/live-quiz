# Bank session 19 Oct 2026: 1 drama race -> bank/race-274.json (Our Friends in the North, for the Newcastle crowd).
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

race("Our Friends in the North - name it", "Television", "hard", ["Our Friends in the North", "drama", "North East", "BBC"], [
 ("The city the four friends come from", "Newcastle", ["Sunderland", "Durham", "Middlesbrough"]),
 ("The four friends", "Nicky, Tosker, Geordie and Mary", ["Nicky, Tommy, Geordie and Mary", "Nicky, Tosker, George and Maggie", "Nick, Tosh, Geordie and Mandy"]),
 ("The future Doctor Who who played Nicky", "Christopher Eccleston", ["David Tennant", "Matt Smith", "Peter Capaldi"]),
 ("Which Doctor he became", "The Ninth", ["The Eighth", "The Tenth", "The Eleventh"]),
 ("The future James Bond who played Geordie", "Daniel Craig", ["Pierce Brosnan", "Timothy Dalton", "Sean Bean"]),
 ("His first Bond film", "Casino Royale", ["Skyfall", "Quantum of Solace", "Spectre"]),
 ("The actor who played Tosker", "Mark Strong", ["Mark Benton", "Mark Bonnar", "Mark Gatiss"]),
 ("The actress who played Mary", "Gina McKee", ["Gina Yashere", "Gina Bellman", "Geena Davis"]),
 ("The County Durham town she grew up in", "Peterlee", ["Seaham", "Consett", "Stanley"]),
 ("Her role in Notting Hill", "Bella", ["Honey", "Anna", "Max"]),
 ("Nicky's later career", "Photographer", ["Teacher", "Policeman", "Footballer"]),
 ("The council boss based on T. Dan Smith", "Austin Donohue", ["Alan Donovan", "Austin Doherty", "Arthur Donohue"]),
 ("The real scandal it echoes", "The Poulson affair", ["The Profumo affair", "Watergate", "The Guinness affair"]),
 ("What it started life as", "A stage play", ["A novel", "A radio series", "A film"]),
 ("The writer", "Peter Flannery", ["Peter Kay", "Peter Morgan", "Peter Bowker"]),
 ("The years the story spans", "1964 to 1995", ["1945 to 1979", "1970 to 2000", "1980 to 2010"]),
 ("Episodes", "9", ["6", "12", "15"]),
 ("The channel", "BBC Two", ["BBC One", "ITV", "Channel 4"]),
 ("The year it was shown", "1996", ["1992", "2000", "2004"]),
 ("The award it won for best drama serial", "BAFTA", ["Emmy", "Golden Globe", "Oscar"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-274.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
