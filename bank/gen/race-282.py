# Bank session 19 Oct 2026: 2 races -> bank/race-282.json (Emmerdale; Neighbours).
# Neither soap had its own race in the live bank (only mixed soap races). Checked against every live race with
# lqsql/audit/race-overlap-live.py before importing.
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

race("Emmerdale - name it", "Television", "medium", ["Emmerdale", "soaps", "ITV"], [
 ("Its original title", "Emmerdale Farm", ["Dales Farm", "Emmerdale Village", "The Dales"]),
 ("The year 'Farm' was dropped from the title", "1989", ["1985", "1995", "1999"]),
 ("The year it began", "1972", ["1968", "1976", "1980"]),
 ("The channel", "ITV", ["BBC One", "Channel 4", "BBC Two"]),
 ("The county it's set in", "Yorkshire", ["Lancashire", "Derbyshire", "Cumbria"]),
 ("The village's original name", "Beckindale", ["Ambridge", "Aidensfield", "Walford"]),
 ("The pub", "The Woolpack", ["The Rovers Return", "The Queen Vic", "The Bull"]),
 ("The pub's whiskery first landlord", "Amos Brearly", ["Jack Duckworth", "Alec Gilroy", "Den Watts"]),
 ("Whose funeral opened the very first episode", "Jacob Sugden", ["Joe Sugden", "Matt Skilbeck", "Henry Wilks"]),
 ("The farming family at its heart in the early years", "The Sugdens", ["The Kings", "The Tates", "The Battersbys"]),
 ("The actress who played matriarch Annie Sugden", "Sheila Mercier", ["Sheila Hancock", "Sheila Ferguson", "Sheila Reid"]),
 ("The scruffy clan who arrived in the 1990s", "The Dingles", ["The Slaters", "The Grants", "The Royles"]),
 ("Their patriarch", "Zak Dingle", ["Phil Mitchell", "Frank Gallagher", "Jim Royle"]),
 ("The 1993 disaster that hit the village", "A plane crash", ["A tram crash", "A flood", "A fire at the mill"]),
 ("The year of that disaster", "1993", ["1988", "1997", "2001"]),
 ("Seth Armstrong's job", "Gamekeeper", ["Postman", "Vicar", "Blacksmith"]),
 ("The actor who played Seth", "Stan Richards", ["Stan Boardman", "Stanley Baxter", "Stan Stennett"]),
 ("The actress who played Kim Tate", "Claire King", ["Claire Sweeney", "Claire Goose", "Claire Rushbrook"]),
 ("The real village it was filmed in until 1997", "Esholt", ["Goathland", "Holmfirth", "Haworth"]),
 ("The estate where the purpose-built village set now stands", "Harewood", ["Chatsworth", "Castle Howard", "Sandringham"])])

race("Neighbours - name it", "Television", "medium", ["Neighbours", "soaps", "Australia"], [
 ("The street", "Ramsay Street", ["Pinewood Drive", "Wisteria Lane", "Coronation Street"]),
 ("The suburb", "Erinsborough", ["Summer Bay", "Weatherfield", "Walford"]),
 ("The city it's near", "Melbourne", ["Sydney", "Brisbane", "Perth"]),
 ("The year it began", "1985", ["1980", "1989", "1992"]),
 ("Its first UK channel", "BBC One", ["ITV", "BBC Two", "Sky One"]),
 ("The UK channel that took it over", "Channel 5", ["ITV2", "Sky One", "Channel 4"]),
 ("Kylie Minogue's character", "Charlene", ["Charlotte", "Chantelle", "Cheryl"]),
 ("Jason Donovan's character", "Scott", ["Shane", "Steve", "Stuart"]),
 ("The year they married on screen", "1987", ["1984", "1990", "1993"]),
 ("The song played at their wedding", "Suddenly", ["Especially for You", "I Should Be So Lucky", "Up Where We Belong"]),
 ("The nosy neighbour with the curlers", "Mrs Mangel", ["Mrs Brown", "Mrs Overall", "Mrs Slocombe"]),
 ("The pub", "The Waterhole", ["The Diner", "The Surf Club", "The Bush Inn"]),
 ("The hotel and shopping complex", "Lassiter's", ["Robinson's", "Daniels'", "Bishop's"]),
 ("Karl and Susan's surname", "Kennedy", ["Robinson", "Bishop", "Willis"]),
 ("Karl's job", "Doctor", ["Vet", "Lawyer", "Mechanic"]),
 ("Susan's job", "Teacher", ["Nurse", "Journalist", "Hairdresser"]),
 ("The actor who has played Paul Robinson since the start", "Stefan Dennis", ["Ian Smith", "Alan Dale", "Guy Pearce"]),
 ("The instrument Harold Bishop played", "Tuba", ["Trumpet", "Trombone", "Bagpipes"]),
 ("The year it ended before being revived", "2022", ["2019", "2020", "2024"]),
 ("The streaming service that brought it back", "Amazon Freevee", ["Netflix", "Disney+", "Paramount+"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-282.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
