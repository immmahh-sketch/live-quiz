# Bank session 18 Oct 2026: 1 game-show race -> bank/race-252.json (Wheel of Fortune).
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

race("Wheel of Fortune - name it", "Television", "medium", ["Wheel of Fortune", "game shows", "ITV"], [
 ("The first UK host", "Nicky Campbell", ["Nicky Byrne", "Nick Knowles", "Nick Owen"]),
 ("The host who took over in 1997", "Bradley Walsh", ["Ben Shephard", "Stephen Mulhern", "Paddy McGuinness"]),
 ("The host after him", "John Leslie", ["John Barrowman", "John Craven", "John Sergeant"]),
 ("The letter-turner who went on to Changing Rooms", "Carol Smillie", ["Carol Vorderman", "Carol Kirkwood", "Carol Decker"]),
 ("Another letter-turner of the 1990s", "Jenny Powell", ["Jenny Eclair", "Jenny Ryan", "Jenny Falconer"]),
 ("The host of the 2024 revival", "Graham Norton", ["Alan Carr", "Rob Brydon", "Jason Manford"]),
 ("The channel", "ITV", ["BBC One", "Channel 4", "Channel 5"]),
 ("The ITV company that made it", "Scottish Television", ["Granada", "Tyne Tees", "Border"]),
 ("The year it began in the UK", "1988", ["1984", "1992", "1996"]),
 ("The year the original UK run ended", "2001", ["1997", "2004", "2008"]),
 ("What contestants solve", "A hidden phrase", ["A riddle", "A sum", "A picture"]),
 ("What you have to pay for", "Vowels", ["Consonants", "Clues", "Spins"]),
 ("The wedge that loses all your money", "Bankrupt", ["Broke", "Bust", "Wipeout"]),
 ("The wedge that just ends your go", "Lose a Turn", ["Pass", "Skip", "Miss a Go"]),
 ("The year the American original began", "1975", ["1969", "1980", "1985"]),
 ("The man who created it", "Merv Griffin", ["Chuck Barris", "Mark Goodson", "Bob Stewart"]),
 ("His other famous quiz", "Jeopardy!", ["Family Feud", "Card Sharks", "Hollywood Squares"]),
 ("The long-time American host", "Pat Sajak", ["Pat Sharp", "Pat Kenny", "Pat Morita"]),
 ("His letter-turning co-star", "Vanna White", ["Vicki Lawrence", "Valerie Bertinelli", "Vanessa Williams"]),
 ("The free letters in the American bonus round", "R, S, T, L, N and E", ["A, E, I, O, U and Y", "S, T, R, A, N and D", "E, T, A, O, I and N"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-252.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
