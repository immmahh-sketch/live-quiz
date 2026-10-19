# Bank session 19 Oct 2026: 2 sitcom races -> bank/race-267.json (Car Share; Mrs Brown's Boys).
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

race("Peter Kay's Car Share - name it", "Television", "medium", ["Car Share", "sitcoms", "BBC", "Peter Kay"], [
 ("The actor who plays John", "Peter Kay", ["Peter Andre", "Peter Davison", "Peter Crouch"]),
 ("John's surname", "Redmond", ["Redfern", "Redgrave", "Redwood"]),
 ("The actress who plays Kayleigh", "Sian Gibson", ["Sian Lloyd", "Sian Phillips", "Sian Williams"]),
 ("Kayleigh's surname", "Kitson", ["Kirkham", "Kitchen", "Kidd"]),
 ("How Sian Gibson knew Peter Kay", "They met at college", ["They're cousins", "They were neighbours", "They're married"]),
 ("The supermarket they work at", "ForeverFresh", ["FreshCo", "ShopRite", "Forever Value"]),
 ("John's job there", "Assistant manager", ["Checkout supervisor", "Delivery driver", "Security guard"]),
 ("Kayleigh's department", "Promotions", ["Bakery", "Checkouts", "Customer services"]),
 ("Why they're in the car together", "A work car-share scheme", ["A taxi firm", "A dating app", "A bus strike"]),
 ("The radio station they listen to", "Forever FM", ["Smooth FM", "Heart", "Radio Forever"]),
 ("The county it's set in", "Greater Manchester", ["Merseyside", "West Yorkshire", "Cumbria"]),
 ("Who co-created it with Peter Kay", "Paul Coleman and Tim Reid", ["Craig Cash and Phil Mealey", "Steve Pemberton and Reece Shearsmith", "Andy Hamilton and Guy Jenkin"]),
 ("Where episodes went out first", "BBC iPlayer", ["Netflix", "Sky Go", "YouTube"]),
 ("The channel", "BBC One", ["ITV", "Channel 4", "Sky One"]),
 ("The year it began", "2015", ["2011", "2013", "2020"]),
 ("Series made", "2", ["3", "4", "5"]),
 ("What was special about the 2017 episode", "It was improvised", ["It was live", "It was silent", "It was animated"]),
 ("The year of the final episode", "2018", ["2016", "2020", "2022"]),
 ("The award it won for best comedy in 2016", "BAFTA", ["Emmy", "Golden Globe", "Oscar"]),
 ("Peter Kay's earlier sitcom", "Phoenix Nights", ["Benidorm", "Early Doors", "The Royle Family"])])

race("Mrs Brown's Boys - name it", "Television", "medium", ["Mrs Brown's Boys", "sitcoms", "BBC", "Ireland"], [
 ("The star who plays Mrs Brown", "Brendan O'Carroll", ["Brendan Gleeson", "Brendan Coyle", "Brendan Cole"]),
 ("Mrs Brown's first name", "Agnes", ["Annie", "Alice", "Agatha"]),
 ("Her favourite phrase", "That's nice!", ["That's grand!", "Lovely jubbly!", "Fair play!"]),
 ("The city it's set in", "Dublin", ["Cork", "Belfast", "Limerick"]),
 ("The country", "Ireland", ["Scotland", "Wales", "Northern Ireland"]),
 ("Her son who is a priest", "Trevor", ["Rory", "Dermot", "Mark"]),
 ("Her best friend", "Winnie", ["Wendy", "Wilma", "Wanda"]),
 ("How Winnie's actress is related to the star", "His sister", ["His wife", "His daughter", "His mother"]),
 ("The character the star's real wife plays", "Cathy", ["Maria", "Betty", "Sharon"]),
 ("The actor who plays Grandad", "Dermot O'Neill", ["Dermot O'Leary", "Dermot Morgan", "Dermot Murnaghan"]),
 ("The star's son who plays Buster", "Danny O'Carroll", ["Danny Dyer", "Danny Mac", "Danny Jones"]),
 ("What the show leaves in", "Fluffed lines", ["Ad breaks", "Subtitles", "Narration"]),
 ("When its specials usually go out", "Christmas Day", ["Easter Sunday", "New Year's Day", "Halloween"]),
 ("Where Mrs Brown started", "On the radio", ["In a book", "In a newspaper column", "On YouTube"]),
 ("The UK channel", "BBC One", ["ITV", "Channel 4", "Sky One"]),
 ("The Irish channel that also shows it", "RTÉ", ["TG4", "TV3", "Virgin Media One"]),
 ("The year it began on TV", "2011", ["2007", "2009", "2017"]),
 ("The film", "Mrs Brown's Boys D'Movie", ["Mrs Brown: The Movie", "Mrs Brown Goes to Hollywood", "Mrs Brown's Big Day Out"]),
 ("The year of the film", "2014", ["2010", "2016", "2019"]),
 ("The award it won for best sitcom in 2012", "BAFTA", ["Emmy", "Golden Globe", "Oscar"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-267.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
