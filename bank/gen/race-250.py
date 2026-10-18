# Bank session 18 Oct 2026: 1 game-show race -> bank/race-250.json (Robot Wars).
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

race("Robot Wars - name it", "Television", "medium", ["Robot Wars", "game shows", "BBC"], [
 ("The host of the first series in 1998", "Jeremy Clarkson", ["Richard Hammond", "James May", "Jeremy Vine"]),
 ("The host from the second series", "Craig Charles", ["Craig David", "Craig Revel Horwood", "Craig Cash"]),
 ("His line to start a fight", "3, 2, 1, Activate!", ["Ready, steady, fight!", "Robots, go!", "Let battle commence!"]),
 ("His line to stop one", "Cease!", ["Halt!", "Freeze!", "Enough!"]),
 ("The pit-side co-host", "Philippa Forrester", ["Kirsty Gallacher", "Gail Porter", "Konnie Huq"]),
 ("The excitable commentator", "Jonathan Pearce", ["Jonathan Agnew", "Jonathan Ross", "Jonathan Davies"]),
 ("The host of the 2016 revival", "Dara Ó Briain", ["Ed Byrne", "Rob Brydon", "Jason Manford"]),
 ("His co-host", "Angela Scanlon", ["Angela Rippon", "Angela Griffin", "Angellica Bell"]),
 ("The channel", "BBC Two", ["ITV", "Channel 4", "Sky One"]),
 ("The year it began", "1998", ["1994", "2002", "2006"]),
 ("Where the idea started", "USA", ["Japan", "Germany", "Canada"]),
 ("The giant house robot with a lance and claw", "Sir Killalot", ["Sir Smash-a-lot", "Lord Crusher", "Baron Bash"]),
 ("The tusked, dinosaur-like house robot", "Matilda", ["Rexie", "Tusky", "Gertie"]),
 ("The house robot with a flamethrower", "Sgt Bash", ["Corporal Burn", "Major Flame", "Captain Blaze"]),
 ("The house robot with an axe", "Shunt", ["Chopper", "Hack", "Cleaver"]),
 ("Dead Metal's weapon", "A circular saw", ["A drill", "A net", "A spike"]),
 ("Mr Psycho's weapon", "A huge hammer", ["A lance", "A drill", "A net"]),
 ("The robot referee", "Refbot", ["Whistlebot", "Judgebot", "Rulebot"]),
 ("The trapdoor in the arena floor", "The Pit", ["The Hole", "The Drop", "The Gap"]),
 ("The robot that won series 3 and 4", "Chaos 2", ["Hypno-Disc", "Razer", "Roadblock"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-250.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
