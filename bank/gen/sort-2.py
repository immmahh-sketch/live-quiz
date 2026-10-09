# Bank session 9 Oct 2026: more Categorise (sort) questions for the real topics with 4 or fewer unused in the live
# bank (3 each for DC and Marvel, which had 3; 2 each for the rest). Writes bank/topics/<slug>__s2.json; import with
#   FILE=<slug>__s2 TOPICS=<slug> LQ_PASSWORD=… node tools/import-bank.mjs topics
import json, os
OUT = {}
def s(slug, diff, text, a, b, A, B):
    assert len(A) >= 2 and len(B) >= 2 and 6 <= len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.setdefault(slug, []).append({"type": "sort", "text": text, "categories": [a, b],
        "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B], "difficulty": diff})

s("dc-batman", "medium", "Secret identity: DC hero or Marvel hero?", "DC", "Marvel",
  ["Bruce Wayne", "Clark Kent", "Diana Prince", "Barry Allen"], ["Peter Parker", "Tony Stark", "Steve Rogers", "Bruce Banner"])
s("dc-batman", "medium", "Played Batman or played Superman on film?", "Batman", "Superman",
  ["Michael Keaton", "Christian Bale", "Robert Pattinson", "George Clooney"], ["Christopher Reeve", "Henry Cavill", "Brandon Routh", "David Corenswet"])
s("dc-batman", "easy", "Batman's ally or Batman's enemy?", "Ally", "Enemy",
  ["Robin", "Alfred", "Commissioner Gordon", "Batgirl"], ["The Joker", "The Penguin", "The Riddler", "Bane"])

s("marvel", "easy", "Hero or villain in the Marvel films?", "Hero", "Villain",
  ["Black Panther", "Doctor Strange", "Ant-Man", "Captain Marvel"], ["Thanos", "Ultron", "Red Skull", "Killmonger"])
s("marvel", "medium", "In the Marvel films, played by a Chris or not?", "Played by a Chris", "Not a Chris",
  ["Captain America", "Thor", "Star-Lord"], ["Iron Man", "Hulk", "Black Widow"])
s("marvel", "easy", "Guardians of the Galaxy or Fantastic Four?", "Guardians of the Galaxy", "Fantastic Four",
  ["Groot", "Rocket", "Gamora", "Drax"], ["Mister Fantastic", "The Thing", "Human Torch", "Invisible Woman"])

s("anagrams-wordplay", "medium", "An anagram of LISTEN, or not?", "Anagram of LISTEN", "Not an anagram",
  ["Silent", "Enlist", "Tinsel", "Inlets"], ["Lentils", "Listed", "Tonsil", "Stolen"])
s("anagrams-wordplay", "easy", "Reads the same backwards, or not?", "Palindrome", "Not a palindrome",
  ["Kayak", "Refer", "Madam", "Rotor"], ["Radio", "Kebab", "Llama", "Rotten"])

s("animals", "medium", "Mammal or not a mammal?", "Mammal", "Not a mammal",
  ["Whale", "Bat", "Platypus", "Dolphin"], ["Penguin", "Shark", "Crocodile", "Ostrich"])
s("animals", "medium", "Lays eggs or gives birth to live young?", "Lays eggs", "Live young",
  ["Chicken", "Turtle", "Salmon", "Echidna"], ["Horse", "Kangaroo", "Rabbit", "Whale"])

s("bonfire-night", "medium", "An autumn date or a winter date?", "Autumn", "Winter",
  ["Halloween", "Bonfire Night", "Harvest festival", "Remembrance Sunday"], ["Christmas Day", "Burns Night", "Hogmanay", "Valentine's Day"])
s("bonfire-night", "easy", "A firework, or something else from Bonfire Night?", "Firework", "Something else",
  ["Catherine wheel", "Rocket", "Roman candle", "Sparkler"], ["Toffee apple", "Parkin", "The guy", "Bonfire"])

s("boy-bands-girl-groups", "easy", "In Take That or in One Direction?", "Take That", "One Direction",
  ["Gary Barlow", "Mark Owen", "Howard Donald", "Jason Orange"], ["Niall Horan", "Louis Tomlinson", "Liam Payne", "Zayn Malik"])
s("boy-bands-girl-groups", "easy", "A Spice Girl or in Girls Aloud?", "Spice Girls", "Girls Aloud",
  ["Geri Halliwell", "Emma Bunton", "Mel B", "Mel C"], ["Cheryl", "Nadine Coyle", "Sarah Harding", "Kimberley Walsh"])

s("christmas-tv", "medium", "A BBC Christmas favourite or an ITV one?", "BBC", "ITV",
  ["Strictly Come Dancing", "Call the Midwife", "Gavin & Stacey", "The Royle Family"], ["I'm a Celebrity... Get Me Out of Here!", "Coronation Street", "Emmerdale", "Downton Abbey"])
s("christmas-tv", "easy", "Christmas telly: animated or live action?", "Animated", "Live action",
  ["The Snowman", "The Gruffalo", "Stick Man", "Shrek the Halls"], ["Elf", "Love Actually", "Home Alone", "The Holiday"])

s("connections", "medium", "One of the Seven Wonders of the Ancient World, or not?", "Ancient Wonder", "Not one",
  ["Great Pyramid of Giza", "Hanging Gardens of Babylon", "Colossus of Rhodes", "Lighthouse of Alexandria"], ["Stonehenge", "Taj Mahal", "Great Wall of China", "Colosseum"])
s("connections", "easy", "Monopoly square or Cluedo room?", "Monopoly", "Cluedo",
  ["Mayfair", "Park Lane", "Old Kent Road", "Pall Mall"], ["Ballroom", "Conservatory", "Library", "Kitchen"])

s("halloween-music", "medium", "Michael Jackson or Ozzy Osbourne?", "Michael Jackson", "Ozzy Osbourne",
  ["Thriller", "Billie Jean", "Bad", "Beat It"], ["Crazy Train", "Mr Crowley", "Bark at the Moon", "No More Tears"])
s("halloween-music", "medium", "Spooky song from the 1980s or the 1990s?", "1980s", "1990s",
  ["Thriller", "Ghostbusters", "Somebody's Watching Me", "Dead Man's Party"], ["Zombie", "Dragula", "Everybody (Backstreet's Back)", "This Is Halloween"])

s("nature-environment", "easy", "Found wild in Britain, or only abroad?", "Wild in Britain", "Only abroad",
  ["Red squirrel", "Otter", "Badger", "Hedgehog"], ["Raccoon", "Skunk", "Chipmunk", "Porcupine"])
s("nature-environment", "hard", "Native British tree or brought in from abroad?", "Native", "Introduced",
  ["Oak", "Ash", "Silver birch", "Rowan"], ["Sycamore", "Horse chestnut", "Eucalyptus", "Monkey puzzle"])

s("newcastle-v-sunderland", "medium", "In Newcastle or in Sunderland?", "Newcastle", "Sunderland",
  ["Grey's Monument", "Bigg Market", "Jesmond Dene", "Grainger Market"], ["Penshaw Monument", "Roker Pier", "Seaburn", "Hylton Castle"])
s("newcastle-v-sunderland", "hard", "An FA Cup won by Newcastle or by Sunderland?", "Newcastle", "Sunderland",
  ["1910", "1924", "1951", "1955"], ["1937", "1973"])
s("no-such-thing-as-a-fish", "hard", "Botanically a true nut, or not?", "True nut", "Not a true nut",
  ["Hazelnut", "Chestnut", "Acorn", "Beech nut"], ["Peanut", "Almond", "Cashew", "Brazil nut"])
s("no-such-thing-as-a-fish", "medium", "Everyday thing named after a real person, or not?", "Named after someone", "Not named after anyone",
  ["Sandwich", "Cardigan", "Wellington boot", "Leotard"], ["Biscuit", "Umbrella", "Jumper", "Trousers"])

s("religion-festivals", "easy", "Christian festival or Jewish festival?", "Christian", "Jewish",
  ["Easter", "Advent", "Pentecost", "Lent"], ["Passover", "Hanukkah", "Yom Kippur", "Rosh Hashanah"])
s("religion-festivals", "medium", "A book of the Old Testament or the New Testament?", "Old Testament", "New Testament",
  ["Genesis", "Exodus", "Psalms", "Isaiah"], ["Matthew", "Acts", "Romans", "Revelation"])

s("the-beatles", "easy", "A Beatles song or a Rolling Stones song?", "Beatles", "Rolling Stones",
  ["Let It Be", "Yesterday", "Come Together", "Help!"], ["Satisfaction", "Paint It Black", "Angie", "Brown Sugar"])
s("the-beatles", "medium", "On Sgt. Pepper or on Abbey Road?", "Sgt. Pepper", "Abbey Road",
  ["Lucy in the Sky with Diamonds", "With a Little Help from My Friends", "When I'm Sixty-Four", "A Day in the Life"], ["Something", "Here Comes the Sun", "Octopus's Garden", "Golden Slumbers"])

here = os.path.dirname(os.path.abspath(__file__))
for slug, items in OUT.items():
    json.dump(items, open(os.path.join(here, '..', 'topics', slug + '__s2.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(sum(map(len, OUT.values())), 'sorts in', len(OUT), 'topics:', ' '.join(OUT))
