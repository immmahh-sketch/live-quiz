# Bank session 19 Oct 2026: 2 sitcom races -> bank/race-254.json (Are You Being Served?; Steptoe and Son).
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

race("Are You Being Served? - name it", "Television", "medium", ["Are You Being Served?", "sitcoms", "BBC"], [
 ("The department store", "Grace Brothers", ["Grant Brothers", "Gregory & Sons", "Graves Brothers"]),
 ("The two departments sharing the floor", "Ladies' and gents' clothing", ["Toys and games", "Food and wine", "Shoes and hats"]),
 ("Who said 'I'm free!'", "Mr Humphries", ["Mr Grainger", "Captain Peacock", "Mr Harman"]),
 ("The actor who played him", "John Inman", ["John Inverdale", "John Thaw", "John Nettles"]),
 ("The actress who played Mrs Slocombe", "Mollie Sugden", ["Thora Hird", "Patricia Routledge", "Peggy Mount"]),
 ("The pet she always talked about", "Her cat", ["Her dog", "Her parrot", "Her goldfish"]),
 ("What kept changing on her", "Her hair colour", ["Her accent", "Her name badge", "Her glasses"]),
 ("The actor who played Captain Peacock", "Frank Thornton", ["Frank Windsor", "Frank Finlay", "Frank Skinner"]),
 ("The actor who played Mr Grainger", "Arthur Brough", ["Arthur Lowe", "Arthur Mullard", "Arthur Haynes"]),
 ("The floor manager", "Mr Rumbold", ["Mr Rumble", "Mr Rambling", "Mr Rumbelow"]),
 ("The cheeky junior in menswear", "Mr Lucas", ["Mr Lewis", "Mr Lawson", "Mr Lomax"]),
 ("The actor who played him", "Trevor Bannister", ["Trevor Eve", "Trevor McDonald", "Trevor Peacock"]),
 ("Young Mr Grace's line", "You've all done very well!", ["Didn't they do well!", "Good game, good game!", "Lovely jubbly!"]),
 ("The writers", "Jeremy Lloyd and David Croft", ["Croft and Perry", "Galton and Simpson", "Clement and La Frenais"]),
 ("The channel", "BBC One", ["ITV", "BBC Two", "Channel 4"]),
 ("The year it began", "1972", ["1968", "1976", "1980"]),
 ("Series made", "10", ["6", "8", "12"]),
 ("The year of the film", "1977", ["1974", "1980", "1983"]),
 ("The sequel set in a country house", "Grace & Favour", ["Grace Under Fire", "Still Being Served", "Back at Grace's"]),
 ("The year of the one-off revival", "2016", ["2010", "2013", "2019"])])

race("Steptoe and Son - name it", "Television", "medium", ["Steptoe and Son", "sitcoms", "BBC"], [
 ("Their trade", "Rag-and-bone men", ["Chimney sweeps", "Milkmen", "Coalmen"]),
 ("Their horse", "Hercules", ["Trigger", "Boxer", "Champion"]),
 ("Where they lived", "Oil Drum Lane", ["Coronation Street", "Albert Square", "Nelson Mandela House"]),
 ("The actor who played old Albert", "Wilfrid Brambell", ["Wilfrid Hyde-White", "Wilfred Pickles", "Wilfrid Lawson"]),
 ("The actor who played Harold", "Harry H. Corbett", ["Harry Enfield", "Harry Secombe", "Harry Worth"]),
 ("The Sooty puppeteer with almost the same name", "Harry Corbett", ["Matthew Corbett", "Ronnie Corbett", "Harry Hill"]),
 ("What Harold called his dad", "You dirty old man!", ["You old goat!", "You daft ha'p'orth!", "You silly old moo!"]),
 ("What Albert ate in the bath", "Pickled onions", ["Jellied eels", "Kippers", "Boiled sweets"]),
 ("Albert's actor's role in A Hard Day's Night", "Paul's grandfather", ["Ringo's uncle", "John's dad", "George's grandfather"]),
 ("The writers", "Ray Galton and Alan Simpson", ["Croft and Perry", "Clement and La Frenais", "Esmonde and Larbey"]),
 ("The comedian they wrote for before", "Tony Hancock", ["Frankie Howerd", "Tommy Cooper", "Kenneth Williams"]),
 ("The series its pilot came from", "Comedy Playhouse", ["Play for Today", "Armchair Theatre", "The Wednesday Play"]),
 ("The year it began", "1962", ["1958", "1966", "1970"]),
 ("The year it ended", "1974", ["1970", "1978", "1982"]),
 ("Films made", "2", ["1", "3", "4"]),
 ("The second film", "Steptoe and Son Ride Again", ["Steptoe and Son Go East", "Carry On Steptoe", "Steptoe Abroad"]),
 ("The American remake", "Sanford and Son", ["All in the Family", "Taxi", "Cheers"]),
 ("The 2008 BBC Four drama about its stars", "The Curse of Steptoe", ["Steptoe Unmasked", "Rag and Bone", "Dirty Old Men"]),
 ("What Harold always wanted", "To better himself", ["To become a millionaire", "To join the army", "To emigrate to Australia"]),
 ("The broadcaster", "BBC", ["ITV", "Channel 4", "Sky"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-254.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
