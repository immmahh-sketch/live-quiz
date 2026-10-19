# Bank session 19 Oct 2026: 2 races -> bank/race-288.json (Sherlock; Happy Valley).
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

race("Sherlock - name it", "Television", "medium", ["Sherlock", "TV drama", "BBC"], [
 ("The actor who played Sherlock", "Benedict Cumberbatch", ["Benedict Wong", "Tom Hiddleston", "Eddie Redmayne"]),
 ("The actor who played Watson", "Martin Freeman", ["Martin Clunes", "Martin Shaw", "Martin Kemp"]),
 ("The pair who created it", "Steven Moffat and Mark Gatiss", ["Russell T Davies and Phil Collinson", "Jed Mercurio and Jimmy McGovern", "Sally Wainwright and Kay Mellor"]),
 ("The co-creator's part in it", "Mycroft", ["Moriarty", "Dr Watson", "Moran"]),
 ("The actor who played Moriarty", "Andrew Scott", ["Andrew Lincoln", "Andrew Garfield", "Andrew Buchan"]),
 ("The address", "221B Baker Street", ["10 Downing Street", "4 Privet Drive", "742 Evergreen Terrace"]),
 ("The landlady", "Mrs Hudson", ["Mrs Hughes", "Mrs Hall", "Mrs Patmore"]),
 ("The Scotland Yard inspector", "Lestrade", ["Gregson", "Hopkins", "Jones"]),
 ("The pathologist with a crush on Sherlock", "Molly Hooper", ["Molly Weasley", "Molly Dobbs", "Molly Ringwald"]),
 ("'The Woman'", "Irene Adler", ["Moneypenny", "Lady Penelope", "Emma Peel"]),
 ("Watson's wife", "Mary", ["Martha", "Margaret", "Melanie"]),
 ("Where Watson served as an army doctor", "Afghanistan", ["Iraq", "The Falklands", "Northern Ireland"]),
 ("How Sherlock describes himself", "A high-functioning sociopath", ["A consulting genius", "A master detective", "A gentleman thief"]),
 ("The very first episode", "A Study in Pink", ["A Study in Scarlet", "A Study in Blue", "The Pink Panther"]),
 ("The Victorian-set special", "The Abominable Bride", ["The Silent Bride", "The Victorian Bride", "The Ghostly Bride"]),
 ("The author of the original stories", "Arthur Conan Doyle", ["Agatha Christie", "Colin Dexter", "Wilkie Collins"]),
 ("The channel", "BBC One", ["ITV", "Channel 4", "Sky One"]),
 ("The year it began", "2010", ["2006", "2013", "2016"]),
 ("Episodes in each series", "3", ["4", "6", "8"]),
 ("How long each episode runs", "90 minutes", ["30 minutes", "60 minutes", "120 minutes"])])

race("Happy Valley - name it", "Television", "medium", ["Happy Valley", "TV drama", "BBC", "Yorkshire"], [
 ("The actress who plays the lead", "Sarah Lancashire", ["Sarah Parish", "Sarah Millican", "Sarah Hadland"]),
 ("Her character", "Catherine Cawood", ["Kate Fleming", "Jane Tennison", "Vera Stanhope"]),
 ("Her rank", "Sergeant", ["Inspector", "Constable", "Superintendent"]),
 ("The valley it's set in", "Calder Valley", ["Rhondda Valley", "Hope Valley", "Eden Valley"]),
 ("The county", "West Yorkshire", ["Lancashire", "Derbyshire", "Cumbria"]),
 ("The writer", "Sally Wainwright", ["Kay Mellor", "Lynda La Plante", "Jed Mercurio"]),
 ("The writer's other drama starring the same lead", "Last Tango in Halifax", ["Gentleman Jack", "Scott & Bailey", "Cold Feet"]),
 ("The villain", "Tommy Lee Royce", ["Tommy Shelby", "Tommy Lee Jones", "Tommy Cooper"]),
 ("The actor who plays him", "James Norton", ["James Nesbitt", "James Corden", "James McAvoy"]),
 ("Catherine's grandson", "Ryan", ["Robbie", "Reece", "Riley"]),
 ("Catherine's sister", "Clare", ["Carol", "Christine", "Cath"]),
 ("The actress who plays her", "Siobhan Finneran", ["Siobhan Redmond", "Siobhan McSweeney", "Sinead Keenan"]),
 ("The young woman kidnapped in the first series", "Ann Gallagher", ["Anna Bates", "Anne Boleyn", "Annie Sugden"]),
 ("The theme song", "Trouble Town", ["Hurt", "Red Right Hand", "Hometown Glory"]),
 ("Who sings it", "Jake Bugg", ["Jake Shears", "Paolo Nutini", "George Ezra"]),
 ("The channel", "BBC One", ["ITV", "Channel 4", "Sky Atlantic"]),
 ("The year it began", "2014", ["2010", "2017", "2020"]),
 ("The year the final series aired", "2023", ["2019", "2021", "2025"]),
 ("Series made", "3", ["2", "4", "5"]),
 ("Episodes in each series", "6", ["4", "8", "10"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-288.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
