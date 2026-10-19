# Bank session 19 Oct 2026: fourth batch of "word connections" questions (user's target: 500 in all; see text-link-1.py and the
# live-quiz-word-links memory): two words are shown and the player types the one word that goes between them to make two new words or
# phrases. Stored as Type-the-answer questions in bank/text-link-4.json; import with: node tools/import-bank.mjs text
# Every link was checked both ways, and every genuine alternative is accepted. Every first answer is new (not used by batches 1-3).
# Wording: two new short forms (Link up / Fill the gap) so none of the earlier wordings is reused, alternating so two questions that
# share a right-hand word (HOUSE, TIME, OVER, FREE...) never share a wording.
import json, os
OUT = []
FORMS = ["Link up: {l} ___ {r}", "Fill the gap: {l} ___ {r}"]
used = {}
n = [0]
def link(left, answers, right, diff):
    assert all(a.isalpha() for a in answers), answers
    k = n[0] % 2
    if used.get(right.lower()) == k: k = 1 - k
    used[right.lower()] = k; n[0] += 1
    OUT.append({"type": "text", "text": FORMS[k].format(l=left.upper(), r=right.upper()), "answers": answers, "category": "Wordplay",
                "tags": ["word links", "wordplay"], "difficulty": diff})

link("Home", ["Land"], "Lord", "medium")                           # homeland / landlord
link("Eye", ["Lash"], "Out", "hard")                               # eyelash / lash out
link("Fire", ["Arm"], "Rest", "medium")                            # firearm / armrest
link("War", ["Ship"], "Yard", "medium")                            # warship / shipyard
link("Back", ["Yard"], "Stick", "medium")                          # backyard / yardstick
link("Pea", ["Nut"], "Butter", "medium")                           # peanut / nut butter
link("Counter", ["Part"], "Time", "hard")                          # counterpart / part-time
link("Finger", ["Tip"], "Top", "hard")                             # fingertip / tip-top
link("White", ["Wash"], "Basin", "medium")                         # whitewash / washbasin
link("Safe", ["Guard"], "Dog", "medium")                           # safeguard / guard dog
link("Hair", ["Cut"], "Throat", "medium")                          # haircut / cutthroat
link("Out", ["Law"], "Suit", "medium")                             # outlaw / lawsuit
link("Air", ["Line"], "Man", "medium")                             # airline / lineman
link("Foot", ["Hold"], "Up", "medium")                             # foothold / hold-up
link("News", ["Cast"], "Off", "medium")                            # newscast / cast off
link("Work", ["Out"], "Line", "medium")                            # workout / outline
link("Blood", ["Shot"], "Gun", "medium")                           # bloodshot / shotgun
link("Brain", ["Wave"], "Length", "medium")                        # brainwave / wavelength
link("Rock", ["Pool"], "Side", "medium")                           # rock pool / poolside
link("Motor", ["Bike", "Cycle"], "Lane", "medium")                 # motorbike / bike lane; motorcycle / cycle lane
link("Egg", ["Plant"], "Pot", "medium")                            # eggplant / plant pot
link("Razor", ["Blade"], "Runner", "medium")                       # razor blade / blade runner
link("Left", ["Over"], "Time", "medium")                           # leftover / overtime
link("Cut", ["Back"], "Bone", "medium")                            # cutback / backbone
link("Honey", ["Comb"], "Over", "hard")                            # honeycomb / comb-over
link("Tooth", ["Brush"], "Stroke", "medium")                       # toothbrush / brushstroke
link("Pay", ["Roll"], "Back", "hard")                              # payroll / rollback
link("Lap", ["Top"], "Hat", "medium")                              # laptop / top hat
link("Boot", ["Camp"], "Fire", "medium")                           # boot camp / campfire
link("Dust", ["Bin"], "Man", "medium")                             # dustbin / binman
link("Thunder", ["Clap"], "Trap", "hard")                          # thunderclap / claptrap
link("Good", ["Will"], "Power", "medium")                          # goodwill / willpower
link("Horse", ["Power", "Play"], "House", "medium")                # horsepower / powerhouse; horseplay / playhouse
link("Free", ["Hand"], "Bag", "medium")                            # freehand / handbag
link("Head", ["Master"], "Mind", "medium")                         # headmaster / mastermind
link("Piggy", ["Bank"], "Note", "medium")                          # piggy bank / banknote
link("Soft", ["Ware"], "House", "medium")                          # software / warehouse
link("Cold", ["Snap"], "Shot", "medium")                           # cold snap / snapshot
link("Day", ["Care"], "Free", "medium")                            # daycare / carefree
link("Stage", ["Coach"], "Man", "medium")                          # stagecoach / coachman
link("War", ["Path"], "Way", "medium")                             # warpath / pathway
link("Touch", ["Down"], "Hill", "easy")                            # touchdown / downhill

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'text-link-4.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'word-link questions written')
