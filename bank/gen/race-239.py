# Bank session 18 Oct 2026: 2 races -> bank/race-239.json (The Young Ones; Dad's Army).
# Dad's Army sticks to jobs, actors and places so it doesn't repeat the 'whose catchphrase?' race.
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

race("The Young Ones - name it", "British sitcoms", "hard", ["The Young Ones", "sitcoms", "1980s TV", "alternative comedy"], [
 ("The self-styled 'people's poet'", "Rik", ["Ray", "Rob", "Ron"]),
 ("The actor who played him", "Rik Mayall", ["Rowan Atkinson", "Mel Smith", "Griff Rhys Jones"]),
 ("The violent punk medical student", "Vyvyan", ["Victor", "Vernon", "Valentine"]),
 ("The actor who played him", "Adrian Edmondson", ["Keith Allen", "Peter Richardson", "Robbie Coltrane"]),
 ("What the punk has stuck in his forehead", "Metal studs", ["A scar", "A tattoo", "Glitter"]),
 ("His pet hamster", "SPG", ["PPG", "SPQ", "HMS"]),
 ("The gloomy hippy", "Neil", ["Nigel", "Norman", "Nick"]),
 ("The actor who played him", "Nigel Planer", ["Nigel Havers", "Nick Frost", "Neil Pearson"]),
 ("The 'cool' one who runs the house", "Mike", ["Mark", "Matt", "Max"]),
 ("The actor who played him", "Christopher Ryan", ["Christopher Biggins", "Christopher Eccleston", "Christopher Strauli"]),
 ("The comedian who played the Balowski family", "Alexei Sayle", ["Keith Allen", "Robbie Coltrane", "Peter Richardson"]),
 ("The co-writer who went on to write Blackadder", "Ben Elton", ["Richard Curtis", "John Lloyd", "Rob Grant"]),
 ("Their college", "Scumbag College", ["Scumbag Poly", "Grot University", "Slob Academy"]),
 ("What turns up in every episode", "A live band", ["A magician", "A poet", "A puppet show"]),
 ("The singer whose 'Living Doll' they took to number one", "Cliff Richard", ["Elvis Presley", "Adam Faith", "Tommy Steele"]),
 ("The year of that charity number one", "1986", ["1983", "1989", "1992"]),
 ("How the last episode ends", "A bus over a cliff", ["A house fire", "A flood", "A prison cell"]),
 ("The channel", "BBC Two", ["BBC One", "ITV", "Channel 4"]),
 ("The year it began", "1982", ["1979", "1985", "1988"]),
 ("How many series were made", "2", ["1", "3", "4"])])

race("Dad's Army - name it", "British sitcoms", "medium", ["Dad's Army", "sitcoms", "Home Guard", "BBC"], [
 ("The seaside town the platoon guards", "Walmington-on-Sea", ["Bexhill-on-Sea", "Frinton-on-Sea", "Leigh-on-Sea"]),
 ("Captain Mainwaring's day job", "Bank manager", ["Headmaster", "Solicitor", "Shopkeeper"]),
 ("The actor who played Mainwaring", "Arthur Lowe", ["Bill Pertwee", "John Laurie", "Richard Wilson"]),
 ("His laid-back sergeant", "Wilson", ["Wilkinson", "Wallace", "Walton"]),
 ("The actor who played the sergeant", "John Le Mesurier", ["John Inman", "John Cleese", "John Thaw"]),
 ("Lance Corporal Jones's day job", "Butcher", ["Baker", "Greengrocer", "Grocer"]),
 ("The actor who played Jones", "Clive Dunn", ["Clive Swift", "Clive Owen", "Clive James"]),
 ("Private Frazer's day job", "Undertaker", ["Fishmonger", "Gravedigger", "Vicar"]),
 ("Private Walker's line of work", "Spiv on the black market", ["Milkman", "Postman", "Bus conductor"]),
 ("The youngest of the platoon", "Pike", ["Perkins", "Potts", "Parker"]),
 ("The actor who played him", "Ian Lavender", ["Ian McShane", "Ian Ogilvy", "Ian Hogg"]),
 ("The gentle old private who needs the toilet", "Godfrey", ["Goodwin", "Gordon", "Gibson"]),
 ("The bossy ARP warden", "Hodges", ["Hopkins", "Hughes", "Harris"]),
 ("Who sang the theme, 'Who Do You Think You Are Kidding, Mr Hitler?'", "Bud Flanagan", ["Max Bygraves", "Vera Lynn", "George Formby"]),
 ("The writers", "Jimmy Perry and David Croft", ["Clement and La Frenais", "Galton and Simpson", "Esmonde and Larbey"]),
 ("The Norfolk town where most of it was filmed", "Thetford", ["Cromer", "King's Lynn", "Great Yarmouth"]),
 ("The year it began", "1968", ["1964", "1972", "1976"]),
 ("The year it ended", "1977", ["1973", "1981", "1985"]),
 ("The war it's set in", "The Second World War", ["The First World War", "The Boer War", "The Korean War"]),
 ("The year of the film remake with Toby Jones", "2016", ["2009", "2012", "2019"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-239.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
