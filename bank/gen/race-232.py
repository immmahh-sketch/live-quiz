# Bank session 18 Oct 2026: 2 races -> bank/race-232.json (Taskmaster; Gladiators).
# Topics found free by probing candidate answers against every race in stock; checked again with lqsql/audit/race-overlap.py.
# Taskmaster winners' wrong options are other contestants from that same series.
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

race("Taskmaster - name it", "Television", "hard", ["Taskmaster", "comedy", "panel shows", "Channel 4"], [
 ("The Taskmaster himself", "Greg Davies", ["Rob Brydon", "Jon Richardson", "Rhod Gilbert"]),
 ("His loyal assistant, who created the show", "Alex Horne", ["Tim Key", "Joe Wilkinson", "Mark Watson"]),
 ("The channel it began on in 2015", "Dave", ["Gold", "W", "Comedy Central"]),
 ("The channel it moved to in 2020", "Channel 4", ["BBC Two", "ITV2", "Sky Max"]),
 ("The task where contestants bring in something from home", "Prize task", ["Show and tell", "Home task", "Bring-in round"]),
 ("The task done in front of the studio audience", "Live task", ["Final task", "Studio challenge", "Tie-breaker"]),
 ("What the series champion takes home", "A golden bust of Greg's head", ["A silver trophy", "A golden Alex", "A crown"]),
 ("What the winner of each episode takes home", "All the prizes", ["A gold star", "A medal", "Nothing at all"]),
 ("Alex Horne's band", "The Horne Section", ["The Taskmasters", "The Alex Band", "Horne and Hardy"]),
 ("Greg Davies's height", "6ft 8in", ["6ft 2in", "6ft 5in", "7ft 1in"]),
 ("Greg Davies's teacher in 'The Inbetweeners'", "Mr Gilbert", ["Mr Ellis", "Mr Garvey", "Mr Hughes"]),
 ("Won series 1", "Josh Widdicombe", ["Frank Skinner", "Romesh Ranganathan", "Roisin Conaty"]),
 ("Won series 2", "Katherine Ryan", ["Richard Osman", "Doc Brown", "Joe Wilkinson"]),
 ("Won series 4", "Noel Fielding", ["Hugh Dennis", "Joe Lycett", "Mel Giedroyc"]),
 ("Won series 5", "Bob Mortimer", ["Aisling Bea", "Nish Kumar", "Sally Phillips"]),
 ("Won series 6", "Liza Tarbuck", ["Russell Howard", "Tim Vine", "Asim Chaudhry"]),
 ("Won series 7", "Kerry Godliman", ["James Acaster", "Rhod Gilbert", "Phil Wang"]),
 ("Won series 9", "Ed Gamble", ["David Baddiel", "Jo Brand", "Rose Matafeo"]),
 ("Won series 14", "Dara Ó Briain", ["Sarah Millican", "Fern Brady", "John Kearns"]),
 ("Won series 15", "Mae Martin", ["Frankie Boyle", "Jenny Eclair", "Kiell Smith-Bynoe"])])

race("Gladiators - name it", "Television", "medium", ["Gladiators", "1990s TV", "game shows", "ITV"], [
 ("The final event, a race over the obstacle course", "Eliminator", ["Annihilator", "Terminator", "Exterminator"]),
 ("Swinging across on rings while a gladiator tries to pull you off", "Hang Tough", ["Hang Ten", "Ring Raid", "Swing Shift"]),
 ("Rolling about the arena in giant metal balls", "Atlaspheres", ["Spheroids", "Globetrotters", "Rollerballs"]),
 ("Racing a gladiator up a climbing wall", "The Wall", ["The Cliff", "The Tower", "The Ladder"]),
 ("Charging down a corridor of gladiators with pads", "Gauntlet", ["Corridor", "Crush", "Tunnel"]),
 ("Dodging gladiators to put balls in the baskets", "Powerball", ["Netball", "Sling Ball", "Hot Shot"]),
 ("The famous referee", "John Anderson", ["Pat Partridge", "George Courtney", "Dickie Bird"]),
 ("His call before each event: 'Gladiators, …'", "Ready!", ["Fight!", "Charge!", "Go!"]),
 ("The original female host", "Ulrika Jonsson", ["Anneka Rice", "Kirsty Young", "Gaby Roslin"]),
 ("The original male host, a former footballer", "John Fashanu", ["Ian Wright", "Vinnie Jones", "Frank Bruno"]),
 ("The Birmingham venue it was filmed in", "National Indoor Arena", ["Wembley Arena", "Sheffield Arena", "Manchester Arena"]),
 ("The year it began on ITV", "1992", ["1988", "1996", "2000"]),
 ("The pantomime villain of the gladiators, with long hair", "Wolf", ["Fox", "Bear", "Hawk"]),
 ("The fan-favourite female gladiator with dark curls", "Jet", ["Jade", "Jinx", "Jem"]),
 ("The blonde gladiator famous alongside her", "Lightning", ["Thunder", "Storm", "Flash"]),
 ("The gladiator Olympic swimmer Sharron Davies became", "Amazon", ["Valkyrie", "Siren", "Athena"]),
 ("The muscle-bound gladiator named after a horned animal", "Rhino", ["Bull", "Ram", "Bison"]),
 ("The American show it was based on", "American Gladiators", ["Gladiators USA", "US Gladiators", "Gladiators America"]),
 ("The channel that brought it back in 2024", "BBC One", ["ITV", "Sky One", "Channel 5"]),
 ("The father and son who host the 2024 version", "Bradley and Barney Walsh", ["Ant and Dec", "Dick and Dom", "Holly and Phil"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-232.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
