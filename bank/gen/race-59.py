# Bank session 10 Oct 2026: 3 more general races -> bank/race-59.json. 20 rows each, target 10; wrong options are
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

race("which country is this famous forest in?", "World geography", "hard", ["forests", "countries"], [
 ("The Black Forest", "Germany", ["Austria", "Switzerland", "Luxembourg"]), ("Sherwood Forest", "England", ["Ireland", "the Isle of Man", "Jersey"]),
 ("The Daintree Rainforest", "Australia", ["Papua New Guinea", "Fiji", "Indonesia"]), ("The Hoh Rainforest", "the USA", ["Greenland", "Iceland", "Ireland"]),
 ("Monteverde Cloud Forest", "Costa Rica", ["Panama", "Nicaragua", "Honduras"]), ("Hoia Baciu, the 'haunted' forest", "Romania", ["Hungary", "Bulgaria", "Moldova"]),
 ("The Crooked Forest", "Poland", ["Czechia", "Slovakia", "Lithuania"]), ("The Forest of Fontainebleau", "France", ["Luxembourg", "Switzerland", "Monaco"]),
 ("Hallerbos, the bluebell wood", "Belgium", ["Luxembourg", "the Netherlands", "Denmark"]), ("The Arashiyama Bamboo Grove", "Japan", ["China", "Taiwan", "South Korea"]),
 ("Sinharaja Forest", "Sri Lanka", ["India", "Bangladesh", "the Maldives"]), ("The Tsingy de Bemaraha stone forest", "Madagascar", ["Mozambique", "Mauritius", "the Comoros"]),
 ("The Great Bear Rainforest", "Canada", ["Greenland", "Iceland", "Ireland"]), ("Chapultepec Forest", "Mexico", ["Guatemala", "Cuba", "Belize"]),
 ("Waipoua Forest, home of the giant kauri", "New Zealand", ["Fiji", "Samoa", "Papua New Guinea"]), ("Galloway Forest", "Scotland", ["Ireland", "the Isle of Man", "Iceland"]),
 ("Tollymore Forest", "Northern Ireland", ["Ireland", "the Isle of Man", "Iceland"]), ("Gwydir Forest", "Wales", ["Ireland", "the Isle of Man", "Iceland"]),
 ("Pacaya-Samiria Reserve", "Peru", ["Bolivia", "Venezuela", "Paraguay"]), ("Yasuní National Park", "Ecuador", ["Bolivia", "Venezuela", "Paraguay"])])

race("which island is this famous sight on?", "Travel", "hard", ["islands", "landmarks"], [
 ("The Statue of Liberty", "Liberty Island", ["Ellis Island", "Manhattan", "Staten Island"]), ("The moai statues", "Easter Island", ["Tahiti", "Pitcairn", "Galápagos"]),
 ("The Blue Grotto", "Capri", ["Ischia", "Elba", "Malta"]), ("The Old Man of Hoy", "Hoy", ["Lewis", "Unst", "Mull"]),
 ("The Old Man of Storr", "Skye", ["Lewis", "Mull", "Arran"]), ("The Needles", "The Isle of Wight", ["The Isle of Man", "Anglesey", "Jersey"]),
 ("Lindisfarne Castle", "Holy Island", ["The Farne Islands", "Anglesey", "The Isle of Man"]), ("Fingal's Cave", "Staffa", ["Iona", "Mull", "Arran"]),
 ("Tanah Lot temple", "Bali", ["Java", "Lombok", "Sumatra"]), ("The Big Buddha (Tian Tan)", "Lantau", ["Hong Kong Island", "Macau", "Taiwan"]),
 ("The floating torii of Itsukushima Shrine", "Miyajima", ["Okinawa", "Hokkaido", "Shikoku"]), ("The palace of Knossos", "Crete", ["Kos", "Naxos", "Cyprus"]),
 ("The Achilleion Palace", "Corfu", ["Kos", "Naxos", "Zakynthos"]), ("The village of Oia", "Santorini", ["Mykonos", "Naxos", "Paros"]),
 ("St Magnus Cathedral", "Orkney", ["Shetland", "Lewis", "Arran"]), ("Tresco Abbey Garden", "Tresco", ["St Mary's", "Lundy", "Jersey"]),
 ("Mount Etna", "Sicily", ["Ischia", "Malta", "Elba"]), ("The nuraghe of Su Nuraxi", "Sardinia", ["Malta", "Elba", "Ischia"]),
 ("Napoleon's birthplace", "Corsica", ["Elba", "Malta", "Ischia"]), ("Brownsea Castle", "Brownsea Island", ["Lundy", "Hayling Island", "Portland"])])

race("which country is this famous valley in?", "World geography", "hard", ["valleys", "countries"], [
 ("The Valley of the Kings", "Egypt", ["Sudan", "Jordan", "Libya"]), ("The Rhine Gorge's castles", "Germany", ["Luxembourg", "Belgium", "the Netherlands"]),
 ("The Loire Valley's châteaux", "France", ["Belgium", "Luxembourg", "Monaco"]), ("The Douro Valley's port vineyards", "Portugal", ["Andorra", "Malta", "Greece"]),
 ("The Kathmandu Valley", "Nepal", ["Bhutan", "Bangladesh", "Sri Lanka"]), ("The Barossa Valley", "Australia", ["New Zealand", "Fiji", "South Africa"]),
 ("The Okanagan Valley", "Canada", ["New Zealand", "Iceland", "Ireland"]), ("The Elqui Valley", "Chile", ["Argentina", "Bolivia", "Uruguay"]),
 ("The Bekaa Valley", "Lebanon", ["Syria", "Jordan", "Cyprus"]), ("The Hunza Valley", "Pakistan", ["Afghanistan", "Tajikistan", "Bangladesh"]),
 ("The Wachau Valley", "Austria", ["Czechia", "Slovakia", "Hungary"]), ("The Rhondda", "Wales", ["Northern Ireland", "the Isle of Man", "Ireland"]),
 ("Glen Coe", "Scotland", ["Northern Ireland", "the Isle of Man", "Ireland"]), ("Swaledale", "England", ["Northern Ireland", "the Isle of Man", "Ireland"]),
 ("The Lauterbrunnen Valley", "Switzerland", ["Liechtenstein", "Slovenia", "Czechia"]), ("The Valley of the Roses", "Bulgaria", ["Romania", "Greece", "North Macedonia"]),
 ("The Val d'Orcia", "Italy", ["Malta", "San Marino", "Greece"]), ("The Cocora Valley's wax palms", "Colombia", ["Venezuela", "Ecuador", "Panama"]),
 ("The Sacred Valley of the Incas", "Peru", ["Bolivia", "Ecuador", "Argentina"]), ("The Viñales Valley", "Cuba", ["Jamaica", "the Dominican Republic", "Puerto Rico"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-59.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
