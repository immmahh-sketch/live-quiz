# Bank session 19 Oct 2026: eighth batch of "word connections" questions (user's target: 500 in all; see text-link-1.py and the
# live-quiz-word-links memory): two words are shown and the player types the one word that goes between them to make two new words or
# phrases. Stored as Type-the-answer questions in bank/text-link-8.json; import with: CHUNK=10 node tools/import-bank.mjs text
# (small chunks, or the server times out with HTTP 546). Every link was checked both ways, and every first answer is new (none used
# by batches 1-7). This batch leans on two-word phrases (tennis court / courtroom, pole vault / vault door) rather than one-word
# compounds, which are running low.
# Wording: two new short forms (Word in between / Fill the blank), alternating so two questions that share a right-hand word never
# share one.
import json, os
OUT = []
FORMS = ["Word in between: {l} ___ {r}", "Fill the blank: {l} ___ {r}"]
used = {}
n = [0]
def link(left, answers, right, diff):
    assert all(a.isalpha() for a in answers), answers
    k = n[0] % 2
    if used.get(right.lower()) == k: k = 1 - k
    used[right.lower()] = k; n[0] += 1
    OUT.append({"type": "text", "text": FORMS[k].format(l=left.upper(), r=right.upper()), "answers": answers, "category": "Wordplay",
                "tags": ["word links", "wordplay"], "difficulty": diff})

link("Oven", ["Glove"], "Box", "medium")                        # oven glove / glovebox
link("Hole", ["Punch"], "Line", "medium")                        # hole punch / punchline
link("Tennis", ["Court"], "Room", "medium")                      # tennis court / courtroom
link("Cricket", ["Bat"], "Man", "easy")                          # cricket bat / Batman
link("Table", ["Tennis"], "Ball", "easy")                        # table tennis / tennis ball
link("Pole", ["Vault"], "Door", "hard")                          # pole vault / vault door
link("Ice", ["Hockey"], "Stick", "medium")                       # ice hockey / hockey stick
link("Pop", ["Music"], "Box", "easy")                            # pop music / music box
link("Folk", ["Song"], "Writer", "medium")                       # folk song / songwriter
link("Soap", ["Opera"], "House", "medium")                       # soap opera / opera house
link("Bath", ["Towel"], "Rail", "medium")                        # bath towel / towel rail
link("Wedding", ["Dress"], "Code", "medium")                     # wedding dress / dress code
link("Leather", ["Jacket"], "Potato", "medium")                  # leather jacket / jacket potato
link("Sweet", ["Potato"], "Peeler", "medium")                    # sweet potato / potato peeler
link("French", ["Toast"], "Rack", "medium")                      # French toast / toast rack
link("Belly", ["Dance"], "Floor", "medium")                      # belly dance / dance floor
link("North", ["Pole"], "Star", "medium")                        # North Pole / Pole Star
link("April", ["Shower"], "Curtain", "medium")                   # April shower / shower curtain
link("Net", ["Curtain"], "Call", "hard")                         # net curtain / curtain call
link("Phone", ["Call"], "Box", "medium")                         # phone call / call box
link("Garden", ["Centre", "Center"], "Forward", "medium")        # garden centre / centre forward
link("Film", ["Crew"], "Cut", "medium")                          # film crew / crew cut
link("Cut", ["Price"], "Tag", "medium")                          # cut price / price tag
link("Tag", ["Team"], "Spirit", "medium")                        # tag team / team spirit
link("Holy", ["Spirit"], "Level", "hard")                        # Holy Spirit / spirit level
link("Sea", ["Level"], "Crossing", "medium")                     # sea level / level crossing
link("Blind", ["Date"], "Stamp", "medium")                       # blind date / date stamp
link("Rubber", ["Stamp"], "Duty", "hard")                        # rubber stamp / stamp duty
link("Jury", ["Duty"], "Free", "medium")                         # jury duty / duty-free
link("Security", ["Check"], "Mate", "medium")                    # security check / checkmate
link("Magic", ["Carpet"], "Bag", "medium")                       # magic carpet / carpet bag
link("Set", ["Square"], "Dance", "medium")                       # set square / square dance
link("Car", ["Boot"], "Sale", "medium")                          # car boot / boot sale
link("Fast", ["Food"], "Court", "easy")                          # fast food / food court
link("Wine", ["List"], "Price", "medium")                        # wine list / list price
link("Room", ["Service"], "Station", "medium")                   # room service / service station

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'text-link-8.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'word-link questions written')
