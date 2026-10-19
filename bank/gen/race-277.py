# Bank session 19 Oct 2026: 2 races -> bank/race-277.json (Heartbeat; Inspector Morse).
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

race("Heartbeat - name it", "Television", "medium", ["Heartbeat", "TV drama", "Yorkshire", "ITV"], [
 ("The village it's set in", "Aidensfield", ["Ambridge", "Holmfirth", "Royston Vasey"]),
 ("The real village where it was filmed", "Goathland", ["Haworth", "Thirsk", "Grassington"]),
 ("The county", "North Yorkshire", ["Lancashire", "Cumbria", "County Durham"]),
 ("The decade it's set in", "The 1960s", ["The 1940s", "The 1970s", "The 1980s"]),
 ("The channel", "ITV", ["BBC One", "Channel 4", "BBC Two"]),
 ("The year it began", "1992", ["1986", "1997", "2001"]),
 ("The year it ended", "2010", ["2003", "2006", "2014"]),
 ("The actor who played the first lead, PC Nick Rowan", "Nick Berry", ["Ross Kemp", "Martin Kemp", "Nick Pickard"]),
 ("His EastEnders character before that", "Wicksy", ["Lofty", "Nick Cotton", "Ricky"]),
 ("The singer whose song gave the show its name", "Buddy Holly", ["Elvis Presley", "Roy Orbison", "Cliff Richard"]),
 ("Nick's wife Kate's job", "Doctor", ["Nurse", "Teacher", "Vet"]),
 ("The village's lovable rogue", "Claude Greengrass", ["Arthur Daley", "Seth Armstrong", "Compo"]),
 ("The actor who played him", "Bill Maynard", ["Bill Treacher", "Bill Owen", "Bill Pertwee"]),
 ("His dog", "Alfred", ["Wellard", "Schmeichel", "Gnasher"]),
 ("The gruff sergeant", "Sergeant Blaketon", ["Sergeant Wilson", "Sergeant Lewis", "Sergeant Bilko"]),
 ("The Yes Minister actor who played him", "Derek Fowlds", ["Paul Eddington", "Nigel Hawthorne", "Derek Jacobi"]),
 ("The village pub", "The Aidensfield Arms", ["The Woolpack", "The Rovers Return", "The Royal Oak"]),
 ("The barmaid played by Tricia Penrose", "Gina", ["Bet", "Peggy", "Gail"]),
 ("What the village station became in the Harry Potter films", "Hogsmeade", ["King's Cross", "Little Whinging", "Godric's Hollow"]),
 ("The hospital spin-off", "The Royal", ["The General", "The Infirmary", "The Cottage Hospital"])])

race("Inspector Morse - name it", "Television", "medium", ["Inspector Morse", "detectives", "ITV"], [
 ("The actor who played Morse", "John Thaw", ["John Nettles", "David Jason", "Dennis Waterman"]),
 ("His earlier show as Jack Regan", "The Sweeney", ["The Professionals", "Z-Cars", "Minder"]),
 ("Morse's sidekick", "Sergeant Lewis", ["Sergeant Hathaway", "Sergeant Ashworth", "Sergeant Troy"]),
 ("The actor who played him", "Kevin Whately", ["Robson Green", "Jimmy Nail", "Tim Healy"]),
 ("The sidekick's home city", "Newcastle", ["Sunderland", "Leeds", "Liverpool"]),
 ("The city it's set in", "Oxford", ["Cambridge", "Bath", "York"]),
 ("Morse's car", "A red Jaguar", ["A green Rover", "A blue Mini", "A white Volvo"]),
 ("His first name, kept secret for years", "Endeavour", ["Ernest", "Edward", "Eustace"]),
 ("His favourite music", "Opera", ["Jazz", "Brass band", "Rock and roll"]),
 ("His favourite drink", "Real ale", ["Whisky", "Red wine", "Gin"]),
 ("The puzzle he always did", "The crossword", ["Sudoku", "The jigsaw", "A chess problem"]),
 ("The author who created him", "Colin Dexter", ["P. D. James", "Ruth Rendell", "Ian Rankin"]),
 ("What the author did in nearly every episode", "A walk-on cameo", ["Wrote the theme", "Played the pathologist", "Read the credits"]),
 ("What the theme tune hides", "MORSE in Morse code", ["The Oxford bells", "A police siren", "The Lewis theme backwards"]),
 ("The composer", "Barrington Pheloung", ["Ron Grainer", "Ed Welch", "Howard Goodall"]),
 ("The channel", "ITV", ["BBC One", "Channel 4", "BBC Two"]),
 ("The year it began", "1987", ["1983", "1991", "1995"]),
 ("The final episode", "The Remorseful Day", ["The Final Case", "Last Orders", "Death of a Detective"]),
 ("The year Morse died on screen", "2000", ["1995", "1998", "2004"]),
 ("The actor who played young Morse in the prequel", "Shaun Evans", ["Shaun Dooley", "Sean Pertwee", "Sean Bean"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-277.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
