# Bank session 18 Oct 2026: 2 races -> bank/race-236.json (The Vicar of Dibley; Red Dwarf).
# Red Dwarf's four actor rows were swapped out after the overlap check: they repeated 'which actor played this British sitcom
# character?'. Topics found free by probing candidate answers against every race in stock; checked again with lqsql/audit/race-overlap.py.
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

race("The Vicar of Dibley - name it", "British sitcoms", "medium", ["The Vicar of Dibley", "sitcoms", "Dawn French", "BBC"], [
 ("The vicar", "Geraldine Granger", ["Gillian Granger", "Geraldine Grange", "Gwendoline Granger"]),
 ("The actor who played her", "Dawn French", ["Jennifer Saunders", "Jo Brand", "Pauline Quirke"]),
 ("The county Dibley is in", "Oxfordshire", ["Berkshire", "Wiltshire", "Gloucestershire"]),
 ("The real village it was filmed in", "Turville", ["Thame", "Henley", "Marlow"]),
 ("The dim but sweet verger", "Alice Tinker", ["Alice Taylor", "Annie Tinker", "Alice Tucker"]),
 ("The actor who played her", "Emma Chambers", ["Sally Phillips", "Ruth Jones", "Jessica Hynes"]),
 ("Her married name", "Horton", ["Hooper", "Hughes", "Harris"]),
 ("The pompous chairman of the parish council", "David Horton", ["Daniel Horton", "David Hooper", "Derek Horton"]),
 ("His gentle son, who marries the verger", "Hugo", ["Hector", "Harry", "Henry"]),
 ("The councillor famous for 'No, no, no, no, no... yes'", "Jim Trott", ["Jim Trent", "Tim Trott", "John Trott"]),
 ("The farmer with the revolting stories", "Owen Newitt", ["Owen Newman", "Ewan Newitt", "Owen Nesbitt"]),
 ("The council's painfully dull minute-taker", "Frank Pickle", ["Fred Pickle", "Frank Parsnip", "Frank Piccolo"]),
 ("The man Geraldine finally marries", "Harry Kennedy", ["Henry Kennedy", "Harry Kingsley", "Hugh Kennedy"]),
 ("The actor who played him", "Richard Armitage", ["Richard E. Grant", "Rupert Penry-Jones", "Hugh Grant"]),
 ("What Geraldine jumps into in its most famous gag, and disappears", "A puddle", ["A pond", "A river", "A swimming pool"]),
 ("How episodes end", "A joke Alice doesn't get", ["A hymn", "A sermon", "A cup of tea"]),
 ("The writer who created it", "Richard Curtis", ["Ben Elton", "John Sullivan", "Simon Nye"]),
 ("The channel", "BBC One", ["ITV", "BBC Two", "Channel 4"]),
 ("The year it began", "1994", ["1990", "1998", "2001"]),
 ("The year the last regular episodes went out", "2007", ["2001", "2004", "2010"])])

race("Red Dwarf - name it", "British sitcoms", "medium", ["Red Dwarf", "sitcoms", "science fiction", "BBC"], [
 ("The company that owns the ship", "Jupiter Mining Corporation", ["Io Mining Corporation", "Saturn Shipping Company", "Titan Haulage"]),
 ("The last human being alive", "Dave Lister", ["Dave Lester", "Dave Lisle", "Dan Lister"]),
 ("The hologram of his dead bunkmate", "Arnold Rimmer", ["Albert Rimmer", "Arnold Rimmington", "Arthur Rimmer"]),
 ("What the H on his forehead stands for", "Hologram", ["Hero", "Hull", "Help"]),
 ("His rank aboard the ship", "Second Technician", ["First Officer", "Chief Engineer", "Captain"]),
 ("The ship's computer", "Holly", ["Hal", "Mother", "Kitt"]),
 ("The cleaning mechanoid who joins them", "Kryten", ["Kraken", "Kelvin", "Krissie"]),
 ("The creature descended from Lister's pet", "The Cat", ["The Dog", "The Rat", "The Fox"]),
 ("How long Lister spent in stasis", "3 million years", ["30 years", "3,000 years", "300,000 years"]),
 ("The little green shuttle they fly around in", "Starbug", ["Blue Midget", "Spacebug", "Moonhopper"]),
 ("The show's made-up swear word", "Smeg", ["Frak", "Gorram", "Frell"]),
 ("Lister's dream: a farm in …", "Fiji", ["Tahiti", "Jamaica", "Bali"]),
 ("Lister's favourite food", "Curry", ["Pizza", "Kebab", "Fish and chips"]),
 ("The ship's cigar-chomping captain", "Captain Hollister", ["Captain Holloway", "Captain Hollis", "Captain Hollings"]),
 ("The kitchen gadget obsessed with toast", "Talkie Toaster", ["Chatty Kettle", "Toasty", "Mr Crumpet"]),
 ("Lister's pet cat, smuggled aboard", "Frankenstein", ["Fluffy", "Tiddles", "Felix"]),
 ("The board game Rimmer is obsessed with", "Risk", ["Cluedo", "Monopoly", "Diplomacy"]),
 ("The writers who created it", "Grant and Naylor", ["Clement and La Frenais", "Esmonde and Larbey", "Armstrong and Bain"]),
 ("The year it began", "1988", ["1984", "1992", "1996"]),
 ("The channel it moved to for its 2009 comeback", "Dave", ["Sky One", "ITV2", "E4"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-236.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
