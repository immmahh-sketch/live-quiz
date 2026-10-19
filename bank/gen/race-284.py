# Bank session 19 Oct 2026: 2 races -> bank/race-284.json (Brookside; Casualty).
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

race("Brookside - name it", "Television", "medium", ["Brookside", "soaps", "Channel 4"], [
 ("The channel", "Channel 4", ["BBC One", "ITV", "BBC Two"]),
 ("When it first went out", "Channel 4's opening night", ["Christmas Day", "New Year's Day", "Election night"]),
 ("The year it began", "1982", ["1978", "1986", "1990"]),
 ("The year it ended", "2003", ["1998", "2006", "2010"]),
 ("The city", "Liverpool", ["Manchester", "Leeds", "Glasgow"]),
 ("The road's full name", "Brookside Close", ["Brookside Avenue", "Brookside Drive", "Brookside Way"]),
 ("What the set was", "Real houses bought by the show", ["A studio set", "A council estate", "A holiday camp"]),
 ("The man who created it", "Phil Redmond", ["Tony Warren", "Julia Smith", "Jimmy McGovern"]),
 ("His earlier school drama", "Grange Hill", ["Byker Grove", "Press Gang", "Waterloo Road"]),
 ("His later soap", "Hollyoaks", ["Doctors", "Family Affairs", "Crossroads"]),
 ("The man famously buried under the patio", "Trevor Jordache", ["Den Watts", "Richard Hillman", "Tom King"]),
 ("Who buried him", "His wife and daughter", ["His brother", "His neighbour", "His lodger"]),
 ("The actress who played daughter Beth", "Anna Friel", ["Anna Maxwell Martin", "Anna Chancellor", "Amanda Holden"]),
 ("The Grant son who got his own spin-off with Debbie", "Damon", ["Kevin", "Gavin", "Terry"]),
 ("The actress who played Sheila Grant", "Sue Johnston", ["Sue Pollard", "Sue Holderness", "Sue Nicholls"]),
 ("Her later role in The Royle Family", "Barbara Royle", ["Denise Royle", "Mary Carroll", "Cheryl Carroll"]),
 ("Ricky Tomlinson's Brookside character", "Bobby Grant", ["Bobby Ewing", "Bobby Beale", "Bobby Davro"]),
 ("The actor who played Barry Grant", "Paul Usher", ["Paul Nicholls", "Paul Bradley", "Paul Barber"]),
 ("The actor who played Jimmy Corkhill", "Dean Sullivan", ["Dean Gaffney", "Dean Holdsworth", "Dean Andrews"]),
 ("The kind of street it was set in", "A cul-de-sac", ["A tower block", "A market square", "A caravan site"])])

race("Casualty - name it", "Television", "medium", ["Casualty", "TV drama", "BBC"], [
 ("The channel", "BBC One", ["ITV", "Channel 4", "BBC Two"]),
 ("The year it began", "1986", ["1981", "1991", "1995"]),
 ("The made-up city it's set in", "Holby", ["Walford", "Weatherfield", "Erinsborough"]),
 ("The hospital", "Holby City Hospital", ["St Swithin's", "County General", "Seattle Grace"]),
 ("The department it follows", "The emergency department", ["Maternity", "Intensive care", "Surgery"]),
 ("The real city the setting is based on", "Bristol", ["Bath", "Plymouth", "Swindon"]),
 ("Where it has been filmed since moving in 2011", "Cardiff", ["Manchester", "Glasgow", "Leeds"]),
 ("The year it moved there", "2011", ["2005", "2015", "2018"]),
 ("The night it's usually on", "Saturday", ["Monday", "Wednesday", "Friday"]),
 ("The longest-serving character", "Charlie Fairhead", ["Charlie Hungerford", "Charlie Endell", "Charlie Cotton"]),
 ("His job", "Nurse", ["Doctor", "Paramedic", "Porter"]),
 ("The actor who plays him", "Derek Thompson", ["Derek Jacobi", "Derek Fowlds", "Derek Griffiths"]),
 ("The actress who played nurse Duffy", "Cathy Shipton", ["Cathy Tyson", "Cathy Dennis", "Kathy Burke"]),
 ("The actress who plays consultant Connie Beauchamp", "Amanda Mealing", ["Amanda Holden", "Amanda Burton", "Amanda Redman"]),
 ("The pair who created it", "Jeremy Brock and Paul Unwin", ["Tony Jordan", "Julia Smith", "Jimmy McGovern"]),
 ("Its spin-off on the wards", "Holby City", ["Holby General", "Holby Nights", "Holby A&E"]),
 ("The year that spin-off began", "1999", ["1994", "2003", "2007"]),
 ("Its short-lived police spin-off", "Holby Blue", ["Holby Cops", "Holby Beat", "Holby Law"]),
 ("The anniversary it marked in 2016", "30th", ["20th", "25th", "40th"]),
 ("The record it holds", "Longest-running emergency medical drama in the world", ["The UK's first soap", "Most-watched BBC show ever", "First British show in colour"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-284.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
