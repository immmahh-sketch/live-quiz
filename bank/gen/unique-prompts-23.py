# Bank session 11 Oct 2026: 21 more Only One prompts (British and American TV comedies and dramas) appended to bank/unique-prompts.json.
# Each is a closed list with every correct answer (other accepted forms after a slash), so a fair answer is never knocked out.
import json, os
NEW = [
 ("Name a character from Ted Lasso", ["Ted Lasso/Ted", "Coach Beard/Beard", "Rebecca Welton/Rebecca", "Keeley Jones/Keeley", "Roy Kent/Roy", "Jamie Tartt/Jamie", "Nate Shelley/Nate/Nathan", "Higgins/Leslie Higgins", "Sam Obisanya/Sam", "Dani Rojas/Dani", "Isaac McAdoo/Isaac", "Colin Hughes/Colin", "Trent Crimm", "Rupert Mannion/Rupert", "Sharon Fieldstone/Dr Sharon", "Jan Maas", "Zava", "Bex", "Mae"]),
 ("Name a character from Schitt's Creek", ["Johnny Rose/Johnny", "Moira Rose/Moira", "David Rose/David", "Alexis Rose/Alexis", "Stevie Budd/Stevie", "Roland Schitt/Roland", "Jocelyn Schitt/Jocelyn", "Mutt", "Ted Mullens/Ted", "Twyla", "Patrick Brewer/Patrick", "Ronnie", "Bob"]),
 ("Name a character from Brooklyn Nine-Nine, dog included", ["Jake Peralta/Jake", "Amy Santiago/Amy", "Rosa Diaz/Rosa", "Terry Jeffords/Terry", "Charles Boyle/Charles", "Gina Linetti/Gina", "Raymond Holt/Holt/Captain Holt", "Hitchcock", "Scully", "Kevin Cozner/Kevin", "Doug Judy", "Adrian Pimento/Pimento", "Madeline Wuntch/Wuntch", "Cheddar"]),
 ("Name a character from Parks and Recreation", ["Leslie Knope/Leslie", "Ron Swanson/Ron", "April Ludgate/April", "Andy Dwyer/Andy", "Tom Haverford/Tom", "Ann Perkins/Ann", "Ben Wyatt/Ben", "Chris Traeger/Chris", "Jerry Gergich/Jerry/Garry", "Donna Meagle/Donna", "Mark Brendanawicz/Mark", "Tammy", "Jean-Ralphio", "Li'l Sebastian", "Craig Middlebrooks/Craig"]),
 ("Name a character from The IT Crowd", ["Roy", "Moss", "Jen", "Douglas Reynholm/Douglas", "Denholm Reynholm/Denholm", "Richmond"]),
 ("Name one of the three main characters in Black Books", ["Bernard Black/Bernard", "Manny", "Fran"]),
 ("Name a character from Phoenix Nights", ["Brian Potter/Brian", "Jerry St Clair/Jerry", "Max", "Paddy", "Ray Von", "Kenny Senior", "Young Kenny", "Holy Mary", "Spencer", "Den Perry", "Les McQueen"]),
 ("Name a character from Still Game", ["Jack", "Victor", "Winston", "Isa", "Navid", "Tam", "Boabby", "Methadone Mick", "Shug", "Meena", "Pete the Jakey"]),
 ("Name a detective or regular in Inspector Morse, Lewis or Endeavour", ["Morse/Endeavour Morse", "Lewis/Robbie Lewis", "Hathaway/James Hathaway", "Fred Thursday/Thursday", "Joan Thursday", "Strange", "Max DeBryn", "Laura Hobson", "Jakes", "Bright", "Innocent"]),
 ("Name one of the lead detectives in Death in Paradise", ["Richard Poole", "Humphrey Goodman", "Jack Mooney", "Neville Parker", "Mervin Wilson"]),
 ("Name a character from Doc Martin", ["Martin Ellingham/Doc Martin/Martin", "Louisa Glasson/Louisa", "Aunt Joan/Joan", "Aunt Ruth/Ruth", "Bert Large/Bert", "Al Large/Al", "Mrs Tishell/Sally Tishell", "PC Penhale/Joe Penhale", "Morwenna", "Pauline", "Elaine"]),
 ("Name a character from Luther", ["John Luther/Luther", "Alice Morgan/Alice", "Justin Ripley/Ripley", "Ian Reed", "Martin Schenk/Schenk", "Zoe Luther/Zoe", "Mark North", "Benny Silver/Benny", "Erin Gray", "Catherine Halliday"]),
 ("Name a character from The Wire", ["Jimmy McNulty/McNulty", "Bunk", "Kima Greggs/Kima", "Lester Freamon/Lester", "Cedric Daniels/Daniels", "Stringer Bell/Stringer", "Avon Barksdale/Avon", "Omar Little/Omar", "Bubbles", "D'Angelo", "Wallace", "Bodie", "Marlo Stanfield/Marlo", "Chris Partlow", "Snoop", "Proposition Joe/Prop Joe", "Herc", "Carver", "Prez", "Bunny Colvin", "Clay Davis", "Tommy Carcetti/Carcetti", "Rawls", "Burrell", "Frank Sobotka", "Ziggy", "Nick Sobotka", "Michael", "Dukie", "Namond", "Randy", "Cutty"]),
 ("Name a character from Twin Peaks", ["Dale Cooper/Agent Cooper", "Laura Palmer", "Leland Palmer", "Sarah Palmer", "Harry Truman/Sheriff Truman", "Audrey Horne", "Ben Horne", "Shelly Johnson", "Bobby Briggs", "Donna Hayward", "James Hurley", "The Log Lady", "BOB", "Lucy", "Andy", "Hawk", "Norma", "Big Ed", "Nadine", "Leo Johnson", "Josie Packard", "Catherine Martell", "Pete Martell", "Windom Earle", "Gordon Cole", "Albert"]),
 ("Name a character from M*A*S*H", ["Hawkeye Pierce/Hawkeye", "Trapper John/Trapper", "B.J. Hunnicutt/BJ", "Frank Burns", "Hot Lips Houlihan/Margaret Houlihan/Hot Lips", "Radar O'Reilly/Radar", "Klinger", "Father Mulcahy", "Henry Blake", "Colonel Potter/Sherman Potter", "Charles Winchester/Winchester"]),
 ("Name a character from Scrubs", ["J.D./JD", "Turk", "Elliot Reid/Elliot", "Carla Espinosa/Carla", "Dr Cox/Perry Cox", "Dr Kelso/Kelso", "The Janitor", "Ted", "The Todd/Todd", "Laverne", "Jordan Sullivan/Jordan", "Doug Murphy/Doug", "Keith"]),
 ("Name a character from How I Met Your Mother", ["Ted Mosby/Ted", "Marshall Eriksen/Marshall", "Lily Aldrin/Lily", "Barney Stinson/Barney", "Robin Scherbatsky/Robin", "Tracy McConnell/The Mother/Tracy", "Ranjit", "Carl", "Victoria", "Stella", "Zoey", "Patrice"]),
 ("Name a member of the family in Modern Family, dog included", ["Jay Pritchett/Jay", "Gloria", "Manny", "Joe", "Claire Dunphy/Claire", "Phil Dunphy/Phil", "Haley", "Alex", "Luke", "Mitchell", "Cameron/Cam", "Lily", "DeDe", "Stella"]),
 ("Name a character from Fleabag, guinea pig included", ["Fleabag", "Claire", "Godmother", "Dad", "Martin", "Boo", "The Priest", "Harry", "Hilary", "Klare", "Belinda"]),
 ("Name a character from Killing Eve", ["Eve Polastri/Eve", "Villanelle/Oksana", "Carolyn Martens/Carolyn", "Konstantin", "Kenny", "Niko", "Bill Pargrave/Bill", "Hugo", "Raymond", "Dasha", "Elena"]),
 ("Name a character from Midsomer Murders", ["Tom Barnaby", "John Barnaby", "Joyce Barnaby/Joyce", "Cully/Cully Barnaby", "Sergeant Troy/Troy", "Sergeant Jones/Ben Jones", "Sergeant Nelson/Charlie Nelson", "Jamie Winter/Winter", "Dr Bullard/George Bullard", "Sykes", "Sarah Barnaby", "Kate Wilding"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
