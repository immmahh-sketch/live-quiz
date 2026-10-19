# Bank session 19 Oct 2026: 1 sitcom race -> bank/race-272.json (Spaced). A Gimme Gimme Gimme race was drafted but had too few solid rows.
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

race("Spaced - name it", "Television", "medium", ["Spaced", "sitcoms", "Channel 4"], [
 ("The actor who played Tim", "Simon Pegg", ["Simon Bird", "Simon Amstell", "Simon Callow"]),
 ("Tim's surname", "Bisley", ["Bailey", "Bisset", "Bixby"]),
 ("The actress who played Daisy", "Jessica Hynes", ["Jessica Alba", "Jessica Ennis", "Jessica Raine"]),
 ("Daisy's surname", "Steiner", ["Stern", "Stewart", "Stone"]),
 ("Why they move in together", "They pretend to be a couple", ["They're cousins", "They won a competition", "They're married"]),
 ("Their address", "23 Meteor Street", ["23 Comet Street", "32 Meteor Street", "23 Planet Road"]),
 ("The landlady", "Marsha", ["Martha", "Maureen", "Marjorie"]),
 ("Tim's best friend", "Mike", ["Mark", "Matt", "Max"]),
 ("The actor who played him", "Nick Frost", ["Nick Moran", "Nick Knowles", "Nick Hancock"]),
 ("Mike's obsession", "The army", ["Football", "Cooking", "Trains"]),
 ("The actor who played Brian the artist", "Mark Heap", ["Mark Benton", "Mark Bonnar", "Mark Gatiss"]),
 ("Where Tim works", "A comic shop", ["A record shop", "A video shop", "A bookshop"]),
 ("The film Tim can't forgive", "The Phantom Menace", ["Titanic", "Jurassic Park", "Independence Day"]),
 ("Daisy's dog", "Colin", ["Kevin", "Clive", "Carl"]),
 ("What it slips into almost every scene", "Film and game references", ["Musical numbers", "Cartoon inserts", "Hidden adverts"]),
 ("The director", "Edgar Wright", ["Edward Wright", "Danny Boyle", "Richard Curtis"]),
 ("The zombie film the team made next", "Shaun of the Dead", ["28 Days Later", "Attack the Block", "Sightseers"]),
 ("The channel", "Channel 4", ["BBC Two", "ITV", "E4"]),
 ("The year it began", "1999", ["1995", "2002", "2006"]),
 ("Series made", "2", ["3", "4", "5"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-272.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
