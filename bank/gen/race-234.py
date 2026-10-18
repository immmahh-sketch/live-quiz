# Bank session 18 Oct 2026: 2 races -> bank/race-234.json (Keeping Up Appearances; Open All Hours).
# Topics found free by probing candidate answers against every race in stock; checked again with lqsql/audit/race-overlap.py.
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

race("Keeping Up Appearances - name it", "British sitcoms", "easy", ["Keeping Up Appearances", "sitcoms", "1990s TV", "BBC"], [
 ("Hyacinth's real surname", "Bucket", ["Bucknell", "Budget", "Buckley"]),
 ("How she insists it's pronounced", "Bouquet", ["Boutique", "Bucquet", "Bouclé"]),
 ("Her long-suffering husband", "Richard", ["Robert", "Roger", "Raymond"]),
 ("The scruffy brother-in-law in the string vest", "Onslow", ["Oswald", "Osbert", "Orville"]),
 ("Onslow's wife, Hyacinth's sister", "Daisy", ["Dolly", "Dora", "Doris"]),
 ("The flirty sister always after a man", "Rose", ["Ruby", "Rita", "Rhoda"]),
 ("The well-off sister with a Mercedes and 'room for a pony'", "Violet", ["Veronica", "Vera", "Valerie"]),
 ("Violet's husband, who likes to dress up", "Bruce", ["Barry", "Brian", "Bernard"]),
 ("Hyacinth's never-seen son, always asking for money", "Sheridan", ["Sebastian", "Sinclair", "Stanford"]),
 ("The nervous neighbour forever spilling her coffee", "Elizabeth", ["Eleanor", "Edith", "Evelyn"]),
 ("Her brother, who hides from Hyacinth", "Emmet", ["Elmer", "Ernest", "Edgar"]),
 ("What the sisters call their wandering father", "Daddy", ["Pops", "Grandad", "Father"]),
 ("Hyacinth's treasured china", "Royal Doulton with hand-painted periwinkles", ["Wedgwood with gold rims", "Spode in willow pattern", "Minton with roses"]),
 ("Her prized telephone", "White slimline with automatic redial", ["Cream Trimphone", "Red rotary dial", "Black Bakelite"]),
 ("The actor who played Hyacinth", "Patricia Routledge", ["Penelope Keith", "June Whitfield", "Thora Hird"]),
 ("Her later TV sleuth", "Hetty Wainthropp", ["Miss Marple", "Rosemary Boxer", "Jessica Fletcher"]),
 ("The writer, also behind 'Last of the Summer Wine'", "Roy Clarke", ["David Croft", "Jimmy Perry", "John Sullivan"]),
 ("The channel", "BBC One", ["ITV", "BBC Two", "Channel 4"]),
 ("The year it began", "1990", ["1985", "1994", "1998"]),
 ("The year it ended", "1995", ["1992", "1999", "2002"])])

race("Open All Hours - name it", "British sitcoms", "medium", ["Open All Hours", "sitcoms", "Ronnie Barker", "David Jason"], [
 ("The penny-pinching shopkeeper", "Arkwright", ["Albert", "Arnold", "Alfred"]),
 ("The actor who played him", "Ronnie Barker", ["Ronnie Corbett", "Leonard Rossiter", "Arthur Lowe"]),
 ("His put-upon nephew", "Granville", ["Gerald", "Gordon", "Graham"]),
 ("The actor who played the nephew", "David Jason", ["Nicholas Lyndhurst", "Richard Beckinsale", "Paul Nicholas"]),
 ("The nephew's job in the shop", "Shop assistant", ["Milkman", "Postman", "Window cleaner"]),
 ("What he does his deliveries on", "A bike", ["A milk float", "A van", "A scooter"]),
 ("The nurse across the road whom Arkwright adores", "Nurse Gladys Emmanuel", ["Nurse Gladys Pugh", "Nurse Ratched", "Nurse Glenda Edwards"]),
 ("What he longs to do with her", "Marry her", ["Open a café with her", "Take her dancing", "Retire to the coast with her"]),
 ("The thing in the shop that snaps shut on fingers", "The till", ["The bacon slicer", "The cash box", "The shutter"]),
 ("Arkwright's speech habit", "A stammer", ["A lisp", "A whistle", "A wheeze"]),
 ("The Yorkshire town it's set in", "Doncaster", ["Barnsley", "Rotherham", "Wakefield"]),
 ("The suburb whose real shop front was used", "Balby", ["Bessacarr", "Wheatley", "Armthorpe"]),
 ("The writer", "Roy Clarke", ["John Sullivan", "Jimmy Perry", "Eric Chappell"]),
 ("Ronnie Barker's 1973 run of one-off comedies that had the pilot", "Seven of One", ["Six Dates with Barker", "The Two Ronnies", "Barker's Half Dozen"]),
 ("The year the first series went out", "1976", ["1972", "1980", "1984"]),
 ("How many series the original ran to", "4", ["2", "6", "8"]),
 ("The title of the revival", "Still Open All Hours", ["Open All Hours Again", "Back to the Shop", "Arkwright's"]),
 ("The year the revival began", "2013", ["2009", "2016", "2019"]),
 ("Granville's son in the revival", "Leroy", ["Lenny", "Lewis", "Lloyd"]),
 ("The actor who played Mrs Featherstone in the revival", "Stephanie Cole", ["Brenda Blethyn", "Liz Smith", "Maureen Lipman"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-234.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
