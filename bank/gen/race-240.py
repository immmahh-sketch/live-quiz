# Bank session 18 Oct 2026: 2 North East races -> bank/race-240.json (The Likely Lads; Vera).
# Topics found free by probing candidate answers against every race in stock (only Ann Cleeves appears, in 'who created this
# detective?'); checked again with lqsql/audit/race-overlap.py.
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

race("The Likely Lads - name it", "British sitcoms", "hard", ["The Likely Lads", "sitcoms", "Newcastle", "North East"], [
 ("Bob's surname", "Ferris", ["Ferguson", "Fenwick", "Farrell"]),
 ("Terry's surname", "Collier", ["Collins", "Connor", "Coulter"]),
 ("The actor who played Bob", "Rodney Bewes", ["Tim Healy", "Kevin Whately", "Jimmy Nail"]),
 ("The actor who played Terry", "James Bolam", ["Tim Healy", "Alun Armstrong", "Brian Glover"]),
 ("The city it's set in", "Newcastle", ["Sunderland", "Middlesbrough", "Gateshead"]),
 ("Bob's fiancée, then wife", "Thelma", ["Tina", "Teresa", "Tracey"]),
 ("The actor who played her", "Brigit Forsyth", ["Sheila Hancock", "Liz Smith", "Wendy Craig"]),
 ("The title of the 1970s sequel", "Whatever Happened to the Likely Lads?", ["Return of the Likely Lads", "The Likely Lads Again", "Still Likely"]),
 ("Where Terry spent the five years in between", "In the army", ["In prison", "In Australia", "At sea"]),
 ("The country he was posted to", "Germany", ["Cyprus", "Malta", "Belgium"]),
 ("Who Bob works for", "Thelma's father", ["His own father", "The council", "A brewery"]),
 ("Where Bob and Thelma set up home in the sequel", "A house on a new estate", ["A flat by the Quayside", "A caravan", "A pub"]),
 ("The episode where they hide from a football score all day", "No Hiding Place", ["Don't Tell Me the Score", "Final Whistle", "Match of the Day"]),
 ("Who sang the sequel's theme, 'Whatever Happened to You'", "Highly Likely", ["Lindisfarne", "The Animals", "Prelude"]),
 ("The writers", "Clement and La Frenais", ["Galton and Simpson", "Esmonde and Larbey", "Perry and Croft"]),
 ("Those writers' later prison sitcom", "Porridge", ["Open All Hours", "Rising Damp", "Bread"]),
 ("Those writers' later Geordie building-site drama", "Auf Wiedersehen, Pet", ["Spender", "Byker Grove", "Our Friends in the North"]),
 ("The year the original began", "1964", ["1960", "1968", "1971"]),
 ("The year the sequel began", "1973", ["1970", "1977", "1980"]),
 ("The year of the film", "1976", ["1972", "1983", "1986"])])

race("Vera - name it", "Crime dramas", "medium", ["Vera", "detectives", "Northumberland", "North East"], [
 ("Vera's full name", "Vera Stanhope", ["Vera Stanley", "Vera Stanton", "Vera Standish"]),
 ("Her rank", "DCI", ["DI", "DS", "Superintendent"]),
 ("The actor who plays her", "Brenda Blethyn", ["Julie Walters", "Imelda Staunton", "Sheridan Smith"]),
 ("The Mike Leigh film that won that actor a prize at Cannes", "Secrets & Lies", ["Vera Drake", "Naked", "Abigail's Party"]),
 ("The writer of the books", "Ann Cleeves", ["Val McDermid", "Ruth Rendell", "P.D. James"]),
 ("That writer's other TV series, set on Scottish islands", "Shetland", ["Orkney", "Skye", "Lewis"]),
 ("Her first sergeant", "Joe Ashworth", ["Joe Ashton", "John Ashworth", "Jim Ashworth"]),
 ("Her later sergeant", "Aiden Healy", ["Aidan Hartley", "Adam Healy", "Ian Healy"]),
 ("The loyal constable, Kenny …", "Lockhart", ["Lockwood", "Lockyer", "Lockley"]),
 ("The pathologist played by Paul Kaye", "Malcolm Donahue", ["Malcolm Dunn", "Martin Donahue", "Malcolm Daly"]),
 ("What she drives", "Land Rover Defender", ["Volvo estate", "Range Rover", "Ford Mondeo"]),
 ("What she calls everyone", "Pet", ["Duck", "Chuck", "Darling"]),
 ("Her trademark look", "Hat and mac", ["Trilby and suit", "Beret and cape", "Cap and anorak"]),
 ("Her late father", "Hector", ["Harold", "Henry", "Hugh"]),
 ("Where she lives", "A remote cottage", ["A city flat", "A narrowboat", "A semi in Gosforth"]),
 ("Her police force", "Northumberland and City Police", ["Northumbria Police", "Durham Constabulary", "Cleveland Police"]),
 ("The channel", "ITV", ["BBC One", "Channel 5", "Sky Atlantic"]),
 ("The year it began", "2011", ["2008", "2014", "2017"]),
 ("The year it ended", "2025", ["2019", "2021", "2023"]),
 ("How many series were made", "14", ["8", "11", "17"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-240.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
