# Bank session 10 Oct 2026: 20 more Only One prompts appended to bank/unique-prompts.json. Each is a closed list with
# every correct answer (other accepted forms after a slash), so a fair answer is never knocked out.
import json, os
NEW = [
 ("Name a country whose English name begins and ends with the letter A", ["Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria"]),
 ("Name a US state whose name ends in the letter A", ["Alabama", "Alaska", "Arizona", "California", "Florida", "Georgia", "Indiana", "Iowa", "Louisiana", "Minnesota", "Montana", "Nebraska", "Nevada", "North Carolina", "North Dakota", "Oklahoma", "Pennsylvania", "South Carolina", "South Dakota", "Virginia", "West Virginia"]),
 ("Name one of the twelve 'minor prophets' of the Old Testament", ["Hosea", "Joel", "Amos", "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk", "Zephaniah", "Haggai", "Zechariah", "Malachi"]),
 ("Name a Shakespeare history play (the king's name will do)", ["King John", "Richard II", "Henry IV", "Henry V", "Henry VI", "Richard III", "Henry VIII", "Edward III"]),
 ("Name a book by George Orwell", ["Down and Out in Paris and London", "Burmese Days", "A Clergyman's Daughter", "Keep the Aspidistra Flying", "The Road to Wigan Pier", "Homage to Catalonia", "Coming Up for Air", "Animal Farm", "Nineteen Eighty-Four/1984"]),
 ("Name a country that shares a land border with Iran", ["Iraq", "Turkey/Türkiye", "Armenia", "Azerbaijan", "Turkmenistan", "Afghanistan", "Pakistan"]),
 ("Name a country that shares a land border with Saudi Arabia", ["Jordan", "Iraq", "Kuwait", "Qatar", "United Arab Emirates/UAE", "Oman", "Yemen"]),
 ("Name a country that shares a land border with Poland or Hungary", ["Germany", "Czechia/Czech Republic", "Slovakia", "Ukraine", "Belarus", "Lithuania", "Russia", "Austria", "Romania", "Serbia", "Croatia", "Slovenia"]),
 ("Name a country that shares a land border with Argentina or Peru", ["Chile", "Bolivia", "Paraguay", "Brazil", "Uruguay", "Ecuador", "Colombia"]),
 ("Name one of the seven hills of ancient Rome", ["Aventine", "Caelian", "Capitoline", "Esquiline", "Palatine", "Quirinal", "Viminal"]),
 ("Name one of Africa's 'Big Five' or 'Ugly Five' safari animals", ["Lion", "Leopard", "Elephant", "Rhino/Rhinoceros", "Buffalo/Cape buffalo", "Hyena", "Wildebeest/Gnu", "Warthog", "Vulture", "Marabou stork"]),
 ("Name a winner of the Best Actor Oscar at the 2011 to 2025 ceremonies", ["Colin Firth", "Jean Dujardin", "Daniel Day-Lewis", "Matthew McConaughey", "Eddie Redmayne", "Leonardo DiCaprio", "Casey Affleck", "Gary Oldman", "Rami Malek", "Joaquin Phoenix", "Anthony Hopkins", "Will Smith", "Brendan Fraser", "Cillian Murphy", "Adrien Brody"]),
 ("Name a winner of the Best Actress Oscar at the 2011 to 2025 ceremonies", ["Natalie Portman", "Meryl Streep", "Jennifer Lawrence", "Cate Blanchett", "Julianne Moore", "Brie Larson", "Emma Stone", "Frances McDormand", "Olivia Colman", "Renée Zellweger/Renee Zellweger", "Jessica Chastain", "Michelle Yeoh", "Mikey Madison"]),
 ("Name a station on the London Underground's Victoria line", ["Walthamstow Central/Walthamstow", "Blackhorse Road", "Tottenham Hale", "Seven Sisters", "Finsbury Park", "Highbury & Islington/Highbury and Islington", "King's Cross St Pancras/King's Cross", "Euston", "Warren Street", "Oxford Circus", "Green Park", "Victoria", "Pimlico", "Vauxhall", "Stockwell", "Brixton"]),
 ("Name one of the Four Horsemen of the Apocalypse or one of the three Fates", ["War", "Famine", "Pestilence/Conquest", "Death", "Clotho", "Lachesis", "Atropos"]),
 ("Name one of the nine Muses of Greek myth", ["Calliope", "Clio", "Erato", "Euterpe", "Melpomene", "Polyhymnia", "Terpsichore", "Thalia", "Urania"]),
 ("Name a Formula One drivers' world champion from 1950 to 1989", ["Giuseppe Farina/Nino Farina", "Juan Manuel Fangio/Fangio", "Alberto Ascari/Ascari", "Mike Hawthorn/Hawthorn", "Jack Brabham/Brabham", "Phil Hill", "Graham Hill", "Jim Clark/Clark", "John Surtees/Surtees", "Denny Hulme/Hulme", "Jackie Stewart/Stewart", "Jochen Rindt/Rindt", "Emerson Fittipaldi/Fittipaldi", "Niki Lauda/Lauda", "James Hunt/Hunt", "Mario Andretti/Andretti", "Jody Scheckter/Scheckter", "Alan Jones", "Nelson Piquet/Piquet", "Keke Rosberg", "Alain Prost/Prost", "Ayrton Senna/Senna"]),
 ("Name one of Arthur Conan Doyle's four Sherlock Holmes novels or five story collections", ["A Study in Scarlet", "The Sign of the Four/The Sign of Four", "The Hound of the Baskervilles", "The Valley of Fear", "The Adventures of Sherlock Holmes", "The Memoirs of Sherlock Holmes", "The Return of Sherlock Holmes", "His Last Bow", "The Case-Book of Sherlock Holmes/The Casebook of Sherlock Holmes"]),
 ("Name a country whose name ends in '-stan'", ["Afghanistan", "Pakistan", "Kazakhstan", "Kyrgyzstan", "Tajikistan", "Turkmenistan", "Uzbekistan"]),
 ("Name one of the moons of Mars or one of the five major moons of Uranus", ["Phobos", "Deimos", "Miranda", "Ariel", "Umbriel", "Titania", "Oberon"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
