# Bank session 10 Oct 2026: 4 more general races -> bank/race-33.json. 20 rows each, target 10; wrong options are
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

race("which city hosts this football derby?", "Football", "hard", ["derbies", "football", "cities"], [
 ("The Old Firm", "Glasgow", ["Dundee", "Aberdeen", "Paisley"]), ("Hearts v Hibs", "Edinburgh", ["Dundee", "Aberdeen", "Perth"]),
 ("The Derby della Madonnina", "Milan", ["Naples", "Florence", "Bologna"]), ("The Derby della Capitale", "Rome", ["Naples", "Florence", "Verona"]),
 ("The Superclásico (Boca v River)", "Buenos Aires", ["Montevideo", "Rosario", "Córdoba"]), ("The Intercontinental Derby", "Istanbul", ["Ankara", "Izmir", "Bursa"]),
 ("The Eternal Derby (Red Star v Partizan)", "Belgrade", ["Zagreb", "Sofia", "Split"]), ("The Steel City derby", "Sheffield", ["Leeds", "Bradford", "Derby"]),
 ("The Second City derby", "Birmingham", ["Coventry", "Wolverhampton", "Leicester"]), ("The Derby della Mole", "Turin", ["Naples", "Verona", "Bologna"]),
 ("The Derby della Lanterna", "Genoa", ["Naples", "Florence", "Verona"]), ("Benfica v Sporting", "Lisbon", ["Porto", "Braga", "Coimbra"]),
 ("The Gran Derbi (Betis v Sevilla)", "Seville", ["Madrid", "Valencia", "Barcelona"]), ("Al Ahly v Zamalek", "Cairo", ["Alexandria", "Casablanca", "Tunis"]),
 ("Rapid v Austria", "Vienna", ["Graz", "Salzburg", "Linz"]), ("HSV v St Pauli", "Hamburg", ["Berlin", "Munich", "Bremen"]),
 ("Dinamo v Steaua (FCSB)", "Bucharest", ["Cluj", "Budapest", "Sofia"]), ("The Fla-Flu (Flamengo v Fluminense)", "Rio de Janeiro", ["Belo Horizonte", "Porto Alegre", "Brasília"]),
 ("Corinthians v Palmeiras", "São Paulo", ["Santos", "Belo Horizonte", "Porto Alegre"]), ("The Potteries derby", "Stoke-on-Trent", ["Crewe", "Derby", "Stafford"])])

race("what's the biggest city in this US state?", "World geography", "hard", ["USA", "cities", "states"], [
 ("Florida", "Jacksonville", ["Miami", "Orlando", "Tampa"]), ("California", "Los Angeles", ["San Diego", "San Francisco", "San Jose"]),
 ("Texas", "Houston", ["Dallas", "San Antonio", "Austin"]), ("Illinois", "Chicago", ["Springfield", "Peoria", "Rockford"]),
 ("Pennsylvania", "Philadelphia", ["Pittsburgh", "Harrisburg", "Allentown"]), ("Ohio", "Columbus", ["Cleveland", "Cincinnati", "Toledo"]),
 ("Georgia", "Atlanta", ["Savannah", "Augusta", "Macon"]), ("Michigan", "Detroit", ["Grand Rapids", "Lansing", "Ann Arbor"]),
 ("Washington", "Seattle", ["Spokane", "Tacoma", "Olympia"]), ("Arizona", "Phoenix", ["Tucson", "Mesa", "Scottsdale"]),
 ("Tennessee", "Nashville", ["Memphis", "Knoxville", "Chattanooga"]), ("Missouri", "Kansas City", ["St Louis", "Springfield", "Jefferson City"]),
 ("Kentucky", "Louisville", ["Lexington", "Frankfort", "Bowling Green"]), ("Louisiana", "New Orleans", ["Baton Rouge", "Shreveport", "Lafayette"]),
 ("Maryland", "Baltimore", ["Annapolis", "Frederick", "Rockville"]), ("Wisconsin", "Milwaukee", ["Madison", "Green Bay", "Kenosha"]),
 ("Nevada", "Las Vegas", ["Reno", "Carson City", "Henderson"]), ("Oregon", "Portland", ["Salem", "Eugene", "Bend"]),
 ("Alaska", "Anchorage", ["Juneau", "Fairbanks", "Sitka"]), ("North Carolina", "Charlotte", ["Raleigh", "Greensboro", "Durham"])])

race("which country did this leader rule?", "History", "medium", ["leaders", "20th century", "countries"], [
 ("Fidel Castro", "Cuba", ["Nicaragua", "Venezuela", "Panama"]), ("Mao Zedong", "China", ["Taiwan", "Mongolia", "Laos"]),
 ("Josip Broz Tito", "Yugoslavia", ["Albania", "Bulgaria", "Hungary"]), ("Francisco Franco", "Spain", ["Greece", "Hungary", "Mexico"]),
 ("António Salazar", "Portugal", ["Greece", "Brazil", "Mexico"]), ("Augusto Pinochet", "Chile", ["Paraguay", "Peru", "Bolivia"]),
 ("Idi Amin", "Uganda", ["Kenya", "Tanzania", "Sudan"]), ("Muammar Gaddafi", "Libya", ["Algeria", "Tunisia", "Sudan"]),
 ("Saddam Hussein", "Iraq", ["Syria", "Iran", "Jordan"]), ("Pol Pot", "Cambodia", ["Laos", "Thailand", "Myanmar"]),
 ("Kim Il-sung", "North Korea", ["South Korea", "Mongolia", "Laos"]), ("Robert Mugabe", "Zimbabwe", ["Zambia", "Mozambique", "Kenya"]),
 ("Nicolae Ceaușescu", "Romania", ["Bulgaria", "Hungary", "Albania"]), ("Benito Mussolini", "Italy", ["Greece", "Albania", "Hungary"]),
 ("Juan Perón", "Argentina", ["Paraguay", "Bolivia", "Uruguay"]), ("Suharto", "Indonesia", ["Malaysia", "Myanmar", "Thailand"]),
 ("Ferdinand Marcos", "the Philippines", ["Malaysia", "Thailand", "Taiwan"]), ("Gamal Abdel Nasser", "Egypt", ["Sudan", "Jordan", "Algeria"]),
 ("Kemal Atatürk", "Turkey", ["Greece", "Iran", "Syria"]), ("Ho Chi Minh", "Vietnam", ["Laos", "Thailand", "Myanmar"])])

race("which country is this tower or skyscraper in?", "World geography", "medium", ["towers", "skyscrapers", "landmarks"], [
 ("The Burj Khalifa", "the UAE", ["Qatar", "Bahrain", "Oman"]), ("The Petronas Towers", "Malaysia", ["Singapore", "Indonesia", "Thailand"]),
 ("The CN Tower", "Canada", ["Austria", "Ireland", "Denmark"]), ("Taipei 101", "Taiwan", ["Hong Kong", "Singapore", "Vietnam"]),
 ("The Shanghai Tower", "China", ["Hong Kong", "Singapore", "Vietnam"]), ("The Skytree", "Japan", ["Vietnam", "Singapore", "Thailand"]),
 ("The Lotte World Tower", "South Korea", ["Vietnam", "Thailand", "Singapore"]), ("The Space Needle", "the USA", ["Ireland", "Denmark", "Austria"]),
 ("Auckland's Sky Tower", "New Zealand", ["Fiji", "Singapore", "Ireland"]), ("The Eureka Tower", "Australia", ["Fiji", "Singapore", "Ireland"]),
 ("The Kingdom Centre", "Saudi Arabia", ["Qatar", "Bahrain", "Oman"]), ("The Ostankino Tower", "Russia", ["Ukraine", "Belarus", "Poland"]),
 ("The Galata Tower", "Turkey", ["Greece", "Cyprus", "Bulgaria"]), ("The Torre Latinoamericana", "Mexico", ["Spain", "Argentina", "Colombia"]),
 ("The Euromast", "the Netherlands", ["Denmark", "Ireland", "Austria"]), ("The Fernsehturm", "Germany", ["Austria", "Switzerland", "Denmark"]),
 ("The Atomium", "Belgium", ["Luxembourg", "Switzerland", "Denmark"]), ("The Milad Tower", "Iran", ["Iraq", "Pakistan", "Oman"]),
 ("The Gran Torre Santiago", "Chile", ["Argentina", "Peru", "Colombia"]), ("The Eiffel Tower", "France", ["Luxembourg", "Switzerland", "Austria"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-33.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
