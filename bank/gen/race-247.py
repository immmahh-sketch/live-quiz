# Bank session 18 Oct 2026: 1 game-show race -> bank/race-247.json (Blankety Blank).
# A Crystal Maze race was drafted too but shared 9 right answers with the existing Crystal Maze word race, so it was dropped.
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

race("Blankety Blank - name it", "Television", "medium", ["Blankety Blank", "game shows", "BBC"], [
 ("The original host", "Terry Wogan", ["Terry Christian", "Terry Nutkins", "Terry Venables"]),
 ("His nationality", "Irish", ["Scottish", "Welsh", "Canadian"]),
 ("The radio station he was famous on", "Radio 2", ["Radio 1", "Radio 4", "Capital"]),
 ("His skinny microphone's nickname", "The wand", ["The stick", "The twig", "The pencil"]),
 ("The host who took over in 1984", "Les Dawson", ["Les Dennis", "Les Ferdinand", "Les McKeown"]),
 ("The relative he always joked about", "His mother-in-law", ["His wife", "His brother", "His aunt"]),
 ("His comic party piece at the piano", "Playing deliberately badly", ["Playing upside down", "Playing blindfold", "Playing with his feet"]),
 ("The year his run ended", "1990", ["1986", "1994", "1997"]),
 ("The drag queen who hosted from the late 1990s", "Lily Savage", ["Dame Edna Everage", "Julian Clary", "Dick Emery"]),
 ("The man behind her", "Paul O'Grady", ["Paul Merton", "Paul Daniels", "Paul Ross"]),
 ("The host of the 2016 Christmas one-off", "David Walliams", ["Matt Lucas", "Alan Carr", "Jimmy Carr"]),
 ("The host of the 2021 revival", "Bradley Walsh", ["Ben Shephard", "Stephen Mulhern", "Paddy McGuinness"]),
 ("The channel it began on", "BBC One", ["ITV", "BBC Two", "Channel 4"]),
 ("The year it began", "1979", ["1975", "1983", "1987"]),
 ("The American show it came from", "The Match Game", ["Password", "The Gong Show", "Hollywood Squares"]),
 ("What you had to do", "Fill in the blank", ["Spot the difference", "Guess the price", "Name the tune"]),
 ("Celebrities on the panel", "6", ["4", "5", "8"]),
 ("Contestants on each show", "2", ["3", "4", "5"]),
 ("The final round", "Supermatch", ["Megamatch", "Superblank", "Head to Head"]),
 ("The famous consolation prize", "A chequebook and pen", ["A Blankety mug", "A teddy bear", "A pen and pencil set"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-247.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
