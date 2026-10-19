# Bank session 19 Oct 2026: 2 races -> bank/race-293.json (Spooks; Killing Eve).
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

race("Spooks - name it", "Television", "medium", ["Spooks", "TV drama", "BBC"], [
 ("The service the officers work for", "MI5", ["MI6", "GCHQ", "Special Branch"]),
 ("The channel", "BBC One", ["ITV", "Channel 4", "Sky One"]),
 ("The year it began", "2002", ["1998", "2005", "2009"]),
 ("The year it ended", "2011", ["2008", "2013", "2015"]),
 ("Series made", "10", ["6", "8", "12"]),
 ("The section's headquarters nickname", "The Grid", ["The Box", "The Hub", "The Yard"]),
 ("The head of section", "Harry Pearce", ["Harry Potter", "Harry Palmer", "Harry Hill"]),
 ("The actor who played him", "Peter Firth", ["Peter Davison", "Peter Capaldi", "Peter Egan"]),
 ("The first main spy hero", "Tom Quinn", ["Tom Barnaby", "Tom Hardy", "Tom Baker"]),
 ("The actor who played him", "Matthew Macfadyen", ["Matthew Horne", "Matthew Rhys", "Matthew Goode"]),
 ("The officer who died in the first series", "Helen Flynn", ["Helen Cawood", "Helen Hardy", "Helen Lewis"]),
 ("The tech expert Malcolm's surname", "Wynn-Jones", ["Wynn-Davies", "Wynn-Smith", "Wynn-Evans"]),
 ("The analyst who loved Harry", "Ruth Evershed", ["Ruth Madoc", "Ruth Wilson", "Ruth Langsford"]),
 ("The actress who played her", "Nicola Walker", ["Nicola Roberts", "Nicola Stapleton", "Nicola Sturgeon"]),
 ("The officer who died saving others in series 4", "Danny Hunter", ["Danny Dyer", "Danny Miller", "Danny Baker"]),
 ("The actor who played him", "David Oyelowo", ["David Harewood", "David Gyasi", "David Jonsson"]),
 ("The later spy hero Lucas's surname", "North", ["South", "East", "West"]),
 ("The actor who played him", "Richard Armitage", ["Richard Madden", "Richard Ayoade", "Richard Osman"]),
 ("The 2015 film", "Spooks: The Greater Good", ["Spooks: Section D", "Spooks: The Final Hour", "Spooks: Black Ops"]),
 ("The Game of Thrones star who led the film", "Kit Harington", ["Sean Bean", "Peter Dinklage", "Rory McCann"])])

race("Killing Eve - name it", "Television", "medium", ["Killing Eve", "TV drama", "BBC"], [
 ("The MI5 officer who hunts the killer", "Eve Polastri", ["Eve Arden", "Eve Myles", "Eve Hewson"]),
 ("The actress who played her", "Sandra Oh", ["Sandra Bullock", "Sandra Dickinson", "Sandy Toksvig"]),
 ("The assassin she chases", "Villanelle", ["Vesper Lynd", "Valentine", "Veronica"]),
 ("The actress who played her", "Jodie Comer", ["Jodie Whittaker", "Jodie Foster", "Jodie Turner-Smith"]),
 ("The Russian handler", "Konstantin", ["Konrad", "Kostya", "Kirill"]),
 ("The actor who played him", "Kim Bodnia", ["Kim Cattrall", "Kim Basinger", "Kim Woodburn"]),
 ("The boss who runs the secret MI6 unit", "Carolyn Martens", ["Camilla Parker", "Caroline Quentin", "Cate Blanchett"]),
 ("The actress who played her", "Fiona Shaw", ["Fiona Bruce", "Fiona Fullerton", "Fiona Phillips"]),
 ("Eve's husband", "Niko", ["Nick", "Nigel", "Noel"]),
 ("The shadowy crime syndicate", "The Twelve", ["The Seven", "The Ten", "The Circle"]),
 ("The writer behind series one", "Phoebe Waller-Bridge", ["Emerald Fennell", "Sally Wainwright", "Lena Dunham"]),
 ("The author of the books it's based on", "Luke Jennings", ["John le Carré", "Ian Fleming", "Mick Herron"]),
 ("The books are called", "Codename Villanelle", ["Codename Eve", "Codename Twelve", "Codename Oxana"]),
 ("The channel it started on", "BBC America", ["BBC One", "Sky Atlantic", "ITV2"]),
 ("The year it began", "2018", ["2014", "2016", "2020"]),
 ("Series made", "4", ["2", "3", "6"]),
 ("The year the final series aired", "2022", ["2019", "2021", "2024"]),
 ("The award Jodie Comer won for it", "An Emmy", ["An Oscar", "A Grammy", "A Tony"]),
 ("The award Sandra Oh won for it", "A Golden Globe", ["A BAFTA", "An Oscar", "A Brit"]),
 ("What Villanelle loves to spend her money on", "Designer clothes", ["Vintage cars", "Racehorses", "Fast boats"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-293.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
