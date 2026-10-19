# Bank session 19 Oct 2026: 2 sitcom races -> bank/race-258.json (Dinnerladies; Still Game).
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

race("Dinnerladies - name it", "Television", "medium", ["Dinnerladies", "sitcoms", "BBC"], [
 ("The writer and star", "Victoria Wood", ["Victoria Coren Mitchell", "Victoria Beckham", "Victoria Derbyshire"]),
 ("Her character", "Bren", ["Brenda", "Bernie", "Babs"]),
 ("Where they work", "A factory canteen", ["A school kitchen", "A hospital café", "A motorway services"]),
 ("The factory", "HWD Components", ["HMV Components", "BWD Engineering", "HDW Electrics"]),
 ("The city it's set in", "Manchester", ["Leeds", "Bolton", "Sheffield"]),
 ("The actress who played Bren's mum", "Julie Walters", ["Julie Andrews", "Julie Hesmondhalgh", "Julie Goodyear"]),
 ("The canteen manager", "Tony", ["Terry", "Trevor", "Tom"]),
 ("The actor who played him", "Andrew Dunn", ["Andrew Lincoln", "Andrew Sachs", "Andrew Scott"]),
 ("The actor who played Stan the handyman", "Duncan Preston", ["Duncan Bannatyne", "Duncan James", "Duncan Goodhew"]),
 ("The actress who played Dolly", "Thelma Barlow", ["Thora Hird", "Liz Dawn", "Betty Driver"]),
 ("The actress who played Jean", "Anne Reid", ["Anne Robinson", "Anne Kirkbride", "Anne Hegerty"]),
 ("The actress who played Twinkle", "Maxine Peake", ["Sheridan Smith", "Joanna Page", "Jessica Hynes"]),
 ("The actress who played Philippa", "Celia Imrie", ["Celia Johnson", "Celia Birtwell", "Celia Walden"]),
 ("How it was filmed", "In front of a studio audience", ["On location", "With no audience", "In a real canteen"]),
 ("The channel", "BBC One", ["ITV", "BBC Two", "Channel 4"]),
 ("The year it began", "1998", ["1994", "2002", "2005"]),
 ("Series made", "2", ["3", "4", "5"]),
 ("The soap spoof from the writer's sketch show", "Acorn Antiques", ["Crossroads", "Emmerdale Farm", "Brookside"]),
 ("Her famous comic song", "The Ballad of Barry and Freda", ["Let's Go Round Again", "The Laughing Policeman", "Right Said Fred"]),
 ("The year she died", "2016", ["2012", "2018", "2020"])])

race("Still Game - name it", "Television", "medium", ["Still Game", "sitcoms", "Scotland"], [
 ("The two old pals", "Jack and Victor", ["Jim and Victor", "Jack and Vince", "Jake and Victor"]),
 ("The actor who played Jack", "Ford Kiernan", ["Billy Connolly", "Rab Christie", "Frankie Boyle"]),
 ("The actor who played Victor", "Greg Hemphill", ["Greg Wise", "Greg James", "Greg Rusedski"]),
 ("Their age group", "Pensioners", ["Students", "Teenagers", "New dads"]),
 ("The city", "Glasgow", ["Edinburgh", "Dundee", "Aberdeen"]),
 ("The made-up district", "Craiglang", ["Craigie", "Crawfield", "Carnwath"]),
 ("Their tower block", "Osprey Heights", ["Eagle House", "Falcon Towers", "Kestrel Court"]),
 ("Their local", "The Clansman", ["The Highlander", "The Thistle", "The Piper"]),
 ("The barman", "Boabby", ["Rab", "Big Davie", "Shug"]),
 ("The shopkeeper", "Navid", ["Raj", "Sanjay", "Imran"]),
 ("His wife", "Meena", ["Priya", "Asha", "Leela"]),
 ("The gossip", "Isa", ["Ina", "Ella", "Agnes"]),
 ("What Winston lost", "A leg", ["An eye", "A finger", "His teeth"]),
 ("What Tam is famous for", "Being tight with money", ["Never sleeping", "Telling lies", "Singing"]),
 ("The sketch show the characters came from", "Chewin' the Fat", ["Rab C. Nesbitt", "Absolutely", "Burnistoun"]),
 ("The channel it began on", "BBC One Scotland", ["STV", "Channel 4", "BBC Three"]),
 ("The year it began", "2002", ["1998", "2006", "2010"]),
 ("Series made", "9", ["6", "7", "11"]),
 ("The year of the final series", "2019", ["2015", "2021", "2023"]),
 ("The Glasgow arena where it came back live in 2014", "The SSE Hydro", ["The Barrowland", "The O2", "Hampden Park"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-258.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
