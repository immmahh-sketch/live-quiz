# Bank session 18 Oct 2026: 2 races -> bank/race-229.json (Line of Duty; Fawlty Towers).
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

race("Line of Duty - name it", "Crime dramas", "medium", ["Line of Duty", "police", "BBC", "drama"], [
 ("The anti-corruption unit", "AC-12", ["AC-9", "CI5", "SO19"]),
 ("Its gaffer, Superintendent …", "Ted Hastings", ["Frank Burnside", "Gene Hunt", "Jack Regan"]),
 ("The actor who plays him", "Adrian Dunbar", ["James Nesbitt", "Liam Neeson", "Stephen Rea"]),
 ("The actor who plays Steve Arnott", "Martin Compston", ["Richard Madden", "Jack Lowden", "Kevin McKidd"]),
 ("The actor who plays Kate Fleming", "Vicky McClure", ["Suranne Jones", "Sheridan Smith", "Sarah Lancashire"]),
 ("The writer who created it", "Jed Mercurio", ["Jimmy McGovern", "Paul Abbott", "Sally Wainwright"]),
 ("Hastings's favourite exclamation, 'Mother of …'", "God", ["Mercy", "Pearl", "Moses"]),
 ("Hastings: 'Now we're sucking …'", "Diesel", ["Petrol", "Lemons", "Fumes"]),
 ("Hastings: 'I didn't float up the … in a bubble'", "Lagan", ["Liffey", "Thames", "Clyde"]),
 ("Who 'H' turned out to be in the final series", "Ian Buckells", ["Patricia Carmichael", "Gill Biggeloe", "Derek Hilton"]),
 ("The bent DC known as 'the Caddy'", "Dot Cottan", ["Tommy Hunter", "Ryan Pilkington", "Mark Moffatt"]),
 ("Keeley Hawes's character in series 2", "Lindsay Denton", ["Jackie Laverty", "Gill Biggeloe", "Steph Corbett"]),
 ("Thandiwe Newton's DCI in series 4", "Roz Huntley", ["Jackie Laverty", "Steph Corbett", "Lisa McQueen"]),
 ("Stephen Graham's undercover cop in series 5", "John Corbett", ["Danny Waldron", "Tony Gates", "Nick Huntley"]),
 ("Kelly Macdonald's DCI in series 6", "Jo Davidson", ["Lisa McQueen", "Tony Gates", "Patricia Carmichael"]),
 ("The city series 1 was filmed in", "Birmingham", ["Leeds", "Bristol", "Sheffield"]),
 ("The city it was filmed in from series 2", "Belfast", ["Glasgow", "Liverpool", "Manchester"]),
 ("What the gang's hitmen wear over their faces", "Balaclavas", ["Bandanas", "Hoods", "Visors"]),
 ("The channel it moved to for series 4", "BBC One", ["BBC Two", "ITV", "Channel 4"]),
 ("The year the final series went out", "2021", ["2019", "2020", "2022"])])

race("Fawlty Towers - name it", "British sitcoms", "medium", ["Fawlty Towers", "sitcoms", "1970s TV", "John Cleese"], [
 ("The seaside town the hotel is in", "Torquay", ["Paignton", "Weymouth", "Eastbourne"]),
 ("Basil's wife", "Sybil", ["Sylvia", "Sheila", "Cynthia"]),
 ("The waiter from Barcelona", "Manuel", ["Miguel", "Pedro", "Carlos"]),
 ("Manuel's baffled reply", "Qué?", ["¿Por qué?", "¡Olé!", "Mañana"]),
 ("The chambermaid and art student", "Polly", ["Pam", "Penny", "Patsy"]),
 ("The old military resident", "The Major", ["The Colonel", "The Brigadier", "The Commander"]),
 ("The two elderly lady residents", "Miss Tibbs and Miss Gatsby", ["Miss Prism and Miss Bates", "Miss Pink and Miss Blue", "Miss Hope and Miss Glory"]),
 ("Manuel's 'Siberian hamster', which is really a rat", "Basil", ["Pedro", "Ratty", "Roland"]),
 ("Basil's warning about the German guests", "Don't mention the war", ["Stand at ease", "Keep calm", "Never surrender"]),
 ("Who wrote it with John Cleese", "Connie Booth", ["Graham Chapman", "Michael Palin", "Eric Idle"]),
 ("How many episodes were made", "12", ["6", "18", "24"]),
 ("The real Torquay hotel whose rude owner inspired it", "Gleneagles", ["Savoy", "Imperial", "Grand"]),
 ("What Basil thrashes his broken-down car with", "A tree branch", ["An umbrella", "A golf club", "A cricket bat"]),
 ("The cowboy builder in 'The Builders'", "O'Reilly", ["O'Brien", "O'Neill", "Murphy"]),
 ("The episode where a guest dies in his room", "The Kipper and the Corpse", ["The Hotel Inspectors", "Gourmet Night", "Communication Problems"]),
 ("What Basil says Sybil's laugh sounds like", "Machine-gunning a seal", ["A donkey braying", "A boiling kettle", "A car alarm"]),
 ("The actor who played Sybil", "Prunella Scales", ["Penelope Keith", "Wendy Craig", "June Whitfield"]),
 ("The actor who played Manuel", "Andrew Sachs", ["David Jason", "Peter Sallis", "Bill Pertwee"]),
 ("The chef who gets drunk on Gourmet Night", "Kurt", ["Klaus", "Karl", "Kevin"]),
 ("The year it first went out", "1975", ["1971", "1979", "1983"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-229.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
