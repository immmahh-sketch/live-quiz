# Bank session 18 Oct 2026: 2 quiz-show races -> bank/race-242.json (Pointless; Mastermind).
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

race("Pointless - name it", "Television", "medium", ["Pointless", "game shows", "BBC"], [
 ("The host", "Alexander Armstrong", ["Hugh Dennis", "Jack Dee", "Nick Hancock"]),
 ("His sidekick, who also dreamed it up", "Richard Osman", ["Richard Ayoade", "Richard Herring", "Richard Bacon"]),
 ("The channel it started on", "BBC Two", ["BBC One", "ITV", "Channel 4"]),
 ("The year it began", "2009", ["2005", "2012", "2014"]),
 ("The score you're hoping for", "0", ["50", "10", "1"]),
 ("Points for a wrong answer", "100", ["50", "10", "1"]),
 ("What a right answer nobody in the survey gave is called", "A pointless answer", ["A golden answer", "A double answer", "A blank answer"]),
 ("Pairs of contestants at the start of a show", "4", ["3", "5", "6"]),
 ("The star-guest version", "Pointless Celebrities", ["Pointless Stars", "Pointless Plus", "Famous Pointless"]),
 ("The company that made it", "Endemol", ["Talkback", "Hat Trick", "Mentorn"]),
 ("The host's comedy double-act partner", "Ben Miller", ["David Mitchell", "Robert Webb", "Hugh Laurie"]),
 ("The school the host went to", "Eton", ["Harrow", "Winchester", "Rugby"]),
 ("The radio station where the host presents", "Classic FM", ["Radio 2", "Smooth", "Magic"]),
 ("The cartoon hero the host voiced in the 2015 reboot", "Danger Mouse", ["Count Duckula", "Bananaman", "SuperTed"]),
 ("Osman's height, often joked about", "6 ft 7 in", ["6 ft 1 in", "6 ft 4 in", "7 ft 0 in"]),
 ("Osman's job at the company before he went on screen", "Creative director", ["Floor manager", "Lawyer", "Accountant"]),
 ("Osman's own BBC quiz from 2017", "House of Games", ["Mind Games", "Home Games", "Board Games"]),
 ("Osman's best-selling crime series", "The Thursday Murder Club", ["The Cuckoo's Calling", "The No. 1 Ladies' Detective Agency", "The Seven Deaths of Evelyn Hardcastle"]),
 ("The year the first of those books came out", "2020", ["2016", "2018", "2022"]),
 ("The band of Osman's brother Mat", "Suede", ["Blur", "Pulp", "Elastica"])])

race("Mastermind - name it", "Television", "medium", ["Mastermind", "quiz shows", "BBC"], [
 ("The first host", "Magnus Magnusson", ["Michael Aspel", "Robert Robinson", "Bamber Gascoigne"]),
 ("His famous line when the buzzer went mid-question", "I've started, so I'll finish", ["Your time starts now", "Fingers on buzzers", "Let's play"]),
 ("The year he hosted his last show", "1997", ["1990", "1994", "2001"]),
 ("The city he was born in", "Reykjavík", ["Oslo", "Copenhagen", "Helsinki"]),
 ("His broadcaster daughter", "Sally Magnusson", ["Sally Phillips", "Sally Gunnell", "Sally Lindsay"]),
 ("The host when it moved to Radio 4 in 1998", "Peter Snow", ["Dan Snow", "Nicholas Parsons", "Ned Sherrin"]),
 ("The host from 2003 to 2021", "John Humphrys", ["John Simpson", "Jon Snow", "John Craven"]),
 ("The host since 2021", "Clive Myrie", ["Clive Anderson", "Clive James", "Clive Owen"]),
 ("The year it began", "1972", ["1968", "1978", "1982"]),
 ("The man who created it", "Bill Wright", ["Bill Cotton", "Bill Oddie", "Bill Paterson"]),
 ("The wartime experience that inspired it", "Being questioned as a prisoner of war", ["Codebreaking at Bletchley Park", "Flying with the Dambusters", "Serving on a submarine"]),
 ("The colour of the famous chair", "Black", ["Red", "Brown", "Green"]),
 ("The two rounds", "Specialist subject and general knowledge", ["Pictures and music", "Quickfire and buzzers", "Spelling and numbers"]),
 ("What you say to skip a question", "Pass", ["Next", "Skip", "Unsure"]),
 ("Contenders in a heat", "4", ["3", "5", "6"]),
 ("The prize the champion takes home", "A glass bowl", ["A silver cup", "A gold medal", "A crystal globe"]),
 ("The London cabbie who won in 1980", "Fred Housego", ["Fred Dibnah", "Fred Elliott", "Fred Talbot"]),
 ("The channel it's on today", "BBC Two", ["ITV", "Channel 4", "BBC Four"]),
 ("The theme tune", "Approaching Menace", ["Night on Bald Mountain", "Mars, the Bringer of War", "Toccata and Fugue"]),
 ("The version for children", "Junior Mastermind", ["Mastermind Kids", "Little Mastermind", "Mini Mastermind"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-242.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
