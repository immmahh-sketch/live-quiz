# Bank session 10 Oct 2026: 4 more general races -> bank/race-47.json. 20 rows each, target 10; wrong options are
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

race("which country calls itself this?", "World geography", "hard", ["countries", "native names"], [
 ("Deutschland", "Germany", ["Denmark", "the Netherlands", "Luxembourg"]), ("España", "Spain", ["Portugal", "Andorra", "Italy"]),
 ("Nippon", "Japan", ["South Korea", "Taiwan", "Vietnam"]), ("Suomi", "Finland", ["Iceland", "Denmark", "Latvia"]),
 ("Hellas", "Greece", ["Cyprus", "Malta", "Bulgaria"]), ("Hrvatska", "Croatia", ["Slovenia", "Serbia", "Slovakia"]),
 ("Magyarország", "Hungary", ["Mongolia", "Romania", "Slovakia"]), ("Sverige", "Sweden", ["Denmark", "Iceland", "Serbia"]),
 ("Norge", "Norway", ["Denmark", "Iceland", "the Netherlands"]), ("Polska", "Poland", ["Portugal", "Slovakia", "Czechia"]),
 ("Shqipëri", "Albania", ["Slovenia", "North Macedonia", "Montenegro"]), ("Eesti", "Estonia", ["Latvia", "Lithuania", "Iceland"]),
 ("Cymru", "Wales", ["Cornwall", "Scotland", "Cyprus"]), ("Éire", "Ireland", ["Scotland", "the Isle of Man", "Iceland"]),
 ("Österreich", "Austria", ["Australia", "Denmark", "Luxembourg"]), ("Helvetia (on its stamps and coins)", "Switzerland", ["Belgium", "Liechtenstein", "Iceland"]),
 ("Bharat", "India", ["Bhutan", "Bangladesh", "Nepal"]), ("Misr", "Egypt", ["Morocco", "Iraq", "Tunisia"]),
 ("Zhongguo", "China", ["Taiwan", "Mongolia", "Vietnam"]), ("Sakartvelo", "Georgia", ["Armenia", "Azerbaijan", "Kazakhstan"])])

race("which language says 'thank you' like this?", "Words and language", "hard", ["languages", "thank you"], [
 ("Arigatō", "Japanese", ["Thai", "Indonesian", "Tagalog"]), ("Xièxie", "Mandarin", ["Cantonese", "Thai", "Tagalog"]),
 ("Kamsahamnida", "Korean", ["Thai", "Mongolian", "Tagalog"]), ("Spasibo", "Russian", ["Ukrainian", "Czech", "Bulgarian"]),
 ("Dziękuję", "Polish", ["Czech", "Slovak", "Ukrainian"]), ("Tack", "Swedish", ["Icelandic", "Estonian", "German"]),
 ("Takk", "Norwegian", ["Estonian", "German", "Latvian"]), ("Tak", "Danish", ["Polish (where it means 'yes')", "Estonian", "Latvian"]),
 ("Kiitos", "Finnish", ["Estonian", "Latvian", "Lithuanian"]), ("Efcharistó", "Greek", ["Italian", "Romanian", "Maltese"]),
 ("Teşekkürler", "Turkish", ["Persian", "Kurdish", "Armenian"]), ("Shukran", "Arabic", ["Persian", "Amharic", "Somali"]),
 ("Toda", "Hebrew", ["Amharic", "Maltese", "Persian"]), ("Dhanyavaad", "Hindi", ["Tamil", "Urdu", "Sinhala"]),
 ("Asante", "Swahili", ["Zulu", "Yoruba", "Amharic"]), ("Diolch", "Welsh", ["Irish", "Scottish Gaelic", "Cornish"]),
 ("Köszönöm", "Hungarian", ["Romanian", "Czech", "Slovak"]), ("Dank je", "Dutch", ["German", "Afrikaans", "Luxembourgish"]),
 ("Mahalo", "Hawaiian", ["Maori", "Samoan", "Tongan"]), ("Cảm ơn", "Vietnamese", ["Thai", "Khmer", "Lao"])])

race("what's the biggest city in this country?", "World geography", "medium", ["cities", "countries"], [
 ("Australia", "Sydney", ["Melbourne", "Canberra", "Brisbane"]), ("Canada", "Toronto", ["Montreal", "Vancouver", "Ottawa"]),
 ("The USA", "New York City", ["Los Angeles", "Chicago", "Washington, DC"]), ("Turkey", "Istanbul", ["Ankara", "Izmir", "Bursa"]),
 ("Brazil", "São Paulo", ["Rio de Janeiro", "Brasília", "Salvador"]), ("Switzerland", "Zurich", ["Geneva", "Bern", "Basel"]),
 ("New Zealand", "Auckland", ["Wellington", "Christchurch", "Hamilton"]), ("Nigeria", "Lagos", ["Abuja", "Kano", "Ibadan"]),
 ("Pakistan", "Karachi", ["Lahore", "Islamabad", "Faisalabad"]), ("South Africa", "Johannesburg", ["Cape Town", "Durban", "Pretoria"]),
 ("Morocco", "Casablanca", ["Rabat", "Marrakesh", "Fez"]), ("Vietnam", "Ho Chi Minh City", ["Hanoi", "Da Nang", "Haiphong"]),
 ("Kazakhstan", "Almaty", ["Astana", "Shymkent", "Karaganda"]), ("Tanzania", "Dar es Salaam", ["Dodoma", "Zanzibar City", "Arusha"]),
 ("Bolivia", "Santa Cruz", ["La Paz", "Sucre", "El Alto"]), ("Scotland", "Glasgow", ["Edinburgh", "Aberdeen", "Dundee"]),
 ("Wales", "Cardiff", ["Swansea", "Newport", "Wrexham"]), ("Germany", "Berlin", ["Hamburg", "Munich", "Frankfurt"]),
 ("Italy", "Rome", ["Milan", "Naples", "Turin"]), ("Spain", "Madrid", ["Barcelona", "Valencia", "Seville"])])

race("which country is this canal in?", "World geography", "medium", ["canals", "countries"], [
 ("The Panama Canal", "Panama", ["Colombia", "Costa Rica", "Nicaragua"]), ("The Suez Canal", "Egypt", ["Israel", "Jordan", "Saudi Arabia"]),
 ("The Kiel Canal", "Germany", ["Denmark", "Poland", "Austria"]), ("The Corinth Canal", "Greece", ["Cyprus", "Turkey", "Malta"]),
 ("The Canal du Midi", "France", ["Monaco", "Switzerland", "Andorra"]), ("The Grand Canal from Beijing to Hangzhou", "China", ["Japan", "Vietnam", "Taiwan"]),
 ("The Rideau Canal", "Canada", ["Mexico", "Iceland", "Greenland"]), ("The Erie Canal", "the USA", ["Mexico", "Greenland", "Iceland"]),
 ("The Göta Canal", "Sweden", ["Denmark", "Iceland", "Estonia"]), ("The Caledonian Canal", "Scotland", ["Northern Ireland", "the Isle of Man", "Iceland"]),
 ("The Manchester Ship Canal", "England", ["Northern Ireland", "the Isle of Man", "Iceland"]), ("The Pontcysyllte Aqueduct", "Wales", ["Northern Ireland", "the Isle of Man", "Cornwall"]),
 ("Venice's Grand Canal", "Italy", ["Croatia", "Malta", "Slovenia"]), ("Amsterdam's canal ring", "the Netherlands", ["Denmark", "Luxembourg", "Austria"]),
 ("The White Sea–Baltic Canal", "Russia", ["Ukraine", "Belarus", "Estonia"]), ("The Telemark Canal", "Norway", ["Denmark", "Iceland", "Estonia"]),
 ("The Danube–Black Sea Canal", "Romania", ["Bulgaria", "Serbia", "Ukraine"]), ("The Royal Canal, Dublin", "Ireland", ["Northern Ireland", "the Isle of Man", "Iceland"]),
 ("Bruges's canals", "Belgium", ["Luxembourg", "Denmark", "Austria"]), ("The Canal de Castilla", "Spain", ["Portugal", "Andorra", "Malta"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-47.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
