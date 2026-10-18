# Bank session 18 Oct 2026: 2 races -> bank/race-235.json (One Foot in the Grave; Porridge).
# Topics found mostly free by probing candidate answers against every race in stock; checked again with lqsql/audit/race-overlap.py.
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

race("One Foot in the Grave - name it", "British sitcoms", "medium", ["One Foot in the Grave", "sitcoms", "1990s TV", "BBC"], [
 ("The grumpy pensioner", "Victor Meldrew", ["Victor Mallory", "Vernon Meldrew", "Victor Mildred"]),
 ("His famous cry", "I don't believe it!", ["Unbelievable!", "You what?", "Well I never!"]),
 ("The actor who played him", "Richard Wilson", ["Leonard Rossiter", "Warren Mitchell", "Brian Murphy"]),
 ("The country that actor comes from", "Scotland", ["Wales", "Ireland", "England"]),
 ("His long-suffering wife", "Margaret", ["Marjorie", "Maureen", "Mildred"]),
 ("The actor who played her", "Annette Crosbie", ["Wendy Craig", "Brenda Blethyn", "Liz Smith"]),
 ("The next-door neighbour who can't stand Victor", "Patrick", ["Peter", "Paul", "Philip"]),
 ("His wife", "Pippa", ["Penny", "Polly", "Patsy"]),
 ("The actor who played that neighbour", "Angus Deayton", ["Ian Hislop", "Paul Merton", "Clive Anderson"]),
 ("Margaret's gossiping friend", "Mrs Warboys", ["Mrs Wilberforce", "Mrs Wainwright", "Mrs Warburton"]),
 ("The cheery neighbour with an unseen mum", "Nick Swainey", ["Nick Swanley", "Mick Swainey", "Nigel Swaine"]),
 ("Victor's job before he was forced to retire", "Security guard", ["Postman", "Bus driver", "Ticket inspector"]),
 ("What replaced him in that job", "A box", ["A robot", "A dog", "His nephew"]),
 ("The writer", "David Renwick", ["David Croft", "Roy Clarke", "John Sullivan"]),
 ("That writer's later magician-detective series", "Jonathan Creek", ["Midsomer Murders", "Lewis", "Death in Paradise"]),
 ("Who sang the theme tune", "Eric Idle", ["John Cleese", "Michael Palin", "Terry Jones"]),
 ("The year it began", "1990", ["1986", "1994", "1998"]),
 ("The year Victor was killed off", "2000", ["1997", "2002", "2005"]),
 ("How Victor died", "Hit by a car", ["A heart attack", "Falling off a ladder", "In his sleep"]),
 ("The channel", "BBC One", ["ITV", "BBC Two", "Channel 4"])])

race("Porridge - name it", "British sitcoms", "medium", ["Porridge", "sitcoms", "1970s TV", "Ronnie Barker"], [
 ("Fletcher's first names", "Norman Stanley", ["Nigel Stanley", "Norman Sidney", "Neville Stanley"]),
 ("The actor who played him", "Ronnie Barker", ["Ronnie Corbett", "Leonard Rossiter", "Arthur Lowe"]),
 ("His young cellmate", "Godber", ["Goddard", "Gordon", "Gilbert"]),
 ("The actor who played the cellmate", "Richard Beckinsale", ["Nicholas Lyndhurst", "Paul Nicholas", "Christopher Strauli"]),
 ("The cellmate's home city", "Birmingham", ["Manchester", "Leeds", "Coventry"]),
 ("The fierce Scottish prison officer", "Mr Mackay", ["Mr McKenzie", "Mr McLeod", "Mr Murray"]),
 ("The soft-hearted prison officer", "Mr Barrowclough", ["Mr Barraclough", "Mr Burrows", "Mr Bradshaw"]),
 ("The prison", "Slade", ["Strangeways", "Wakefield", "Parkhurst"]),
 ("The county it's in", "Cumberland", ["Northumberland", "Yorkshire", "Lancashire"]),
 ("The inmate who runs the prison from his cell", "Grouty", ["Grimshaw", "Grundy", "Gripper"]),
 ("The actor who played him", "Peter Vaughan", ["Bob Hoskins", "Bernard Hill", "Kenneth Cope"]),
 ("The elderly lifer played by David Jason", "Blanco", ["Bianco", "Blackie", "Bronco"]),
 ("The gentle inmate played by Christopher Biggins", "Lukewarm", ["Tepid", "Mildew", "Softly"]),
 ("Fletcher's daughter", "Ingrid", ["Inga", "Irene", "Isobel"]),
 ("The writers", "Clement and La Frenais", ["Galton and Simpson", "Esmonde and Larbey", "Perry and Croft"]),
 ("The pilot, from Ronnie Barker's 'Seven of One'", "Prisoner and Escort", ["Open All Hours", "My Old Man", "I'll Fly You for a Quid"]),
 ("The sequel series after Fletcher's release", "Going Straight", ["Out of Slade", "Back on the Out", "Fletch Lives"]),
 ("The year it began", "1974", ["1970", "1978", "1982"]),
 ("The year of the film", "1979", ["1976", "1983", "1986"]),
 ("Who 'Fletcher' was in the 2016 revival", "His grandson", ["His son", "His nephew", "His brother"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-235.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
