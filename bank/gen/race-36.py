# Bank session 10 Oct 2026: 4 more general races -> bank/race-36.json. 20 rows each, target 10; wrong options are
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

race("which sport is this venue famous for?", "Sport", "medium", ["venues", "sport"], [
 ("The Ryōgoku Kokugikan, Tokyo", "Sumo wrestling", ["Judo", "Karate", "Kendo"]), ("Lambeau Field", "American football", ["Ice hockey", "Basketball", "Rugby league"]),
 ("Yankee Stadium", "Baseball", ["Ice hockey", "Basketball", "Lacrosse"]), ("Holmenkollen", "Ski jumping", ["Bobsleigh", "Luge", "Speed skating"]),
 ("Kitzbühel's Hahnenkamm", "Alpine skiing", ["Bobsleigh", "Luge", "Speed skating"]), ("Hickstead", "Show jumping", ["Greyhound racing", "Speedway", "Croquet"]),
 ("Badminton House", "Eventing", ["Badminton", "Croquet", "Bowls"]), ("Cowdray Park", "Polo", ["Croquet", "Bowls", "Lacrosse"]),
 ("Lee Valley VeloPark", "Track cycling", ["Speedway", "Athletics", "Swimming"]), ("Alexandra Palace", "Darts", ["Pool", "Table tennis", "Bowls"]),
 ("The Crucible", "Snooker", ["Pool", "Table tennis", "Squash"]), ("Augusta National", "Golf", ["Croquet", "Bowls", "Lacrosse"]),
 ("Lord's", "Cricket", ["Croquet", "Bowls", "Rugby league"]), ("Wimbledon", "Tennis", ["Squash", "Badminton", "Table tennis"]),
 ("Twickenham", "Rugby union", ["Hockey", "Lacrosse", "Netball"]), ("Ascot", "Horse racing", ["Greyhound racing", "Speedway", "Croquet"]),
 ("Henley", "Rowing", ["Sailing", "Swimming", "Water polo"]), ("Silverstone", "Motor racing", ["Speedway", "Greyhound racing", "Athletics"]),
 ("Lee Valley White Water Centre", "Canoe slalom", ["Sailing", "Swimming", "Water polo"]), ("Hampden Park", "Football", ["Rugby league", "Hockey", "Lacrosse"])])

race("which country does this cartoon or comic character come from?", "Film and TV", "medium", ["cartoons", "comics", "countries"], [
 ("Tintin", "Belgium", ["Luxembourg", "Austria", "Canada"]), ("Asterix", "France", ["Luxembourg", "Spain", "Canada"]),
 ("Astro Boy", "Japan", ["China", "Taiwan", "Vietnam"]), ("The Moomins", "Finland", ["Norway", "Iceland", "Estonia"]),
 ("Pippi Longstocking", "Sweden", ["Norway", "Iceland", "Estonia"]), ("Mafalda", "Argentina", ["Uruguay", "Spain", "Mexico"]),
 ("Peppa Pig", "the United Kingdom", ["Ireland", "Canada", "New Zealand"]), ("Pingu", "Switzerland", ["Austria", "Norway", "Canada"]),
 ("Maya the Bee", "Germany", ["Austria", "Hungary", "Slovenia"]), ("Masha and the Bear", "Russia", ["Ukraine", "Belarus", "Slovakia"]),
 ("Miffy", "the Netherlands", ["Luxembourg", "Norway", "Austria"]), ("Bluey", "Australia", ["New Zealand", "Canada", "Ireland"]),
 ("Rasmus Klump (Barnaby Bear)", "Denmark", ["Norway", "Iceland", "Estonia"]), ("Popeye", "the USA", ["Canada", "Ireland", "Mexico"]),
 ("Pororo the Little Penguin", "South Korea", ["China", "Taiwan", "Vietnam"]), ("Chhota Bheem", "India", ["Pakistan", "Sri Lanka", "Bangladesh"]),
 ("Bolek and Lolek", "Poland", ["Ukraine", "Slovakia", "Hungary"]), ("Krtek, the Little Mole", "Czechia", ["Slovakia", "Slovenia", "Hungary"]),
 ("La Linea", "Italy", ["Spain", "Greece", "Croatia"]), ("Condorito", "Chile", ["Peru", "Uruguay", "Colombia"])])

race("which country does this sauce or condiment come from?", "Food and drink", "hard", ["sauces", "condiments", "countries"], [
 ("Tabasco", "the USA", ["Canada", "Cuba", "Trinidad and Tobago"]), ("Sriracha", "Thailand", ["Vietnam", "Malaysia", "Cambodia"]),
 ("Harissa", "Tunisia", ["Egypt", "Lebanon", "Turkey"]), ("Pesto", "Italy", ["Malta", "Portugal", "Croatia"]),
 ("Chimichurri", "Argentina", ["Brazil", "Peru", "Colombia"]), ("Gochujang", "South Korea", ["Vietnam", "Taiwan", "Malaysia"]),
 ("Wasabi", "Japan", ["Taiwan", "Vietnam", "Malaysia"]), ("Tzatziki", "Greece", ["Lebanon", "Malta", "Portugal"]),
 ("HP Sauce", "the United Kingdom", ["Ireland", "Canada", "New Zealand"]), ("Vegemite", "Australia", ["New Zealand", "Canada", "Ireland"]),
 ("Mole", "Mexico", ["Peru", "Colombia", "Cuba"]), ("Romesco", "Spain", ["Portugal", "Malta", "Croatia"]),
 ("Béarnaise", "France", ["Belgium", "Switzerland", "Germany"]), ("Tkemali", "Georgia", ["Armenia", "Azerbaijan", "Turkey"]),
 ("Mango chutney", "India", ["Pakistan", "Sri Lanka", "Bangladesh"]), ("Hoisin", "China", ["Taiwan", "Malaysia", "Cambodia"]),
 ("Jerk seasoning", "Jamaica", ["Trinidad and Tobago", "Barbados", "Cuba"]), ("Zhug", "Yemen", ["Oman", "Saudi Arabia", "Ethiopia"]),
 ("Banana ketchup", "the Philippines", ["Indonesia", "Malaysia", "Vietnam"]), ("Pebre", "Chile", ["Peru", "Colombia", "Brazil"])])

race("what does this unit measure?", "Science and nature", "medium", ["units", "physics", "measurement"], [
 ("The newton", "Force", ["Momentum", "Acceleration", "Density"]), ("The watt", "Power", ["Momentum", "Density", "Torque"]),
 ("The volt", "Voltage", ["Wavelength", "Viscosity", "Torque"]), ("The ampere", "Electric current", ["Wavelength", "Density", "Humidity"]),
 ("The ohm", "Resistance", ["Wavelength", "Humidity", "Acceleration"]), ("The kelvin", "Temperature", ["Humidity", "Altitude", "Density"]),
 ("The joule", "Energy", ["Momentum", "Torque", "Acceleration"]), ("The pascal", "Pressure", ["Density", "Viscosity", "Humidity"]),
 ("The hertz", "Frequency", ["Wavelength", "Acceleration", "Momentum"]), ("The tesla", "Magnetic field strength", ["Momentum", "Density", "Wavelength"]),
 ("The coulomb", "Electric charge", ["Viscosity", "Humidity", "Density"]), ("The farad", "Capacitance", ["Viscosity", "Humidity", "Torque"]),
 ("The becquerel", "Radioactivity", ["Humidity", "Viscosity", "Acceleration"]), ("The lumen", "Light output", ["Wavelength", "Humidity", "Density"]),
 ("The decibel", "Loudness", ["Wavelength", "Humidity", "Viscosity"]), ("The mole", "Amount of substance", ["Density", "Volume", "Humidity"]),
 ("The knot", "Speed", ["Altitude", "Depth", "Acceleration"]), ("The light year", "Distance", ["Time", "Brightness", "Mass"]),
 ("The hectare", "Area", ["Volume", "Depth", "Altitude"]), ("The carat", "Weight of gemstones", ["Clarity", "Hardness", "Value"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-36.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
