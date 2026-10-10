# Bank session 10 Oct 2026: 2 more general races -> bank/race-70.json. 20 rows each, target 10; wrong options are
# the same kind of thing, never another row's right answer, and never also right for that row.
import json, os
R = []
def race(title, cat, diff, tags, rows):
    rights = {r[1] for r in rows}
    assert len(rows) == 20, (title, len(rows))
    assert len(rights) == 20, (title, 'duplicate right answers')
    bad = [(q, w) for q, right, wrong in rows for w in wrong if w in rights]
    assert not bad, (title, 'recycled', bad)
    for q, right, wrong in rows:
        assert len(wrong) == 3 and len(set(wrong)) == 3 and right not in wrong, (title, q)
    R.append({"type": "race", "text": "The Race: " + title, "target": 10, "category": cat, "tags": tags, "difficulty": diff,
              "bank": [{"q": q, "right": right, "wrong": wrong} for q, right, wrong in rows]})

race("which famous 'Bay'?", "General knowledge", "medium", ["bays", "wordplay"], [
 ("Where Captain Cook landed in Australia, and convicts were meant to go", "Botany", ["Moreton", "Jervis", "Shark"]), ("The Lancashire resort with Eric's statue on the prom", "Morecambe", ["Heysham", "Fleetwood", "Lytham"]),
 ("The Yorkshire smugglers' village just south of Whitby", "Robin Hood's", ["Runswick", "Saltwick", "Sandsend"]), ("The Welsh Senedd stands beside it", "Cardiff", ["Swansea", "Newport", "Penarth"]),
 ("The US naval base and prison camp on Cuba", "Guantanamo", ["Havana", "Matanzas", "Cienfuegos"]), ("The failed 1961 invasion of Cuba, the Bay of ...", "Pigs", ["Goats", "Sharks", "Dogs"]),
 ("Jamaica's resort city on the north coast", "Montego", ["Negril", "Port Antonio", "Ocho Rios"]), ("The stormy Bay of ... off France and Spain", "Biscay", ["Brest", "Gascony", "Cantabria"]),
 ("The Bay of ... between India and Myanmar", "Bengal", ["Burma", "Madras", "Ceylon"]), ("Vietnam's bay of limestone islands", "Ha Long", ["Cam Ranh", "Nha Trang", "Da Nang"]),
 ("The North Tyneside resort with St Mary's Lighthouse", "Whitley", ["Cullercoats", "Seaton", "Blyth"]), ("The great Welsh bay famous for its dolphins", "Cardigan", ["Carmarthen", "Swansea", "Tremadog"]),
 ("Canada's huge inland sea, and a fur-trading company", "Hudson", ["Baffin", "Frobisher", "James"]), ("The Florida city facing St Petersburg across the water", "Tampa", ["Biscayne", "Pensacola", "Sarasota"]),
 ("The director of Transformers and Armageddon", "Michael", ["Tony", "Roland", "Simon"]), ("The Irish bay of the song: 'If you ever go across the sea to Ireland...'", "Galway", ["Dublin", "Donegal", "Bantry"]),
 ("The Australian surf town at the country's most easterly point", "Byron", ["Jervis", "Shark", "Moreton"]), ("The Californian bay of Cannery Row and the famous aquarium", "Monterey", ["Half Moon", "Santa Monica", "Morro"]),
 ("New Zealand's Bay of ..., near where the Treaty of Waitangi was signed", "Islands", ["Plenty", "Poverty", "Hawke's"]), ("The North Wales resort between Llandudno and Rhyl", "Colwyn", ["Prestatyn", "Abergele", "Conwy"])])

race("which famous 'Hall'?", "General knowledge", "hard", ["halls", "wordplay"], [
 ("The New York concert hall: 'How do you get there? Practise!'", "Carnegie", ["Lincoln", "Radio City", "Avery Fisher"]), ("London's round home of the Proms", "Albert", ["Festival", "Victoria", "Alexandra"]),
 ("Woody Allen's 1977 Oscar winner", "Annie", ["Hannah", "Alice", "Manhattan"]), ("Mr Toad's home", "Toad", ["Badger", "Mole", "Ratty"]),
 ("New York's corrupt old Democratic machine", "Tammany", ["Tweed", "Federal", "Gracie"]), ("The oldest part of Parliament, where monarchs lie in state", "Westminster", ["St Stephen's", "Banqueting", "Painted"]),
 ("Hilary Mantel's novel about Thomas Cromwell", "Wolf", ["Fox", "Bear", "Hawk"]), ("Mr Rochester's house in Jane Eyre", "Thornfield", ["Ferndean", "Lowood", "Gateshead"]),
 ("Where Stevens the butler serves in The Remains of the Day", "Darlington", ["Downton", "Brideshead", "Gosford"]), ("The hound haunts the family of this Dartmoor house", "Baskerville", ["Moriarty", "Grimpen", "Stapleton"]),
 ("Edinburgh's grand concert hall on Lothian Road", "Usher", ["Queen's", "Assembly", "Playhouse"]), ("Manchester's concert hall, home of the Hallé", "Bridgewater", ["Free Trade", "Lowry", "Apollo"]),
 ("Birmingham's concert hall in the ICC", "Symphony", ["Town", "Victoria", "Philharmonic"]), ("London's chamber music hall, named after its street", "Wigmore", ["Cadogan", "Conway", "Kings Place"]),
 ("The Texan model who was with Mick Jagger for over 20 years", "Jerry", ["Bianca", "Marianne", "Patti"]), ("The game show host behind the famous goat-and-car puzzle", "Monty", ["Bob", "Chuck", "Bill"]),
 ("Northumberland's Vanbrugh mansion near Seaton Sluice", "Seaton Delaval", ["Wallington", "Belsay", "Lindisfarne"]), ("The Norfolk estate whose vast beach ends Shakespeare in Love", "Holkham", ["Sandringham", "Blickling", "Felbrigg"]),
 ("The Elizabethan house with 'more glass than wall'", "Hardwick", ["Haddon", "Kedleston", "Burghley"]), ("Where Hogwarts students eat their feasts", "Great", ["Grand", "Dining", "Banquet"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-70.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
