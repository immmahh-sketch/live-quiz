# Bank session 10 Oct 2026: 20 more Only One prompts (capitals by letter, borders, bands, Golden Boot, Apollo, 1800s PMs) appended to bank/unique-prompts.json. Each is a closed list with
# every correct answer (other accepted forms after a slash), so a fair answer is never knocked out.
import json, os
NEW = [
 ("Name a national capital city beginning with the letter C (capitals of independent countries)", ["Cairo", "Canberra", "Caracas", "Castries", "Chișinău/Chisinau", "Colombo", "Conakry", "Copenhagen"]),
 ("Name a national capital city beginning with the letter D", ["Dakar", "Damascus", "Dhaka", "Dili", "Djibouti", "Dodoma", "Doha", "Dublin", "Dushanbe"]),
 ("Name a national capital city beginning with the letter K", ["Kabul", "Kampala", "Kathmandu", "Khartoum", "Kigali", "Kingston", "Kingstown", "Kinshasa", "Kuala Lumpur", "Kuwait City/Kuwait", "Kyiv/Kiev"]),
 ("Name a national capital city beginning with the letter L", ["La Paz", "Libreville", "Lilongwe", "Lima", "Lisbon", "Ljubljana", "Lomé/Lome", "London", "Luanda", "Lusaka", "Luxembourg/Luxembourg City"]),
 ("Name a national capital city beginning with the letter P", ["Palikir", "Panama City", "Paramaribo", "Paris", "Phnom Penh", "Podgorica", "Port Louis", "Port Moresby", "Port of Spain", "Port Vila", "Port-au-Prince", "Porto-Novo", "Prague", "Praia", "Pretoria", "Pristina", "Pyongyang"]),
 ("Name a national capital city beginning with the letter N", ["Nairobi", "Nassau", "Naypyidaw/Nay Pyi Taw", "N'Djamena/Ndjamena", "New Delhi", "Ngerulmud", "Niamey", "Nicosia", "Nouakchott", "Nuku'alofa/Nukualofa"]),
 ("Name a national capital city beginning with the letter O or H", ["Oslo", "Ottawa", "Ouagadougou", "Hanoi", "Harare", "Havana", "Helsinki", "Honiara"]),
 ("Name a national capital city beginning with the letter Q or R", ["Quito", "Rabat", "Reykjavík/Reykjavik", "Riga", "Riyadh", "Rome", "Roseau"]),
 ("Name a national capital city beginning with the letter V or W", ["Vaduz", "Valletta", "Vatican City", "Victoria", "Vienna", "Vientiane", "Vilnius", "Warsaw", "Washington/Washington, D.C.", "Wellington", "Windhoek"]),
 ("Name a country that shares a land border with Bolivia or Paraguay", ["Brazil", "Argentina", "Chile", "Peru", "Bolivia", "Paraguay"]),
 ("Name a country that shares a land border with Sudan or Chad", ["Egypt", "Libya", "Chad", "Sudan", "Central African Republic/CAR", "South Sudan", "Ethiopia", "Eritrea", "Cameroon", "Nigeria", "Niger"]),
 ("Name a country that shares a land border with Iraq or Syria", ["Turkey/Türkiye", "Iran", "Kuwait", "Saudi Arabia", "Jordan", "Syria", "Iraq", "Israel", "Lebanon"]),
 ("Name a country that shares a land border with Romania or Serbia", ["Ukraine", "Moldova", "Bulgaria", "Hungary", "Serbia", "Romania", "North Macedonia/Macedonia", "Kosovo", "Montenegro", "Bosnia and Herzegovina/Bosnia", "Croatia"]),
 ("Name a country that shares a land border with Myanmar or Laos", ["Bangladesh", "India", "China", "Thailand", "Laos", "Vietnam", "Cambodia", "Myanmar/Burma"]),
 ("Name a member of the Eagles or the Doors, any line-up", ["Glenn Frey", "Don Henley", "Bernie Leadon", "Randy Meisner", "Don Felder", "Joe Walsh", "Timothy B. Schmit/Timothy Schmit", "Vince Gill", "Deacon Frey", "Jim Morrison", "Ray Manzarek", "Robby Krieger", "John Densmore"]),
 ("Name a member of U2 or Coldplay", ["Bono", "The Edge/Edge", "Adam Clayton", "Larry Mullen Jr/Larry Mullen", "Chris Martin", "Jonny Buckland", "Guy Berryman", "Will Champion", "Phil Harvey"]),
 ("Name a member of the Sex Pistols or the Clash, any line-up", ["Johnny Rotten/John Lydon", "Steve Jones", "Paul Cook", "Glen Matlock", "Sid Vicious", "Joe Strummer", "Mick Jones", "Paul Simonon", "Topper Headon/Nicky Headon", "Terry Chimes", "Nick Sheppard", "Vince White", "Pete Howard"]),
 ("Name a winner (or joint winner) of the Premier League Golden Boot from 1999–2000 to 2024–25", ["Kevin Phillips", "Jimmy Floyd Hasselbaink/Hasselbaink", "Thierry Henry/Henry", "Ruud van Nistelrooy/Van Nistelrooy", "Didier Drogba/Drogba", "Cristiano Ronaldo/Ronaldo", "Nicolas Anelka/Anelka", "Dimitar Berbatov/Berbatov", "Carlos Tevez/Tevez", "Robin van Persie/Van Persie", "Luis Suárez/Luis Suarez/Suárez/Suarez", "Sergio Agüero/Sergio Aguero/Agüero/Aguero", "Harry Kane/Kane", "Mohamed Salah/Salah", "Sadio Mané/Sadio Mane/Mané/Mane", "Pierre-Emerick Aubameyang/Aubameyang", "Jamie Vardy/Vardy", "Son Heung-min/Son", "Erling Haaland/Haaland"]),
 ("Name an Apollo mission that landed astronauts on the Moon", ["Apollo 11", "Apollo 12", "Apollo 14", "Apollo 15", "Apollo 16", "Apollo 17"]),
 ("Name a British Prime Minister who held office at any time from 1801 to 1900", ["William Pitt the Younger/Pitt the Younger/William Pitt/Pitt", "Henry Addington/Addington/Lord Sidmouth", "Lord Grenville/Grenville", "Duke of Portland/Portland", "Spencer Perceval/Perceval", "Lord Liverpool/Liverpool", "George Canning/Canning", "Lord Goderich/Goderich", "Duke of Wellington/Wellington", "Earl Grey/Lord Grey/Grey", "Lord Melbourne/Melbourne", "Robert Peel/Sir Robert Peel/Peel", "Lord John Russell/John Russell/Russell", "Earl of Derby/Lord Derby/Derby", "Lord Aberdeen/Aberdeen", "Lord Palmerston/Palmerston", "Benjamin Disraeli/Disraeli", "William Gladstone/Gladstone", "Lord Salisbury/Salisbury", "Lord Rosebery/Rosebery"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
