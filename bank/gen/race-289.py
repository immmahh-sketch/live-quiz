# Bank session 19 Oct 2026: 2 races -> bank/race-289.json (Broadchurch; Poldark).
# Neither show had a race in the live bank. Checked against every live race with lqsql/audit/race-overlap-live.py before importing.
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

race("Broadchurch - name it", "Television", "medium", ["Broadchurch", "TV drama", "ITV"], [
 ("The detective brought in from outside", "DI Alec Hardy", ["DI Jack Frost", "DI Tom Barnaby", "DI Jim Bergerac"]),
 ("The actor who played him", "David Tennant", ["David Jason", "David Morrissey", "David Mitchell"]),
 ("His health problem", "A heart condition", ["A bad back", "Diabetes", "Asthma"]),
 ("His local partner", "DS Ellie Miller", ["DS Kate Fleming", "DS Jackie Reid", "DS Lindsay Denton"]),
 ("The actress who played her", "Olivia Colman", ["Olivia Williams", "Olivia Newton-John", "Olivia Cooke"]),
 ("The boy whose death starts the story", "Danny Latimer", ["Danny Miller", "Danny Baker", "Danny Mitchell"]),
 ("His mother", "Beth Latimer", ["Beth Jordache", "Beth Tyler", "Beth Smith"]),
 ("The actress who played her", "Jodie Whittaker", ["Jodie Comer", "Jodie Foster", "Jodie Prenger"]),
 ("The famous role she took on later", "The Thirteenth Doctor", ["Lara Croft", "Wonder Woman", "Miss Marple"]),
 ("Who turned out to be the killer", "Joe Miller", ["Mark Latimer", "Nigel Carter", "Paul Coates"]),
 ("The writer who created it", "Chris Chibnall", ["Chris Lang", "Steven Moffat", "Jed Mercurio"]),
 ("The show that writer went on to run", "Doctor Who", ["Sherlock", "Line of Duty", "Torchwood"]),
 ("The county it's set in", "Dorset", ["Devon", "Cornwall", "Somerset"]),
 ("The beach with the famous golden cliffs", "West Bay", ["Lulworth Cove", "Durdle Door", "Beachy Head"]),
 ("The Icelandic composer of the music", "Ólafur Arnalds", ["Max Richter", "Hans Zimmer", "Ludovico Einaudi"]),
 ("The channel", "ITV", ["BBC One", "Channel 4", "Sky One"]),
 ("The year it began", "2013", ["2009", "2016", "2019"]),
 ("The year the final series aired", "2017", ["2015", "2019", "2021"]),
 ("Series made", "3", ["2", "4", "5"]),
 ("The American remake", "Gracepoint", ["Graceland", "Gracemoor", "Gracefield"])])

race("Poldark - name it", "Television", "medium", ["Poldark", "TV drama", "BBC", "Cornwall"], [
 ("Poldark's first name", "Ross", ["Rob", "Rick", "Roy"]),
 ("The county it's set in", "Cornwall", ["Devon", "Dorset", "Somerset"]),
 ("The century it's set in", "The 18th century", ["The 17th century", "The 19th century", "The 20th century"]),
 ("The war Ross comes home from", "American War of Independence", ["Napoleonic Wars", "Crimean War", "Boer War"]),
 ("The business he tries to revive", "Tin mining", ["Fishing", "Farming", "Smuggling"]),
 ("The novelist who created him", "Winston Graham", ["Daphne du Maurier", "Thomas Hardy", "Catherine Cookson"]),
 ("The actor who played him in 2015", "Aidan Turner", ["Aidan Gillen", "Richard Armitage", "Tom Hughes"]),
 ("The actor who played him in the 1970s", "Robin Ellis", ["Robin Askwith", "Robin Nedwell", "Robert Powell"]),
 ("The famous shirtless scene", "Scything a field", ["Fencing on a cliff", "Rowing to France", "Dancing at a ball"]),
 ("His wife", "Demelza", ["Delilah", "Desdemona", "Daisy"]),
 ("What she was when he first took her in", "A kitchen maid", ["A governess", "A nurse", "A cook"]),
 ("Her dog", "Garrick", ["Gnasher", "Wellard", "Buddy"]),
 ("The actress who played her in 2015", "Eleanor Tomlinson", ["Eleanor Bron", "Emilia Clarke", "Ellie Kendrick"]),
 ("Ross's first love", "Elizabeth", ["Emma", "Eleanor", "Edith"]),
 ("His cousin, who marries her", "Francis", ["Frank", "Freddie", "Felix"]),
 ("His great rival", "George Warleggan", ["George Wickham", "George Knightley", "George Osborne"]),
 ("The channel", "BBC One", ["ITV", "Channel 4", "Sky One"]),
 ("The year the original series began", "1975", ["1970", "1981", "1987"]),
 ("The year the remake began", "2015", ["2011", "2018", "2020"]),
 ("Series in the remake", "5", ["3", "4", "6"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-289.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
