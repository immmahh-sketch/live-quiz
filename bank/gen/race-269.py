# Bank session 19 Oct 2026: 2 sitcom races -> bank/race-269.json (To the Manor Born; Butterflies).
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

race("To the Manor Born - name it", "Television", "medium", ["To the Manor Born", "sitcoms", "BBC"], [
 ("The lady of the manor", "Audrey fforbes-Hamilton", ["Audrey fforbes-Hampton", "Audrey Hamilton-Smythe", "Aubrey fforbes-Hamilton"]),
 ("The actress who played her", "Penelope Keith", ["Penelope Wilton", "Penelope Cruz", "Penelope Tree"]),
 ("Her role in The Good Life", "Margo Leadbetter", ["Barbara Good", "Hyacinth Bucket", "Mrs Slocombe"]),
 ("The manor", "Grantleigh Manor", ["Grantham Manor", "Greenleigh Hall", "Grantley Court"]),
 ("Where she has to move", "The Old Lodge", ["The Gatehouse", "The Dower House", "The Cottage"]),
 ("Her loyal butler", "Brabinger", ["Benson", "Barrington", "Bunter"]),
 ("Her best friend", "Marjory Frobisher", ["Margery Fairfax", "Mabel Fortescue", "Mavis Fletcher"]),
 ("The actress who played her", "Angela Thorne", ["Angela Rippon", "Angela Lansbury", "Angela Griffin"]),
 ("The new owner", "Richard DeVere", ["Richard Devereux", "Robert DeVere", "Richard De Vries"]),
 ("The actor who played him", "Peter Bowles", ["Peter Davison", "Peter Sallis", "Peter Vaughan"]),
 ("How he made his money", "A supermarket chain", ["Oil", "Property", "Banking"]),
 ("His company", "Cavendish Foods", ["DeVere Foods", "Grantleigh Holdings", "Bowles Brothers"]),
 ("His hospital sitcom", "Only When I Laugh", ["Doctor in the House", "Surgical Spirit", "Green Wing"]),
 ("The county it's set in", "Somerset", ["Devon", "Dorset", "Wiltshire"]),
 ("The estate where it was filmed", "Cricket St Thomas", ["Castle Howard", "Highclere Castle", "Chatsworth"]),
 ("The writer", "Peter Spence", ["Peter Kay", "Peter Cook", "Peter Nichols"]),
 ("The channel", "BBC One", ["ITV", "BBC Two", "Channel 4"]),
 ("The year it began", "1979", ["1975", "1983", "1987"]),
 ("Viewers for the last episode of its first series in 1979, in millions", "24", ["12", "18", "30"]),
 ("The year of the one-off Christmas return", "2007", ["2003", "2010", "2014"])])

race("Butterflies - name it", "Television", "medium", ["Butterflies", "sitcoms", "BBC"], [
 ("The restless mum", "Ria Parkinson", ["Rita Parkinson", "Ria Parker", "Rose Parkinson"]),
 ("The actress who played her", "Wendy Craig", ["Wendy Richard", "Wendy Hiller", "Wendy Turner"]),
 ("Her earlier family sitcom", "...And Mother Makes Three", ["Bless This House", "Father, Dear Father", "Mother's Ruin"]),
 ("What Ria is famously bad at", "Cooking", ["Driving", "Gardening", "Singing"]),
 ("Her husband", "Ben", ["Bill", "Bob", "Barry"]),
 ("His job", "Dentist", ["Doctor", "Vet", "Teacher"]),
 ("His hobby", "Collecting butterflies", ["Collecting stamps", "Collecting coins", "Model trains"]),
 ("The actor who played him", "Geoffrey Palmer", ["Geoffrey Whitehead", "Geoffrey Boycott", "Geoffrey Rush"]),
 ("His later sitcom with Judi Dench", "As Time Goes By", ["Waiting for God", "Ever Decreasing Circles", "To the Manor Born"]),
 ("Their sons", "Russell and Adam", ["Robert and Adam", "Russell and Andy", "Ross and Adam"]),
 ("The actor who played Adam", "Nicholas Lyndhurst", ["Nicholas Parsons", "Nicholas Hoult", "Nicholas Ball"]),
 ("The actor who played Russell", "Andrew Hall", ["Andrew Lincoln", "Andrew Sachs", "Andrew Scott"]),
 ("The man who tempts Ria", "Leonard", ["Lionel", "Lawrence", "Leslie"]),
 ("The actor who played him", "Bruce Montague", ["Bruce Forsyth", "Bruce Willis", "Bruce Jones"]),
 ("The writer", "Carla Lane", ["Roy Clarke", "John Sullivan", "Victoria Wood"]),
 ("Her later Liverpool sitcom", "Bread", ["Brookside", "Hollyoaks", "Scully"]),
 ("The theme song", "Love Is Like a Butterfly", ["Butterfly Kisses", "Fly Like an Eagle", "Wings of a Dove"]),
 ("The singer of the original", "Dolly Parton", ["Tammy Wynette", "Loretta Lynn", "Patsy Cline"]),
 ("The channel", "BBC Two", ["BBC One", "ITV", "Channel 4"]),
 ("The year it began", "1978", ["1974", "1982", "1986"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-269.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
