# Bank session 19 Oct 2026: 1 sitcom race -> bank/race-263.json (The Brittas Empire). An Early Doors race was drafted but had too few solid rows.
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

race("The Brittas Empire - name it", "Television", "medium", ["The Brittas Empire", "sitcoms", "BBC"], [
 ("The manager", "Gordon Brittas", ["Gordon Brittan", "Gerald Brittas", "Graham Brittas"]),
 ("The actor who played him", "Chris Barrie", ["Chris Addison", "Chris Langham", "Chris Lowe"]),
 ("That actor's role in Red Dwarf", "Rimmer", ["Kryten", "Lister", "Holly"]),
 ("The puppet satire he did voices for", "Spitting Image", ["Thunderbirds", "The Muppets", "Rainbow"]),
 ("Where Brittas works", "Whitbury Leisure Centre", ["Whitby Leisure Centre", "Westbury Sports Centre", "Whitchurch Leisure Centre"]),
 ("What Brittas is like", "Well-meaning but disastrous", ["Lazy and rude", "Cruel and greedy", "Shy and quiet"]),
 ("His attitude to rules", "Follows every one to the letter", ["Ignores them all", "Writes his own", "Lets the staff decide"]),
 ("His wife", "Helen", ["Hannah", "Heather", "Hazel"]),
 ("The actress who played her", "Pippa Haywood", ["Pippa Guard", "Philippa Forrester", "Penny Haywood"]),
 ("What Helen is always taking", "Pills", ["Holidays", "Notes", "Photos"]),
 ("What receptionist Carole keeps in her drawers", "Her babies", ["Biscuits", "Cash", "Love letters"]),
 ("The actress who played Carole", "Harriet Thorpe", ["Harriet Harman", "Harriet Walter", "Harriet Scott"]),
 ("Brittas's deputy", "Laura", ["Linda", "Lucy", "Lisa"]),
 ("The actor who played Colin", "Michael Burns", ["Michael Ball", "Michael Barrymore", "Michael Bublé"]),
 ("The writers", "Richard Fegen and Andrew Norriss", ["Galton and Simpson", "Croft and Perry", "Clement and La Frenais"]),
 ("The children's show Andrew Norriss went on to write", "Bernard's Watch", ["Woof!", "Byker Grove", "Grange Hill"]),
 ("The channel", "BBC One", ["ITV", "BBC Two", "Channel 4"]),
 ("The year it began", "1991", ["1987", "1995", "1999"]),
 ("The year it ended", "1997", ["1994", "2000", "2003"]),
 ("Series made", "7", ["4", "5", "9"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-263.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
