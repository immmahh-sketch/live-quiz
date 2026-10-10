# Bank session 10 Oct 2026 (sixth pass): 2 more Match questions for 14 more topics that had 5 live.
# Writes bank/topics/<slug>__m7.json; import each with FILE=<slug>__m7 TOPICS=<slug> LQ_PASSWORD=… node tools/import-bank.mjs topics
import json, os
OUT = {}
def m(slug, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.setdefault(slug, []).append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff})


m("20th-century", "medium", "Match each Prime Minister to something from their time in office",
  ("Clement Attlee", "The NHS is founded"), ("Margaret Thatcher", "The Falklands War"), ("Neville Chamberlain", "'Peace for our time' at Munich"), ("Harold Wilson", "England win the World Cup"))
m("20th-century", "medium", "Match each invention to the decade it arrived",
  ("Television", "1920s"), ("Jet engine", "1930s"), ("Microwave oven", "1940s"), ("World Wide Web", "1980s"))

m("mythology", "medium", "Match each Norse god to their role",
  ("Odin", "King of the gods"), ("Loki", "The trickster"), ("Freya", "Goddess of love and beauty"), ("Heimdall", "Guard of the rainbow bridge"))
m("mythology", "hard", "Match each Egyptian god to the head they're shown with",
  ("Anubis", "A jackal"), ("Horus", "A falcon"), ("Thoth", "An ibis"), ("Sobek", "A crocodile"))

m("landmarks", "medium", "Match each landmark to its architect",
  ("St Paul's Cathedral", "Christopher Wren"), ("Sagrada Família", "Antoni Gaudí"), ("Sydney Opera House", "Jørn Utzon"), ("The Shard", "Renzo Piano"))
m("landmarks", "medium", "Match each statue to its city",
  ("Christ the Redeemer", "Rio de Janeiro"), ("The Little Mermaid", "Copenhagen"), ("Manneken Pis", "Brussels"), ("The Motherland Calls", "Volgograd"))

m("disney", "easy", "Match each villain to their film",
  ("Jafar", "Aladdin"), ("Ursula", "The Little Mermaid"), ("Scar", "The Lion King"), ("Mother Gothel", "Tangled"))
m("disney", "easy", "Match each song to its film",
  ("Let It Go", "Frozen"), ("How Far I'll Go", "Moana"), ("Be Our Guest", "Beauty and the Beast"), ("I Just Can't Wait to Be King", "The Lion King"))

m("the-1960s", "medium", "Match each 1960s number one to its act",
  ("She Loves You", "The Beatles"), ("Pretty Flamingo", "Manfred Mann"), ("You Really Got Me", "The Kinks"), ("Puppet on a String", "Sandie Shaw"))
m("the-1960s", "medium", "Match each 1960s icon to what made them famous",
  ("Twiggy", "Modelling"), ("Mary Quant", "The miniskirt"), ("Vidal Sassoon", "The bob haircut"), ("David Bailey", "Photography"))

m("the-1970s", "easy", "Match each 1970s TV show to its catchphrase",
  ("Some Mothers Do 'Ave 'Em", "Ooh, Betty!"), ("Are You Being Served?", "I'm free!"), ("The Generation Game", "Nice to see you, to see you nice!"), ("Fawlty Towers", "Don't mention the war!"))
m("the-1970s", "medium", "Match each 1970s moment to its year",
  ("Decimal Day", "1971"), ("The three-day week", "1974"), ("The Queen's Silver Jubilee", "1977"), ("Margaret Thatcher becomes Prime Minister", "1979"))

m("video-games", "easy", "Match each console to its maker",
  ("PlayStation", "Sony"), ("Xbox", "Microsoft"), ("Switch", "Nintendo"), ("Mega Drive", "Sega"))
m("video-games", "medium", "Match each game to the year it came out",
  ("Pong", "1972"), ("Pac-Man", "1980"), ("Tetris", "1984"), ("Minecraft", "2011"))

m("marvel", "easy", "Match each hero to the actor who played them in the Marvel films",
  ("Black Widow", "Scarlett Johansson"), ("Hawkeye", "Jeremy Renner"), ("Doctor Strange", "Benedict Cumberbatch"), ("Ant-Man", "Paul Rudd"))
m("marvel", "easy", "Match each hero to their real name",
  ("Iron Man", "Tony Stark"), ("Captain America", "Steve Rogers"), ("Black Panther", "T'Challa"), ("The Hulk", "Bruce Banner"))

m("world-cup", "medium", "Match each host to the year of its World Cup",
  ("South Africa", "2010"), ("Qatar", "2022"), ("Japan and South Korea", "2002"), ("Russia", "2018"))
m("world-cup", "easy", "Match each player to his famous World Cup moment",
  ("Diego Maradona", "The Hand of God"), ("Geoff Hurst", "A hat-trick in the final"), ("Zinedine Zidane", "A headbutt in the 2006 final"), ("Paul Gascoigne", "Tears in the 1990 semi-final"))

m("horror-films", "easy", "Match each killer to their weapon",
  ("Freddy Krueger", "A bladed glove"), ("Leatherface", "A chainsaw"), ("Michael Myers", "A kitchen knife"), ("Jason Voorhees", "A machete"))
m("horror-films", "medium", "Match each horror film to its director",
  ("Psycho", "Alfred Hitchcock"), ("The Shining", "Stanley Kubrick"), ("Halloween", "John Carpenter"), ("Get Out", "Jordan Peele"))

m("motorsport", "medium", "Match each race to what races in it",
  ("Isle of Man TT", "Motorbikes"), ("NASCAR", "Stock cars"), ("Le Mans 24 Hours", "Sports cars"), ("Dakar Rally", "Off-road trucks, cars and bikes"))
m("motorsport", "medium", "Match each British F1 champion to the year of his first title",
  ("Nigel Mansell", "1992"), ("Damon Hill", "1996"), ("Lewis Hamilton", "2008"), ("Jenson Button", "2009"))

m("games-toys", "easy", "Match each board game to how you win it",
  ("Cluedo", "Solve the murder"), ("Risk", "Conquer the world"), ("Monopoly", "Bankrupt everyone else"), ("Scrabble", "Score the most with your words"))
m("games-toys", "medium", "Match each toy to the country it comes from",
  ("LEGO", "Denmark"), ("Rubik's Cube", "Hungary"), ("Barbie", "USA"), ("Tamagotchi", "Japan"))

m("flags", "hard", "Match each country to the creature on its flag",
  ("Wales", "A dragon"), ("Sri Lanka", "A lion holding a sword"), ("Uganda", "A crane"), ("Papua New Guinea", "A bird of paradise"))
m("flags", "medium", "Match each country to the shape on its flag",
  ("Japan", "A red circle"), ("Nepal", "Two stacked triangles"), ("Israel", "A Star of David"), ("Switzerland", "A white cross"))

m("usa", "medium", "Match each state to its capital",
  ("California", "Sacramento"), ("New York", "Albany"), ("Texas", "Austin"), ("Florida", "Tallahassee"))
m("usa", "easy", "Match each landmark to its state",
  ("Mount Rushmore", "South Dakota"), ("The Grand Canyon", "Arizona"), ("The Golden Gate Bridge", "California"), ("Graceland", "Tennessee"))

here = os.path.dirname(os.path.abspath(__file__))
for slug, items in OUT.items():
    json.dump(items, open(os.path.join(here, '..', 'topics', slug + '__m7.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(sum(map(len, OUT.values())), 'matches in', len(OUT), 'topics:', ' '.join(OUT))
