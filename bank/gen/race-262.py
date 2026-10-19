# Bank session 19 Oct 2026: 2 sitcom races -> bank/race-262.json (Miranda; Citizen Smith).
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

race("Miranda - name it", "Television", "medium", ["Miranda", "sitcoms", "BBC"], [
 ("The writer and star", "Miranda Hart", ["Miranda Richardson", "Miranda Kerr", "Miranda Lambert"]),
 ("The shop she owns", "A joke shop", ["A bakery", "A florist", "A bookshop"]),
 ("Her best friend who runs it", "Stevie", ["Stella", "Sophie", "Suzy"]),
 ("The actress who plays her", "Sarah Hadland", ["Sarah Lancashire", "Sarah Millican", "Sarah Alexander"]),
 ("The chef she fancies", "Gary", ["Gavin", "Graham", "Greg"]),
 ("The actor who plays him", "Tom Ellis", ["Tom Hardy", "Tom Hiddleston", "Tom Hollander"]),
 ("Her mum", "Penny", ["Pamela", "Peggy", "Polly"]),
 ("The actress who plays her", "Patricia Hodge", ["Patricia Routledge", "Patricia Arquette", "Patricia Hayes"]),
 ("Mum's favourite phrase", "Such fun!", ["What fun!", "How lovely!", "Jolly good!"]),
 ("Her posh old school friend", "Tilly", ["Tally", "Tina", "Tessa"]),
 ("That friend's catchphrase", "Bear with!", ["Hold on!", "One mo!", "Steady on!"]),
 ("What Miranda does to the audience", "Talks to them directly", ["Throws sweets", "Sings to them", "Ignores them"]),
 ("What she loves to do across a room", "Gallop", ["Skip", "Moonwalk", "Cartwheel"]),
 ("How each episode ends", "The cast wave goodbye", ["A dance-off", "A blooper reel", "A song"]),
 ("The channel it began on", "BBC Two", ["BBC Three", "ITV", "Channel 4"]),
 ("The year it began", "2009", ["2005", "2012", "2017"]),
 ("Series made", "3", ["2", "4", "5"]),
 ("The year of the final specials", "2015", ["2011", "2018", "2020"]),
 ("Her role in Call the Midwife", "Chummy", ["Trixie", "Jenny", "Sister Evangelina"]),
 ("The star's height", "6 ft 1 in", ["5 ft 7 in", "5 ft 10 in", "6 ft 4 in"])])

race("Citizen Smith - name it", "Television", "medium", ["Citizen Smith", "sitcoms", "BBC"], [
 ("The would-be revolutionary", "Wolfie Smith", ["Wolfie Jones", "Woody Smith", "Wally Smith"]),
 ("The actor who played him", "Robert Lindsay", ["Robert Powell", "Robert Carlyle", "Robert Webb"]),
 ("What he called himself", "An urban guerrilla", ["A rebel without a cause", "A man of the people", "A working-class hero"]),
 ("His movement", "Tooting Popular Front", ["Tooting Liberation Army", "Balham Popular Front", "Peckham People's Party"]),
 ("His battle cry", "Power to the people!", ["Workers unite!", "Down with the rich!", "Up the revolution!"]),
 ("His other cry", "Freedom for Tooting!", ["Freedom for Balham!", "Tooting forever!", "Free Tooting!"]),
 ("The part of London it's set in", "Tooting", ["Brixton", "Peckham", "Clapham"]),
 ("His coat", "An Afghan coat", ["A donkey jacket", "A Barbour", "A parka"]),
 ("His girlfriend", "Shirley", ["Sharon", "Sheila", "Sandra"]),
 ("The actor who played her dad, also Grouty in Porridge", "Peter Vaughan", ["Peter Davison", "Peter Bowles", "Peter Sallis"]),
 ("His best friend", "Ken", ["Kevin", "Keith", "Kenny"]),
 ("The actor who played him, later Barry in Last of the Summer Wine", "Mike Grady", ["Mike Reid", "Mike Read", "Mike Myers"]),
 ("The writer", "John Sullivan", ["Roy Clarke", "Carla Lane", "Jimmy Perry"]),
 ("That writer's next big hit", "Only Fools and Horses", ["Porridge", "Open All Hours", "Rising Damp"]),
 ("The channel", "BBC One", ["ITV", "BBC Two", "Channel 4"]),
 ("The year it began", "1977", ["1973", "1981", "1985"]),
 ("Series made", "4", ["2", "3", "6"]),
 ("The tune it opened with", "The Red Flag", ["The Internationale", "Jerusalem", "Land of Hope and Glory"]),
 ("The star's later family sitcom", "My Family", ["Outnumbered", "2point4 Children", "Butterflies"]),
 ("The musical that won him an Olivier and a Tony", "Me and My Girl", ["Oliver!", "Les Misérables", "Cats"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-262.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
