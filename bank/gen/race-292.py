# Bank session 19 Oct 2026: 2 races -> bank/race-292.json (Life on Mars; Fleabag).
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

race("Life on Mars - name it", "Television", "medium", ["Life on Mars", "TV drama", "BBC"], [
 ("The detective who wakes up in the past", "Sam Tyler", ["Sam Spade", "Sam Gamgee", "Sam Malone"]),
 ("The actor who played him", "John Simm", ["John Nettles", "John Hannah", "John Barrowman"]),
 ("His boss in the past", "Gene Hunt", ["Gene Kelly", "Gene Wilder", "Gene Vincent"]),
 ("The actor who played him", "Philip Glenister", ["Philip Glenny", "Philip Madoc", "Philip Jackson"]),
 ("The city it's set in", "Manchester", ["Leeds", "Liverpool", "Newcastle"]),
 ("The year Sam wakes up in", "1973", ["1969", "1977", "1981"]),
 ("What happens to him in 2006", "He is hit by a car", ["He falls off a roof", "He is shot", "He drowns"]),
 ("The WPC he falls for", "Annie Cartwright", ["Annie Hall", "Annie Wilkes", "Annie Sugden"]),
 ("The actress who played her", "Liz White", ["Liz Hurley", "Liz Smith", "Liz Carr"]),
 ("Gene Hunt's car", "A Ford Cortina", ["A Rover SD1", "A Jaguar XJ", "A Morris Marina"]),
 ("Gene's nickname for himself", "The Gene Genie", ["The Gene Machine", "The Guv'nor", "The Big Cat"]),
 ("Sam's sidekick DS", "Ray Carling", ["Ray Doyle", "Ray Winstone", "Ray Reardon"]),
 ("The Bowie song that gives the show its name", "Life on Mars?", ["Starman", "Heroes", "Changes"]),
 ("The channel", "BBC One", ["ITV", "Channel 4", "Sky One"]),
 ("The year it began", "2006", ["2002", "2009", "2012"]),
 ("Series made", "2", ["1", "3", "4"]),
 ("The spin-off", "Ashes to Ashes", ["Life on Venus", "Hunt's Squad", "A Division"]),
 ("The actress who led the spin-off", "Keeley Hawes", ["Keeley Donovan", "Kelly Reilly", "Kelly Macdonald"]),
 ("The decade the spin-off is set in", "The 1980s", ["The 1960s", "The 1990s", "The 1970s"]),
 ("The country that made a US remake in 2008", "America", ["Australia", "Canada", "Ireland"])])

race("Fleabag - name it", "Television", "medium", ["Fleabag", "TV drama", "BBC"], [
 ("The writer and star", "Phoebe Waller-Bridge", ["Michaela Coel", "Sharon Horgan", "Daisy May Cooper"]),
 ("Where it began", "The Edinburgh Fringe", ["The West End", "A radio play", "A novel"]),
 ("The year the first series began", "2016", ["2012", "2018", "2020"]),
 ("The year the second series aired", "2019", ["2017", "2021", "2023"]),
 ("Series made", "2", ["1", "4", "5"]),
 ("The channel it started on", "BBC Three", ["BBC One", "Channel 4", "ITV2"]),
 ("The business Fleabag runs", "A guinea pig cafe", ["A bookshop", "A cake shop", "A bar"]),
 ("What she does to the audience", "Speaks straight to the camera", ["Reads them poems", "Sings to them", "Ignores them"]),
 ("Her sister", "Claire", ["Clare", "Carrie", "Cathy"]),
 ("The actress who played her", "Sian Clifford", ["Sian Gibson", "Siobhan Finneran", "Sian Phillips"]),
 ("The actress who played the Godmother", "Olivia Colman", ["Olivia Williams", "Olivia Cooke", "Olivia Munn"]),
 ("The 'hot' man in series two", "The Priest", ["The Doctor", "The Plumber", "The Teacher"]),
 ("The actor who played him", "Andrew Scott", ["Andrew Lincoln", "Andrew Garfield", "Andrew Buchan"]),
 ("The actor who played their dad", "Bill Paterson", ["Bill Nighy", "Bill Bailey", "Bill Treacher"]),
 ("Her best friend who died", "Boo", ["Bea", "Bex", "Bree"]),
 ("The number of Emmys Phoebe Waller-Bridge won for it", "3", ["1", "5", "6"]),
 ("The streaming service that co-produced it", "Amazon Prime", ["Netflix", "Disney+", "Apple TV+"]),
 ("The spy show she wrote next", "Killing Eve", ["Bodyguard", "Homeland", "The Night Manager"]),
 ("The Bond film she helped write", "No Time to Die", ["Skyfall", "Spectre", "Casino Royale"]),
 ("The 2018 Star Wars film in which she voiced a droid", "Solo", ["The Last Jedi", "Rogue One", "The Force Awakens"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-292.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
