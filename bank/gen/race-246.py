# Bank session 18 Oct 2026: 2 game-show races -> bank/race-246.json (Play Your Cards Right; The Price Is Right).
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

race("Play Your Cards Right - name it", "Television", "medium", ["Play Your Cards Right", "game shows", "ITV"], [
 ("The host", "Bruce Forsyth", ["Bob Monkhouse", "Les Dennis", "Jim Davidson"]),
 ("The year it began", "1980", ["1976", "1984", "1988"]),
 ("The year the first run ended", "1987", ["1983", "1990", "1993"]),
 ("The year it first came back", "1994", ["1990", "1998", "2001"]),
 ("The channel", "ITV", ["BBC One", "BBC Two", "Channel 4"]),
 ("The ITV company that made it", "LWT", ["Thames", "Granada", "Central"]),
 ("The American show it came from", "Card Sharks", ["Card Kings", "High Card", "Deal Me In"]),
 ("What the audience shouted", "Higher or lower", ["Twist or stick", "Deal or no deal", "Snap or swap"]),
 ("The glamorous card turners", "The Dolly Dealers", ["The Card Girls", "The Lovely Lucys", "The Queens of Hearts"]),
 ("Who played", "Couples", ["Families", "Workmates", "Neighbours"]),
 ("Teams on each show", "2", ["3", "4", "5"]),
 ("Where the ace ranked", "Highest", ["Lowest", "Wild", "Bonus"]),
 ("The star prize", "A car", ["A speedboat", "A caravan", "A holiday"]),
 ("What you got for a pair", "Nothing", ["Double points", "A bonus card", "A free go"]),
 ("'What do points make?'", "Prizes!", ["Points!", "Money!", "Winners!"]),
 ("The host's name for an extra treat", "Brucie Bonus", ["Bruce's Box", "Forsyth Fortune", "Lucky Bruce"]),
 ("The host's line praising the losers", "Didn't they do well!", ["Weren't they wonderful!", "What a pair!", "Give them a hand!"]),
 ("His famous greeting", "Nice to see you, to see you nice!", ["Hello, good evening and welcome", "Hi-de-hi!", "Evening, all"]),
 ("The year he was knighted", "2011", ["2005", "2014", "2017"]),
 ("The year he started hosting Strictly", "2004", ["2000", "2008", "2010"])])

race("The Price Is Right - name it", "Television", "medium", ["The Price Is Right", "game shows", "ITV"], [
 ("The first UK host", "Leslie Crowther", ["Les Dennis", "Leslie Phillips", "Lionel Blair"]),
 ("His famous call", "Come on down!", ["Come on in!", "Step right up!", "Get on down!"]),
 ("His earlier children's show", "Crackerjack", ["Blue Peter", "Magpie", "Tiswas"]),
 ("The year it began in the UK", "1984", ["1979", "1990", "1996"]),
 ("The year his run ended", "1988", ["1986", "1992", "1995"]),
 ("The channel", "ITV", ["BBC One", "BBC Two", "Channel 4"]),
 ("The ITV company that made it", "Central", ["Granada", "Thames", "Anglia"]),
 ("The host of the 1989 Sky version", "Bob Warman", ["Bob Holness", "Bob Wilson", "Bob Carolgees"]),
 ("The host in the mid-1990s", "Bruce Forsyth", ["Des O'Connor", "Bob Monkhouse", "Jim Davidson"]),
 ("The host from 2006", "Joe Pasquale", ["Joe Swash", "Joe Lycett", "Joe Wicks"]),
 ("The reality show that host had won", "I'm a Celebrity", ["Strictly Come Dancing", "Big Brother", "Dancing on Ice"]),
 ("The comedian who revived it in his Epic Gameshow", "Alan Carr", ["Jimmy Carr", "Rob Brydon", "Paddy McGuinness"]),
 ("The American host for 35 years", "Bob Barker", ["Bob Hope", "Bob Newhart", "Bob Saget"]),
 ("His American successor", "Drew Carey", ["Jim Carrey", "Steve Carell", "Tim Allen"]),
 ("Where the format came from", "USA", ["Netherlands", "Australia", "Canada"]),
 ("What contestants had to guess", "The price of prizes", ["The weight of prizes", "The age of antiques", "The size of rooms"]),
 ("The golden rule when you bid", "Don't go over the price", ["Don't go under the price", "Never bid zero", "Never bid twice"]),
 ("Where the picked contestants stood", "Contestants' Row", ["Bidders' Bench", "Price Row", "The Front Line"]),
 ("The big wheel round", "Showcase Showdown", ["Wheel Deal", "Spin to Win", "Big Wheel Bonanza"]),
 ("The final round", "The Showcase", ["The Big Shop", "The Grand Finale", "The Final Price"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-246.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
