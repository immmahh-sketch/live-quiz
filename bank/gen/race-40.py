# Bank session 10 Oct 2026: 4 more general races -> bank/race-40.json. 20 rows each, target 10; wrong options are
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

race("which country is this famous road in?", "Travel", "medium", ["roads", "road trips", "countries"], [
 ("Route 66", "the USA", ["Mexico", "England", "Spain"]), ("The Great Ocean Road", "Australia", ["Fiji", "Namibia", "England"]),
 ("The Amalfi Coast road", "Italy", ["Greece", "Spain", "Portugal"]), ("The Ring Road (Route 1)", "Iceland", ["Greenland", "Denmark", "Finland"]),
 ("The Transfăgărășan", "Romania", ["Bulgaria", "Hungary", "Serbia"]), ("Trollstigen", "Norway", ["Sweden", "Finland", "Denmark"]),
 ("The Grossglockner High Alpine Road", "Austria", ["Germany", "Slovenia", "Hungary"]), ("The North Coast 500", "Scotland", ["Wales", "England", "Northern Ireland"]),
 ("The Cabot Trail", "Canada", ["Mexico", "Greenland", "England"]), ("The Garden Route", "South Africa", ["Namibia", "Botswana", "Mozambique"]),
 ("The Milford Road", "New Zealand", ["Fiji", "England", "Wales"]), ("The Yungas 'Death Road'", "Bolivia", ["Peru", "Ecuador", "Paraguay"]),
 ("The Col du Tourmalet", "France", ["Spain", "Belgium", "Portugal"]), ("The Furka Pass", "Switzerland", ["Germany", "Slovenia", "Liechtenstein"]),
 ("The Kolyma Highway ('Road of Bones')", "Russia", ["Kazakhstan", "Mongolia", "Ukraine"]), ("Ruta 40", "Argentina", ["Uruguay", "Paraguay", "Peru"]),
 ("The Carretera Austral", "Chile", ["Peru", "Ecuador", "Uruguay"]), ("The Hải Vân Pass", "Vietnam", ["Laos", "Cambodia", "Thailand"]),
 ("The Wild Atlantic Way", "Ireland", ["Wales", "England", "Portugal"]), ("The Leh–Manali Highway", "India", ["Nepal", "Pakistan", "Bhutan"])])

race("which show is this a spin-off of?", "Film and TV", "medium", ["TV", "spin-offs"], [
 ("Frasier", "Cheers", ["Taxi", "Seinfeld", "M*A*S*H"]), ("Joey", "Friends", ["Seinfeld", "Scrubs", "Two and a Half Men"]),
 ("Better Call Saul", "Breaking Bad", ["The Sopranos", "The Wire", "Mad Men"]), ("Torchwood", "Doctor Who", ["Red Dwarf", "Sherlock", "Merlin"]),
 ("Angel", "Buffy the Vampire Slayer", ["Charmed", "Smallville", "True Blood"]), ("Young Sheldon", "The Big Bang Theory", ["Two and a Half Men", "Scrubs", "Seinfeld"]),
 ("Private Practice", "Grey's Anatomy", ["ER", "Scrubs", "House"]), ("Lewis", "Inspector Morse", ["A Touch of Frost", "Midsomer Murders", "Taggart"]),
 ("Mork & Mindy", "Happy Days", ["Taxi", "The Brady Bunch", "M*A*S*H"]), ("Rhoda", "The Mary Tyler Moore Show", ["The Bob Newhart Show", "Taxi", "The Brady Bunch"]),
 ("The Jeffersons", "All in the Family", ["The Brady Bunch", "Taxi", "The Partridge Family"]), ("House of the Dragon", "Game of Thrones", ["Vikings", "Lost", "True Blood"]),
 ("Fear the Walking Dead", "The Walking Dead", ["Lost", "Vikings", "True Blood"]), ("The Cleveland Show", "Family Guy", ["American Dad!", "King of the Hill", "Futurama"]),
 ("Daria", "Beavis and Butt-Head", ["The Ren & Stimpy Show", "South Park", "King of the Hill"]), ("Rock & Chips", "Only Fools and Horses", ["Last of the Summer Wine", "Porridge", "Open All Hours"]),
 ("Holby City", "Casualty", ["EastEnders", "The Bill", "ER"]), ("NCIS", "JAG", ["CSI", "Magnum, P.I.", "The A-Team"]),
 ("Max and Paddy's Road to Nowhere", "Phoenix Nights", ["Peter Kay's Car Share", "The Royle Family", "Early Doors"]), ("The Simpsons", "The Tracey Ullman Show", ["Saturday Night Live", "The Carol Burnett Show", "The Late Show"])])

race("which city used to be called this?", "World geography", "hard", ["cities", "old names"], [
 ("Constantinople", "Istanbul", ["Ankara", "Athens", "Thessaloniki"]), ("Bombay", "Mumbai", ["Delhi", "Bangalore", "Hyderabad"]),
 ("Peking", "Beijing", ["Shanghai", "Nanjing", "Hong Kong"]), ("Saigon", "Ho Chi Minh City", ["Hanoi", "Da Nang", "Phnom Penh"]),
 ("Leningrad", "St Petersburg", ["Moscow", "Novgorod", "Riga"]), ("New Amsterdam", "New York", ["Boston", "Philadelphia", "Baltimore"]),
 ("Edo", "Tokyo", ["Osaka", "Kyoto", "Nagasaki"]), ("Batavia", "Jakarta", ["Surabaya", "Bandung", "Singapore"]),
 ("Madras", "Chennai", ["Bangalore", "Hyderabad", "Colombo"]), ("Calcutta", "Kolkata", ["Delhi", "Dhaka", "Hyderabad"]),
 ("Rangoon", "Yangon", ["Mandalay", "Dhaka", "Bangkok"]), ("Salisbury, Rhodesia", "Harare", ["Bulawayo", "Lusaka", "Gaborone"]),
 ("Léopoldville", "Kinshasa", ["Lubumbashi", "Brazzaville", "Kisangani"]), ("Christiania", "Oslo", ["Bergen", "Stockholm", "Copenhagen"]),
 ("Danzig", "Gdańsk", ["Warsaw", "Kraków", "Szczecin"]), ("Königsberg", "Kaliningrad", ["Riga", "Vilnius", "Minsk"]),
 ("Stalingrad", "Volgograd", ["Samara", "Rostov-on-Don", "Moscow"]), ("Lutetia", "Paris", ["Lyon", "Marseille", "Brussels"]),
 ("Pressburg", "Bratislava", ["Vienna", "Budapest", "Prague"]), ("Smyrna", "Izmir", ["Antalya", "Ankara", "Athens"])])

race("which country's football team has this nickname?", "Football", "medium", ["football", "national teams", "nicknames"], [
 ("The Three Lions", "England", ["Scotland", "Wales", "Ireland"]), ("The Socceroos", "Australia", ["New Zealand", "the USA", "Canada"]),
 ("The Super Eagles", "Nigeria", ["Ivory Coast", "Mali", "Zambia"]), ("The Black Stars", "Ghana", ["Ivory Coast", "Mali", "Kenya"]),
 ("The Indomitable Lions", "Cameroon", ["Ivory Coast", "Mali", "Tunisia"]), ("The Azzurri", "Italy", ["Uruguay", "Portugal", "Switzerland"]),
 ("Les Bleus", "France", ["Switzerland", "Portugal", "Croatia"]), ("Oranje", "the Netherlands", ["Denmark", "Sweden", "Austria"]),
 ("The Seleção", "Brazil", ["Colombia", "Peru", "Ecuador"]), ("La Albiceleste", "Argentina", ["Uruguay", "Chile", "Paraguay"]),
 ("El Tri", "Mexico", ["Costa Rica", "Honduras", "the USA"]), ("The Red Devils", "Belgium", ["Switzerland", "Austria", "Denmark"]),
 ("The Taeguk Warriors", "South Korea", ["North Korea", "China", "Iran"]), ("Samurai Blue", "Japan", ["China", "Iran", "Saudi Arabia"]),
 ("Bafana Bafana", "South Africa", ["Zambia", "Kenya", "Mali"]), ("The Pharaohs", "Egypt", ["Tunisia", "Algeria", "Saudi Arabia"]),
 ("The Atlas Lions", "Morocco", ["Tunisia", "Algeria", "Mali"]), ("Die Mannschaft", "Germany", ["Austria", "Switzerland", "Denmark"]),
 ("The Reggae Boyz", "Jamaica", ["Trinidad and Tobago", "Haiti", "Honduras"]), ("The Teranga Lions", "Senegal", ["Mali", "Ivory Coast", "Zambia"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-40.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
