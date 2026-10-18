# Bank session 18 Oct 2026: 2 game-show races -> bank/race-243.json (Blockbusters; The Generation Game).
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

race("Blockbusters - name it", "Television", "medium", ["Blockbusters", "game shows", "ITV"], [
 ("The original host", "Bob Holness", ["Bob Monkhouse", "Bob Carolgees", "Bob Wilson"]),
 ("The request everyone remembers", "I'll have a P please, Bob", ["Can I buy a vowel?", "Is that your final answer?", "Come on down!"]),
 ("The channel", "ITV", ["BBC One", "Channel 4", "BBC Two"]),
 ("The year it began", "1983", ["1979", "1987", "1990"]),
 ("The year the original ITV run ended", "1993", ["1989", "1997", "2001"]),
 ("The shape of each space on the board", "Hexagon", ["Square", "Triangle", "Circle"]),
 ("Spaces on the board", "20", ["16", "25", "30"]),
 ("What each space showed", "A letter", ["A number", "A picture", "A colour"]),
 ("Players in each game", "3", ["4", "5", "6"]),
 ("Who the contestants were", "Sixth-formers", ["Pensioners", "Married couples", "Celebrities"]),
 ("The dance they did at the end", "The hand jive", ["The Macarena", "The YMCA", "The twist"]),
 ("The final round", "Gold Run", ["Hot Run", "Speed Run", "Final Run"]),
 ("Seconds for that final round", "60", ["30", "45", "90"]),
 ("Where the format came from", "USA", ["Australia", "Canada", "Netherlands"]),
 ("The ITV company that made it", "Central", ["Granada", "Thames", "LWT"]),
 ("The host of the 1997 Sky One version", "Michael Aspel", ["Michael Barrymore", "Michael Parkinson", "Michael Ball"]),
 ("The host of the 2012 Challenge revival", "Simon Mayo", ["Simon Amstell", "Simon Cowell", "Simon Bates"]),
 ("The host of the 2019 Comedy Central revival", "Dara Ó Briain", ["Jimmy Carr", "Rob Brydon", "Alan Carr"]),
 ("The famous role the first host once played on radio", "James Bond", ["Sherlock Holmes", "Dick Barton", "Paul Temple"]),
 ("The panel show he later hosted on the BBC", "Call My Bluff", ["Going for Gold", "Catchphrase", "Countdown"])])

race("The Generation Game - name it", "Television", "medium", ["The Generation Game", "game shows", "BBC"], [
 ("The first host", "Bruce Forsyth", ["Des O'Connor", "Bob Monkhouse", "Tom O'Connor"]),
 ("His co-host and wife in the 1970s", "Anthea Redfern", ["Wilnelia Merced", "Gloria Hunniford", "Jan Leeming"]),
 ("What he asked her to do", "Give us a twirl", ["Show us a smile", "Give us a wave", "Take a bow"]),
 ("His famous greeting", "Nice to see you, to see you nice!", ["Hello, good evening and welcome", "Hi-de-hi!", "Evening, all"]),
 ("His two-word line, said twice", "Good game, good game", ["Super, smashing, great!", "Lovely jubbly!", "Pass the sick bag!"]),
 ("The statue pose he struck", "The Thinker", ["The Salute", "The Bow", "The Wave"]),
 ("The host who took over in 1978", "Larry Grayson", ["Danny La Rue", "Frankie Howerd", "Kenneth Williams"]),
 ("His catchphrase", "Shut that door!", ["Ooh, you are awful!", "Hello, possums!", "I'm free!"]),
 ("His imaginary friend", "Everard", ["Ernest", "Edward", "Eric"]),
 ("His co-host", "Isla St Clair", ["Isla Fisher", "Lulu", "Sheena Easton"]),
 ("Forsyth's co-host when he came back in 1990", "Rosemarie Ford", ["Debbie McGee", "Sally Gunnell", "Su Pollard"]),
 ("The host from 1995", "Jim Davidson", ["Jim Bowen", "Jimmy Tarbuck", "Jim Moir"]),
 ("The pair who hosted the 2018 revival", "Mel and Sue", ["Ant and Dec", "French and Saunders", "Vic and Bob"]),
 ("Who made up each team", "Two relatives from different generations", ["Two neighbours", "Two workmates", "A boss and an employee"]),
 ("Teams on each show", "4", ["2", "5", "6"]),
 ("The prize everyone remembers", "A cuddly toy", ["A teasmade", "A fondue set", "A carriage clock"]),
 ("What the prizes went past on in the final", "A conveyor belt", ["A revolving stage", "A spinning wheel", "A moving staircase"]),
 ("The channel", "BBC One", ["ITV", "BBC Two", "Channel 4"]),
 ("The year it began", "1971", ["1968", "1975", "1979"]),
 ("The country the format came from", "Netherlands", ["Germany", "USA", "Belgium"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-243.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
