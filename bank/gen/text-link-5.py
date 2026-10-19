# Bank session 19 Oct 2026: fifth batch of "word connections" questions (user's target: 500 in all; see text-link-1.py and the
# live-quiz-word-links memory): two words are shown and the player types the one word that goes between them to make two new words or
# phrases. Stored as Type-the-answer questions in bank/text-link-5.json; import with: node tools/import-bank.mjs text
# Every link was checked both ways and every genuine alternative is accepted (hot KEY / keyboard and hot SPRING / springboard; fire
# WALL / wallpaper and fire FLY / flypaper). Every first answer is new (none used by batches 1-4).
# Wording: two new short forms (Bridge the gap / Join the dots), alternating so two questions that share a right-hand word never
# share a wording.
import json, os
OUT = []
FORMS = ["Bridge the gap: {l} ___ {r}", "Join the dots: {l} ___ {r}"]
used = {}
n = [0]
def link(left, answers, right, diff):
    assert all(a.isalpha() for a in answers), answers
    k = n[0] % 2
    if used.get(right.lower()) == k: k = 1 - k
    used[right.lower()] = k; n[0] += 1
    OUT.append({"type": "text", "text": FORMS[k].format(l=left.upper(), r=right.upper()), "answers": answers, "category": "Wordplay",
                "tags": ["word links", "wordplay"], "difficulty": diff})

link("Arm", ["Band"], "Stand", "medium")                         # armband / bandstand
link("Crow", ["Bar"], "Code", "medium")                          # crowbar / barcode
link("Road", ["Block"], "Head", "medium")                        # roadblock / blockhead
link("Bed", ["Bug"], "Bear", "hard")                             # bedbug / bugbear
link("Wild", ["Cat"], "Walk", "medium")                          # wildcat / catwalk
link("Rain", ["Coat"], "Tail", "medium")                         # raincoat / coattail
link("Pea", ["Cock"], "Pit", "medium")                           # peacock / cockpit
link("Hard", ["Drive"], "Way", "medium")                         # hard drive / driveway
link("Rain", ["Drop"], "Out", "medium")                          # raindrop / dropout
link("Poker", ["Face"], "Paint", "medium")                       # poker face / face paint
link("Mine", ["Field"], "Day", "medium")                         # minefield / field day
link("Dance", ["Floor"], "Plan", "medium")                       # dancefloor / floor plan
link("Fair", ["Game"], "Plan", "medium")                         # fair game / game plan
link("Town", ["Hall"], "Way", "medium")                          # town hall / hallway
link("Mole", ["Hill"], "Side", "hard")                           # molehill / hillside
link("Black", ["Jack"], "Pot", "medium")                         # blackjack / jackpot
link("Traffic", ["Jam"], "Session", "medium")                    # traffic jam / jam session
link("Hot", ["Key", "Spring"], "Board", "medium")                # hotkey / keyboard; hot spring / springboard
link("Side", ["Kick"], "Boxing", "medium")                       # sidekick / kickboxing
link("Pen", ["Knife"], "Edge", "medium")                         # penknife / knife edge
link("Bow", ["Leg"], "Room", "hard")                             # bow-leg / legroom
link("Night", ["Life"], "Boat", "medium")                        # nightlife / lifeboat
link("Dead", ["Lock"], "Smith", "medium")                        # deadlock / locksmith
link("Butter", ["Milk"], "Maid", "medium")                       # buttermilk / milkmaid
link("Back", ["Pack"], "Horse", "medium")                        # backpack / packhorse
link("Key", ["Pad"], "Lock", "medium")                           # keypad / padlock
link("Sauce", ["Pan"], "Cake", "easy")                           # saucepan / pancake
link("Over", ["Pass"], "Word", "medium")                         # overpass / password
link("Apple", ["Pie"], "Chart", "medium")                        # apple pie / pie chart
link("Hair", ["Pin"], "Ball", "medium")                          # hairpin / pinball
link("Horse", ["Race"], "Track", "medium")                       # horse race / racetrack
link("Hand", ["Rail"], "Road", "medium")                         # handrail / railroad
link("Ear", ["Ring"], "Leader", "medium")                        # earring / ringleader
link("Bed", ["Rock"], "Pool", "medium")                          # bedrock / rock pool
link("Grass", ["Root"], "Beer", "hard")                          # grassroots / root beer
link("Quick", ["Sand"], "Stone", "medium")                       # quicksand / sandstone
link("Car", ["Seat"], "Belt", "medium")                          # car seat / seatbelt
link("Bed", ["Sheet"], "Music", "medium")                        # bedsheet / sheet music
link("Sweat", ["Shirt"], "Tail", "medium")                       # sweatshirt / shirttail
link("Road", ["Show"], "Case", "medium")                         # roadshow / showcase
link("Star", ["Sign"], "Post", "medium")                         # star sign / signpost
link("Baby", ["Sit"], "Com", "medium")                           # babysit / sitcom
link("Sheep", ["Skin"], "Head", "medium")                        # sheepskin / skinhead
link("Cow", ["Slip"], "Knot", "hard")                            # cowslip / slip knot
link("Air", ["Space"], "Craft", "medium")                        # airspace / spacecraft
link("Sun", ["Spot"], "Light", "easy")                           # sunspot / spotlight
link("Pig", ["Tail"], "Gate", "medium")                          # pigtail / tailgate
link("Over", ["Take"], "Away", "medium")                         # overtake / takeaway
link("Small", ["Talk"], "Show", "medium")                        # small talk / talk show
link("Fish", ["Tank"], "Top", "medium")                          # fish tank / tank top
link("Red", ["Tape"], "Worm", "medium")                          # red tape / tapeworm
link("Rip", ["Tide"], "Table", "hard")                           # riptide / tide table
link("Big", ["Toe"], "Nail", "easy")                             # big toe / toenail
link("Fast", ["Track"], "Suit", "medium")                        # fast track / tracksuit
link("Steam", ["Train"], "Spotter", "medium")                    # steam train / trainspotter
link("Apple", ["Tree"], "House", "easy")                         # apple tree / treehouse
link("Day", ["Trip"], "Wire", "medium")                          # day trip / tripwire
link("Inner", ["Tube"], "Station", "easy")                       # inner tube / tube station
link("Down", ["Turn"], "Table", "medium")                        # downturn / turntable
link("Fire", ["Wall", "Fly"], "Paper", "medium")                 # firewall / wallpaper; firefly / flypaper
link("Wrist", ["Watch"], "Dog", "medium")                        # wristwatch / watchdog
link("Bat", ["Wing"], "Span", "hard")                            # bat wing / wingspan
link("Hot", ["Wire"], "Less", "medium")                          # hotwire / wireless

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'text-link-5.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'word-link questions written')
