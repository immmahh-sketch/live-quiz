# Bank session 10 Oct 2026: 20 more Only One prompts (capitals, borders, bands, Bond, Bake Off, Wimbledon) appended to bank/unique-prompts.json. Each is a closed list with
# every correct answer (other accepted forms after a slash), so a fair answer is never knocked out.
import json, os
NEW = [
 ("Name a national capital city beginning with E, F, G, I, J, Y or Z", ["Freetown", "Funafuti", "Gaborone", "Georgetown", "Gitega", "Guatemala City", "Islamabad", "Jakarta", "Jerusalem", "Juba", "Yamoussoukro", "Yaoundé/Yaounde", "Yerevan", "Zagreb"]),
 ("Name a country that shares a land border with Ukraine or Belarus", ["Russia", "Belarus", "Ukraine", "Poland", "Slovakia", "Hungary", "Romania", "Moldova", "Lithuania", "Latvia"]),
 ("Name a country that shares a land border with the Democratic Republic of the Congo or Angola", ["Democratic Republic of the Congo/DR Congo/DRC", "Republic of the Congo/Congo-Brazzaville/Congo", "Central African Republic/CAR", "South Sudan", "Uganda", "Rwanda", "Burundi", "Tanzania", "Zambia", "Angola", "Namibia"]),
 ("Name a country that shares a land border with Venezuela or Ecuador", ["Colombia", "Brazil", "Guyana", "Peru", "Venezuela", "Ecuador"]),
 ("Name a country or territory that shares a land border with Israel or Jordan", ["Lebanon", "Syria", "Jordan", "Egypt", "Israel", "Iraq", "Saudi Arabia", "Palestine/West Bank/Gaza"]),
 ("Name a member of Duran Duran or Spandau Ballet", ["Simon Le Bon", "Nick Rhodes", "John Taylor", "Roger Taylor", "Andy Taylor", "Warren Cuccurullo", "Tony Hadley", "Gary Kemp", "Martin Kemp", "Steve Norman", "John Keeble"]),
 ("Name a member of the Beach Boys or the Police", ["Brian Wilson", "Dennis Wilson", "Carl Wilson", "Mike Love", "Al Jardine", "Bruce Johnston", "David Marks", "Sting", "Andy Summers", "Stewart Copeland", "Henry Padovani"]),
 ("Name a club that has won the English top-flight league title since 1990", ["Liverpool", "Arsenal", "Leeds United/Leeds", "Manchester United/Man United/Man Utd", "Blackburn Rovers/Blackburn", "Chelsea", "Manchester City/Man City", "Leicester City/Leicester"]),
 ("Name a country that has won the men's European Championship (the Euros), up to 2024", ["Germany/West Germany", "Spain", "France", "Italy", "Soviet Union/USSR", "Czechoslovakia", "Netherlands/Holland", "Denmark", "Greece", "Portugal"]),
 ("Name a UK Poet Laureate since 1900", ["Alfred Austin", "Robert Bridges", "John Masefield", "Cecil Day-Lewis", "John Betjeman", "Ted Hughes", "Andrew Motion", "Carol Ann Duffy", "Simon Armitage"]),
 ("Name a book of the New Testament (the numbered letters, like 1 and 2 Peter, count as one)", ["Matthew", "Mark", "Luke", "John", "Acts/Acts of the Apostles", "Romans", "Corinthians", "Galatians", "Ephesians", "Philippians", "Colossians", "Thessalonians", "Timothy", "Titus", "Philemon", "Hebrews", "James", "Peter", "Jude", "Revelation/Revelations"]),
 ("Name a Disney animated feature film released before 1970", ["Snow White and the Seven Dwarfs/Snow White", "Pinocchio", "Fantasia", "Dumbo", "Bambi", "Saludos Amigos", "The Three Caballeros", "Make Mine Music", "Fun and Fancy Free", "Melody Time", "The Adventures of Ichabod and Mr. Toad", "Cinderella", "Alice in Wonderland", "Peter Pan", "Lady and the Tramp", "Sleeping Beauty", "One Hundred and One Dalmatians/101 Dalmatians", "The Sword in the Stone", "The Jungle Book"]),
 ("Name a British Formula One drivers' world champion, up to 2024", ["Mike Hawthorn", "Graham Hill", "Jim Clark", "John Surtees", "Jackie Stewart", "James Hunt", "Nigel Mansell", "Damon Hill", "Lewis Hamilton", "Jenson Button"]),
 ("Name an official James Bond film starring Roger Moore", ["Live and Let Die", "The Man with the Golden Gun", "The Spy Who Loved Me", "Moonraker", "For Your Eyes Only", "Octopussy", "A View to a Kill"]),
 ("Name an official James Bond film starring Sean Connery or Pierce Brosnan", ["Dr. No/Dr No/Doctor No", "From Russia with Love", "Goldfinger", "Thunderball", "You Only Live Twice", "Diamonds Are Forever", "GoldenEye", "Tomorrow Never Dies", "The World Is Not Enough", "Die Another Day"]),
 ("Name one of Michael Jackson's brothers or sisters", ["Rebbie", "Jackie", "Tito", "Jermaine", "La Toya", "Marlon", "Randy", "Janet"]),
 ("Name a winner of The Great British Bake Off, up to 2024", ["Edd Kimber", "Jo Wheatley", "John Whaite", "Frances Quinn", "Nancy Birtwhistle", "Nadiya Hussain/Nadiya", "Candice Brown", "Sophie Faldo", "Rahul Mandal", "David Atherton", "Peter Sawkins", "Giuseppe Dell'Anno", "Syabira Yusoff", "Matty Edgell", "Georgie Grasso"]),
 ("Name a man who won the Wimbledon singles title from 1980 to 1999", ["Björn Borg/Bjorn Borg/Borg", "John McEnroe/McEnroe", "Jimmy Connors/Connors", "Boris Becker/Becker", "Pat Cash/Cash", "Stefan Edberg/Edberg", "Michael Stich/Stich", "Andre Agassi/Agassi", "Pete Sampras/Sampras", "Richard Krajicek/Krajicek"]),
 ("Name a Chancellor of (West) Germany since 1949", ["Konrad Adenauer/Adenauer", "Ludwig Erhard/Erhard", "Kurt Georg Kiesinger/Kiesinger", "Willy Brandt/Brandt", "Helmut Schmidt/Schmidt", "Helmut Kohl/Kohl", "Gerhard Schröder/Gerhard Schroeder/Schröder/Schroeder", "Angela Merkel/Merkel", "Olaf Scholz/Scholz", "Friedrich Merz/Merz"]),
 ("Name a woman who won the Wimbledon singles title from 1980 to 2009", ["Evonne Goolagong/Evonne Goolagong Cawley/Goolagong", "Chris Evert/Chris Evert Lloyd/Evert", "Martina Navratilova/Navratilova", "Steffi Graf/Graf", "Conchita Martínez/Conchita Martinez/Martinez", "Martina Hingis/Hingis", "Jana Novotná/Jana Novotna/Novotna", "Lindsay Davenport/Davenport", "Venus Williams/Venus", "Serena Williams/Serena", "Amélie Mauresmo/Amelie Mauresmo/Mauresmo", "Maria Sharapova/Sharapova"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
