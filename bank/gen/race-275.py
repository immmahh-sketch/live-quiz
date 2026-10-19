# Bank session 19 Oct 2026: 1 music TV race -> bank/race-275.json (The Tube, made in Newcastle).
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

race("The Tube - name it", "Television", "hard", ["The Tube", "music TV", "North East", "Channel 4"], [
 ("The channel", "Channel 4", ["BBC Two", "ITV", "BBC One"]),
 ("The city it came from", "Newcastle", ["Manchester", "Liverpool", "Glasgow"]),
 ("The TV company whose studio it used", "Tyne Tees", ["Granada", "Yorkshire", "Border"]),
 ("Its studio", "Studio 5", ["Studio 1", "Studio 3", "Studio 8"]),
 ("The day it went out", "Friday", ["Monday", "Wednesday", "Saturday"]),
 ("When it went out", "Early evening", ["Breakfast", "Late night", "Lunchtime"]),
 ("How it was broadcast", "Live", ["Pre-recorded", "Animated", "Radio only"]),
 ("The year it began", "1982", ["1978", "1986", "1990"]),
 ("The year it ended", "1987", ["1984", "1990", "1993"]),
 ("Its male presenter", "Jools Holland", ["Jonathan Ross", "Mark Lamarr", "Chris Evans"]),
 ("His band", "Squeeze", ["Madness", "The Specials", "Dexys Midnight Runners"]),
 ("Why he was suspended", "He swore in a live trailer", ["He fell asleep on air", "He insulted a guest", "He played the wrong song"]),
 ("His later music show", "Later... with Jools Holland", ["Top of the Pops", "The Old Grey Whistle Test", "The Word"]),
 ("Its female presenter", "Paula Yates", ["Paula Abdul", "Paula Hamilton", "Paula Wilcox"]),
 ("The man she married in 1986", "Bob Geldof", ["Bono", "Sting", "Midge Ure"]),
 ("The Scottish presenter", "Muriel Gray", ["Muriel Young", "Mariella Frostrup", "Kirsty Wark"]),
 ("Another presenter, later in Men Behaving Badly", "Leslie Ash", ["Leslie Grantham", "Lesley Joseph", "Lesley Garrett"]),
 ("The band who played their last TV show on the first episode", "The Jam", ["The Police", "The Clash", "The Specials"]),
 ("The band it famously launched in 1983", "Frankie Goes to Hollywood", ["Duran Duran", "Culture Club", "Spandau Ballet"]),
 ("Its producer", "Malcolm Gerrie", ["Malcolm McLaren", "Malcolm Allison", "Malcolm Hardee"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-275.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
