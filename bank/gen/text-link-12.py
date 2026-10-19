# Bank session 19 Oct 2026: twelfth and last batch of "word connections" questions (user's target: 500 in all; see text-link-1.py
# and the live-quiz-word-links memory): two words are shown and the player types the one word that goes between them to make two new
# words or phrases. Stored as Type-the-answer questions in bank/text-link-12.json; import with: CHUNK=10 node tools/import-bank.mjs text
# Every link was checked both ways, and every first answer is new (none used by batches 1-11). Themes: nature and plants, festivals,
# science, shapes and colours, books, games, space and a few jobs. Second answers are accepted where genuine (wild ROSE / rose garden
# and wild FLOWER / flower garden; code RED / red alert and code AMBER / amber alert; home VIDEO / video game and home COMPUTER /
# computer game).
# Wording: two new short forms (Half and half / Share a word), alternating so two questions that share a right-hand word never share one.
import json, os
OUT = []
FORMS = ["Half and half: {l} ___ {r}", "Share a word: {l} ___ {r}"]
used = {}
n = [0]
def link(left, answers, right, diff):
    assert all(a.isalpha() for a in answers), answers
    k = n[0] % 2
    if used.get(right.lower()) == k: k = 1 - k
    used[right.lower()] = k; n[0] += 1
    OUT.append({"type": "text", "text": FORMS[k].format(l=left.upper(), r=right.upper()), "answers": answers, "category": "Wordplay",
                "tags": ["word links", "wordplay"], "difficulty": diff})

link("Wild", ["Rose", "Flower"], "Garden", "easy")             # wild rose / rose garden; wildflower / flower garden
link("Water", ["Lily"], "Pad", "easy")                           # water lily / lily pad
link("Scots", ["Pine"], "Cone", "easy")                          # Scots pine / pine cone
link("Pine", ["Cone"], "Head", "medium")                         # pine cone / conehead
link("Oak", ["Leaf"], "Blower", "easy")                          # oak leaf / leaf blower
link("Olive", ["Branch"], "Manager", "easy")                     # olive branch / branch manager
link("Black", ["Olive"], "Oil", "easy")                          # black olive / olive oil
link("Olive", ["Oil"], "Painting", "easy")                       # olive oil / oil painting
link("Bird", ["Seed"], "Pod", "medium")                          # birdseed / seed pod
link("Brain", ["Stem"], "Cell", "medium")                        # brain stem / stem cell
link("Prison", ["Cell"], "Phone", "easy")                        # prison cell / cell phone
link("Pampas", ["Grass"], "Snake", "medium")                     # pampas grass / grass snake
link("Button", ["Mushroom"], "Cloud", "easy")                    # button mushroom / mushroom cloud
link("Top", ["Banana"], "Split", "easy")                         # top banana / banana split
link("Baby", ["Carrot"], "Cake", "easy")                         # baby carrot / carrot cake
link("Sweet", ["Pea"], "Shooter", "easy")                        # sweet pea / pea shooter
link("Merry", ["Christmas"], "Tree", "easy")                     # Merry Christmas / Christmas tree
link("Happy", ["Easter"], "Egg", "easy")                         # Happy Easter / Easter egg
link("Secret", ["Santa"], "Claus", "easy")                       # Secret Santa / Santa Claus
link("Christmas", ["Turkey"], "Dinner", "medium")                # Christmas turkey / turkey dinner
link("Halloween", ["Pumpkin"], "Pie", "easy")                    # Halloween pumpkin / pumpkin pie
link("Holy", ["Ghost"], "Train", "easy")                         # Holy Ghost / ghost train
link("Wicked", ["Witch"], "Doctor", "easy")                      # wicked witch / witch doctor
link("Birthday", ["Present"], "Day", "medium")                   # birthday present / present day
link("Happy", ["Birthday"], "Cake", "easy")                      # Happy Birthday / birthday cake
link("Atom", ["Bomb"], "Disposal", "medium")                     # atom bomb / bomb disposal
link("Science", ["Lab"], "Coat", "easy")                         # science lab / lab coat
link("Computer", ["Science"], "Fiction", "easy")                 # computer science / science fiction
link("Home", ["Video", "Computer"], "Game", "easy")              # home video / video game; home computer / computer game
link("Computer", ["Virus"], "Scan", "medium")                    # computer virus / virus scan
link("Toy", ["Robot"], "Wars", "easy")                           # toy robot / Robot Wars
link("Zero", ["Gravity"], "Wave", "medium")                      # zero gravity / gravity wave
link("Absolute", ["Zero"], "Hour", "medium")                     # absolute zero / zero hour
link("Electric", ["Guitar"], "Solo", "easy")                     # electric guitar / guitar solo
link("Car", ["Battery"], "Hen", "medium")                        # car battery / battery hen
link("Mother", ["Hen"], "Party", "easy")                         # mother hen / hen party
link("Crop", ["Circle"], "Line", "medium")                       # crop circle / Circle Line
link("Ice", ["Cube"], "Root", "medium")                          # ice cube / cube root
link("Green", ["Arrow"], "Key", "medium")                        # Green Arrow / arrow key
link("Black", ["Diamond"], "Ring", "easy")                       # black diamond / diamond ring
link("Olympic", ["Gold"], "Medal", "easy")                       # Olympic gold / gold medal
link("Sterling", ["Silver"], "Lining", "medium")                 # sterling silver / silver lining
link("Navy", ["Blue"], "Whale", "easy")                          # navy blue / blue whale
link("Code", ["Red", "Amber"], "Alert", "easy")                  # code red / red alert; code amber / amber alert
link("Graphic", ["Novel"], "Idea", "medium")                     # graphic novel / novel idea
link("Mobile", ["Library"], "Card", "easy")                      # mobile library / library card
link("Tooth", ["Fairy"], "Tale", "easy")                         # tooth fairy / fairy tale
link("Comic", ["Strip"], "Light", "medium")                      # comic strip / strip light
link("Film", ["Script"], "Writer", "easy")                       # film script / scriptwriter
link("Loaded", ["Dice"], "Game", "easy")                         # loaded dice / dice game
link("Online", ["Bingo"], "Hall", "easy")                        # online bingo / bingo hall
link("National", ["Lottery"], "Ticket", "easy")                  # National Lottery / lottery ticket
link("Jigsaw", ["Puzzle"], "Book", "easy")                       # jigsaw puzzle / puzzle book
link("Pool", ["Cue"], "Ball", "easy")                            # pool cue / cue ball
link("Space", ["Rocket"], "Science", "easy")                     # space rocket / rocket science
link("Red", ["Planet"], "Earth", "easy")                         # Red Planet / Planet Earth
link("Planet", ["Earth"], "Day", "easy")                         # Planet Earth / Earth Day
link("Spy", ["Satellite"], "Dish", "medium")                     # spy satellite / satellite dish
link("Satellite", ["Dish"], "Washer", "easy")                    # satellite dish / dishwasher
link("Town", ["Council"], "House", "easy")                       # town council / council house
link("Circus", ["Clown"], "Fish", "easy")                        # circus clown / clownfish
link("Flying", ["Circus"], "Clown", "medium")                    # flying circus / circus clown

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'text-link-12.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'word-link questions written')
