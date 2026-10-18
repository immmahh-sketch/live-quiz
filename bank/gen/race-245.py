# Bank session 18 Oct 2026: 2 game-show races -> bank/race-245.json (Deal or No Deal; The Weakest Link).
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

race("Deal or No Deal - name it", "Television", "medium", ["Deal or No Deal", "game shows", "Channel 4"], [
 ("The original host", "Noel Edmonds", ["Noel Fielding", "Noel Gallagher", "Noel Clarke"]),
 ("The original channel", "Channel 4", ["BBC One", "Sky One", "Channel 5"]),
 ("The year it began", "2005", ["2001", "2008", "2011"]),
 ("The year the original run ended", "2016", ["2013", "2019", "2021"]),
 ("Sealed boxes in each game", "22", ["20", "24", "26"]),
 ("The top prize", "£250,000", ["£100,000", "£500,000", "£1,000,000"]),
 ("The smallest amount in a box", "1p", ["£1", "10p", "50p"]),
 ("The unseen figure making offers", "The Banker", ["The Bank Manager", "The Dealer", "The Broker"]),
 ("What the host took his calls on", "An old-fashioned phone", ["A walkie-talkie", "A pager", "A laptop"]),
 ("What the Banker sometimes offered instead of cash", "A swap", ["A holiday", "A car", "A second chance"]),
 ("The colour of the big amounts on the board", "Red", ["Blue", "Green", "Gold"]),
 ("The city where it was filmed", "Bristol", ["Manchester", "Glasgow", "Cardiff"]),
 ("The country the format came from", "Netherlands", ["Germany", "USA", "Australia"]),
 ("The company that made it", "Endemol", ["Talkback", "Hat Trick", "Celador"]),
 ("The host of the revival", "Stephen Mulhern", ["Stephen Fry", "Stephen Merchant", "Stephen Mangan"]),
 ("The revival's channel", "ITV", ["BBC Two", "E4", "Dave"]),
 ("The year of the revival", "2023", ["2018", "2020", "2025"]),
 ("The original host's Saturday-night show of the 1990s", "Noel's House Party", ["Noel's Big Night", "Noel's Saturday Show", "Noel's Party Time"]),
 ("The pink spotty character from that show", "Mr Blobby", ["Mr Tumble", "Mr Motivator", "Mr Benn"]),
 ("The original host's Saturday-morning kids' show", "Multi-Coloured Swap Shop", ["Tiswas", "Saturday Superstore", "Going Live!"])])

race("The Weakest Link - name it", "Television", "medium", ["The Weakest Link", "quiz shows", "BBC"], [
 ("The original host", "Anne Robinson", ["Anne Diamond", "Anne Hegerty", "Ann Widdecombe"]),
 ("Her famous line", "You are the weakest link. Goodbye!", ["Off you pop!", "You're fired!", "Better luck next time!"]),
 ("Her nickname", "The Queen of Mean", ["The Iron Lady", "The Ice Queen", "Lady Grim"]),
 ("How she signed off each show", "A wink", ["A salute", "A bow", "A wave"]),
 ("The channel it started on", "BBC Two", ["ITV", "Channel 4", "Channel 5"]),
 ("The year it began", "2000", ["1997", "2003", "2006"]),
 ("The year the original run ended", "2012", ["2008", "2015", "2018"]),
 ("The host of the 2021 revival", "Romesh Ranganathan", ["Rob Beckett", "Rhod Gilbert", "Russell Howard"]),
 ("Players at the start of the original show", "9", ["6", "8", "10"]),
 ("The word you shout to save the money", "Bank", ["Save", "Keep", "Stop"]),
 ("What the ladder of cash amounts is called", "The chain", ["The ladder", "The tower", "The pyramid"]),
 ("What a wrong answer does to the unbanked money", "Wipes it out", ["Doubles it", "Halves it", "Freezes it"]),
 ("The most a team could bank in one round of the original", "£1,000", ["£500", "£2,000", "£5,000"]),
 ("How players are knocked out", "A vote", ["A buzzer race", "A coin toss", "Points"]),
 ("The player with the best stats in a round", "The strongest link", ["The top link", "The golden link", "The safest link"]),
 ("Questions each in the final head-to-head", "5", ["3", "7", "12"]),
 ("The voice-over man of the original", "Jon Briggs", ["Peter Dickson", "Charles Foster", "John Sachs"]),
 ("The country where the format was created", "Britain", ["USA", "Netherlands", "Australia"]),
 ("The original host's consumer show", "Watchdog", ["Rogue Traders", "Crimewatch", "That's Life!"]),
 ("The quiz she took over in 2021", "Countdown", ["Pointless", "Eggheads", "Tipping Point"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-245.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
