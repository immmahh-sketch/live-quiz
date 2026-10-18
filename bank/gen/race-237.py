# Bank session 18 Oct 2026: 2 races -> bank/race-237.json (Men Behaving Badly; Rising Damp).
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

race("Men Behaving Badly - name it", "British sitcoms", "medium", ["Men Behaving Badly", "sitcoms", "1990s TV"], [
 ("Gary's surname", "Strang", ["Strong", "Stewart", "Strand"]),
 ("The actor who played Gary", "Martin Clunes", ["Neil Pearson", "Nick Berry", "Hugh Dennis"]),
 ("Gary's slobbish flatmate from series 2", "Tony", ["Terry", "Trevor", "Tommy"]),
 ("The actor who played him", "Neil Morrissey", ["Neil Stuke", "Nick Hancock", "Jason Merrells"]),
 ("Gary's original flatmate in series 1", "Dermot", ["Derek", "Declan", "Desmond"]),
 ("The actor who played him", "Harry Enfield", ["Paul Whitehouse", "Steve Coogan", "Rory Bremner"]),
 ("Gary's girlfriend, a nurse", "Dorothy", ["Doris", "Daphne", "Dolores"]),
 ("The actor who played her", "Caroline Quentin", ["Caroline Aherne", "Amanda Holden", "Sarah Lancashire"]),
 ("The upstairs neighbour the flatmate fancies", "Deborah", ["Diana", "Dawn", "Donna"]),
 ("The actor who played her", "Leslie Ash", ["Lisa Faulkner", "Michelle Collins", "Patsy Kensit"]),
 ("The business Gary runs", "Security alarms", ["Double glazing", "An estate agency", "Car hire"]),
 ("Gary's dim, elderly colleague", "George", ["Gordon", "Graham", "Geoffrey"]),
 ("What's always in the fridge", "Lager", ["Cider", "Bitter", "Wine"]),
 ("The writer", "Simon Nye", ["Ben Elton", "Richard Curtis", "John Sullivan"]),
 ("The channel it started on", "ITV", ["BBC Two", "Channel 4", "Sky One"]),
 ("The channel it moved to", "BBC One", ["E4", "Sky Two", "UK Gold"]),
 ("The year it began", "1992", ["1988", "1995", "1999"]),
 ("The year its last episodes went out", "1998", ["1994", "2001", "2004"]),
 ("Neil Morrissey's famous children's TV voice", "Bob the Builder", ["Postman Pat", "Fireman Sam", "Thomas the Tank Engine"]),
 ("Martin Clunes's later Cornish drama", "Doc Martin", ["Poldark", "Wycliffe", "Doctor Finlay"])])

race("Rising Damp - name it", "British sitcoms", "medium", ["Rising Damp", "sitcoms", "1970s TV", "Leonard Rossiter"], [
 ("The seedy, penny-pinching landlord", "Rigsby", ["Ripley", "Rigby", "Rimmer"]),
 ("The actor who played him", "Leonard Rossiter", ["Ronnie Barker", "Warren Mitchell", "Arthur Lowe"]),
 ("His cat", "Vienna", ["Venice", "Verona", "Vera"]),
 ("The prim tenant he adores", "Miss Jones", ["Miss Jenkins", "Miss Jarvis", "Miss James"]),
 ("The actor who played her", "Frances de la Tour", ["Penelope Keith", "Liz Smith", "Felicity Kendal"]),
 ("What he sighs whenever she's near", "Oh, Miss Jones!", ["Ooh, matron!", "Hello, sailor!", "Lovely jubbly!"]),
 ("The long-haired student tenant", "Alan", ["Andrew", "Adrian", "Anthony"]),
 ("What that student studies", "Medicine", ["Law", "Art", "Engineering"]),
 ("The actor who played him", "Richard Beckinsale", ["Nicholas Lyndhurst", "Robin Nedwell", "Paul Nicholas"]),
 ("The suave tenant", "Philip", ["Patrick", "Peter", "Paul"]),
 ("What that tenant claims his father is", "An African chief", ["An ambassador", "A king", "A diplomat"]),
 ("The actor who played him", "Don Warrington", ["Rudolph Walker", "Norman Beaton", "Lenny Henry"]),
 ("The kind of place they all live in", "A run-down lodging house", ["A seaside hotel", "A pub", "A council flat"]),
 ("The writer", "Eric Chappell", ["Roy Clarke", "John Esmonde", "Ray Galton"]),
 ("The stage play it grew out of", "The Banana Box", ["The Lodger", "Rooms to Let", "The Landlord"]),
 ("The ITV company that made it", "Yorkshire Television", ["Granada", "Tyne Tees", "Central"]),
 ("The year it began", "1974", ["1970", "1978", "1982"]),
 ("How many series were made", "4", ["2", "6", "8"]),
 ("The year of the film", "1980", ["1977", "1984", "1987"]),
 ("Leonard Rossiter's other classic sitcom", "The Fall and Rise of Reginald Perrin", ["Whatever Happened to the Likely Lads?", "Butterflies", "The Good Life"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-237.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
