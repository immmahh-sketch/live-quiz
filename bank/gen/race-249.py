# Bank session 18 Oct 2026: 1 game-show race -> bank/race-249.json (Big Break).
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

race("Big Break - name it", "Television", "medium", ["Big Break", "game shows", "snooker", "BBC"], [
 ("The host", "Jim Davidson", ["Jimmy Tarbuck", "Jim Moir", "Jim Bowen"]),
 ("The snooker star alongside him", "John Virgo", ["John Parrott", "John Higgins", "John Spencer"]),
 ("The title that star won in 1979", "UK Championship", ["World Championship", "The Masters", "Welsh Open"]),
 ("The channel", "BBC One", ["ITV", "BBC Two", "Channel 4"]),
 ("The year it began", "1991", ["1987", "1995", "1999"]),
 ("The year it ended", "2002", ["1998", "2005", "2008"]),
 ("The theme song", "Snooker Loopy", ["Pot the Lot", "Cue Ball Crazy", "Rack 'Em Up"]),
 ("The duo who sang it", "Chas & Dave", ["Madness", "The Wombles", "Spitting Image"]),
 ("Who the contestants were paired with", "Snooker professionals", ["Darts players", "Golfers", "Comedians"]),
 ("The round named after a famous old snooker show", "Pot Black", ["Pot Luck", "Black Ball", "Clear the Table"]),
 ("The host's other Saturday-night game show from 1995", "The Generation Game", ["Bullseye", "Blankety Blank", "Big Brother"]),
 ("His 1980s sitcom set in south London", "Up the Elephant and Round the Castle", ["Only Fools and Horses", "Minder", "Shelley"]),
 ("The reality show he won in 2014", "Celebrity Big Brother", ["I'm a Celebrity", "Strictly Come Dancing", "Dancing on Ice"]),
 ("Pockets on a snooker table", "6", ["4", "8", "10"]),
 ("Reds at the start of a frame", "15", ["10", "12", "21"]),
 ("Points for a red", "1", ["2", "3", "4"]),
 ("Points for the black", "7", ["5", "8", "9"]),
 ("The colour worth 2", "Yellow", ["Green", "Brown", "Blue"]),
 ("The colour you pot last", "Black", ["Pink", "Blue", "White"]),
 ("A maximum break", "147", ["144", "150", "155"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-249.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
