# Bank session 10 Oct 2026: 20 more Only One prompts appended to bank/unique-prompts.json. Each is a closed list with
# every correct answer (other accepted forms after a slash), so a fair answer is never knocked out.
import json, os
NEW = [
 ("Name a country beginning with the letter A", ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda/Antigua", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan"]),
 ("Name a country beginning with the letter G", ["Gabon", "Gambia/The Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana"]),
 ("Name a country beginning with the letter P", ["Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines/The Philippines", "Poland", "Portugal"]),
 ("Name a country beginning with the letter T", ["Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste/East Timor", "Togo", "Tonga", "Trinidad and Tobago/Trinidad", "Tunisia", "Turkey/Türkiye", "Turkmenistan", "Tuvalu"]),
 ("Name a country beginning with the letter I or N", ["Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Ivory Coast/Côte d'Ivoire", "Namibia", "Nauru", "Nepal", "Netherlands/The Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "North Macedonia/Macedonia", "Norway"]),
 ("Name a US state beginning with C, K or T", ["California", "Colorado", "Connecticut", "Kansas", "Kentucky", "Tennessee", "Texas"]),
 ("Name a US state beginning with W, V or D", ["Washington", "West Virginia", "Wisconsin", "Wyoming", "Vermont", "Virginia", "Delaware"]),
 ("Name a London mainline railway terminus", ["Euston", "King's Cross/Kings Cross", "St Pancras", "Paddington", "Victoria", "Waterloo", "Liverpool Street", "Charing Cross", "London Bridge", "Marylebone", "Fenchurch Street", "Cannon Street", "Blackfriars", "Moorgate"]),
 ("Name a country that has won the men's 50-over Cricket World Cup", ["West Indies/Windies", "India", "Australia", "Pakistan", "Sri Lanka", "England"]),
 ("Name a Shakespeare tragedy", ["Titus Andronicus", "Romeo and Juliet", "Julius Caesar", "Hamlet", "Troilus and Cressida", "Othello", "King Lear", "Macbeth", "Antony and Cleopatra", "Coriolanus", "Timon of Athens"]),
 ("Name an Agatha Christie detective, or one of their sidekicks", ["Hercule Poirot/Poirot", "Miss Marple/Jane Marple", "Tommy Beresford/Tommy", "Tuppence Beresford/Tuppence", "Parker Pyne", "Harley Quin/Mr Quin", "Mr Satterthwaite", "Superintendent Battle/Battle", "Ariadne Oliver", "Colonel Race", "Inspector Japp/Japp", "Captain Hastings/Hastings", "Miss Lemon"]),
 ("Name one of the nine official regions of England", ["North East", "North West", "Yorkshire and the Humber/Yorkshire", "East Midlands", "West Midlands", "East of England/East Anglia", "London", "South East", "South West"]),
 ("Name someone who has been Prince of Wales since 1900", ["Edward VII", "George V", "Edward VIII", "Charles III/Charles", "William/Prince William"]),
 ("Name one of the Seven Summits, the highest peak on each continent (either list)", ["Everest", "Aconcagua", "Denali/Mount McKinley", "Kilimanjaro", "Elbrus", "Vinson/Mount Vinson", "Puncak Jaya/Carstensz Pyramid", "Kosciuszko/Mount Kosciuszko", "Mont Blanc"]),
 ("Name a British player who has won a Grand Slam singles title since 1970", ["Andy Murray", "Virginia Wade", "Sue Barker", "Emma Raducanu"]),
 ("Name a member of the Rat Pack", ["Frank Sinatra", "Dean Martin", "Sammy Davis Jr", "Peter Lawford", "Joey Bishop"]),
 ("Name one of the Three Stooges (any line-up) or the Three Tenors", ["Moe Howard/Moe", "Larry Fine/Larry", "Curly Howard/Curly", "Shemp Howard/Shemp", "Joe Besser", "Curly Joe DeRita/Curly Joe", "Luciano Pavarotti/Pavarotti", "Plácido Domingo/Placido Domingo/Domingo", "José Carreras/Jose Carreras/Carreras"]),
 ("Name a country that shares a land border with Austria or Switzerland", ["Germany", "Czechia/Czech Republic", "Slovakia", "Hungary", "Slovenia", "Italy", "Switzerland", "Liechtenstein", "Austria", "France"]),
 ("Name a country that shares a land border with Russia", ["Norway", "Finland", "Estonia", "Latvia", "Lithuania", "Poland", "Belarus", "Ukraine", "Georgia", "Azerbaijan", "Kazakhstan", "China", "Mongolia", "North Korea"]),
 ("Name a country in the Americas with a Pacific coastline", ["Canada", "United States/USA/America", "Mexico", "Guatemala", "El Salvador", "Honduras", "Nicaragua", "Costa Rica", "Panama", "Colombia", "Ecuador", "Peru", "Chile"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
