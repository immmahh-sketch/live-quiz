# Bank session 10 Oct 2026: 3 more general races -> bank/race-55.json. 20 rows each, target 10; wrong options are
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

race("which city is this cricket ground in?", "Cricket", "medium", ["cricket", "grounds", "cities"], [
 ("Lord's", "London", ["Canterbury", "Hove", "Taunton"]), ("The MCG", "Melbourne", ["Adelaide", "Hobart", "Canberra"]),
 ("The SCG", "Sydney", ["Adelaide", "Hobart", "Canberra"]), ("Eden Gardens", "Kolkata", ["Delhi", "Chennai", "Bengaluru"]),
 ("The Wankhede Stadium", "Mumbai", ["Delhi", "Chennai", "Bengaluru"]), ("The Gabba", "Brisbane", ["Adelaide", "Hobart", "Canberra"]),
 ("The WACA", "Perth", ["Adelaide", "Hobart", "Darwin"]), ("Headingley", "Leeds", ["Bradford", "Sheffield", "York"]),
 ("Old Trafford (the cricket one)", "Manchester", ["Liverpool", "Bolton", "Preston"]), ("Edgbaston", "Birmingham", ["Coventry", "Worcester", "Derby"]),
 ("Trent Bridge", "Nottingham", ["Derby", "Leicester", "Northampton"]), ("The Riverside", "Chester-le-Street", ["Darlington", "Sunderland", "Newcastle"]),
 ("Sophia Gardens", "Cardiff", ["Swansea", "Newport", "Bristol"]), ("The Basin Reserve", "Wellington", ["Auckland", "Christchurch", "Dunedin"]),
 ("The Kensington Oval", "Bridgetown", ["Port of Spain", "St John's", "Georgetown"]), ("Sabina Park", "Kingston", ["Port of Spain", "St John's", "Georgetown"]),
 ("Newlands", "Cape Town", ["Port Elizabeth", "Pretoria", "Centurion"]), ("The Wanderers", "Johannesburg", ["Pretoria", "Centurion", "Port Elizabeth"]),
 ("The Gaddafi Stadium", "Lahore", ["Karachi", "Islamabad", "Rawalpindi"]), ("Kingsmead", "Durban", ["Port Elizabeth", "Pretoria", "Bloemfontein"])])

race("which country is this ski resort in?", "Travel", "medium", ["skiing", "resorts", "countries"], [
 ("Chamonix", "France", ["Liechtenstein", "Poland", "Romania"]), ("Zermatt", "Switzerland", ["Liechtenstein", "Czechia", "Poland"]),
 ("St Anton", "Austria", ["Liechtenstein", "Czechia", "Poland"]), ("Cortina d'Ampezzo", "Italy", ["Liechtenstein", "Romania", "Greece"]),
 ("Aspen", "the USA", ["New Zealand", "Argentina", "Iceland"]), ("Whistler", "Canada", ["New Zealand", "Iceland", "Argentina"]),
 ("Niseko", "Japan", ["South Korea", "China", "Mongolia"]), ("Thredbo", "Australia", ["New Zealand", "Argentina", "Lebanon"]),
 ("Åre", "Sweden", ["Iceland", "Poland", "Czechia"]), ("Levi", "Finland", ["Iceland", "Estonia", "Poland"]),
 ("Hemsedal", "Norway", ["Iceland", "Estonia", "Czechia"]), ("Bansko", "Bulgaria", ["Romania", "Greece", "Turkey"]),
 ("Jasná", "Slovakia", ["Czechia", "Poland", "Romania"]), ("Kranjska Gora", "Slovenia", ["Croatia", "Czechia", "Romania"]),
 ("Baqueira-Beret", "Spain", ["Portugal", "Greece", "Morocco"]), ("Grandvalira", "Andorra", ["Liechtenstein", "Monaco", "San Marino"]),
 ("Valle Nevado", "Chile", ["Argentina", "Peru", "Bolivia"]), ("Gulmarg", "India", ["Pakistan", "Nepal", "China"]),
 ("Aviemore", "Scotland", ["Wales", "Ireland", "Iceland"]), ("Garmisch-Partenkirchen", "Germany", ["Liechtenstein", "Czechia", "Poland"])])

race("where is this zoo or aquarium?", "Animals", "medium", ["zoos", "aquariums", "cities"], [
 ("Taronga Zoo", "Sydney", ["Melbourne", "Brisbane", "Perth"]), ("Schönbrunn Zoo, the world's oldest", "Vienna", ["Salzburg", "Graz", "Budapest"]),
 ("Artis", "Amsterdam", ["Utrecht", "The Hague", "Antwerp"]), ("The Bronx Zoo", "New York", ["Boston", "Philadelphia", "Washington, DC"]),
 ("Monterey Bay Aquarium", "Monterey", ["San Diego", "Los Angeles", "Sacramento"]), ("Georgia Aquarium", "Atlanta", ["Savannah", "Charlotte", "Nashville"]),
 ("L'Oceanogràfic", "Valencia", ["Barcelona", "Málaga", "Alicante"]), ("Loro Parque", "Tenerife", ["Gran Canaria", "Lanzarote", "Majorca"]),
 ("Ueno Zoo", "Tokyo", ["Osaka", "Kyoto", "Yokohama"]), ("Henry Doorly Zoo", "Omaha", ["Kansas City", "Des Moines", "Denver"]),
 ("The Deep", "Hull", ["Grimsby", "Scarborough", "Whitby"]), ("The National Marine Aquarium", "Plymouth", ["Exeter", "Torquay", "Falmouth"]),
 ("Wilhelma", "Stuttgart", ["Frankfurt", "Nuremberg", "Cologne"]), ("Hellabrunn Zoo", "Munich", ["Frankfurt", "Nuremberg", "Cologne"]),
 ("Burgers' Zoo", "Arnhem", ["Utrecht", "The Hague", "Eindhoven"]), ("Blijdorp Zoo", "Rotterdam", ["Utrecht", "The Hague", "Eindhoven"]),
 ("The Ménagerie du Jardin des Plantes", "Paris", ["Lyon", "Marseille", "Lille"]), ("The Bioparco", "Rome", ["Naples", "Florence", "Milan"]),
 ("Shedd Aquarium", "Chicago", ["Detroit", "Milwaukee", "Cleveland"]), ("The S.E.A. Aquarium on Sentosa", "Singapore", ["Kuala Lumpur", "Bangkok", "Jakarta"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-55.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
