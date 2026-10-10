# Bank session 10 Oct 2026: 20 more Only One prompts appended to bank/unique-prompts.json. Each is a closed list with
# every correct answer (other accepted forms after a slash), so a fair answer is never knocked out.
import json, os
NEW = [
 ("Name a country that shares a land border with Turkey or Greece", ["Greece", "Turkey/Türkiye", "Bulgaria", "Georgia", "Armenia", "Azerbaijan", "Iran", "Iraq", "Syria", "Albania", "North Macedonia/Macedonia"]),
 ("Name a country that shares a land border with South Africa or Mozambique", ["Namibia", "Botswana", "Zimbabwe", "Mozambique", "Eswatini/Swaziland", "Lesotho", "South Africa", "Tanzania", "Malawi", "Zambia"]),
 ("Name a country that shares a land border with Nigeria or Ghana", ["Benin", "Niger", "Chad", "Cameroon", "Ivory Coast/Côte d'Ivoire", "Burkina Faso", "Togo"]),
 ("Name a country that shares a land border with Afghanistan or Pakistan", ["Pakistan", "Afghanistan", "Iran", "Turkmenistan", "Uzbekistan", "Tajikistan", "China", "India"]),
 ("Name a country that shares a land border with Czechia or Slovakia", ["Germany", "Poland", "Austria", "Slovakia", "Czechia/Czech Republic", "Hungary", "Ukraine"]),
 ("Name a member of the Kinks or the Hollies (classic line-ups)", ["Ray Davies", "Dave Davies", "Pete Quaife", "Mick Avory", "Allan Clarke", "Graham Nash", "Tony Hicks", "Bobby Elliott", "Eric Haydock"]),
 ("Name an English county that borders Greater London", ["Hertfordshire", "Essex", "Kent", "Surrey", "Buckinghamshire", "Berkshire"]),
 ("Name a county that borders one of Yorkshire's counties", ["County Durham/Durham", "Cumbria", "Lancashire", "Greater Manchester", "Cheshire", "Derbyshire", "Nottinghamshire", "Lincolnshire"]),
 ("Name a sea that washes the coast of Italy or Turkey", ["Mediterranean", "Black Sea", "Aegean", "Sea of Marmara/Marmara", "Adriatic", "Ionian", "Tyrrhenian", "Ligurian"]),
 ("Name a US state that borders Texas or Colorado", ["New Mexico", "Oklahoma", "Arkansas", "Louisiana", "Wyoming", "Nebraska", "Kansas", "Arizona", "Utah", "Texas", "Colorado"]),
 ("Name a UK city that has hosted the Eurovision Song Contest", ["London", "Brighton", "Edinburgh", "Harrogate", "Birmingham", "Liverpool"]),
 ("Name one of London's eight Royal Parks", ["Hyde Park", "Kensington Gardens", "Green Park", "St James's Park", "Regent's Park", "Greenwich Park", "Richmond Park", "Bushy Park"]),
 ("Name a London club playing in the Premier League in the 2025–26 season", ["Arsenal", "Chelsea", "Tottenham Hotspur/Tottenham/Spurs", "West Ham United/West Ham", "Crystal Palace", "Fulham", "Brentford"]),
 ("Name one of the 'Twelve Caesars' written about by Suetonius", ["Julius Caesar", "Augustus", "Tiberius", "Caligula", "Claudius", "Nero", "Galba", "Otho", "Vitellius", "Vespasian", "Titus", "Domitian"]),
 ("Name one of Rome's 'Five Good Emperors'", ["Nerva", "Trajan", "Hadrian", "Antoninus Pius", "Marcus Aurelius"]),
 ("Name a national capital city beginning with the letter A", ["Abu Dhabi", "Abuja", "Accra", "Addis Ababa", "Algiers", "Amman", "Amsterdam", "Andorra la Vella", "Ankara", "Antananarivo", "Apia", "Ashgabat", "Asmara", "Astana", "Asunción/Asuncion", "Athens"]),
 ("Name a national capital city beginning with the letter B", ["Baghdad", "Baku", "Bamako", "Bandar Seri Begawan", "Bangkok", "Bangui", "Banjul", "Basseterre", "Beijing", "Beirut", "Belgrade", "Belmopan", "Berlin", "Bern", "Bishkek", "Bissau", "Bogotá/Bogota", "Brasília/Brasilia", "Bratislava", "Brazzaville", "Bridgetown", "Brussels", "Bucharest", "Budapest", "Buenos Aires"]),
 ("Name a national capital city beginning with the letter M", ["Madrid", "Majuro", "Malabo", "Malé/Male", "Managua", "Manama", "Manila", "Maputo", "Maseru", "Mbabane", "Mexico City", "Minsk", "Mogadishu", "Monaco", "Monrovia", "Montevideo", "Moroni", "Moscow", "Muscat"]),
 ("Name a national capital city beginning with the letter S", ["San José/San Jose", "San Marino", "San Salvador", "Sana'a/Sanaa", "Santiago", "Santo Domingo", "São Tomé/Sao Tome", "Sarajevo", "Seoul", "Singapore", "Skopje", "Sofia", "Stockholm", "Sucre", "Suva"]),
 ("Name a national capital city beginning with the letter T", ["Taipei", "Tallinn", "Tarawa", "Tashkent", "Tbilisi", "Tegucigalpa", "Tehran", "Thimphu", "Tirana", "Tokyo", "Tripoli", "Tunis"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
