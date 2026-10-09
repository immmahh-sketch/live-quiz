# Bank session 9 Oct 2026 (second pass): 2 more Put in Order questions for 17 topics that had 4 live (signature
# topics left out). Items are listed in the right order; wording is specific so it can't clash with another topic's.
# Writes bank/topics/<slug>__o3.json; import each with FILE=<slug>__o3 TOPICS=<slug> LQ_PASSWORD=… node tools/import-bank.mjs topics
import json, os
OUT = {}
def o(slug, diff, text, *items):
    assert 4 <= len(items) <= 5 and len(set(items)) == len(items), text
    OUT.setdefault(slug, []).append({"type": "order", "text": text, "items": list(items), "difficulty": diff})

o("australia", "hard", "Put these Sydney landmarks in the order they opened, earliest first", "Sydney Harbour Bridge", "Sydney Opera House", "Sydney Tower", "Stadium Australia")
o("australia", "medium", "Put these Australian and New Zealand cities in order from west to east", "Perth", "Adelaide", "Melbourne", "Sydney", "Auckland")

o("british-history", "medium", "Put these battles on British soil in order, earliest first", "Hastings", "Bannockburn", "Bosworth", "Culloden")
o("british-history", "medium", "Put these Victorian and Edwardian moments in order, earliest first", "The Great Exhibition", "Darwin publishes On the Origin of Species", "Queen Victoria dies", "The Titanic sinks")

o("christmas", "hard", "Put these reindeer in the order they're named in 'A Visit from St. Nicholas', starting with Dasher", "Dasher", "Prancer", "Comet", "Cupid", "Blitzen")
o("christmas", "medium", "Put these royal Christmas broadcasts in order, earliest first", "George V's first radio message", "Elizabeth II's first Christmas message", "The first televised Christmas message", "Charles III's first Christmas message")

o("christmas-movies", "medium", "Put these animated Christmas films in order of release, earliest first", "The Polar Express", "Arthur Christmas", "The Grinch (2018)", "Klaus")
o("christmas-movies", "easy", "Put the Home Alone films in order of release, earliest first", "Home Alone", "Home Alone 2: Lost in New York", "Home Alone 3", "Home Sweet Home Alone")

o("christmas-music", "medium", "Put these Christmas number ones in order, from the 1970s on", "Merry Xmas Everybody (Slade)", "Mistletoe and Wine (Cliff Richard)", "2 Become 1 (Spice Girls)", "Hallelujah (Alexandra Burke)")
o("christmas-music", "medium", "Put these Christmas singles in order of release, starting in the 1980s", "Merry Christmas Everyone (Shakin' Stevens)", "Fairytale of New York", "All I Want for Christmas Is You", "Santa Tell Me (Ariana Grande)")

o("dc-batman", "medium", "Put these Batman films in order of release, earliest first", "Batman (1989)", "Batman Returns", "Batman Forever", "Batman Begins", "The Batman")
o("dc-batman", "medium", "Put these Superman films in order of release, earliest first", "Superman (1978)", "Superman II", "Superman Returns", "Man of Steel", "Superman (2025)")

o("easter-spring", "easy", "Put the days of Holy Week in order, starting with Palm Sunday", "Palm Sunday", "Maundy Thursday", "Good Friday", "Holy Saturday", "Easter Sunday")
o("easter-spring", "medium", "Put these Lent and Easter days in order, earliest first", "Shrove Tuesday", "Ash Wednesday", "Mothering Sunday", "Palm Sunday", "Easter Monday")

o("famous-firsts", "medium", "Put these firsts for women in order, earliest first", "First woman to take her seat as an MP", "First woman in space", "First woman to climb Everest", "First woman to be UK Prime Minister")
o("famous-firsts", "medium", "Put these medical firsts in order, earliest first", "Jenner's smallpox vaccine", "Ether used as an anaesthetic", "Fleming discovers penicillin", "First human heart transplant", "First test-tube baby")

o("maths-numbers", "medium", "Put these metric prefixes in order, smallest first", "Milli", "Centi", "Kilo", "Mega", "Giga")
o("maths-numbers", "medium", "Put these in order of value, smallest first", "√9", "π", "√16", "2³", "3²")

o("name-the-year", "medium", "Put these London landmarks in the order they opened, earliest first", "Tower Bridge", "The BT Tower", "The London Eye", "The Shard")
o("name-the-year", "medium", "Put these royal weddings of the last 80 years in order, earliest first", "Elizabeth and Philip", "Charles and Diana", "William and Kate", "Harry and Meghan")

o("newcastle-v-sunderland", "medium", "Put these Newcastle strikers in the order they joined the club, earliest first", "Malcolm Macdonald", "Kevin Keegan", "Andy Cole", "Alan Shearer", "Alexander Isak")
o("newcastle-v-sunderland", "medium", "Put these Sunderland strikers in the order they joined the club, earliest first", "Niall Quinn", "Kevin Phillips", "Darren Bent", "Jermain Defoe")

o("space", "easy", "Put these planets in order going outward from the Sun, starting with Mars", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
o("space", "medium", "Put these space milestones in order, earliest first", "Gagarin orbits the Earth", "Leonov makes the first spacewalk", "Apollo 8 orbits the Moon", "Apollo 11 lands on the Moon", "Apollo 17, the last Moon landing")

o("the-1960s", "medium", "Put these 1960s number ones in order, earliest first", "She Loves You", "(I Can't Get No) Satisfaction", "Hey Jude", "Sugar, Sugar")
o("the-1960s", "medium", "Put these 1960s moments in order, earliest first", "The Pill is offered on the NHS", "The Beatles release Love Me Do", "The Aberfan disaster", "Concorde's first flight")

o("the-1980s", "easy", "Put these 1980s number ones in order, earliest first", "Come On Eileen", "Relax", "Never Gonna Give You Up", "Ride on Time")
o("the-1980s", "medium", "Put these 1980s TV shows in order of their first episode, earliest first", "Only Fools and Horses", "Brookside", "EastEnders", "Red Dwarf")

o("the-2000s", "medium", "Put these 2000s number ones in order, earliest first", "Can't Get You Out of My Head", "Crazy (Gnarls Barkley)", "Bleeding Love", "Hallelujah (Alexandra Burke)")
o("the-2000s", "medium", "Put these 2000s gadgets in order of launch, earliest first", "iPod", "Xbox 360", "Wii", "iPhone", "Kindle")

o("the-2010s", "medium", "Put these 2010s chart-toppers in order, earliest first", "Wake Me Up (Avicii)", "Uptown Funk", "Despacito", "Shallow")
o("the-2010s", "medium", "Put these 2010s sporting moments in order, earliest first", "Mo Farah's double gold at London 2012", "Andy Murray's first Wimbledon title", "Leicester City win the Premier League", "England reach the World Cup semi-finals", "Ben Stokes's Headingley Ashes innings")

o("valentines", "medium", "Put these love songs from the 1970s to the 2010s in order of release", "Wonderful Tonight", "Careless Whisper", "I Will Always Love You (Whitney Houston)", "Perfect (Ed Sheeran)")
o("valentines", "medium", "Put these love stories in the order they were written, earliest first", "Romeo and Juliet", "Pride and Prejudice", "Jane Eyre", "Gone with the Wind")

here = os.path.dirname(os.path.abspath(__file__))
for slug, items in OUT.items():
    json.dump(items, open(os.path.join(here, '..', 'topics', slug + '__o3.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(sum(map(len, OUT.values())), 'orders in', len(OUT), 'topics:', ' '.join(OUT))
