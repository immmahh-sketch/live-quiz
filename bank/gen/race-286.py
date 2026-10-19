# Bank session 19 Oct 2026: 2 races -> bank/race-286.json (All Creatures Great and Small; Crossroads).
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

race("All Creatures Great and Small - name it", "Television", "medium", ["All Creatures Great and Small", "TV drama", "Yorkshire"], [
 ("The vet who wrote the books", "James Herriot", ["Gerald Durrell", "Laurie Lee", "Thomas Hardy"]),
 ("His real name", "Alf Wight", ["Alf Garnett", "Alf Roberts", "Alf Stewart"]),
 ("The real town where he worked", "Thirsk", ["Ripon", "Malton", "Richmond"]),
 ("The made-up town in the books", "Darrowby", ["Aidensfield", "Beckindale", "Causton"]),
 ("The practice's house", "Skeldale House", ["Nonnatus House", "Harewood House", "Castle Howard"]),
 ("The senior vet", "Siegfried Farnon", ["Sebastian Farnon", "Stanley Farnon", "Simon Farnon"]),
 ("His younger brother", "Tristan", ["Tobias", "Timothy", "Theo"]),
 ("The housekeeper", "Mrs Hall", ["Mrs Mangel", "Mrs Hudson", "Mrs Overall"]),
 ("The pampered Pekinese", "Tricki Woo", ["Gnasher", "Wellard", "Buddy"]),
 ("The dog's owner", "Mrs Pumphrey", ["Mrs Bucket", "Mrs Brown", "Mrs Slocombe"]),
 ("The woman James marries", "Helen", ["Hilda", "Hannah", "Harriet"]),
 ("The channel of the original series", "BBC One", ["ITV", "BBC Two", "Channel 4"]),
 ("The year the original series began", "1978", ["1972", "1983", "1988"]),
 ("The actor who played James in the original", "Christopher Timothy", ["Christopher Eccleston", "Christopher Biggins", "Christopher Ellison"]),
 ("The actor who played Siegfried in the original", "Robert Hardy", ["Robert Lindsay", "Robert Powell", "Robert Bathurst"]),
 ("The future Doctor Who who played Tristan", "Peter Davison", ["Tom Baker", "Colin Baker", "Sylvester McCoy"]),
 ("The channel of the remake", "Channel 5", ["Sky One", "ITV2", "Dave"]),
 ("The year the remake began", "2020", ["2016", "2018", "2022"]),
 ("The remake's James", "Nicholas Ralph", ["Nicholas Hoult", "Nicholas Lyndhurst", "Nicholas Farrell"]),
 ("The remake's Siegfried", "Samuel West", ["Timothy West", "Samuel Anderson", "Simon Callow"])])

race("Crossroads - name it", "Television", "medium", ["Crossroads", "soaps", "ITV"], [
 ("The business at its heart", "A motel", ["A pub", "A hospital", "A holiday camp"]),
 ("The part of England", "The Midlands", ["Yorkshire", "Cornwall", "East Anglia"]),
 ("The city its studios were in", "Birmingham", ["London", "Manchester", "Leeds"]),
 ("The village", "King's Oak", ["Beckindale", "Walford", "Ambridge"]),
 ("The ITV company that made it", "ATV", ["Granada", "Thames", "Yorkshire Television"]),
 ("The channel", "ITV", ["BBC One", "Channel 4", "BBC Two"]),
 ("The year it began", "1964", ["1960", "1968", "1972"]),
 ("The year the original run ended", "1988", ["1981", "1993", "1999"]),
 ("The year of the short-lived revival", "2001", ["1995", "2005", "2010"]),
 ("The actress who played motel owner Meg", "Noele Gordon", ["Pat Phoenix", "Violet Carson", "Doris Speed"]),
 ("How Meg left in 1981", "On the QE2", ["On a plane", "In a hearse", "On a horse"]),
 ("The simple handyman in the woolly hat", "Benny", ["Trigger", "Compo", "Barney"]),
 ("The actor who played him", "Paul Henry", ["Paul Daniels", "Paul Shane", "Paul Nicholas"]),
 ("What he called Diane", "Miss Diane", ["Lady Di", "Princess", "Duchess"]),
 ("Meg's son who used a wheelchair", "Sandy", ["Sammy", "Stanley", "Sidney"]),
 ("The gossipy cleaner", "Amy Turtle", ["Hilda Ogden", "Ena Sharples", "Dot Cotton"]),
 ("The theme tune composer", "Tony Hatch", ["Ron Grainer", "Harry South", "Laurie Johnson"]),
 ("The band who recorded a version of the theme", "Wings", ["The Beatles", "Queen", "ELO"]),
 ("What it was mocked for", "Wobbly sets", ["Huge budgets", "Car chases", "Celebrity cameos"]),
 ("Victoria Wood's spoof of it", "Acorn Antiques", ["Dinnerladies", "Bread", "Butterflies"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-286.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
