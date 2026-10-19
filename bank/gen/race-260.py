# Bank session 19 Oct 2026: 1 sitcom race -> bank/race-260.json (Bottom).
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

race("Bottom - name it", "Television", "medium", ["Bottom", "sitcoms", "BBC"], [
 ("The actor who played Richie", "Rik Mayall", ["Rik Waller", "Rick Astley", "Rick Wakeman"]),
 ("The actor who played Eddie", "Adrian Edmondson", ["Adrian Chiles", "Adrian Lester", "Adrian Dunbar"]),
 ("Richie's full name", "Richard Richard", ["Richie Rich", "Richard Ritchie", "Rich Richards"]),
 ("Eddie's surname", "Hitler", ["Himmler", "Hiller", "Hilton"]),
 ("What Richie desperately wants", "A girlfriend", ["A job", "Fame", "Money"]),
 ("Their trademark comedy", "Violent slapstick", ["Gentle wordplay", "Musical numbers", "Silent mime"]),
 ("The part of London they live in", "Hammersmith", ["Shepherd's Bush", "Brixton", "Peckham"]),
 ("Their friend Dave's surname", "Hedgehog", ["Badger", "Ferret", "Weasel"]),
 ("Their other friend", "Spudgun", ["Mashgun", "Spudface", "Chipshot"]),
 ("Who wrote it", "The two stars", ["Ben Elton", "Richard Curtis", "John Sullivan"]),
 ("The channel", "BBC Two", ["BBC One", "Channel 4", "ITV"]),
 ("The year it began", "1991", ["1987", "1995", "1999"]),
 ("Series made", "3", ["2", "4", "5"]),
 ("Their stage shows", "Bottom Live", ["Bottom on Tour", "Bottom Unplugged", "Bottom Encore"]),
 ("Their 1999 film", "Guest House Paradiso", ["Bottom: The Movie", "Hammersmith Nights", "Bed and Breakfast Paradise"]),
 ("Their earlier sitcom as Rik and Vyvyan", "The Young Ones", ["Red Dwarf", "Blackadder", "Spitting Image"]),
 ("Their stunt-loving double act", "The Dangerous Brothers", ["The Stupid Brothers", "The Crazy Brothers", "The Reckless Brothers"]),
 ("Mayall's role in Blackadder", "Lord Flashheart", ["Lord Melchett", "Lord Percy", "Captain Darling"]),
 ("Mayall's sleazy MP in The New Statesman", "Alan B'Stard", ["Alan Partridge", "Alan Clark", "Alan Brady"]),
 ("Edmondson's comedian wife", "Jennifer Saunders", ["Dawn French", "Joanna Lumley", "Ruby Wax"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-260.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
