# Bank session 10 Oct 2026 (seventh pass): 2 more Match questions for 14 more topics that had 5 live. A currency, a
# Christmas number one and a phobia match were swapped out: the live bank already had them.
# Writes bank/topics/<slug>__m8.json; import each with FILE=<slug>__m8 TOPICS=<slug> LQ_PASSWORD=… node tools/import-bank.mjs topics
import json, os
OUT = {}
def m(slug, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.setdefault(slug, []).append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff})


m("europe", "hard", "Match each country to the name of its parliament",
  ("Iceland", "Althing"), ("Norway", "Storting"), ("Germany", "Bundestag"), ("Ireland", "Dáil"))
m("europe", "medium", "Match each river to the capital city it flows through",
  ("Danube", "Budapest"), ("Vltava", "Prague"), ("Tagus", "Lisbon"), ("Liffey", "Dublin"))

m("famous-firsts", "medium", "Match each first to the country that did it",
  ("First to give women the vote", "New Zealand"), ("First to legalise same-sex marriage", "Netherlands"), ("First to put a person in space", "Soviet Union"), ("First to use paper money", "China"))
m("famous-firsts", "hard", "Match each British first to its decade",
  ("First motorway", "1950s"), ("First cash machine", "1960s"), ("First test-tube baby", "1970s"), ("First text message", "1990s"))

m("famous-people", "medium", "Match each explorer to what they're famous for",
  ("Marco Polo", "Travelling to China"), ("Vasco da Gama", "A sea route to India"), ("Ferdinand Magellan", "The first voyage round the world"), ("Roald Amundsen", "First to the South Pole"))
m("famous-people", "easy", "Match each queen to the land she ruled",
  ("Cleopatra", "Egypt"), ("Boudica", "The Iceni of Britain"), ("Marie Antoinette", "France"), ("Catherine the Great", "Russia"))

m("fashion", "medium", "Match each piece of clothing to the person it's named after",
  ("Cardigan", "The Earl of Cardigan"), ("Wellington boot", "The Duke of Wellington"), ("Leotard", "Jules Léotard, a French acrobat"), ("Bloomers", "Amelia Bloomer, an American campaigner"))
m("fashion", "easy", "Match each fabric to where it comes from",
  ("Silk", "Silkworms"), ("Wool", "Sheep"), ("Linen", "Flax"), ("Cashmere", "Goats"))

m("halloween", "medium", "Match each monster to the author who created it",
  ("Dracula", "Bram Stoker"), ("Frankenstein's monster", "Mary Shelley"), ("Mr Hyde", "Robert Louis Stevenson"), ("The Invisible Man", "H. G. Wells"))
m("halloween", "easy", "Match each witch to her story",
  ("The Wicked Witch of the West", "The Wizard of Oz"), ("The White Witch", "The Lion, the Witch and the Wardrobe"), ("The Grand High Witch", "The Witches"), ("Sabrina Spellman", "Sabrina the Teenage Witch"))

m("horse-racing", "medium", "Match each racecourse to its big race",
  ("Aintree", "The Grand National"), ("Epsom", "The Derby"), ("Cheltenham", "The Gold Cup"), ("Doncaster", "The St Leger"))
m("horse-racing", "easy", "Match each snooker player to his nickname",
  ("Ronnie O'Sullivan", "The Rocket"), ("Steve Davis", "The Nugget"), ("Jimmy White", "The Whirlwind"), ("Alex Higgins", "The Hurricane"))

m("maths-numbers", "medium", "Match each number word to its value",
  ("Dozen", "12"), ("Score", "20"), ("Gross", "144"), ("Googol", "10 to the power of 100"))
m("maths-numbers", "hard", "Match each Greek letter to what it usually stands for in maths and science",
  ("Pi", "Circumference divided by diameter"), ("Sigma", "Add them all up"), ("Delta", "A change in something"), ("Lambda", "Wavelength"))

m("nature-environment", "medium", "Match each tree to its fruit or seed",
  ("Oak", "Acorn"), ("Horse chestnut", "Conker"), ("Sycamore", "Spinning 'helicopter'"), ("Beech", "Beechnut"))
m("nature-environment", "medium", "Match each British animal to its home",
  ("Badger", "Sett"), ("Otter", "Holt"), ("Fox", "Earth"), ("Beaver", "Lodge"))

m("quiz-shows", "easy", "Match each famous line to its quiz show",
  ("I've started, so I'll finish", "Mastermind"), ("Is that your final answer?", "Who Wants to Be a Millionaire?"), ("You are the weakest link, goodbye", "The Weakest Link"), ("Your starter for ten", "University Challenge"))
m("quiz-shows", "easy", "Match each game show to its original host",
  ("Countdown", "Richard Whiteley"), ("Blockbusters", "Bob Holness"), ("Bullseye", "Jim Bowen"), ("Catchphrase", "Roy Walker"))

m("science-technology", "medium", "Match each unit to what it measures",
  ("Newton", "Force"), ("Joule", "Energy"), ("Watt", "Power"), ("Ohm", "Electrical resistance"))
m("science-technology", "medium", "Match each discovery to the scientist behind it",
  ("Penicillin", "Alexander Fleming"), ("Radium", "Marie Curie"), ("The expanding universe", "Edwin Hubble"), ("The X-ray photo that revealed DNA's shape", "Rosalind Franklin"))

m("theatre", "medium", "Match each musical to its composer",
  ("Cats", "Andrew Lloyd Webber"), ("Les Misérables", "Claude-Michel Schönberg"), ("Hamilton", "Lin-Manuel Miranda"), ("Matilda the Musical", "Tim Minchin"))
m("theatre", "easy", "Match each Shakespeare play to where it's set",
  ("Hamlet", "Denmark"), ("Othello", "Venice"), ("Romeo and Juliet", "Verona"), ("Macbeth", "Scotland"))

m("words-language", "medium", "Match each collective noun to its animals",
  ("A murder", "Crows"), ("A parliament", "Owls"), ("A pride", "Lions"), ("A murmuration", "Starlings"))
m("words-language", "medium", "Match each English word to the language it was borrowed from",
  ("Bungalow", "Hindi"), ("Ketchup", "Chinese"), ("Kindergarten", "German"), ("Safari", "Swahili"))

m("the-2010s", "easy", "Match each 2010s event to its year",
  ("William and Kate's wedding", "2011"), ("The London Olympics", "2012"), ("The Brexit referendum", "2016"), ("Harry and Meghan's wedding", "2018"))
m("the-2010s", "medium", "Match each app, gadget or game to the year it launched",
  ("iPad", "2010"), ("Snapchat", "2011"), ("Apple Watch", "2015"), ("Fortnite", "2017"))

m("number-ones", "hard", "Match each number one that a TV advert sent to the top to its act",
  ("Inside", "Stiltskin"), ("Flat Beat", "Mr Oizo"), ("I'd Like to Teach the World to Sing", "The New Seekers"), ("Stand by Me", "Ben E. King"))
m("number-ones", "medium", "Match each film to its number one theme song",
  ("Robin Hood: Prince of Thieves", "(Everything I Do) I Do It for You"), ("Four Weddings and a Funeral", "Love Is All Around"), ("Titanic", "My Heart Will Go On"), ("Ghost", "Unchained Melody"))
here = os.path.dirname(os.path.abspath(__file__))
for slug, items in OUT.items():
    json.dump(items, open(os.path.join(here, '..', 'topics', slug + '__m8.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(sum(map(len, OUT.values())), 'matches in', len(OUT), 'topics:', ' '.join(OUT))
