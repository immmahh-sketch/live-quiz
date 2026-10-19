# Bank session 19 Oct 2026: 2 races -> bank/race-279.json (Minder; Taggart).
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

race("Minder - name it", "Television", "medium", ["Minder", "TV drama", "ITV"], [
 ("The actor who played Arthur Daley", "George Cole", ["George Layton", "George Sewell", "George Baker"]),
 ("The actor who played his minder, Terry", "Dennis Waterman", ["Martin Shaw", "Lewis Collins", "Ray Winstone"]),
 ("Terry's surname", "McCann", ["Malone", "McGuire", "Mullins"]),
 ("What Terry did before minding", "Boxing", ["Football", "Horse racing", "Wrestling"]),
 ("Arthur's drinking club", "The Winchester", ["The Nag's Head", "The Queen Vic", "The Rovers Return"]),
 ("The club's barman", "Dave", ["Mike", "Mick", "Del"]),
 ("What Arthur called his wife", "'Er indoors", ["The missus", "Her ladyship", "The old girl"]),
 ("His phrase for a profitable deal", "A nice little earner", ["Lovely jubbly", "A right result", "Pukka"]),
 ("The make of his car", "Jaguar", ["Rolls-Royce", "Mercedes", "Rover"]),
 ("The detective always after Arthur", "DS Chisholm", ["DS Carter", "DI Burnside", "DS Tosh Lines"]),
 ("The city it's set in", "London", ["Liverpool", "Manchester", "Birmingham"]),
 ("The channel", "ITV", ["BBC One", "Channel 4", "BBC Two"]),
 ("The film company that made it", "Euston Films", ["Granada", "LWT", "Central"]),
 ("The year it began", "1979", ["1975", "1983", "1987"]),
 ("The year the original run ended", "1994", ["1989", "1998", "2001"]),
 ("The theme song", "I Could Be So Good for You", ["Get Up", "Who Pays the Ferryman?", "Going Underground"]),
 ("Arthur's nephew, Terry's replacement", "Ray Daley", ["Dave Daley", "Ronnie Daley", "Tony Daley"]),
 ("The actor who played him", "Gary Webster", ["Gary Kemp", "Gary Olsen", "Gary Oldman"]),
 ("The star of the 2009 revival", "Shane Richie", ["Danny Dyer", "Martin Kemp", "Ross Kemp"]),
 ("The channel that showed the revival", "Channel 5", ["Sky One", "ITV2", "BBC Three"])])

race("Taggart - name it", "Television", "medium", ["Taggart", "detectives", "Scotland", "ITV"], [
 ("The actor who played Taggart", "Mark McManus", ["Mark Heap", "Mark Lester", "Mark Williams"]),
 ("The city it's set in", "Glasgow", ["Edinburgh", "Aberdeen", "Dundee"]),
 ("The CID it was based at", "Maryhill", ["Leith", "Partick", "Govan"]),
 ("The famous line", "There's been a murder", ["Evenin' all", "Just one more thing", "Book 'em, Danno"]),
 ("The channel", "ITV", ["BBC One", "Channel 4", "BBC Two"]),
 ("The year of the first story", "1983", ["1979", "1987", "1990"]),
 ("The title of that first story", "Killer", ["Murder", "Dead Man", "The Killing"]),
 ("The year the lead actor died", "1994", ["1990", "1998", "2001"]),
 ("The year the last episode was made", "2010", ["2002", "2006", "2014"]),
 ("Taggart's teetotal, churchgoing sidekick", "Mike Jardine", ["Robbie Ross", "Ian Fraser", "Mike Lewis"]),
 ("The actor who played him", "James MacPherson", ["James Nesbitt", "James Cosmo", "James McAvoy"]),
 ("The detective who became the team's mainstay", "Jackie Reid", ["Jackie Tyler", "Jackie Ross", "Jackie Mason"]),
 ("The actress who played her", "Blythe Duff", ["Kirsty Wark", "Ashley Jensen", "Dawn Steele"]),
 ("The boss who led the team in later years", "Matt Burke", ["Matt Ward", "Matt Cooper", "Matt Lewis"]),
 ("The actor who played him", "Alex Norton", ["Alex Ferguson", "Alex Salmond", "Alex Jennings"]),
 ("Taggart's wife", "Jean", ["Jenny", "Joan", "Janet"]),
 ("What Jean used to get about", "A wheelchair", ["A guide dog", "Crutches", "A mobility scooter"]),
 ("The theme song", "No Mean City", ["Glasgow Belongs to Me", "Flower of Scotland", "Caledonia"]),
 ("The singer of the theme", "Maggie Bell", ["Lulu", "Sheena Easton", "Barbara Dickson"]),
 ("The writer who created it", "Glenn Chandler", ["Ian Rankin", "Peter McDougall", "Val McDermid"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-279.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
