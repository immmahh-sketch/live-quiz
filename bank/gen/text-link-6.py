# Bank session 19 Oct 2026: sixth batch of "word connections" questions (user's target: 500 in all; see text-link-1.py and the
# live-quiz-word-links memory): two words are shown and the player types the one word that goes between them to make two new words or
# phrases. Stored as Type-the-answer questions in bank/text-link-6.json; import with: node tools/import-bank.mjs text
# (re-run until it says added 0: a first run can wrongly skip many). Every link was checked both ways and every genuine alternative is
# accepted (arm PIT / pit stop and arm REST / rest stop). Every first answer is new (none used by batches 1-5).
# Wording: two new short forms (Twin links / Meet in the middle), alternating so two questions that share a right-hand word never
# share a wording.
import json, os
OUT = []
FORMS = ["Twin links: {l} ___ {r}", "Meet in the middle: {l} ___ {r}"]
used = {}
n = [0]
def link(left, answers, right, diff):
    assert all(a.isalpha() for a in answers), answers
    k = n[0] % 2
    if used.get(right.lower()) == k: k = 1 - k
    used[right.lower()] = k; n[0] += 1
    OUT.append({"type": "text", "text": FORMS[k].format(l=left.upper(), r=right.upper()), "answers": answers, "category": "Wordplay",
                "tags": ["word links", "wordplay"], "difficulty": diff})

link("Cook", ["Book"], "Case", "easy")                          # cookbook / bookcase
link("Book", ["Shelf"], "Life", "medium")                        # bookshelf / shelf life
link("Sea", ["Shore"], "Line", "medium")                         # seashore / shoreline
link("Spider", ["Web"], "Site", "easy")                          # spider web / website
link("Hair", ["Spray"], "Paint", "medium")                       # hairspray / spray paint
link("Shoe", ["String"], "Bean", "medium")                       # shoestring / string bean
link("Police", ["Station"], "Master", "medium")                  # police station / stationmaster
link("Short", ["Bread"], "Winner", "medium")                     # shortbread / breadwinner
link("Foot", ["Stool"], "Pigeon", "hard")                        # footstool / stool pigeon
link("Clock", ["Work"], "Force", "medium")                       # clockwork / workforce
link("Butter", ["Scotch"], "Egg", "hard")                        # butterscotch / scotch egg
link("Candle", ["Stick"], "Man", "medium")                       # candlestick / stickman
link("Hand", ["Cuff"], "Link", "medium")                         # handcuff / cufflink
link("Head", ["Stone"], "Age", "medium")                         # headstone / Stone Age
link("Sea", ["Horse"], "Power", "medium")                        # seahorse / horsepower
link("Steam", ["Roller"], "Coaster", "medium")                   # steamroller / roller coaster
link("Jelly", ["Bean"], "Bag", "medium")                         # jelly bean / beanbag
link("Hour", ["Glass"], "Eye", "hard")                           # hourglass / glass eye
link("Tooth", ["Pick"], "Pocket", "medium")                      # toothpick / pickpocket
link("Back", ["Fire"], "Arm", "hard")                            # backfire / firearm
link("Eye", ["Sight"], "Seeing", "medium")                       # eyesight / sightseeing
link("Under", ["Cover"], "Up", "medium")                         # undercover / cover-up
link("Shop", ["Lift"], "Off", "medium")                          # shoplift / lift-off
link("Sea", ["Sick"], "Bed", "hard")                             # seasick / sickbed
link("Copy", ["Right"], "Hand", "medium")                        # copyright / right hand
link("Paper", ["Weight"], "Lifter", "medium")                    # paperweight / weightlifter
link("Arm", ["Pit", "Rest"], "Stop", "medium")                   # armpit / pit stop; armrest / rest stop
link("Gate", ["Crash"], "Course", "medium")                      # gatecrash / crash course
link("Key", ["Hole"], "Punch", "medium")                         # keyhole / hole punch
link("Duck", ["Pond"], "Weed", "hard")                           # duck pond / pondweed
link("Wind", ["Pipe"], "Line", "medium")                         # windpipe / pipeline
link("Hat", ["Trick"], "Shot", "medium")                         # hat trick / trick shot
link("Cork", ["Screw"], "Driver", "medium")                      # corkscrew / screwdriver
link("Lamp", ["Post"], "Card", "medium")                         # lamppost / postcard
link("Pot", ["Belly"], "Dancer", "medium")                       # pot belly / belly dancer
link("Hair", ["Net"], "Work", "medium")                          # hairnet / network
link("Pen", ["Friend"], "Ship", "medium")                        # pen friend / friendship
link("Honey", ["Bee"], "Hive", "easy")                           # honeybee / beehive
link("Hand", ["Gun"], "Fire", "medium")                          # handgun / gunfire
link("Paper", ["Plane"], "Crash", "medium")                      # paper plane / plane crash
link("Jet", ["Stream"], "Line", "medium")                        # jet stream / streamline
link("Wind", ["Surf"], "Board", "medium")                        # windsurf / surfboard
link("Bat", ["Cave"], "Man", "easy")                             # batcave / caveman
link("Red", ["Cross"], "Word", "medium")                         # Red Cross / crossword
link("Rush", ["Hour"], "Glass", "medium")                        # rush hour / hourglass

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'text-link-6.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'word-link questions written')
