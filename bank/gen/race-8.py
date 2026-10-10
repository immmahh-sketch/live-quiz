# Bank session 10 Oct 2026: 4 more general races -> bank/race-8.json. 20 rows each, target 10; wrong options are
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

race("which country is this river in?", "World geography", "medium", ["rivers", "countries"], [
 ("The Thames", "England", ["Belgium", "the Netherlands", "the Isle of Man"]), ("The Seine", "France", ["Belgium", "Switzerland", "Luxembourg"]),
 ("The Tiber", "Italy", ["Greece", "Malta", "Croatia"]), ("The Volga", "Russia", ["Ukraine", "Belarus", "Kazakhstan"]),
 ("The Yangtze", "China", ["Vietnam", "Mongolia", "Taiwan"]), ("The Shannon", "Ireland", ["the Isle of Man", "Iceland", "Belgium"]),
 ("The Murray", "Australia", ["Papua New Guinea", "Fiji", "Indonesia"]), ("The Waikato", "New Zealand", ["Fiji", "Samoa", "Tonga"]),
 ("The Ebro", "Spain", ["Andorra", "Morocco", "Malta"]), ("The Vistula", "Poland", ["Germany", "Czechia", "Lithuania"]),
 ("The Mississippi", "USA", ["Mexico", "Cuba", "the Bahamas"]), ("The Tay", "Scotland", ["the Isle of Man", "Norway", "Iceland"]),
 ("The Shinano", "Japan", ["Taiwan", "the Philippines", "Vietnam"]), ("The Mackenzie", "Canada", ["Greenland", "Iceland", "Norway"]),
 ("The Chao Phraya", "Thailand", ["Laos", "Cambodia", "Vietnam"]), ("The Irrawaddy", "Myanmar", ["Bangladesh", "Nepal", "Laos"]),
 ("The Han", "South Korea", ["Taiwan", "Mongolia", "the Philippines"]), ("The São Francisco", "Brazil", ["Argentina", "Colombia", "Peru"]),
 ("The Taff", "Wales", ["the Isle of Man", "Jersey", "Guernsey"]), ("The Lagan", "Northern Ireland", ["the Isle of Man", "Jersey", "Guernsey"])])

race("which US state is this city in?", "World geography", "medium", ["USA", "states", "cities"], [
 ("Las Vegas", "Nevada", ["New Mexico", "Idaho", "Oregon"]), ("Miami", "Florida", ["Alabama", "South Carolina", "Mississippi"]),
 ("Seattle", "Washington", ["Oregon", "Idaho", "Montana"]), ("Chicago", "Illinois", ["Wisconsin", "Indiana", "Iowa"]),
 ("Boston", "Massachusetts", ["Connecticut", "Vermont", "New York"]), ("Detroit", "Michigan", ["Wisconsin", "Indiana", "Missouri"]),
 ("Nashville", "Tennessee", ["Kentucky", "Alabama", "Arkansas"]), ("New Orleans", "Louisiana", ["Mississippi", "Alabama", "Arkansas"]),
 ("Denver", "Colorado", ["Wyoming", "Kansas", "New Mexico"]), ("Phoenix", "Arizona", ["New Mexico", "Oklahoma", "Idaho"]),
 ("Atlanta", "Georgia", ["Alabama", "South Carolina", "North Carolina"]), ("Houston", "Texas", ["Oklahoma", "Arkansas", "New Mexico"]),
 ("Philadelphia", "Pennsylvania", ["New Jersey", "Delaware", "New York"]), ("Salt Lake City", "Utah", ["Idaho", "Wyoming", "Montana"]),
 ("Baltimore", "Maryland", ["Virginia", "Delaware", "New Jersey"]), ("Anchorage", "Alaska", ["Montana", "Oregon", "Wyoming"]),
 ("Honolulu", "Hawaii", ["Oregon", "New Mexico", "Virginia"]), ("Minneapolis", "Minnesota", ["Wisconsin", "Iowa", "Nebraska"]),
 ("Cleveland", "Ohio", ["Indiana", "Kentucky", "New York"]), ("San Diego", "California", ["Oregon", "New Mexico", "Idaho"])])

race("name the famous horse", "Animals", "medium", ["horses", "famous animals"], [
 ("The Lone Ranger's horse", "Silver", ["Champion", "Topper", "Duke"]), ("Don Quixote's horse", "Rocinante", ["Dapple", "Dulcinea", "Hidalgo"]),
 ("Napoleon's famous grey", "Marengo", ["Austerlitz", "Jena", "Waterloo"]), ("Wellington's horse at Waterloo", "Copenhagen", ["Waterloo", "Salamanca", "Vitoria"]),
 ("Alexander the Great's horse", "Bucephalus", ["Pegasus", "Xanthus", "Arion"]), ("Dick Turpin's horse", "Black Bess", ["Black Beauty", "Black Jack", "Brown Bess"]),
 ("Roy Rogers' horse", "Trigger", ["Champion", "Topper", "Buttermilk"]), ("Woody's horse in Toy Story", "Bullseye", ["Buster", "Slinky", "Spirit"]),
 ("Gandalf's horse", "Shadowfax", ["Brego", "Bill", "Hasufel"]), ("Steptoe and Son's horse", "Hercules", ["Samson", "Dobbin", "Albert"]),
 ("The Derby winner kidnapped in 1983", "Shergar", ["Arkle", "Nijinsky", "Shirley Heights"]), ("Three-time Grand National winner", "Red Rum", ["L'Escargot", "Crisp", "Aldaniti"]),
 ("The grey who won the 1989 Gold Cup", "Desert Orchid", ["Arkle", "Best Mate", "Kauto Star"]), ("Animal Farm's cart-horse sent to the knacker's", "Boxer", ["Clover", "Mollie", "Benjamin"]),
 ("The horse in War Horse", "Joey", ["Topthorn", "Albert", "Ginger"]), ("Tonto's horse", "Scout", ["Paint", "Pinto", "Lightning"]),
 ("Zorro's horse", "Tornado", ["Phantom", "Diablo", "Thunder"]), ("The palace horse in Tangled", "Maximus", ["Pascal", "Flynn", "Achilles"]),
 ("Odin's eight-legged horse", "Sleipnir", ["Gullfaxi", "Skinfaxi", "Arvakr"]), ("The racehorse who won all 14 of his races", "Frankel", ["Sea the Stars", "Enable", "Dancing Brave"])])

race("which country does this club play in?", "Football", "medium", ["clubs", "countries"], [
 ("Ajax", "the Netherlands", ["Denmark", "Germany", "Finland"]), ("Benfica", "Portugal", ["Spain", "Italy", "Uruguay"]),
 ("Celtic", "Scotland", ["Ireland", "Wales", "Northern Ireland"]), ("Galatasaray", "Turkey", ["Cyprus", "Bulgaria", "Albania"]),
 ("Olympiacos", "Greece", ["Cyprus", "Italy", "Bulgaria"]), ("Boca Juniors", "Argentina", ["Uruguay", "Chile", "Colombia"]),
 ("Flamengo", "Brazil", ["Uruguay", "Colombia", "Mexico"]), ("Red Star Belgrade", "Serbia", ["Bosnia", "Slovenia", "Montenegro"]),
 ("Club Brugge", "Belgium", ["Denmark", "France", "Luxembourg"]), ("Dinamo Zagreb", "Croatia", ["Slovenia", "Romania", "Bosnia"]),
 ("Sparta Prague", "Czechia", ["Slovakia", "Slovenia", "Russia"]), ("Ferencváros", "Hungary", ["Romania", "Slovakia", "Bulgaria"]),
 ("Legia Warsaw", "Poland", ["Belarus", "Lithuania", "Russia"]), ("Rosenborg", "Norway", ["Denmark", "Finland", "Iceland"]),
 ("Malmö FF", "Sweden", ["Denmark", "Finland", "Iceland"]), ("Shakhtar Donetsk", "Ukraine", ["Russia", "Belarus", "Moldova"]),
 ("Al Ahly", "Egypt", ["Morocco", "Tunisia", "Saudi Arabia"]), ("Young Boys", "Switzerland", ["Germany", "Luxembourg", "Liechtenstein"]),
 ("Red Bull Salzburg", "Austria", ["Germany", "Slovenia", "Liechtenstein"]), ("LA Galaxy", "USA", ["Mexico", "Canada", "Costa Rica"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-8.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
