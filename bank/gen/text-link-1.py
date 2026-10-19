# Bank session 19 Oct 2026: the first batch of "word connections" questions (requested by the user: two words are shown and the player
# types the word that goes between them to make two new words or phrases, e.g. ALARM ___ TOWER -> Clock, for alarm clock and clock
# tower). Stored as Type-the-answer questions in bank/text-link-1.json; import with: node tools/import-bank.mjs text
# The question text is kept short on purpose: the server skips a question as a near-duplicate when most of its words match an old
# one, so a long shared instruction made nearly all of the first 39 look like repeats. Eleven that still clashed on a shared word
# (LIGHT, HOLE...) use one of three other short wordings (V1-V3). CROSS ___ PLAY stayed blocked (an earlier try with a longer wording was retired, and the
# server still counts it), so it was swapped for FOOT ___ BOOK. Every answer was checked both ways. Where a second word also works (alarm BELL / bell tower, foot BATH / bathroom) it is accepted
# too, so a fair answer is never marked wrong; the first answer in each list is the one the question was written around.
# Difficulty: easy = both links are everyday compounds; medium = one link is a less obvious compound; hard = a rarer second word.
import json, os
OUT = []
V1, V2, V3 = "Find the middle word: {l} ___ {r}", "Link these two: {l} ___ {r}", "Join with one word: {l} ___ {r}"
def link(left, answers, right, diff, form=None):
    assert all(a.isalpha() for a in answers), answers
    text = form.format(l=left.upper(), r=right.upper()) if form else f"{left.upper()} ___ {right.upper()}: which word links them?"
    OUT.append({"type": "text", "text": text,
                "answers": answers, "category": "Wordplay", "tags": ["word links", "wordplay"], "difficulty": diff})

link("Alarm", ["Clock", "Bell"], "Tower", "easy")                  # alarm clock / clock tower; alarm bell / bell tower
link("Sun", ["Flower"], "Pot", "easy")                              # sunflower / flowerpot
link("Rain", ["Bow"], "Tie", "easy")                                # rainbow / bow tie
link("Gold", ["Fish"], "Bowl", "easy")                              # goldfish / fishbowl
link("Light", ["House"], "Keeper", "easy")                          # lighthouse / housekeeper
link("Bed", ["Room"], "Mate", "easy")                               # bedroom / roommate
link("School", ["Boy", "Girl"], "Friend", "easy")                   # schoolboy / boyfriend; schoolgirl / girlfriend
link("Tea", ["Pot"], "Hole", "easy")                                # teapot / pothole
link("Honey", ["Moon"], "Light", "easy", V1)                            # honeymoon / moonlight
link("Sea", ["Side"], "Show", "easy")                               # seaside / sideshow
link("Night", ["Club", "Light"], "House", "easy")                   # nightclub / clubhouse; nightlight / lighthouse
link("Foot", ["Ball", "Bath", "Rest"], "Room", "easy")              # football / ballroom; footbath / bathroom; footrest / restroom
link("Black", ["Board", "Mail"], "Room", "easy", V1)                    # blackboard / boardroom; blackmail / mailroom
link("Hand", ["Bag"], "Pipe", "medium")                             # handbag / bagpipe
link("Water", ["Fall"], "Out", "medium")                            # waterfall / fallout
link("Birth", ["Day"], "Light", "medium", V2)                           # birthday / daylight
link("Snow", ["Man"], "Hole", "medium", V1)                             # snowman / manhole
link("Book", ["Worm"], "Hole", "medium", V2)                            # bookworm / wormhole
link("Sand", ["Paper"], "Weight", "medium")                         # sandpaper / paperweight
link("Butter", ["Fly"], "Wheel", "medium")                          # butterfly / flywheel
link("Finger", ["Print"], "Out", "medium", V1)                          # fingerprint / printout
link("Play", ["Ground"], "Hog", "medium")                           # playground / groundhog
link("Day", ["Dream"], "Team", "medium")                            # daydream / dream team
link("Break", ["Fast"], "Food", "medium")                           # breakfast / fast food
link("Foot", ["Note"], "Book", "medium", V1)                           # footnote / notebook
link("Wind", ["Mill"], "Stone", "medium")                           # windmill / millstone
link("Flash", ["Light"], "Weight", "medium", V3)                        # flashlight / lightweight
link("Over", ["Time", "Head"], "Line", "medium")                    # overtime / timeline; overhead / headline
link("Pan", ["Cake"], "Walk", "medium")                             # pancake / cakewalk
link("Hot", ["Dog"], "House", "medium", V1)                             # hot dog / doghouse
link("Red", ["Neck"], "Tie", "medium", V1)                              # redneck / necktie
link("Fire", ["Place", "Door"], "Mat", "medium")                    # fireplace / placemat; fire door / doormat
link("Tooth", ["Paste"], "Board", "hard")                           # toothpaste / pasteboard
link("Eye", ["Brow"], "Beat", "hard")                               # eyebrow / browbeat
link("Back", ["Bone"], "Head", "hard")                              # backbone / bonehead
link("Work", ["Shop"], "Lift", "hard")                              # workshop / shoplift
link("Suit", ["Case"], "Load", "hard")                              # suitcase / caseload
link("Car", ["Port"], "Hole", "hard", V3)                               # carport / porthole
link("Grand", ["Stand"], "By", "hard")                              # grandstand / standby

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'text-link-1.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'word-link questions written')
