# Bank session 10 Oct 2026: 4 more general races -> bank/race-43.json. 20 rows each, target 10; wrong options are
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

race("in which city did this Olympic moment happen?", "Sport", "hard", ["Olympics", "host cities"], [
 ("Usain Bolt wins his first Olympic golds", "Beijing", ["Munich", "Melbourne", "Amsterdam"]),
 ("Jesse Owens wins four golds", "Berlin", ["Amsterdam", "Antwerp", "St Louis"]),
 ("Team GB's 'Super Saturday'", "London", ["Munich", "Melbourne", "Antwerp"]),
 ("Bob Beamon's astonishing long jump", "Mexico City", ["Munich", "Melbourne", "St Louis"]),
 ("Nadia Comăneci scores the first perfect 10", "Montreal", ["Munich", "Melbourne", "Amsterdam"]),
 ("Cathy Freeman wins the 400 m at her home Games", "Sydney", ["Melbourne", "Munich", "Antwerp"]),
 ("Torvill and Dean skate their Boléro", "Sarajevo", ["Lake Placid", "Innsbruck", "Grenoble"]),
 ("Eddie 'the Eagle' Edwards ski-jumps for Britain", "Calgary", ["Lake Placid", "Albertville", "Lillehammer"]),
 ("The USA's basketball 'Dream Team' plays", "Barcelona", ["Munich", "Melbourne", "Amsterdam"]),
 ("Michael Johnson wins the 200 m and 400 m in gold shoes", "Atlanta", ["St Louis", "Munich", "Melbourne"]),
 ("Kelly Holmes wins the 800 m and 1,500 m double", "Athens", ["Munich", "Melbourne", "Antwerp"]),
 ("Simone Biles pulls out with 'the twisties'", "Tokyo", ["Munich", "Melbourne", "Amsterdam"]),
 ("Abebe Bikila wins the marathon barefoot", "Rome", ["Melbourne", "Munich", "Amsterdam"]),
 ("Ben Johnson is stripped of his 100 m gold", "Seoul", ["Munich", "Melbourne", "Amsterdam"]),
 ("Carl Lewis wins four golds to match Jesse Owens", "Los Angeles", ["St Louis", "Munich", "Melbourne"]),
 ("Eric Liddell wins the 400 m, as told in Chariots of Fire", "Paris", ["Amsterdam", "Antwerp", "St Louis"]),
 ("Jim Thorpe wins both the pentathlon and decathlon", "Stockholm", ["Antwerp", "Amsterdam", "St Louis"]),
 ("Emil Zátopek wins the 5,000 m, 10,000 m and marathon", "Helsinki", ["Melbourne", "Antwerp", "Amsterdam"]),
 ("Usain Bolt wins his third Olympic 100 m in a row", "Rio de Janeiro", ["Munich", "Melbourne", "Amsterdam"]),
 ("Seb Coe beats Steve Ovett to win the 1,500 m", "Moscow", ["Munich", "Melbourne", "Amsterdam"])])

race("which company owns this brand?", "Business", "hard", ["brands", "companies"], [
 ("KitKat (outside the USA)", "Nestlé", ["Ferrero", "Lindt", "Kraft Heinz"]), ("Cadbury", "Mondelēz", ["Ferrero", "Hershey", "Lindt"]),
 ("Walkers crisps", "PepsiCo", ["Kellogg's", "Kraft Heinz", "Ferrero"]), ("Maltesers", "Mars", ["Ferrero", "Hershey", "Lindt"]),
 ("Costa Coffee", "Coca-Cola", ["Starbucks", "Whitbread", "Kraft Heinz"]), ("Guinness", "Diageo", ["Heineken", "AB InBev", "Carlsberg"]),
 ("Gillette", "Procter & Gamble", ["Kimberly-Clark", "Colgate-Palmolive", "Johnson & Johnson"]), ("YouTube", "Alphabet (Google)", ["Apple", "Netflix", "Oracle"]),
 ("Instagram", "Meta", ["Apple", "Snap", "Oracle"]), ("LinkedIn", "Microsoft", ["Apple", "Oracle", "Salesforce"]),
 ("Audible", "Amazon", ["Apple", "Spotify", "Netflix"]), ("Moët & Chandon", "LVMH", ["Kering", "Richemont", "Pernod Ricard"]),
 ("Zara", "Inditex", ["H&M", "Fast Retailing", "Arcadia"]), ("Rolls-Royce cars", "BMW", ["Volkswagen", "Mercedes-Benz Group", "Toyota"]),
 ("Jaguar Land Rover", "Tata", ["Ford", "Stellantis", "Hyundai"]), ("Volvo Cars", "Geely", ["Ford", "Stellantis", "Hyundai"]),
 ("Primark", "Associated British Foods", ["Arcadia", "Next", "Tesco"]), ("Dettol", "Reckitt", ["Johnson & Johnson", "Colgate-Palmolive", "Kimberly-Clark"]),
 ("Marmite", "Unilever", ["Kraft Heinz", "Kellogg's", "General Mills"]), ("Pixar", "Disney", ["Warner Bros.", "Universal", "Paramount"])])

race("what does this instrument measure?", "Science and nature", "medium", ["instruments", "measurement"], [
 ("Barometer", "Air pressure", ["Wind direction", "Sunshine", "Snowfall"]), ("Thermometer", "Temperature", ["Sunshine", "Snowfall", "Salinity"]),
 ("Anemometer", "Wind speed", ["Wind direction", "Sunshine", "Snowfall"]), ("Hygrometer", "Humidity", ["Salinity", "Sunshine", "Snowfall"]),
 ("Seismograph", "Earthquakes", ["Tide height", "Magnetism", "Wind direction"]), ("Altimeter", "Altitude", ["Depth", "Tide height", "Magnetism"]),
 ("Odometer", "Distance travelled", ["Fuel level", "Tyre pressure", "Engine temperature"]), ("Speedometer", "Speed", ["Fuel level", "Tyre pressure", "Engine temperature"]),
 ("Ammeter", "Electric current", ["Magnetism", "Brightness", "Torque"]), ("Voltmeter", "Voltage", ["Magnetism", "Brightness", "Torque"]),
 ("Pedometer", "Steps", ["Pulse", "Calories eaten", "Sleep"]), ("Sphygmomanometer", "Blood pressure", ["Pulse", "Hearing", "Eyesight"]),
 ("Hydrometer", "Density of a liquid", ["Viscosity", "Hardness", "Brightness"]), ("Rain gauge", "Rainfall", ["Sunshine", "Wind direction", "Tide height"]),
 ("Geiger counter", "Radiation", ["Magnetism", "Brightness", "Salinity"]), ("Spirometer", "Lung capacity", ["Pulse", "Hearing", "Eyesight"]),
 ("Tachometer", "Engine revs", ["Fuel level", "Tyre pressure", "Engine temperature"]), ("Chronometer", "Time", ["Wind direction", "Magnetism", "Tide height"]),
 ("Breathalyser", "Alcohol in the breath", ["Pulse", "Blood sugar", "Hearing"]), ("pH meter", "Acidity", ["Salinity", "Viscosity", "Hardness"])])

race("which country did this TV show first come from?", "Film and TV", "hard", ["TV", "world TV", "countries"], [
 ("Yo soy Betty, la fea (the original Ugly Betty)", "Colombia", ["Venezuela", "Argentina", "Chile"]), ("Prisoners of War (the original Homeland)", "Israel", ["the USA", "Lebanon", "Greece"]),
 ("The Killing (Forbrydelsen)", "Denmark", ["Finland", "Poland", "Austria"]), ("Money Heist", "Spain", ["Portugal", "Argentina", "Chile"]),
 ("Dark", "Germany", ["Austria", "Switzerland", "Poland"]), ("Lupin", "France", ["Switzerland", "Canada", "Luxembourg"]),
 ("Skam", "Norway", ["Finland", "Poland", "Austria"]), ("Gomorrah", "Italy", ["Greece", "Portugal", "Malta"]),
 ("Sacred Games", "India", ["Pakistan", "Bangladesh", "Sri Lanka"]), ("3%", "Brazil", ["Argentina", "Portugal", "Chile"]),
 ("Wallander (the original)", "Sweden", ["Finland", "Poland", "Austria"]), ("The Masked Singer", "South Korea", ["China", "Taiwan", "Thailand"]),
 ("Dragons' Den (as Money Tigers)", "Japan", ["China", "Taiwan", "the USA"]), ("Big Brother", "the Netherlands", ["the USA", "Austria", "Switzerland"]),
 ("Who Wants to Be a Millionaire?", "the United Kingdom", ["the USA", "Ireland", "Canada"]), ("Professor T", "Belgium", ["Luxembourg", "Switzerland", "Austria"]),
 ("Magnificent Century", "Turkey", ["Greece", "Egypt", "Iran"]), ("The House of Flowers", "Mexico", ["Argentina", "Chile", "Venezuela"]),
 ("Trapped", "Iceland", ["Finland", "Greenland", "the Faroe Islands"]), ("Neighbours", "Australia", ["New Zealand", "the USA", "Canada"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-43.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
