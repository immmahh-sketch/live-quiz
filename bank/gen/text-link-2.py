# Bank session 19 Oct 2026: second batch of "word connections" questions (see text-link-1.py and the live-quiz-word-links memory): two
# words are shown and the player types the one word that goes between them to make two new words or phrases. Stored as Type-the-answer
# questions in bank/text-link-2.json; import with: node tools/import-bank.mjs text
# Every link was checked both ways, and every genuine alternative is accepted (paper CUP / cupboard, high ROAD / roadside, sea STAR /
# starfish). The wording is two short forms that no earlier question uses, alternating, so the server's near-duplicate rule (about 80% of
# words shared) doesn't skip them; no two questions with the same right-hand word share a wording.
# EGG ___ SHOCK (answer Shell) was skipped as a repeat of SEA ___ FISH, whose accepted answers include Shell, so it became FLOOD ___ WAY.
import json, os
OUT = []
FORMS = ["Missing link: {l} ___ {r}", "One word fits: {l} ___ {r}"]
n = [0]
def link(left, answers, right, diff):
    assert all(a.isalpha() for a in answers), answers
    text = FORMS[n[0] % 2].format(l=left.upper(), r=right.upper()); n[0] += 1
    OUT.append({"type": "text", "text": text, "answers": answers, "category": "Wordplay", "tags": ["word links", "wordplay"], "difficulty": diff})

link("Paper", ["Clip", "Cup"], "Board", "medium")                 # paperclip / clipboard; paper cup / cupboard
link("News", ["Paper"], "Boy", "easy")                            # newspaper / paperboy
link("Bus", ["Stop"], "Watch", "medium")                          # bus stop / stopwatch
link("Basket", ["Ball"], "Park", "easy")                          # basketball / ballpark
link("High", ["Way", "Road"], "Side", "medium")                   # highway / wayside; high road / roadside
link("Drift", ["Wood"], "Work", "hard")                           # driftwood / woodwork
link("Salt", ["Water"], "Fall", "medium")                         # saltwater / waterfall
link("Super", ["Market"], "Place", "medium")                      # supermarket / marketplace
link("Door", ["Step"], "Ladder", "medium")                        # doorstep / stepladder
link("Time", ["Table"], "Spoon", "medium")                        # timetable / tablespoon
link("Sea", ["Shell", "Star"], "Fish", "medium")                  # seashell / shellfish; sea star / starfish
link("Finger", ["Nail"], "File", "medium")                        # fingernail / nail file
link("Horse", ["Shoe"], "Lace", "medium")                         # horseshoe / shoelace
link("Tea", ["Spoon"], "Feed", "hard")                            # teaspoon / spoon-feed
link("Tool", ["Box"], "Office", "medium")                         # toolbox / box office
link("Fountain", ["Pen"], "Knife", "medium")                      # fountain pen / penknife
link("Lucky", ["Dip"], "Stick", "hard")                           # lucky dip / dipstick
link("Cat", ["Walk"], "Way", "easy")                              # catwalk / walkway
link("Heart", ["Beat"], "Box", "medium")                          # heartbeat / beatbox
link("World", ["Wide"], "Spread", "hard")                         # worldwide / widespread
link("Blue", ["Bell"], "Boy", "medium")                           # bluebell / bellboy
link("Mind", ["Set"], "Up", "hard")                               # mindset / set up
link("Flood", ["Gate"], "Way", "hard")                           # floodgate / gateway

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'text-link-2.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'word-link questions written')
