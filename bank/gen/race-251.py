# Bank session 18 Oct 2026: 1 game-show race -> bank/race-251.json (Takeshi's Castle).
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

race("Takeshi's Castle - name it", "Television", "hard", ["Takeshi's Castle", "game shows", "Japan"], [
 ("The star", "Takeshi Kitano", ["Akira Kurosawa", "Hayao Miyazaki", "Ken Watanabe"]),
 ("His comedy stage name", "Beat Takeshi", ["Funny Takeshi", "Laughing Takeshi", "Crazy Takeshi"]),
 ("His character in the show", "Count Takeshi", ["Lord Takeshi", "Emperor Takeshi", "Baron Takeshi"]),
 ("The country it came from", "Japan", ["South Korea", "China", "Thailand"]),
 ("The Japanese channel that made it", "TBS", ["NHK", "Fuji TV", "TV Asahi"]),
 ("The year it began", "1986", ["1980", "1992", "1998"]),
 ("The voice of the UK version", "Craig Charles", ["Craig Cash", "Craig David", "Craig Revel Horwood"]),
 ("The UK channel that showed it", "Challenge", ["Dave", "Sky One", "Channel 4"]),
 ("The year of the Prime Video revival", "2023", ["2015", "2019", "2025"]),
 ("The American spoof version", "MXC", ["Wipeout", "Fear Factor", "American Gladiators"]),
 ("Contestants at the start of a show", "Around 100", ["About 20", "About 50", "About 500"]),
 ("Who led the contestants", "General Tani", ["General Sato", "General Kato", "General Tanaka"]),
 ("The game with stepping stones over water", "Skipping Stones", ["Hop to It", "Jumping Rocks", "Stepping Out"]),
 ("The game with doors, some of them fake", "Knock Knock", ["Door Dash", "Who's There?", "Open Sesame"]),
 ("What the finalists rode in", "Go-karts", ["Bumper cars", "Hovercraft", "Quad bikes"]),
 ("What they had to shoot through", "Paper rings", ["Balloons", "Targets", "Bottles"]),
 ("How often somebody won", "Rarely", ["Every week", "Never", "Always"]),
 ("The star's 1983 war film with David Bowie", "Merry Christmas, Mr. Lawrence", ["Empire of the Sun", "The Last Emperor", "Tora! Tora! Tora!"]),
 ("The 2000 film where he plays a teacher", "Battle Royale", ["Ringu", "Audition", "Ichi the Killer"]),
 ("The blind swordsman film he directed in 2003", "Zatoichi", ["Rashomon", "Ran", "Kagemusha"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-251.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
