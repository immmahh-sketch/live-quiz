# Bank session 19 Oct 2026: 2 sitcom races -> bank/race-265.json (Friday Night Dinner; Bread).
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

race("Friday Night Dinner - name it", "Television", "medium", ["Friday Night Dinner", "sitcoms", "Channel 4"], [
 ("The family", "The Goodmans", ["The Goldmans", "The Goodwins", "The Greenbergs"]),
 ("The part of London they live in", "North London", ["South London", "East London", "West London"]),
 ("Their faith", "Jewish", ["Catholic", "Quaker", "Hindu"]),
 ("Dad", "Martin", ["Michael", "Malcolm", "Maurice"]),
 ("The actor who played him", "Paul Ritter", ["Paul Rudd", "Paul Whitehouse", "Paul Kaye"]),
 ("What Martin does when he gets hot", "Takes his shirt off", ["Opens the fridge", "Sits in the garden", "Turns the heating off"]),
 ("The year that actor died", "2021", ["2018", "2023", "2025"]),
 ("Mum", "Jackie", ["Janet", "Joan", "Judy"]),
 ("The actress who played her", "Tamsin Greig", ["Tamsin Egerton", "Tamsin Outhwaite", "Tamsin Grey"]),
 ("The two sons", "Adam and Jonny", ["Aaron and Josh", "Adam and Joey", "Alex and Jonny"]),
 ("The actor who played Adam", "Simon Bird", ["Simon Amstell", "Simon Pegg", "Simon Callow"]),
 ("That actor's Inbetweeners role", "Will McKenzie", ["Simon Cooper", "Jay Cartwright", "Neil Sutherland"]),
 ("The actor who played Jonny", "Tom Rosenthal", ["Tom Davis", "Tom Allen", "Tom Basden"]),
 ("The creepy neighbour", "Jim", ["Jack", "Jeff", "Jerry"]),
 ("The actor who played him", "Mark Heap", ["Mark Benton", "Mark Bonnar", "Mark Gatiss"]),
 ("Jim's dog", "Wilson", ["Winston", "Wallace", "Wilbur"]),
 ("Its creator", "Robert Popper", ["Robert Webb", "Robert Peston", "Robert Smith"]),
 ("The channel", "Channel 4", ["BBC Two", "ITV", "E4"]),
 ("The year it began", "2011", ["2007", "2014", "2017"]),
 ("Series made", "6", ["4", "5", "8"])])

race("Bread - name it", "Television", "medium", ["Bread", "sitcoms", "BBC"], [
 ("The family", "The Boswells", ["The Bosworths", "The Bagshaws", "The Barlows"]),
 ("Their city", "Liverpool", ["Manchester", "Birmingham", "Leeds"]),
 ("How the family get by", "Working the benefits system", ["Running a bakery", "Winning the pools", "Selling cars"]),
 ("Mum", "Nellie", ["Nora", "Nancy", "Norma"]),
 ("The actress who played her", "Jean Boht", ["Jean Alexander", "Jean Marsh", "Jean Simmons"]),
 ("The eldest son", "Joey", ["Johnny", "Jimmy", "Jackie"]),
 ("The actor who played him", "Peter Howitt", ["Peter Davison", "Peter Kay", "Peter Purves"]),
 ("The actor who played Billy", "Nick Conway", ["Nick Berry", "Nick Pickard", "Nick Hancock"]),
 ("The daughter", "Aveline", ["Adeline", "Avril", "Ava"]),
 ("Children in the family", "5", ["3", "4", "6"]),
 ("Where Grandad lives", "Next door", ["Upstairs", "In a care home", "In Wales"]),
 ("Dad Freddie's other woman", "Lilo Lil", ["Hula Lil", "Lazy Lil", "Lucky Lil"]),
 ("The writer", "Carla Lane", ["Roy Clarke", "John Sullivan", "Victoria Wood"]),
 ("Her earlier Liverpool sitcom", "The Liver Birds", ["Brookside", "Hollyoaks", "Scully"]),
 ("The channel", "BBC One", ["ITV", "BBC Two", "Channel 4"]),
 ("The year it began", "1986", ["1982", "1990", "1994"]),
 ("The year it ended", "1991", ["1988", "1995", "1999"]),
 ("Series made", "7", ["4", "6", "9"]),
 ("Viewers at its peak, in millions", "21", ["10", "15", "30"]),
 ("The actor who played Grandad", "Kenneth Waller", ["Kenneth Cranham", "Kenneth Williams", "Kenneth Connor"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-265.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
