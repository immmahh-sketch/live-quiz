# Bank session 9 Oct 2026: 32 more Only One prompts appended to bank/unique-prompts.json. Each is a closed list with
# every correct answer (other accepted forms after a slash), so a fair answer is never knocked out.
import json, os
NEW = [
 ("Name a colour of the rainbow", ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet/Purple"]),
 ("Name a chess piece", ["King", "Queen", "Rook/Castle", "Bishop", "Knight/Horse", "Pawn"]),
 ("Name a rank or a suit in a standard pack of cards", ["Ace", "Two/2", "Three/3", "Four/4", "Five/5", "Six/6", "Seven/7", "Eight/8", "Nine/9", "Ten/10", "Jack/Knave", "Queen", "King", "Hearts/Heart", "Diamonds/Diamond", "Clubs/Club", "Spades/Spade"]),
 ("Name an event in the athletics decathlon or the Olympic modern pentathlon", ["100 metres/100m", "Long jump", "Shot put/Shot", "High jump", "400 metres/400m", "110 metres hurdles/110m hurdles/Hurdles", "Discus", "Pole vault", "Javelin", "1500 metres/1500m", "Fencing", "Swimming", "Riding/Show jumping/Horse riding", "Running", "Shooting", "Laser run", "Obstacle course/Obstacle"]),
 ("Name one of the Seven Wonders of the Ancient World", ["Great Pyramid of Giza/Great Pyramid/Pyramids", "Hanging Gardens of Babylon/Hanging Gardens", "Statue of Zeus at Olympia/Statue of Zeus", "Temple of Artemis at Ephesus/Temple of Artemis", "Mausoleum at Halicarnassus/Mausoleum", "Colossus of Rhodes/Colossus", "Lighthouse of Alexandria/Pharos of Alexandria/Pharos"]),
 ("Name a country in the G7, or a permanent member of the UN Security Council", ["United Kingdom/UK/Britain", "United States/USA/America", "France", "Germany", "Italy", "Japan", "Canada", "China", "Russia"]),
 ("Name a member of the Rolling Stones or The Who, past or present", ["Mick Jagger", "Keith Richards", "Charlie Watts", "Ronnie Wood", "Bill Wyman", "Brian Jones", "Mick Taylor", "Ian Stewart", "Roger Daltrey", "Pete Townshend", "John Entwistle", "Keith Moon", "Kenney Jones"]),
 ("Name one of the Bee Gees or the Jackson 5", ["Barry Gibb", "Robin Gibb", "Maurice Gibb", "Jackie Jackson", "Tito Jackson", "Jermaine Jackson", "Marlon Jackson", "Michael Jackson", "Randy Jackson"]),
 ("Name a member of Busted, McFly or S Club 7", ["James Bourne", "Matt Willis", "Charlie Simpson", "Tom Fletcher", "Danny Jones", "Dougie Poynter", "Harry Judd", "Tina Barrett", "Paul Cattermole", "Jon Lee", "Bradley McIntosh", "Jo O'Meara", "Hannah Spearritt", "Rachel Stevens"]),
 ("Name one of the March sisters in Little Women or the Bennet sisters in Pride and Prejudice", ["Meg", "Jo", "Beth", "Amy", "Jane", "Elizabeth/Lizzy", "Mary", "Kitty/Catherine", "Lydia"]),
 ("Name a Six Nations rugby team, or a country that has won the men's Rugby World Cup", ["England", "Scotland", "Wales", "Ireland", "France", "Italy", "New Zealand", "Australia", "South Africa"]),
 ("Name a tennis Grand Slam tournament or one of golf's men's majors", ["Australian Open", "French Open/Roland Garros", "Wimbledon", "US Open", "The Masters/Masters", "PGA Championship/US PGA", "The Open/Open Championship/British Open"]),
 ("Name one of Henry VIII's six wives", ["Catherine of Aragon", "Anne Boleyn", "Jane Seymour", "Anne of Cleves", "Catherine Howard", "Catherine Parr"]),
 ("Name a Nordic country or its capital city", ["Denmark", "Norway", "Sweden", "Finland", "Iceland", "Copenhagen", "Oslo", "Stockholm", "Helsinki", "Reykjavík/Reykjavik"]),
 ("Name one of the Great Lakes of North America or one of New York City's five boroughs", ["Superior", "Michigan", "Huron", "Erie", "Ontario", "Manhattan", "Brooklyn", "Queens", "The Bronx/Bronx", "Staten Island"]),
 ("Name a UK city that has hosted the Summer Olympics or the Commonwealth Games", ["London", "Cardiff", "Edinburgh", "Manchester", "Glasgow", "Birmingham"]),
 ("Name a woodwind or brass instrument", ["Flute", "Piccolo", "Oboe", "Cor anglais/English horn", "Clarinet", "Bass clarinet", "Bassoon", "Contrabassoon/Double bassoon", "Saxophone/Sax", "Recorder", "Trumpet", "Cornet", "Flugelhorn", "Bugle", "French horn/Horn", "Trombone", "Euphonium", "Tuba", "Sousaphone"]),
 ("Name a member of the team in the first Avengers film (2012), or its villain", ["Iron Man/Tony Stark", "Captain America/Steve Rogers", "Thor", "Hulk/Bruce Banner", "Black Widow/Natasha Romanoff", "Hawkeye/Clint Barton", "Nick Fury", "Loki"]),
 ("Name one of the Seven Deadly Sins", ["Pride", "Greed/Avarice", "Lust", "Envy", "Gluttony", "Wrath/Anger", "Sloth"]),
 ("Name a character from Fawlty Towers", ["Basil Fawlty/Basil", "Sybil Fawlty/Sybil", "Polly", "Manuel", "Major Gowen/The Major", "Miss Tibbs", "Miss Gatsby", "Terry"]),
 ("Name a character from The Vicar of Dibley", ["Geraldine Granger/Geraldine", "Alice Tinker/Alice", "Hugo Horton/Hugo", "David Horton/David", "Owen Newitt/Owen", "Jim Trott/Jim", "Frank Pickle/Frank", "Letitia Cropley/Letitia"]),
 ("Name a member of the Addams Family", ["Gomez", "Morticia", "Wednesday", "Pugsley", "Uncle Fester/Fester", "Grandmama/Granny", "Lurch", "Thing", "Cousin Itt/Itt"]),
 ("Name a member of Mystery Inc. in Scooby-Doo", ["Scooby-Doo/Scooby", "Shaggy", "Fred", "Daphne", "Velma", "Scrappy-Doo/Scrappy"]),
 ("Name one of the Flintstones or the Rubbles", ["Fred Flintstone", "Wilma Flintstone/Wilma", "Pebbles", "Dino", "Barney Rubble/Barney", "Betty Rubble/Betty", "Bamm-Bamm"]),
 ("Name one of the Premier League's so-called 'Big Six' clubs", ["Manchester United/Man Utd/Man United", "Manchester City/Man City", "Liverpool", "Arsenal", "Chelsea", "Tottenham Hotspur/Tottenham/Spurs"]),
 ("Name a Kardashian, a Jenner or an Osbourne", ["Kourtney Kardashian/Kourtney", "Kim Kardashian/Kim", "Khloé Kardashian/Khloe Kardashian/Khloe", "Rob Kardashian", "Kris Jenner/Kris", "Kendall Jenner/Kendall", "Kylie Jenner/Kylie", "Caitlyn Jenner/Caitlyn", "Ozzy Osbourne/Ozzy", "Sharon Osbourne/Sharon", "Kelly Osbourne/Kelly", "Jack Osbourne/Jack", "Aimee Osbourne/Aimee"]),
 ("Name one of the Three Musketeers (or d'Artagnan), or one of the Marx Brothers", ["Athos", "Porthos", "Aramis", "D'Artagnan/Dartagnan", "Groucho", "Harpo", "Chico", "Zeppo", "Gummo"]),
 ("Name one of the first five books of the Bible or one of the four Gospels", ["Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy", "Matthew", "Mark", "Luke", "John"]),
 ("Name a letter used in Roman numerals", ["I", "V", "X", "L", "C", "D", "M"]),
 ("Name a type of triangle, or a shape with five to ten sides", ["Equilateral", "Isosceles", "Scalene", "Right-angled/Right angle/Right-angle", "Acute", "Obtuse", "Pentagon", "Hexagon", "Heptagon/Septagon", "Octagon", "Nonagon/Enneagon", "Decagon"]),
 ("Name a presenter or judge of The Great British Bake Off", ["Mel Giedroyc/Mel", "Sue Perkins/Sue", "Sandi Toksvig/Sandi", "Noel Fielding/Noel", "Matt Lucas/Matt", "Alison Hammond/Alison", "Mary Berry", "Paul Hollywood", "Prue Leith/Prue"]),
 ("Name one of the five senses or one of the four seasons", ["Sight/Seeing", "Hearing", "Smell/Smelling", "Taste/Tasting", "Touch", "Spring", "Summer", "Autumn/Fall", "Winter"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
