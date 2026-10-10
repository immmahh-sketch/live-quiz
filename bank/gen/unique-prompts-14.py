# Bank session 10 Oct 2026: 20 more Only One prompts (borders, bands, snooker, darts, leaders, Pixar, cities) appended to bank/unique-prompts.json. Each is a closed list with
# every correct answer (other accepted forms after a slash), so a fair answer is never knocked out.
import json, os
NEW = [
 ("Name a country that shares a land border with Kazakhstan or Mongolia", ["Russia", "China", "Kyrgyzstan", "Uzbekistan", "Turkmenistan", "Kazakhstan", "Mongolia"]),
 ("Name a country that shares a land border with Tanzania or Zambia", ["Kenya", "Uganda", "Rwanda", "Burundi", "Democratic Republic of the Congo/DR Congo/DRC", "Zambia", "Malawi", "Mozambique", "Tanzania", "Zimbabwe", "Botswana", "Namibia", "Angola"]),
 ("Name a country or territory that shares a land border with Mali or Algeria", ["Algeria", "Mali", "Niger", "Burkina Faso", "Ivory Coast/Côte d'Ivoire", "Guinea", "Senegal", "Mauritania", "Morocco", "Tunisia", "Libya", "Western Sahara"]),
 ("Name a country that shares a land border with Cambodia or Malaysia", ["Thailand", "Laos", "Vietnam", "Indonesia", "Brunei", "Cambodia", "Malaysia"]),
 ("Name a member of the Jam or the Smiths", ["Paul Weller", "Bruce Foxton", "Rick Buckler", "Morrissey", "Johnny Marr", "Andy Rourke", "Mike Joyce", "Craig Gannon"]),
 ("Name a member of the Stone Roses or the Happy Mondays", ["Ian Brown", "John Squire", "Mani/Gary Mounfield", "Reni/Alan Wren", "Shaun Ryder", "Bez", "Paul Ryder", "Mark Day", "Gaz Whelan", "Paul Davis", "Rowetta"]),
 ("Name a member of Blondie or Talking Heads", ["Debbie Harry", "Chris Stein", "Clem Burke", "Jimmy Destri", "Gary Valentine", "Nigel Harrison", "Frank Infante", "David Byrne", "Tina Weymouth", "Chris Frantz", "Jerry Harrison"]),
 ("Name a member of a 1980s British pop duo: Pet Shop Boys, Erasure, Soft Cell, Tears for Fears, Eurythmics or Yazoo", ["Neil Tennant", "Chris Lowe", "Andy Bell", "Vince Clarke", "Marc Almond", "Dave Ball", "Roland Orzabal", "Curt Smith", "Annie Lennox", "Dave Stewart", "Alison Moyet"]),
 ("Name a full-length Pixar film released from 2020 to 2025", ["Onward", "Soul", "Luca", "Turning Red", "Lightyear", "Elemental", "Inside Out 2", "Elio"]),
 ("Name a Marvel Studios film with 'Thor', 'Iron Man' or 'Spider-Man' in its title, up to 2025", ["Thor", "Thor: The Dark World", "Thor: Ragnarok", "Thor: Love and Thunder", "Iron Man", "Iron Man 2", "Iron Man 3", "Spider-Man: Homecoming", "Spider-Man: Far From Home", "Spider-Man: No Way Home"]),
 ("Name a Plantagenet king of England, including the Lancaster and York branches", ["Henry II", "Richard I/Richard the Lionheart", "John/King John", "Henry III", "Edward I", "Edward II", "Edward III", "Richard II", "Henry IV", "Henry V", "Henry VI", "Edward IV", "Edward V", "Richard III"]),
 ("Name a UK Prime Minister who held office at any time from 1900 to 1945", ["Lord Salisbury/Salisbury", "Arthur Balfour/Balfour", "Henry Campbell-Bannerman/Campbell-Bannerman", "H. H. Asquith/Herbert Asquith/Asquith", "David Lloyd George/Lloyd George", "Bonar Law/Andrew Bonar Law", "Stanley Baldwin/Baldwin", "Ramsay MacDonald/MacDonald", "Neville Chamberlain/Chamberlain", "Winston Churchill/Churchill"]),
 ("Name a US President who held office at any time from 1900 to 1960", ["William McKinley/McKinley", "Theodore Roosevelt/Teddy Roosevelt", "William Howard Taft/Taft", "Woodrow Wilson/Wilson", "Warren Harding/Harding", "Calvin Coolidge/Coolidge", "Herbert Hoover/Hoover", "Franklin D. Roosevelt/Franklin Roosevelt/FDR", "Harry Truman/Harry S. Truman/Truman", "Dwight Eisenhower/Eisenhower/Ike"]),
 ("Name a winner of the World Snooker Championship from 1990 to 2025", ["Stephen Hendry/Hendry", "John Parrott/Parrott", "Ken Doherty/Doherty", "John Higgins/Higgins", "Mark Williams", "Ronnie O'Sullivan/O'Sullivan", "Peter Ebdon/Ebdon", "Shaun Murphy/Murphy", "Graeme Dott/Dott", "Neil Robertson/Robertson", "Mark Selby/Selby", "Stuart Bingham/Bingham", "Judd Trump/Trump", "Luca Brecel/Brecel", "Kyren Wilson", "Zhao Xintong/Zhao"]),
 ("Name a winner of the PDC World Darts Championship, up to 2026", ["Dennis Priestley/Priestley", "Phil Taylor/Taylor", "John Part/Part", "Raymond van Barneveld/Van Barneveld", "Adrian Lewis", "Michael van Gerwen/Van Gerwen", "Gary Anderson/Anderson", "Rob Cross/Cross", "Peter Wright/Wright", "Gerwyn Price/Price", "Michael Smith", "Luke Humphries/Humphries", "Luke Littler/Littler"]),
 ("Name a novel in Philip Pullman's His Dark Materials or The Book of Dust", ["Northern Lights/The Golden Compass", "The Subtle Knife", "The Amber Spyglass", "La Belle Sauvage", "The Secret Commonwealth", "The Rose Field"]),
 ("Name one of the twelve great Roman gods and goddesses (the Dii Consentes)", ["Jupiter", "Juno", "Neptune", "Minerva", "Mars", "Venus", "Apollo", "Diana", "Vulcan", "Vesta", "Mercury", "Ceres"]),
 ("Name a Premier League or EFL club with 'City' in its name, in the 2025–26 season", ["Manchester City/Man City", "Birmingham City", "Bristol City", "Bradford City", "Cardiff City", "Coventry City", "Exeter City", "Hull City", "Leicester City", "Lincoln City", "Norwich City", "Stoke City", "Swansea City", "Salford City"]),
 ("Name a country that won tennis's Davis Cup from 2000 to 2024", ["Spain", "France", "Russia", "Australia", "Croatia", "USA/United States", "Serbia", "Czech Republic/Czechia", "Switzerland", "Great Britain/GB/UK", "Argentina", "Canada", "Italy"]),
 ("Name a city that has hosted the Commonwealth Games, up to 2026", ["Hamilton", "London", "Sydney", "Auckland", "Vancouver", "Cardiff", "Perth", "Kingston", "Edinburgh", "Christchurch", "Edmonton", "Brisbane", "Victoria", "Kuala Lumpur", "Manchester", "Melbourne", "Delhi/New Delhi", "Glasgow", "Gold Coast", "Birmingham"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
