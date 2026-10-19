# Bank session 19 Oct 2026: 2 races -> bank/race-290.json (Luther; Bodyguard).
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

race("Luther - name it", "Television", "medium", ["Luther", "TV drama", "BBC"], [
 ("The actor who played Luther", "Idris Elba", ["David Harewood", "Adrian Lester", "Chiwetel Ejiofor"]),
 ("Luther's first name", "John", ["James", "Jack", "Joe"]),
 ("His rank", "Detective Chief Inspector", ["Detective Sergeant", "Detective Constable", "Superintendent"]),
 ("The city", "London", ["Manchester", "Birmingham", "Glasgow"]),
 ("His trademark coat", "A long grey coat", ["A trench coat", "A leather jacket", "A parka"]),
 ("The brilliant killer who becomes his ally", "Alice Morgan", ["Alice Gray", "Alice Watson", "Alice Mason"]),
 ("The actress who played her", "Ruth Wilson", ["Ruth Jones", "Ruth Madoc", "Ruth Sheen"]),
 ("His loyal young sergeant", "Justin Ripley", ["Justin Hastings", "Justin Coates", "Justin Ward"]),
 ("The actor who played him", "Warren Brown", ["Warren Clarke", "Warren Mitchell", "Warren Beatty"]),
 ("Luther's wife", "Zoe", ["Zara", "Zelda", "Zena"]),
 ("The writer who created it", "Neil Cross", ["Neil Gaiman", "Jed Mercurio", "Chris Lang"]),
 ("The channel", "BBC One", ["ITV", "Channel 4", "Sky One"]),
 ("The year it began", "2010", ["2006", "2013", "2016"]),
 ("The year the last TV series aired", "2019", ["2015", "2021", "2023"]),
 ("TV series made", "5", ["3", "4", "6"]),
 ("The 2023 film", "The Fallen Sun", ["The Rising Sun", "The Last Light", "The Dark Hour"]),
 ("The service that made the film", "Netflix", ["Amazon Prime", "Disney+", "Apple TV+"]),
 ("The film's villain", "Andy Serkis", ["Andy Samberg", "Andrew Scott", "Andrew Lincoln"]),
 ("Idris Elba's role in The Wire", "Stringer Bell", ["Omar Little", "Jimmy McNulty", "Avon Barksdale"]),
 ("Idris Elba's Marvel role", "Heimdall", ["Odin", "Loki", "Groot"])])

race("Bodyguard - name it", "Television", "medium", ["Bodyguard", "TV drama", "BBC"], [
 ("The actor who played the bodyguard", "Richard Madden", ["Richard Armitage", "Richard E. Grant", "Rob Brydon"]),
 ("His character", "David Budd", ["David Brent", "David Platt", "David Bowman"]),
 ("Where he served as a soldier", "Afghanistan", ["Iraq", "The Falklands", "Northern Ireland"]),
 ("His estranged wife", "Vicky", ["Becky", "Nicky", "Ricky"]),
 ("The police force he works for", "Metropolitan Police", ["West Yorkshire Police", "Police Scotland", "Thames Valley Police"]),
 ("The politician he has to protect", "The Home Secretary", ["The Prime Minister", "The Chancellor", "The Foreign Secretary"]),
 ("Her name", "Julia Montague", ["Julia Wakefield", "Julia Hartley", "Julia Beaumont"]),
 ("The actress who played her", "Keeley Hawes", ["Keeley Donovan", "Kelly Holmes", "Kelly Reilly"]),
 ("Her earlier Line of Duty character", "Lindsay Denton", ["Kate Fleming", "Jo Davidson", "Roz Huntley"]),
 ("The writer who created it", "Jed Mercurio", ["Neil Cross", "Sally Wainwright", "Chris Chibnall"]),
 ("His other big police drama", "Line of Duty", ["Happy Valley", "Luther", "Broadchurch"]),
 ("What happens in the gripping opening", "A bomb threat on a train", ["A shooting at a wedding", "A hijacked plane", "A bank raid"]),
 ("The channel", "BBC One", ["ITV", "Channel 4", "Sky One"]),
 ("The year it was shown", "2018", ["2014", "2016", "2020"]),
 ("Episodes made", "6", ["3", "4", "8"]),
 ("Series made so far", "1", ["2", "3", "4"]),
 ("The award Richard Madden won for it", "A Golden Globe", ["An Oscar", "A Grammy", "A Tony"]),
 ("His earlier Game of Thrones role", "Robb Stark", ["Jon Snow", "Theon Greyjoy", "Ramsay Bolton"]),
 ("His later Amazon spy series", "Citadel", ["Jack Ryan", "The Night Manager", "Killing Eve"]),
 ("The country he comes from", "Scotland", ["Wales", "Ireland", "Northern Ireland"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-290.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
