# Bank session 19 Oct 2026: 2 sitcom races -> bank/race-253.json (The Inbetweeners; Yes Minister).
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

race("The Inbetweeners - name it", "Television", "medium", ["The Inbetweeners", "sitcoms", "E4"], [
 ("The new boy who narrates it", "Will McKenzie", ["Will Mellor", "Will Young", "Will Poulter"]),
 ("The actor who plays him", "Simon Bird", ["Simon Amstell", "Simon Pegg", "Simon Callow"]),
 ("The actor who plays Simon", "Joe Thomas", ["Joe Wilkinson", "Joe Lycett", "Joe Swash"]),
 ("The actor who plays Jay", "James Buckley", ["James Corden", "James Acaster", "James Blunt"]),
 ("The actor who plays Neil", "Blake Harrison", ["Ralf Little", "Marc Wootton", "Tom Rosenthal"]),
 ("Will's mum", "Polly McKenzie", ["Pam McKenzie", "Penny McKenzie", "Paula McKenzie"]),
 ("Jay's dad, played by David Schaal", "Terry Cartwright", ["Tony Cartwright", "Trevor Cartwright", "Terry Sutherland"]),
 ("The girl Simon pines for", "Carli D'Amato", ["Kerry Hughes", "Carla Daniels", "Chloe Ashton"]),
 ("The head of sixth form", "Mr Gilbert", ["Mr Gibbs", "Mr Gilby", "Mr Garrett"]),
 ("The actor who plays him", "Greg Davies", ["Greg James", "Greg Rusedski", "Greg Wise"]),
 ("Their school", "Rudge Park Comprehensive", ["Grange Hill", "Waterloo Road", "Hollins Park"]),
 ("Simon's car", "Yellow Fiat Cinquecento", ["Red Mini Metro", "Blue Ford Fiesta", "Green Nissan Micra"]),
 ("The channel", "E4", ["BBC Three", "ITV2", "Channel 5"]),
 ("The year it began", "2008", ["2004", "2012", "2015"]),
 ("Series made", "3", ["2", "4", "5"]),
 ("The year of the first film", "2011", ["2009", "2013", "2016"]),
 ("Where the boys holiday in it", "Malia", ["Magaluf", "Ayia Napa", "Faliraki"]),
 ("Where they go in the 2014 sequel", "Australia", ["Thailand", "USA", "Spain"]),
 ("The writers", "Iain Morris and Damon Beesley", ["Ricky Gervais and Stephen Merchant", "Steve Coogan and Armando Iannucci", "Simon Pegg and Edgar Wright"]),
 ("The US channel that remade it", "MTV", ["HBO", "NBC", "Fox"])])

race("Yes Minister - name it", "Television", "medium", ["Yes Minister", "sitcoms", "BBC"], [
 ("The minister", "Jim Hacker", ["Jim Bergerac", "Jim Trott", "Jim Hawkins"]),
 ("The actor who plays him", "Paul Eddington", ["Paul Daniels", "Paul Merton", "Paul Whitehouse"]),
 ("His wife", "Annie", ["Mary", "Elizabeth", "Judy"]),
 ("His party", "Never said", ["Labour", "Conservative", "Liberal"]),
 ("The Permanent Secretary", "Sir Humphrey Appleby", ["Sir Humphrey Hawkins", "Sir Humphrey Ashby", "Sir Humphrey Appleton"]),
 ("The actor who plays him", "Nigel Hawthorne", ["Nigel Havers", "Nigel Planer", "Nigel Kennedy"]),
 ("That actor's Oscar-nominated film role", "The Madness of King George", ["The King's Speech", "Mrs Brown", "Amadeus"]),
 ("The private secretary", "Bernard Woolley", ["Bernard Bresslaw", "Bernard Manning", "Bernard Black"]),
 ("The actor who plays him", "Derek Fowlds", ["Derek Jacobi", "Derek Nimmo", "Derek Griffiths"]),
 ("The department", "Administrative Affairs", ["Home Affairs", "Foreign Affairs", "Social Affairs"]),
 ("The word Sir Humphrey uses for a doomed decision", "Courageous", ["Bold", "Brave", "Daring"]),
 ("The sequel", "Yes, Prime Minister", ["No, Prime Minister", "Yes, Chancellor", "Yes, Your Majesty"]),
 ("The writers", "Antony Jay and Jonathan Lynn", ["Galton and Simpson", "Clement and La Frenais", "Croft and Perry"]),
 ("The channel", "BBC Two", ["BBC One", "ITV", "Channel 4"]),
 ("The year it began", "1980", ["1976", "1984", "1988"]),
 ("Series made", "3", ["2", "4", "5"]),
 ("Episodes in each series", "7", ["6", "8", "10"]),
 ("The Prime Minister who said it was her favourite", "Margaret Thatcher", ["Harold Wilson", "John Major", "Tony Blair"]),
 ("The channel that revived it in 2013", "Gold", ["Dave", "BBC Four", "Sky Arts"]),
 ("The revival's Jim Hacker", "David Haig", ["David Mitchell", "David Tennant", "David Jason"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-253.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
