# Bank session 19 Oct 2026: 2 sitcom races -> bank/race-255.json (The IT Crowd; Some Mothers Do 'Ave 'Em).
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

race("The IT Crowd - name it", "Television", "medium", ["The IT Crowd", "sitcoms", "Channel 4"], [
 ("The company", "Reynholm Industries", ["Wernham Hogg", "Grace Brothers", "Initech"]),
 ("Where the IT department works", "The basement", ["The attic", "The roof", "The canteen"]),
 ("The first boss", "Denholm Reynholm", ["David Brent", "Mr Rumbold", "Mr Burns"]),
 ("The actor who played him", "Chris Morris", ["Chris Addison", "Chris Evans", "Chris Martin"]),
 ("His son, who takes over", "Douglas Reynholm", ["Derek Reynholm", "Duncan Reynholm", "Dennis Reynholm"]),
 ("The actor who played the son", "Matt Berry", ["Matt Lucas", "Matt LeBlanc", "Matt Smith"]),
 ("The actor who played Roy", "Chris O'Dowd", ["Dara Ó Briain", "Ardal O'Hanlon", "Dylan Moran"]),
 ("The actor who played Moss", "Richard Ayoade", ["Richard Osman", "Richard Hammond", "Richard Bacon"]),
 ("The actress who played Jen", "Katherine Parkinson", ["Katherine Ryan", "Katherine Jenkins", "Kate Winslet"]),
 ("Jen's job title", "Relationship Manager", ["Head of IT", "Office Manager", "Systems Analyst"]),
 ("Roy's answer to every caller", "Have you tried turning it off and on again?", ["Have you checked the fuse?", "Did you save your work?", "Is the screen on?"]),
 ("How Moss reports a fire", "By email", ["By text", "By fax", "By carrier pigeon"]),
 ("What they convince Jen the internet is", "A black box with a light", ["A cloud", "A USB stick", "A phone"]),
 ("The new emergency number from the song", "0118 999 881 999 119 725 3", ["999 0118 881 725 119 3", "0118 881 999 725 3", "0800 999 881 999 119"]),
 ("The writer", "Graham Linehan", ["Graham Norton", "Graham Fellows", "Graham Taylor"]),
 ("His earlier sitcom", "Father Ted", ["Phoenix Nights", "Spaced", "Peep Show"]),
 ("The channel", "Channel 4", ["BBC Two", "E4", "ITV"]),
 ("The year it began", "2006", ["2002", "2009", "2012"]),
 ("Series made", "4", ["3", "5", "6"]),
 ("The year of the final special", "2013", ["2010", "2015", "2018"])])

race("Some Mothers Do 'Ave 'Em - name it", "Television", "medium", ["Some Mothers Do 'Ave 'Em", "sitcoms", "BBC"], [
 ("The accident-prone hero", "Frank Spencer", ["Frank Butcher", "Frank Gallagher", "Frank Pike"]),
 ("The actor who played him", "Michael Crawford", ["Michael Caine", "Michael Palin", "Michael Ball"]),
 ("His wife", "Betty", ["Brenda", "Barbara", "Beryl"]),
 ("The actress who played her", "Michele Dotrice", ["Wendy Craig", "Penelope Keith", "Lynda Baron"]),
 ("His famous cry", "Ooh, Betty!", ["Oh, Brenda!", "Ooh, Mother!", "Oh, crikey!"]),
 ("What the cat did in his beret", "A whoopsie", ["A wee", "Was sick", "Had kittens"]),
 ("His trademark hat", "A beret", ["A flat cap", "A bowler", "A trilby"]),
 ("His trademark coat", "A raincoat", ["A duffel coat", "A parka", "A blazer"]),
 ("Their baby daughter", "Jessica", ["Emma", "Sarah", "Lucy"]),
 ("What Frank was always doing", "Losing jobs", ["Winning prizes", "Moving house", "Changing his name"]),
 ("What the star famously did himself", "His own stunts", ["His own theme tune", "His own make-up", "His own scripts"]),
 ("The famous stunt on wheels", "Roller-skating under a lorry", ["Cycling off a pier", "Skiing down a hill", "Skateboarding on a roof"]),
 ("The writer", "Raymond Allen", ["Roy Clarke", "John Sullivan", "Carla Lane"]),
 ("The channel", "BBC One", ["ITV", "BBC Two", "Channel 4"]),
 ("The year it began", "1973", ["1969", "1977", "1981"]),
 ("The year it ended", "1978", ["1975", "1982", "1985"]),
 ("Series made", "3", ["2", "4", "5"]),
 ("The star's Hollywood musical of 1969", "Hello, Dolly!", ["Oliver!", "Mary Poppins", "My Fair Lady"]),
 ("His most famous stage role", "The Phantom of the Opera", ["Les Misérables", "Cats", "Evita"]),
 ("The charity show Frank came back for in 2016", "Sport Relief", ["Comic Relief", "Children in Need", "Stand Up To Cancer"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-255.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
