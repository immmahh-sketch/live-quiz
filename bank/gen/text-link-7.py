# Bank session 19 Oct 2026: seventh batch of "word connections" questions (user's target: 500 in all; see text-link-1.py and the
# live-quiz-word-links memory): two words are shown and the player types the one word that goes between them to make two new words or
# phrases. Stored as Type-the-answer questions in bank/text-link-7.json; import with: node tools/import-bank.mjs text
# (re-run until it says added 0: a first run can wrongly skip many). Every link was checked both ways. Every first answer is new (none
# used by batches 1-6).
# Wording: two new short forms (Spot the link / Middle man), alternating so two questions that share a right-hand word never share one.
import json, os
OUT = []
FORMS = ["Spot the link: {l} ___ {r}", "Middle man: {l} ___ {r}"]
used = {}
n = [0]
def link(left, answers, right, diff):
    assert all(a.isalpha() for a in answers), answers
    k = n[0] % 2
    if used.get(right.lower()) == k: k = 1 - k
    used[right.lower()] = k; n[0] += 1
    OUT.append({"type": "text", "text": FORMS[k].format(l=left.upper(), r=right.upper()), "answers": answers, "category": "Wordplay",
                "tags": ["word links", "wordplay"], "difficulty": diff})

link("Mouse", ["Trap"], "Door", "medium")                       # mousetrap / trapdoor
link("Fish", ["Hook"], "Up", "medium")                           # fishhook / hook-up
link("Flash", ["Point"], "Blank", "medium")                      # flashpoint / point-blank
link("Fly", ["Wheel"], "Chair", "medium")                        # flywheel / wheelchair
link("Foot", ["Bridge"], "Head", "hard")                         # footbridge / bridgehead
link("Grand", ["Child"], "Care", "medium")                       # grandchild / childcare
link("Gun", ["Boat"], "House", "medium")                         # gunboat / boathouse
link("Head", ["Phone"], "Box", "easy")                           # headphone / phone box
link("Hot", ["Bed"], "Room", "medium")                           # hotbed / bedroom
link("Hot", ["Plate"], "Glass", "medium")                        # hotplate / plate glass
link("Ice", ["Cream"], "Cheese", "medium")                       # ice cream / cream cheese
link("Land", ["Slide"], "Show", "medium")                        # landslide / slideshow
link("Love", ["Story"], "Book", "easy")                          # love story / storybook
link("News", ["Flash"], "Light", "medium")                       # newsflash / flashlight
link("Night", ["Shift"], "Work", "medium")                       # night shift / shiftwork
link("Over", ["Draw"], "Bridge", "hard")                         # overdraw / drawbridge
link("Space", ["Suit"], "Case", "medium")                        # spacesuit / suitcase
link("Top", ["Spin"], "Doctor", "hard")                          # topspin / spin doctor
link("Watch", ["Word"], "Play", "medium")                        # watchword / wordplay
link("Wood", ["Wind"], "Pipe", "medium")                         # woodwind / windpipe
link("Work", ["Bench"], "Mark", "medium")                        # workbench / benchmark
link("Back", ["Log"], "Book", "medium")                          # backlog / logbook
link("Blue", ["Bottle"], "Neck", "medium")                       # bluebottle / bottleneck
link("Box", ["Car"], "Park", "medium")                           # boxcar / car park
link("Ear", ["Drum"], "Stick", "medium")                         # eardrum / drumstick
link("Push", ["Up"], "Hill", "medium")                           # push-up / uphill
link("Stand", ["By"], "Pass", "hard")                            # standby / bypass
link("Take", ["Away"], "Day", "medium")                          # takeaway / Away Day
link("Fire", ["Brand"], "New", "medium")                         # firebrand / brand new
link("Free", ["Style"], "Guide", "medium")                       # freestyle / style guide
link("Test", ["Match"], "Box", "medium")                         # Test match / matchbox
link("Sound", ["Bite"], "Size", "hard")                          # sound bite / bite-size
link("Garden", ["Party"], "Line", "medium")                      # garden party / party line
link("Picnic", ["Basket"], "Ball", "medium")                     # picnic basket / basketball
link("Easter", ["Egg"], "Cup", "easy")                           # Easter egg / eggcup
link("Blow", ["Torch"], "Light", "medium")                       # blowtorch / torchlight
link("Cold", ["War"], "Path", "medium")                          # Cold War / warpath

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'text-link-7.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'word-link questions written')
