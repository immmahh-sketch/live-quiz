# Bank session 19 Oct 2026: ninth batch of "word connections" questions (user's target: 500 in all; see text-link-1.py and the
# live-quiz-word-links memory): two words are shown and the player types the one word that goes between them to make two new words or
# phrases. Stored as Type-the-answer questions in bank/text-link-9.json; import with: CHUNK=10 node tools/import-bank.mjs text
# Every link was checked both ways, and every first answer is new (none used by batches 1-8). A food, drink, meals and days theme,
# built from two-word phrases (fruit salad / salad bowl, Black Friday / Friday night). Genuine second answers are accepted (fruit
# PUNCH / punch bowl, wedding GIFT / gift list, fire ENGINE / engine room).
# Wording: two new short forms (Common link / Link word), alternating so two questions that share a right-hand word never share one.
import json, os
OUT = []
FORMS = ["Common link: {l} ___ {r}", "Link word: {l} ___ {r}"]
used = {}
n = [0]
def link(left, answers, right, diff):
    assert all(a.isalpha() for a in answers), answers
    k = n[0] % 2
    if used.get(right.lower()) == k: k = 1 - k
    used[right.lower()] = k; n[0] += 1
    OUT.append({"type": "text", "text": FORMS[k].format(l=left.upper(), r=right.upper()), "answers": answers, "category": "Wordplay",
                "tags": ["word links", "wordplay"], "difficulty": diff})

link("Fruit", ["Salad", "Punch"], "Bowl", "medium")            # fruit salad / salad bowl; fruit punch / punch bowl
link("Cherry", ["Tomato"], "Soup", "medium")                     # cherry tomato / tomato soup
link("Roast", ["Chicken"], "Wing", "medium")                     # roast chicken / chicken wing
link("Blood", ["Orange"], "Juice", "easy")                       # blood orange / orange juice
link("Bitter", ["Lemon"], "Curd", "medium")                      # bitter lemon / lemon curd
link("Hot", ["Chocolate"], "Button", "easy")                     # hot chocolate / chocolate button
link("Spring", ["Onion"], "Ring", "easy")                        # spring onion / onion ring
link("Black", ["Pepper"], "Mill", "medium")                      # black pepper / pepper mill
link("Cream", ["Cheese"], "Board", "medium")                     # cream cheese / cheeseboard
link("Peanut", ["Butter"], "Knife", "medium")                    # peanut butter / butter knife
link("Green", ["Tea"], "Leaf", "easy")                           # green tea / tea leaf
link("Black", ["Coffee"], "Table", "easy")                       # black coffee / coffee table
link("Ginger", ["Beer"], "Garden", "easy")                       # ginger beer / beer garden
link("Red", ["Wine"], "Glass", "easy")                           # red wine / wine glass
link("Pub", ["Quiz"], "Master", "easy")                          # pub quiz / quizmaster
link("Virtual", ["Reality"], "TV", "medium")                     # virtual reality / reality TV
link("Natural", ["Talent"], "Show", "medium")                    # natural talent / talent show
link("Head", ["Chef"], "Hat", "medium")                          # head chef / chef's hat
link("Riot", ["Police"], "Dog", "medium")                        # riot police / police dog
link("Fire", ["Escape", "Engine"], "Room", "medium")             # fire escape / escape room; fire engine / engine room
link("Fire", ["Alarm"], "Clock", "easy")                         # fire alarm / alarm clock
link("Summer", ["Holiday"], "Camp", "easy")                      # summer holiday / holiday camp
link("High", ["School"], "Bus", "easy")                          # high school / school bus
link("School", ["Bus"], "Stop", "easy")                          # school bus / bus stop
link("Train", ["Ticket"], "Office", "easy")                      # train ticket / ticket office
link("Wedding", ["Guest", "Gift"], "List", "easy")               # wedding guest / guest list; wedding gift / gift list
link("Royal", ["Icing"], "Sugar", "medium")                      # royal icing / icing sugar
link("Icing", ["Sugar"], "Cube", "easy")                         # icing sugar / sugar cube
link("Chicken", ["Soup"], "Spoon", "easy")                       # chicken soup / soup spoon
link("Club", ["Sandwich"], "Box", "easy")                        # club sandwich / sandwich box
link("Packed", ["Lunch"], "Box", "easy")                         # packed lunch / lunch box
link("Christmas", ["Dinner"], "Party", "easy")                   # Christmas dinner / dinner party
link("Last", ["Supper"], "Club", "medium")                       # Last Supper / supper club
link("Mixed", ["Grill"], "Pan", "medium")                        # mixed grill / grill pan
link("Sunday", ["Roast"], "Potato", "easy")                      # Sunday roast / roast potato
link("Black", ["Friday"], "Night", "easy")                       # Black Friday / Friday night
link("Blue", ["Monday"], "Morning", "easy")                      # Blue Monday / Monday morning
link("Leap", ["Year"], "Book", "easy")                           # leap year / yearbook

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'text-link-9.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'word-link questions written')
