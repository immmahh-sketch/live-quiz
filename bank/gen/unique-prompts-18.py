# Bank session 10 Oct 2026: 20 more Only One prompts (albums, film series, presenters, popes, realms) appended to bank/unique-prompts.json.
# Each is a closed list with every correct answer (other accepted forms after a slash), so a fair answer is never knocked out.
import json, os
NEW = [
 ("Name a studio album by U2", ["Boy", "October", "War", "The Unforgettable Fire", "The Joshua Tree", "Rattle and Hum", "Achtung Baby", "Zooropa", "Pop", "All That You Can't Leave Behind", "How to Dismantle an Atomic Bomb", "No Line on the Horizon", "Songs of Innocence", "Songs of Experience", "Songs of Surrender"]),
 ("Name a studio album by Madonna", ["Madonna", "Like a Virgin", "True Blue", "Like a Prayer", "Erotica", "Bedtime Stories", "Ray of Light", "Music", "American Life", "Confessions on a Dance Floor", "Hard Candy", "MDNA", "Rebel Heart", "Madame X"]),
 ("Name a film in the Rocky or Creed series", ["Rocky", "Rocky II", "Rocky III", "Rocky IV", "Rocky V", "Rocky Balboa", "Creed", "Creed II", "Creed III"]),
 ("Name a film in the Die Hard or Lethal Weapon series", ["Die Hard", "Die Hard 2", "Die Hard with a Vengeance", "Live Free or Die Hard/Die Hard 4.0", "A Good Day to Die Hard", "Lethal Weapon", "Lethal Weapon 2", "Lethal Weapon 3", "Lethal Weapon 4"]),
 ("Name an Indiana Jones film or a Back to the Future film", ["Raiders of the Lost Ark", "Temple of Doom/Indiana Jones and the Temple of Doom", "The Last Crusade/Indiana Jones and the Last Crusade", "Kingdom of the Crystal Skull/Indiana Jones and the Kingdom of the Crystal Skull", "Dial of Destiny/Indiana Jones and the Dial of Destiny", "Back to the Future", "Back to the Future Part II", "Back to the Future Part III"]),
 ("Name a film in the Godfather or Jaws series", ["The Godfather", "The Godfather Part II", "The Godfather Part III", "Jaws", "Jaws 2", "Jaws 3-D/Jaws 3", "Jaws: The Revenge"]),
 ("Name a Disney animated film from its 'Renaissance', 1989 to 1999", ["The Little Mermaid", "The Rescuers Down Under", "Beauty and the Beast", "Aladdin", "The Lion King", "Pocahontas", "The Hunchback of Notre Dame", "Hercules", "Mulan", "Tarzan"]),
 ("Name a US state with a coastline on the Atlantic Ocean", ["Maine", "New Hampshire", "Massachusetts", "Rhode Island", "Connecticut", "New York", "New Jersey", "Delaware", "Maryland", "Virginia", "North Carolina", "South Carolina", "Georgia", "Florida"]),
 ("Name a course that has hosted golf's Open Championship, up to 2025", ["St Andrews", "Carnoustie", "Muirfield", "Royal Troon/Troon", "Turnberry", "Royal Birkdale/Birkdale", "Royal Lytham & St Annes/Lytham", "Royal Liverpool/Hoylake", "Royal St George's/Sandwich", "Royal Portrush/Portrush", "Prestwick", "Musselburgh", "Royal Cinque Ports/Deal", "Prince's"]),
 ("Name a Formula One team on the 2026 grid", ["Red Bull", "Ferrari", "Mercedes", "McLaren", "Aston Martin", "Alpine", "Williams", "Racing Bulls/RB", "Haas", "Audi/Sauber", "Cadillac"]),
 ("Name a main presenter of Match of the Day, up to the 2025-26 season", ["Kenneth Wolstenholme", "David Coleman", "Jimmy Hill", "Des Lynam", "Gary Lineker", "Gabby Logan", "Mark Chapman", "Kelly Cates"]),
 ("Name a presenter of Countdown, up to 2025", ["Richard Whiteley", "Des Lynam", "Des O'Connor", "Jeff Stelling", "Nick Hewer", "Anne Robinson", "Colin Murray"]),
 ("Name an act that won Eurovision for the UK or for Ireland", ["Sandie Shaw", "Lulu", "Brotherhood of Man", "Bucks Fizz", "Katrina and the Waves", "Dana", "Johnny Logan", "Linda Martin", "Niamh Kavanagh", "Paul Harrington and Charlie McGettigan", "Eimear Quinn"]),
 ("Name a Pope since 1900, up to 2026", ["Leo XIII", "Pius X", "Benedict XV", "Pius XI", "Pius XII", "John XXIII", "Paul VI", "John Paul I", "John Paul II", "Benedict XVI", "Francis", "Leo XIV"]),
 ("Name one of the eight Bridgerton siblings", ["Anthony", "Benedict", "Colin", "Daphne", "Eloise", "Francesca", "Gregory", "Hyacinth"]),
 ("Name a country where King Charles III is head of state in 2026", ["United Kingdom/UK/Britain", "Canada", "Australia", "New Zealand", "Jamaica", "The Bahamas/Bahamas", "Belize", "Antigua and Barbuda", "Grenada", "Papua New Guinea", "Saint Kitts and Nevis/St Kitts and Nevis", "Saint Lucia/St Lucia", "Saint Vincent and the Grenadines/St Vincent", "Solomon Islands", "Tuvalu"]),
 ("Name a station or utility on the UK Monopoly board", ["King's Cross Station/King's Cross", "Marylebone Station/Marylebone", "Fenchurch St Station/Fenchurch Street", "Liverpool Street Station/Liverpool Street", "Electric Company", "Water Works"]),
 ("Name a person carved on Mount Rushmore or pictured on a US banknote in use today", ["George Washington/Washington", "Thomas Jefferson/Jefferson", "Abraham Lincoln/Lincoln", "Theodore Roosevelt/Teddy Roosevelt/Roosevelt", "Alexander Hamilton/Hamilton", "Andrew Jackson/Jackson", "Ulysses S. Grant/Grant", "Benjamin Franklin/Franklin"]),
 ("Name a UK Christmas number one by the Beatles or the Spice Girls", ["I Want to Hold Your Hand", "I Feel Fine", "Day Tripper/We Can Work It Out", "Hello, Goodbye", "2 Become 1", "Too Much", "Goodbye"]),
 ("Name a US city that has hosted a Summer or Winter Olympics, up to 2026", ["St Louis/St. Louis", "Los Angeles/LA", "Lake Placid", "Squaw Valley/Palisades Tahoe", "Atlanta", "Salt Lake City"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
