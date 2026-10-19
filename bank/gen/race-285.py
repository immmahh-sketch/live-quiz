# Bank session 19 Oct 2026: 2 races -> bank/race-285.json (Call the Midwife; Doc Martin).
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

race("Call the Midwife - name it", "Television", "medium", ["Call the Midwife", "TV drama", "BBC"], [
 ("The channel", "BBC One", ["ITV", "Channel 4", "Sky One"]),
 ("The year it began", "2012", ["2008", "2015", "2018"]),
 ("The decade the first series is set in", "The 1950s", ["The 1940s", "The 1960s", "The 1970s"]),
 ("The part of London", "East End", ["West End", "South London", "North London"]),
 ("The district", "Poplar", ["Peckham", "Walford", "Whitechapel"]),
 ("The convent the midwives live in", "Nonnatus House", ["St Mary's House", "Holy Cross House", "Bethlehem House"]),
 ("The kind of nuns they are", "Anglican", ["Roman Catholic", "Methodist", "Quaker"]),
 ("How the midwives get about", "Bicycles", ["Scooters", "Horses", "Motorbikes"]),
 ("The midwife whose memoirs it's based on", "Jennifer Worth", ["Jennifer Saunders", "Vera Brittain", "Catherine Cookson"]),
 ("The writer who created it", "Heidi Thomas", ["Sally Wainwright", "Kay Mellor", "Lynda La Plante"]),
 ("The voice of the older Jenny, narrating", "Vanessa Redgrave", ["Judi Dench", "Maggie Smith", "Helen Mirren"]),
 ("The actress who played young Jenny", "Jessica Raine", ["Jessica Hynes", "Jessica Alba", "Jessica Chastain"]),
 ("The comedy star who played Chummy", "Miranda Hart", ["Sue Perkins", "Jo Brand", "Dawn French"]),
 ("Chummy's real first name", "Camilla", ["Charlotte", "Clementine", "Cordelia"]),
 ("The actress who plays Sister Julienne", "Jenny Agutter", ["Penelope Keith", "Jane Asher", "Felicity Kendal"]),
 ("The actress who played Sister Evangelina", "Pam Ferris", ["Pam St Clement", "Pam Ayres", "Patricia Routledge"]),
 ("The actress who played Sister Monica Joan", "Judy Parfitt", ["Judi Dench", "Judy Cornwell", "Judy Loe"]),
 ("Dr Turner's first name", "Patrick", ["Peter", "Paul", "Philip"]),
 ("The actor who plays him", "Stephen McGann", ["Stephen Fry", "Stephen Tompkinson", "Stephen Mangan"]),
 ("When the special is shown each year", "Christmas Day", ["Boxing Day", "New Year's Eve", "Christmas Eve"])])

race("Doc Martin - name it", "Television", "medium", ["Doc Martin", "TV drama", "ITV", "Cornwall"], [
 ("The actor who played him", "Martin Clunes", ["Martin Freeman", "Martin Kemp", "Martin Shaw"]),
 ("The star's earlier sitcom", "Men Behaving Badly", ["Cold Feet", "Game On", "Coupling"]),
 ("The film the character grew out of", "Saving Grace", ["Calendar Girls", "The Full Monty", "Brassed Off"]),
 ("The doctor's surname", "Ellingham", ["Ellison", "Elliott", "Ellington"]),
 ("His old job in London", "Surgeon", ["Dentist", "Vet", "Pharmacist"]),
 ("Why he gave it up", "He developed a fear of blood", ["He lost his licence", "He broke his hand", "He was sued"]),
 ("His manner with patients", "Grumpy and blunt", ["Cheerful", "Shy", "Flirtatious"]),
 ("The made-up village", "Portwenn", ["Aidensfield", "Lochdubh", "Ambridge"]),
 ("The real village it's filmed in", "Port Isaac", ["Padstow", "St Ives", "Polperro"]),
 ("The county", "Cornwall", ["Devon", "Dorset", "Somerset"]),
 ("The channel", "ITV", ["BBC One", "Channel 4", "Sky One"]),
 ("The year it began", "2004", ["2000", "2008", "2012"]),
 ("The year it ended", "2022", ["2016", "2019", "2024"]),
 ("The woman he loves and marries", "Louisa", ["Lucy", "Laura", "Lisa"]),
 ("Her job", "Teacher", ["Nurse", "Police officer", "Shopkeeper"]),
 ("The actress who played her", "Caroline Catz", ["Caroline Quentin", "Caroline Aherne", "Caroline Langrishe"]),
 ("His farming aunt", "Joan", ["Jean", "Jane", "June"]),
 ("The actress who played her", "Stephanie Cole", ["Stephanie Beacham", "Stephanie Powers", "Stephanie Turner"]),
 ("The father-and-son plumbers", "The Larges", ["The Trotters", "The Steptoes", "The Boswells"]),
 ("The dog that keeps following him", "Buddy", ["Rex", "Wellard", "Max"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-285.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
