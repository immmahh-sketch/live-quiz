# Bank session 19 Oct 2026: 1 sitcom race -> bank/race-259.json (Ghosts).
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

race("Ghosts - name it", "Television", "medium", ["Ghosts", "sitcoms", "BBC"], [
 ("The house", "Button House", ["Bolton House", "Barton Hall", "Bunton Manor"]),
 ("The couple who inherit it", "Alison and Mike", ["Allie and Mark", "Anna and Mike", "Alison and Matt"]),
 ("Who can see the ghosts", "Alison", ["Mike", "The builder", "The vicar"]),
 ("Why she can see them", "A near-death fall from a window", ["A lightning strike", "A car crash", "A séance"]),
 ("The actress who plays her", "Charlotte Ritchie", ["Charlotte Crosby", "Charlotte Church", "Charlotte Hawkins"]),
 ("The ghost who carries his own head", "Humphrey", ["Henry", "Hugh", "Harold"]),
 ("The caveman ghost", "Robin", ["Rocky", "Ugg", "Bruce"]),
 ("The trouserless MP ghost", "Julian", ["Jeremy", "Jonathan", "James"]),
 ("The Second World War ghost", "The Captain", ["The Major", "The Colonel", "The Sergeant"]),
 ("The scout leader with an arrow through his neck", "Pat", ["Phil", "Peter", "Paul"]),
 ("The posh Edwardian lady of the house", "Fanny", ["Fiona", "Florence", "Felicity"]),
 ("The romantic poet ghost", "Thomas Thorne", ["Thomas Byron", "Thomas Keats", "Thomas Shelley"]),
 ("The ghosts who live in the cellar", "The plague victims", ["The miners", "The monks", "The soldiers"]),
 ("The team who write and star in it", "The Horrible Histories team", ["The Mighty Boosh", "The League of Gentlemen", "Monty Python"]),
 ("The channel", "BBC One", ["BBC Two", "ITV", "Channel 4"]),
 ("The year it began", "2019", ["2015", "2017", "2021"]),
 ("Series made", "5", ["3", "4", "6"]),
 ("The year of the final Christmas special", "2023", ["2020", "2022", "2025"]),
 ("The American channel that remade it", "CBS", ["NBC", "ABC", "Fox"]),
 ("What Alison inherits it from", "A distant relative", ["Her parents", "A lottery win", "Her old school"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-259.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
