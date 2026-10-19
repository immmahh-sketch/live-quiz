# Bank session 19 Oct 2026: third batch of "word connections" questions (see text-link-1.py, text-link-2.py and the live-quiz-word-links
# memory): two words are shown and the player types the one word that goes between them to make two new words or phrases. Stored as
# Type-the-answer questions in bank/text-link-3.json; import with: node tools/import-bank.mjs text
# BACK ___ WORK (Fire) was skipped by the server, so it became COLD ___ LINE. Every link was checked both ways, and every answer is new (none of the earlier batches' answers, including their accepted
# alternatives, is reused, because the server skips a question whose answer and words overlap an old one). Wording: the two short forms
# from batch 2, chosen so that two questions sharing a right-hand word (UP, DOWN, FIELD) never share a wording.
import json, os
OUT = []
FORMS = ["Missing link: {l} ___ {r}", "One word fits: {l} ___ {r}"]
used = {}
n = [0]
def link(left, answers, right, diff):
    assert all(a.isalpha() for a in answers), answers
    k = n[0] % 2
    if used.get(right.lower()) == k: k = 1 - k
    used[right.lower()] = k; n[0] += 1
    text = FORMS[k].format(l=left.upper(), r=right.upper())
    OUT.append({"type": "text", "text": text, "answers": answers, "category": "Wordplay", "tags": ["word links", "wordplay"], "difficulty": diff})

link("Black", ["Bird"], "Song", "easy")                           # blackbird / birdsong
link("Pop", ["Corn"], "Field", "easy")                            # popcorn / cornfield
link("Arm", ["Chair"], "Lift", "medium")                          # armchair / chairlift
link("Neck", ["Lace"], "Up", "medium")                            # necklace / lace up
link("Sea", ["Weed"], "Killer", "medium")                         # seaweed / weedkiller
link("Land", ["Mark"], "Up", "hard")                              # landmark / markup
link("Sun", ["Burn"], "Out", "medium")                            # sunburn / burnout
link("Cold", ["Front"], "Line", "medium")                         # cold front / frontline
link("Week", ["End"], "Game", "medium")                           # weekend / end game
link("Hand", ["Shake"], "Down", "medium")                         # handshake / shakedown
link("Sweet", ["Heart"], "Break", "easy")                         # sweetheart / heartbreak
link("Jail", ["Break"], "Down", "medium")                         # jailbreak / breakdown
link("Scare", ["Crow"], "Bar", "medium")                          # scarecrow / crowbar
link("Wind", ["Screen"], "Saver", "medium")                       # windscreen / screensaver
link("Gold", ["Mine"], "Field", "medium")                         # goldmine / minefield
link("Pick", ["Pocket"], "Money", "hard")                         # pickpocket / pocket money
link("Fire", ["Proof"], "Read", "hard")                           # fireproof / proofread
link("Chain", ["Saw"], "Dust", "hard")                            # chainsaw / sawdust
link("Sand", ["Storm"], "Cloud", "medium")                        # sandstorm / storm cloud

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'text-link-3.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'word-link questions written')
