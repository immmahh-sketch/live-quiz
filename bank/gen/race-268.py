# Bank session 19 Oct 2026: 1 sitcom race -> bank/race-268.json (Man About the House).
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

race("Man About the House - name it", "Television", "medium", ["Man About the House", "sitcoms", "ITV"], [
 ("The man", "Robin Tripp", ["Robin Trott", "Robin Tribe", "Robert Tripp"]),
 ("The actor who played him", "Richard O'Sullivan", ["Richard Wilson", "Richard Briers", "Richard Beckinsale"]),
 ("What he was studying", "Cookery", ["Law", "Medicine", "Art"]),
 ("Why the girls let him move in", "He can cook", ["He's rich", "He's their cousin", "He fixes cars"]),
 ("His two flatmates", "Chrissy and Jo", ["Chrissy and Jane", "Chris and Jo", "Kirsty and Jo"]),
 ("The actress who played Chrissy", "Paula Wilcox", ["Paula Yates", "Paula Radcliffe", "Paula Abdul"]),
 ("The actress who played Jo", "Sally Thomsett", ["Sally Phillips", "Sally Lindsay", "Sally Gunnell"]),
 ("Their landlords", "The Ropers", ["The Rodgers", "The Ridleys", "The Rogers"]),
 ("The actor who played George", "Brian Murphy", ["Brian Blessed", "Brian Cox", "Brian Conley"]),
 ("The actress who played Mildred", "Yootha Joyce", ["Thora Hird", "Peggy Mount", "Hattie Jacques"]),
 ("The part of London it's set in", "Earls Court", ["Notting Hill", "Clapham", "Islington"]),
 ("The writers", "Johnnie Mortimer and Brian Cooke", ["Galton and Simpson", "Croft and Perry", "Clement and La Frenais"]),
 ("The channel", "ITV", ["BBC One", "BBC Two", "Channel 4"]),
 ("The ITV company that made it", "Thames", ["LWT", "Granada", "Central"]),
 ("The year it began", "1973", ["1969", "1977", "1981"]),
 ("The year it ended", "1976", ["1972", "1980", "1984"]),
 ("The year of the film", "1974", ["1971", "1978", "1983"]),
 ("The landlords' spin-off", "George and Mildred", ["Mr and Mrs Roper", "Keeping Up with the Ropers", "Roper's Rest"]),
 ("Robin's spin-off", "Robin's Nest", ["Robin's House", "Robin's Kitchen", "Robin's Place"]),
 ("The American remake", "Three's Company", ["Two's a Crowd", "Full House", "Friends"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-268.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
