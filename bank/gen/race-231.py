# Bank session 18 Oct 2026: 2 races -> bank/race-231.json (The Good Life; Last of the Summer Wine).
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

race("The Good Life - name it", "British sitcoms", "medium", ["The Good Life", "sitcoms", "1970s TV", "BBC"], [
 ("The London suburb where it's set", "Surbiton", ["Sutton", "Croydon", "Kingston"]),
 ("Tom and Barbara's surname", "Good", ["Green", "Gold", "Grant"]),
 ("The birthday on which Tom quits his job", "40th", ["30th", "35th", "50th"]),
 ("What Tom designed before he quit", "Plastic toys for cereal packets", ["Kitchen gadgets", "Car parts", "Greetings cards"]),
 ("The firm Tom and Jerry both worked for", "JJM", ["ICI", "GKN", "JCB"]),
 ("What the Goods set out to be", "Self-sufficient", ["Self-employed", "Self-made", "Self-contained"]),
 ("The snobbish neighbour", "Margo Leadbetter", ["Margaret Leadbetter", "Marjorie Leadbetter", "Margo Lidbetter"]),
 ("Her husband", "Jerry", ["Jeremy", "Geoffrey", "Jimmy"]),
 ("The Goods' goat", "Geraldine", ["Gertrude", "Gwendoline", "Gladys"]),
 ("The Goods' pigs", "Pinky and Perky", ["Babe and Bertie", "Percy and Polly", "Pip and Squeak"]),
 ("The Goods' cockerel, named after a revolutionary", "Lenin", ["Stalin", "Trotsky", "Marx"]),
 ("The actor who played Tom", "Richard Briers", ["Nicholas Lyndhurst", "Peter Bowles", "Martin Jarvis"]),
 ("The actor who played Barbara", "Felicity Kendal", ["Wendy Craig", "Judi Dench", "Jan Francis"]),
 ("The actor who played Margo", "Penelope Keith", ["Prunella Scales", "Patricia Routledge", "June Whitfield"]),
 ("The actor who played Jerry", "Paul Eddington", ["Leonard Rossiter", "Richard Wilson", "Terry Scott"]),
 ("The writing partnership behind it", "Esmonde and Larbey", ["Galton and Simpson", "Perry and Croft", "Clement and La Frenais"]),
 ("The year it began", "1975", ["1970", "1980", "1983"]),
 ("Who watched a special recording of an episode in 1978", "The Queen", ["Princess Margaret", "Prince Charles", "The Queen Mother"]),
 ("Its title when shown in America", "Good Neighbors", ["The Simple Life", "Back to the Land", "Suburban Farmers"]),
 ("Penelope Keith's next sitcom, as Audrey fforbes-Hamilton", "To the Manor Born", ["Keeping Up Appearances", "Executive Stress", "Next of Kin"])])

race("Last of the Summer Wine - name it", "British sitcoms", "medium", ["Last of the Summer Wine", "sitcoms", "Yorkshire", "BBC"], [
 ("The writer of every single episode", "Roy Clarke", ["Jimmy Perry", "Ray Galton", "Eric Chappell"]),
 ("The scruffy one in wellies and a woolly hat", "Compo", ["Cobbo", "Clompo", "Crusty"]),
 ("The actor who played him", "Bill Owen", ["Bill Maynard", "Bill Pertwee", "Bill Treacher"]),
 ("The gentle one, played by Peter Sallis", "Clegg", ["Clagg", "Clough", "Craig"]),
 ("The pompous ex-soldier, Foggy …", "Dewhurst", ["Dewsbury", "Dunwoody", "Dawson"]),
 ("The original third man, Cyril …", "Blamire", ["Bentley", "Barraclough", "Braithwaite"]),
 ("The fearsome neighbour in wrinkled stockings", "Nora Batty", ["Nora Barker", "Nellie Batty", "Nora Bates"]),
 ("Her henpecked husband", "Wally", ["Wilf", "Willie", "Wilbur"]),
 ("The woman who runs the café", "Ivy", ["Edie", "Ida", "Iris"]),
 ("Her husband", "Sid", ["Stan", "Sam", "Seth"]),
 ("The woman Howard sneaks off to meet", "Marina", ["Mavis", "Myra", "Maureen"]),
 ("Howard's wife", "Pearl", ["Pauline", "Phyllis", "Peggy"]),
 ("The actor who played the café owner", "Jane Freeman", ["Thora Hird", "Kathy Staff", "Dora Bryan"]),
 ("The Yorkshire town it was filmed in", "Holmfirth", ["Hebden Bridge", "Haworth", "Harrogate"]),
 ("That town's county", "West Yorkshire", ["North Yorkshire", "South Yorkshire", "Lancashire"]),
 ("Who wrote the theme music", "Ronnie Hazlehurst", ["Ron Grainer", "Tony Hatch", "Max Harris"]),
 ("The title of the 1973 pilot", "Of Funerals and Fish", ["Of Wellies and Wine", "Three Old Men", "Summer's End"]),
 ("The year it began", "1973", ["1968", "1978", "1983"]),
 ("The year it ended", "2010", ["2000", "2005", "2015"]),
 ("The record it holds", "Longest-running sitcom", ["Most-watched sitcom", "Most episodes of any drama", "Biggest cast"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-231.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
