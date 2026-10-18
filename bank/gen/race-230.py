# Bank session 18 Oct 2026: 2 races -> bank/race-230.json (Derry Girls; Hi-de-Hi!).
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

race("Derry Girls - name it", "British sitcoms", "medium", ["Derry Girls", "sitcoms", "Northern Ireland", "Channel 4"], [
 ("The city it's set in", "Derry", ["Belfast", "Omagh", "Newry"]),
 ("The writer who created it", "Lisa McGee", ["Sharon Horgan", "Phoebe Waller-Bridge", "Aisling Bea"]),
 ("The heroine whose diary we hear", "Erin Quinn", ["Erin Doyle", "Aine Quinn", "Erin O'Neill"]),
 ("Erin's dreamy, odd cousin", "Orla", ["Aoife", "Niamh", "Siobhan"]),
 ("The anxious swot of the gang", "Clare", ["Cara", "Ciara", "Clodagh"]),
 ("The wild one with the filthy mouth", "Michelle", ["Marie", "Maeve", "Maura"]),
 ("Michelle's cousin from England", "James", ["Jack", "Jamie", "Jonathan"]),
 ("What everyone calls him", "The wee English fella", ["The wee Scottish lad", "The posh boy", "The new fella"]),
 ("The deadpan nun in charge of the school", "Sister Michael", ["Sister Agnes", "Sister Mary", "Sister Bernadette"]),
 ("Erin's grandad, Granda …", "Joe", ["Pat", "Seamus", "Frank"]),
 ("Erin's dad, whom Granda can't stand", "Gerry", ["Dermot", "Declan", "Brendan"]),
 ("The famously boring uncle", "Colm", ["Kevin", "Liam", "Sean"]),
 ("The girls' school", "Our Lady Immaculate College", ["St Mary's Grammar", "Sacred Heart College", "St Columb's College"]),
 ("The handsome young priest in series 1", "Father Peter", ["Father Ted", "Father Dougal", "Father Brown"]),
 ("The surly owner of the corner shop", "Dennis", ["Desmond", "Donal", "Derek"]),
 ("The girls' goody-goody rival", "Jenny Joyce", ["Jenny Doyle", "Jessica Joyce", "Julie Joyce"]),
 ("The Cranberries song over the opening titles", "Dreams", ["Zombie", "Linger", "Ode to My Family"]),
 ("The American president who visits in series 2", "Bill Clinton", ["George Bush", "Ronald Reagan", "Jimmy Carter"]),
 ("The channel it was made for", "Channel 4", ["BBC Two", "ITV", "RTÉ"]),
 ("The 1998 vote at the heart of the final episode", "Good Friday Agreement", ["Anglo-Irish Agreement", "Downing Street Declaration", "Sunningdale Agreement"])])

race("Hi-de-Hi! - name it", "British sitcoms", "medium", ["Hi-de-Hi", "sitcoms", "1980s TV", "holiday camps"], [
 ("The holiday camp", "Maplins", ["Butlins", "Pontins", "Warners"]),
 ("Its seaside town", "Crimpton-on-Sea", ["Skegness", "Clacton", "Bognor"]),
 ("The year the first series is set in", "1959", ["1949", "1969", "1979"]),
 ("The camp's never-seen owner", "Joe Maplin", ["Billy Butlin", "Fred Pontin", "Harry Warner"]),
 ("The university lecturer who became entertainments manager", "Jeffrey Fairbrother", ["Gerald Fairweather", "Jeremy Fairburn", "Geoffrey Fairfax"]),
 ("The man who later replaced him", "Clive Dempster", ["Clive Dunn", "Colin Dempsey", "Charles Dempster"]),
 ("The Welsh sports organiser on the tannoy", "Gladys Pugh", ["Glenys Price", "Gwen Pugh", "Megan Jones"]),
 ("Her greeting to the campers", "Hi-de-Hi!", ["Wakey wakey!", "Hello campers!", "Rise and shine!"]),
 ("What the campers shout back", "Ho-de-Ho!", ["Ha-de-Ha!", "Hip hip hooray!", "Hello Gladys!"]),
 ("The camp comic", "Ted Bovis", ["Ted Bates", "Tom Bovey", "Terry Bowes"]),
 ("His young sidekick", "Spike Dixon", ["Spike Milligan", "Spud Dixon", "Spike Daniels"]),
 ("The chalet maid desperate to be a Yellowcoat", "Peggy", ["Polly", "Patsy", "Pearl"]),
 ("The colour of the entertainers' jackets", "Yellow", ["Red", "Blue", "Green"]),
 ("The drunk who works the Punch and Judy show", "Mr Partridge", ["Mr Pheasant", "Mr Peacock", "Mr Plover"]),
 ("The ex-jockey who runs the riding stables", "Fred Quilley", ["Fred Quigley", "Frank Quilley", "Fred Quinn"]),
 ("The snooty ballroom-dancing couple", "Barry and Yvonne", ["Fred and Ginger", "Lionel and Mavis", "Torvill and Dean"]),
 ("The writers, also behind 'Dad's Army'", "Jimmy Perry and David Croft", ["Clement and La Frenais", "Galton and Simpson", "Croft and Lloyd"]),
 ("The actor who played Ted", "Paul Shane", ["Bernard Bresslaw", "Jack Douglas", "Freddie Davies"]),
 ("Su Pollard's 1986 number two hit", "Starting Together", ["Come What May", "Together Again", "Starting Over"]),
 ("The year it began", "1980", ["1975", "1984", "1988"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-230.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
