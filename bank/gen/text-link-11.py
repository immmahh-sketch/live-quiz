# Bank session 19 Oct 2026: eleventh batch of "word connections" questions (user's target: 500 in all; see text-link-1.py and the
# live-quiz-word-links memory): two words are shown and the player types the one word that goes between them to make two new words or
# phrases. Stored as Type-the-answer questions in bank/text-link-11.json; import with: CHUNK=10 node tools/import-bank.mjs text
# Every link was checked both ways, and every first answer is new (none used by batches 1-10). Themes: the body, the home, clothes,
# music, places, money and sport, all two-word phrase chains (black eye / eye test, village green / green belt). A second answer is
# accepted where one is genuine (gold RECORD / record player and gold DISC / disc player).
# Wording: two new short forms (Lucky link / Bind the pair), alternating so two questions that share a right-hand word never share one.
import json, os
OUT = []
FORMS = ["Lucky link: {l} ___ {r}", "Bind the pair: {l} ___ {r}"]
used = {}
n = [0]
def link(left, answers, right, diff):
    assert all(a.isalpha() for a in answers), answers
    k = n[0] % 2
    if used.get(right.lower()) == k: k = 1 - k
    used[right.lower()] = k; n[0] += 1
    OUT.append({"type": "text", "text": FORMS[k].format(l=left.upper(), r=right.upper()), "answers": answers, "category": "Wordplay",
                "tags": ["word links", "wordplay"], "difficulty": diff})

link("Black", ["Eye"], "Test", "easy")                          # black eye / eye test
link("Runny", ["Nose"], "Bleed", "easy")                         # runny nose / nosebleed
link("Big", ["Mouth"], "Wash", "easy")                           # big mouth / mouthwash
link("Mother", ["Tongue"], "Twister", "easy")                    # mother tongue / tongue twister
link("Double", ["Chin"], "Up", "easy")                           # double chin / chin up
link("Cold", ["Shoulder"], "Bag", "easy")                        # cold shoulder / shoulder bag
link("Little", ["Finger"], "Food", "easy")                       # little finger / finger food
link("Bird", ["Brain"], "Storm", "easy")                         # bird brain / brainstorm
link("Cold", ["Blood"], "Bank", "easy")                          # cold blood / blood bank
link("Long", ["Hair"], "Band", "easy")                           # long hair / hairband
link("Kitchen", ["Sink"], "Hole", "medium")                      # kitchen sink / sinkhole
link("Public", ["Toilet"], "Paper", "easy")                      # public toilet / toilet paper
link("Corner", ["Sofa"], "Bed", "easy")                          # corner sofa / sofa bed
link("Lava", ["Lamp"], "Shade", "easy")                          # lava lamp / lampshade
link("Scented", ["Candle"], "Light", "easy")                     # scented candle / candlelight
link("Wing", ["Mirror"], "Image", "medium")                      # wing mirror / mirror image
link("Sun", ["Roof"], "Rack", "easy")                            # sunroof / roof rack
link("Dairy", ["Farm"], "Yard", "easy")                          # dairy farm / farmyard
link("Wind", ["Sock"], "Puppet", "easy")                         # windsock / sock puppet
link("Straw", ["Hat"], "Trick", "easy")                          # straw hat / hat trick
link("Flat", ["Cap"], "Gun", "easy")                             # flat cap / cap gun
link("Black", ["Belt"], "Buckle", "easy")                        # black belt / belt buckle
link("Belly", ["Button"], "Hole", "easy")                        # belly button / buttonhole
link("Blue", ["Collar"], "Bone", "easy")                         # blue collar / collarbone
link("Drum", ["Kit"], "Bag", "easy")                             # drum kit / kitbag
link("Lead", ["Singer"], "Songwriter", "easy")                   # lead singer / singer-songwriter
link("Gold", ["Record", "Disc"], "Player", "easy")               # gold record / record player; gold disc / disc player
link("Singles", ["Chart"], "Show", "easy")                       # singles chart / chart show
link("Grand", ["Piano"], "Stool", "easy")                        # grand piano / piano stool
link("Inner", ["City"], "Hall", "easy")                          # inner city / city hall
link("Home", ["Town"], "Hall", "easy")                           # home town / town hall
link("Olympic", ["Village"], "Green", "easy")                    # Olympic village / village green
link("Village", ["Green"], "Belt", "easy")                       # village green / green belt
link("Cross", ["Country"], "Music", "medium")                    # cross-country / country music
link("High", ["Street"], "Food", "easy")                         # high street / street food
link("Pebble", ["Beach"], "Ball", "easy")                        # Pebble Beach / beach ball
link("Desert", ["Island"], "Hopping", "easy")                    # desert island / island hopping
link("Concrete", ["Jungle"], "Book", "easy")                     # concrete jungle / The Jungle Book
link("Rain", ["Forest"], "Fire", "easy")                         # rainforest / forest fire
link("Rocky", ["Mountain"], "Bike", "easy")                      # Rocky Mountain / mountain bike
link("Gold", ["Coin"], "Toss", "easy")                           # gold coin / coin toss
link("Hard", ["Cash"], "Machine", "easy")                        # hard cash / cash machine
link("Phone", ["Bill"], "Board", "medium")                       # phone bill / billboard
link("Income", ["Tax"], "Haven", "medium")                       # income tax / tax haven
link("Tax", ["Credit"], "Card", "easy")                          # tax credit / credit card
link("Crazy", ["Golf"], "Club", "easy")                          # crazy golf / golf club
link("Football", ["Pitch"], "Invasion", "easy")                  # football pitch / pitch invasion
link("Own", ["Goal"], "Kick", "easy")                            # own goal / goal kick
link("London", ["Marathon"], "Runner", "easy")                   # London Marathon / marathon runner
link("Gold", ["Medal"], "Table", "easy")                         # gold medal / medal table
link("Premier", ["League"], "Table", "easy")                     # Premier League / league table
link("Junior", ["Doctor"], "Who", "easy")                        # junior doctor / Doctor Who
link("Teaching", ["Staff"], "Room", "easy")                      # teaching staff / staff room

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'text-link-11.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'word-link questions written')
