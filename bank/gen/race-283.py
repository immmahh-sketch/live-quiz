# Bank session 19 Oct 2026: 2 races -> bank/race-283.json (The Professionals; Home and Away).
# Neither show had a race in the live bank. Checked against every live race with lqsql/audit/race-overlap-live.py before importing.
# The overlap check notes The Sweeney race uses Lewis Collins, Martin Shaw and Laurie Johnson as wrong options; avoid both races on one night.
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

race("The Professionals - name it", "Television", "medium", ["The Professionals", "TV drama", "ITV"], [
 ("The actor who played Bodie", "Lewis Collins", ["Dennis Waterman", "Michael Elphick", "Patrick Mower"]),
 ("The actor who played Doyle", "Martin Shaw", ["Gareth Hunt", "Ian McShane", "John Thaw"]),
 ("Doyle's first name", "Ray", ["Rob", "Rick", "Ron"]),
 ("What Bodie did before", "Soldier", ["Boxer", "Teacher", "Fireman"]),
 ("What Doyle did before", "Policeman", ["Boxer", "Teacher", "Fireman"]),
 ("Their boss", "Cowley", ["Haskins", "Mullett", "Strange"]),
 ("The boss's first name", "George", ["Gordon", "Graham", "Gerald"]),
 ("The actor who played him", "Gordon Jackson", ["Patrick Malahide", "Garfield Morgan", "Bruce Alexander"]),
 ("That actor's earlier role as the butler Hudson", "Upstairs, Downstairs", ["Downton Abbey", "The Forsyte Saga", "Brideshead Revisited"]),
 ("The squad they worked for", "CI5", ["MI5", "CID", "Special Branch"]),
 ("What CI5 stands for", "Criminal Intelligence 5", ["Central Investigation 5", "Crime Investigation 5", "Counter Intelligence 5"]),
 ("The car most linked to the show", "Ford Capri", ["Jaguar Mark 2", "Mini Cooper", "Austin Allegro"]),
 ("The channel", "ITV", ["BBC One", "BBC Two", "Channel 4"]),
 ("The ITV company it was made for", "LWT", ["Thames", "Granada", "Central"]),
 ("The year it began", "1977", ["1972", "1981", "1985"]),
 ("The year it ended", "1983", ["1979", "1987", "1990"]),
 ("The writer who created it", "Brian Clemens", ["Robert Banks Stewart", "Glenn Chandler", "Geoff McQueen"]),
 ("The theme tune composer", "Laurie Johnson", ["Harry South", "Ron Grainer", "Tony Hatch"]),
 ("Martin Shaw's later judge", "Judge John Deed", ["Kavanagh QC", "Rumpole of the Bailey", "Silk"]),
 ("Martin Shaw's 1960s North East detective", "Inspector George Gently", ["DCI Banks", "Inspector Lynley", "Inspector Wexford"])])

race("Home and Away - name it", "Television", "medium", ["Home and Away", "soaps", "Australia"], [
 ("The town it's set in", "Summer Bay", ["Erinsborough", "Byron Bay", "Bondi"]),
 ("The state", "New South Wales", ["Victoria", "Queensland", "Western Australia"]),
 ("The city it's filmed near", "Sydney", ["Melbourne", "Brisbane", "Perth"]),
 ("The real beach used for filming", "Palm Beach", ["Manly Beach", "Bondi Beach", "Coogee Beach"]),
 ("The year it began", "1988", ["1983", "1992", "1996"]),
 ("Its Australian channel", "Seven Network", ["Network Ten", "Nine Network", "ABC"]),
 ("Its first UK channel", "ITV", ["BBC One", "Channel 4", "Sky One"]),
 ("Its UK channel now", "Channel 5", ["ITV2", "Sky One", "E4"]),
 ("The foster parents it began with", "Tom and Pippa Fletcher", ["Karl and Susan Kennedy", "Harold and Madge Bishop", "Ken and Deirdre Barlow"]),
 ("What the Fletchers ran", "A caravan park", ["A surf shop", "A diner", "A pub"]),
 ("What Alf Stewart runs", "A bait shop", ["A surf shop", "A diner", "A pub"]),
 ("Alf's favourite insult", "Flamin' galah", ["Strewth", "Fair dinkum", "Crikey"]),
 ("The actor who plays Alf", "Ray Meagher", ["Ian Smith", "Alan Dale", "Stefan Dennis"]),
 ("The actress who played Sally Fletcher", "Kate Ritchie", ["Kylie Minogue", "Natalie Imbruglia", "Delta Goodrem"]),
 ("Long-serving Irene's surname", "Roberts", ["Mangel", "Bishop", "Kennedy"]),
 ("Chris Hemsworth's character", "Kim Hyde", ["Shane Parrish", "Jack Holden", "Darryl Braxton"]),
 ("Isla Fisher's character", "Shannon Reed", ["Sally Fletcher", "Chloe Richards", "Leah Patterson"]),
 ("Melissa George's character", "Angel Parrish", ["Chloe Richards", "Selina Cook", "Hayley Smith"]),
 ("The Braxton brothers' nickname", "The River Boys", ["The Bay Boys", "The Surf Boys", "The Beach Boys"]),
 ("The Melbourne soap it's always compared with", "Neighbours", ["Sons and Daughters", "Prisoner", "A Country Practice"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-283.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
