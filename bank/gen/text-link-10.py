# Bank session 19 Oct 2026: tenth batch of "word connections" questions (user's target: 500 in all; see text-link-1.py and the
# live-quiz-word-links memory): two words are shown and the player types the one word that goes between them to make two new words or
# phrases. Stored as Type-the-answer questions in bank/text-link-10.json; import with: CHUNK=10 node tools/import-bank.mjs text
# Every link was checked both ways, and every first answer is new (none used by batches 1-9). Themes: transport, animals, jobs,
# school, weather and TV, all two-word phrase chains (water taxi / taxi rank, Black Swan / Swan Lake / lake district).
# Wording: two new short forms (Go-between / Missing word), alternating so two questions that share a right-hand word never share one.
import json, os
OUT = []
FORMS = ["Go-between: {l} ___ {r}", "Missing word: {l} ___ {r}"]
used = {}
n = [0]
def link(left, answers, right, diff):
    assert all(a.isalpha() for a in answers), answers
    k = n[0] % 2
    if used.get(right.lower()) == k: k = 1 - k
    used[right.lower()] = k; n[0] += 1
    OUT.append({"type": "text", "text": FORMS[k].format(l=left.upper(), r=right.upper()), "answers": answers, "category": "Wordplay",
                "tags": ["word links", "wordplay"], "difficulty": diff})

link("Water", ["Taxi"], "Rank", "medium")                       # water taxi / taxi rank
link("Car", ["Ferry"], "Port", "medium")                         # car ferry / ferry port
link("Hand", ["Luggage"], "Rack", "easy")                        # hand luggage / luggage rack
link("Channel", ["Tunnel"], "Vision", "medium")                  # Channel Tunnel / tunnel vision
link("Unleaded", ["Petrol"], "Station", "medium")                # unleaded petrol / petrol station
link("Spare", ["Tyre"], "Pressure", "medium")                    # spare tyre / tyre pressure
link("Phone", ["Number"], "Plate", "easy")                       # phone number / number plate
link("Driving", ["Licence", "License"], "Plate", "medium")       # driving licence / licence plate
link("Shetland", ["Pony"], "Tail", "easy")                       # Shetland pony / ponytail
link("Black", ["Sheep"], "Dog", "easy")                          # black sheep / sheepdog
link("Spring", ["Lamb"], "Chop", "easy")                         # spring lamb / lamb chop
link("Mad", ["Cow"], "Disease", "easy")                          # mad cow / cow disease
link("Pit", ["Bull"], "Dog", "easy")                             # pit bull / bulldog
link("Field", ["Mouse"], "Trap", "easy")                         # field mouse / mousetrap
link("Pack", ["Rat"], "Race", "easy")                            # pack rat / rat race
link("Grass", ["Snake"], "Charmer", "easy")                      # grass snake / snake charmer
link("Polar", ["Bear"], "Hug", "easy")                           # polar bear / bear hug
link("Giant", ["Panda"], "Car", "easy")                          # giant panda / panda car
link("Sea", ["Lion"], "Cub", "easy")                             # sea lion / lion cub
link("Cheeky", ["Monkey"], "Business", "easy")                   # cheeky monkey / monkey business
link("Killer", ["Whale"], "Song", "easy")                        # killer whale / whale song
link("White", ["Shark"], "Attack", "easy")                       # white shark / shark attack
link("Hermit", ["Crab"], "Stick", "medium")                      # hermit crab / crab stick
link("Black", ["Swan"], "Lake", "easy")                          # black swan / Swan Lake
link("Swan", ["Lake"], "District", "easy")                       # Swan Lake / Lake District
link("Rubber", ["Duck"], "Pond", "easy")                         # rubber duck / duck pond
link("Mother", ["Goose"], "Bumps", "easy")                       # Mother Goose / goose bumps
link("Fire", ["Ant"], "Hill", "easy")                            # fire ant / anthill
link("Test", ["Pilot"], "Light", "medium")                       # test pilot / pilot light
link("Team", ["Captain"], "Hook", "medium")                      # team captain / Captain Hook
link("Toy", ["Soldier"], "Ant", "medium")                        # toy soldier / soldier ant
link("Driving", ["Lesson"], "Plan", "easy")                      # driving lesson / lesson plan
link("Final", ["Exam"], "Paper", "easy")                         # final exam / exam paper
link("Cup", ["Final"], "Whistle", "easy")                        # cup final / final whistle
link("Final", ["Whistle"], "Blower", "easy")                     # final whistle / whistle-blower
link("School", ["Report"], "Card", "easy")                       # school report / report card
link("Evening", ["Class"], "Act", "medium")                      # evening class / class act
link("Rising", ["Sun"], "Cream", "easy")                         # rising sun / sun cream
link("Acid", ["Rain"], "Check", "medium")                        # acid rain / rain check
link("Fresh", ["Snow"], "White", "easy")                         # fresh snow / Snow White
link("Dense", ["Fog"], "Horn", "easy")                           # dense fog / foghorn
link("Forked", ["Lightning"], "Bolt", "medium")                  # forked lightning / lightning bolt
link("Jack", ["Frost"], "Bite", "easy")                          # Jack Frost / frostbite
link("Black", ["Ice"], "Rink", "easy")                           # black ice / ice rink
link("Dead", ["Heat"], "Wave", "easy")                           # dead heat / heatwave
link("Storm", ["Cloud"], "Nine", "medium")                       # storm cloud / cloud nine
link("Remote", ["Control"], "Panel", "medium")                   # remote control / control panel
link("Solar", ["Panel"], "Show", "medium")                       # solar panel / panel show
link("Football", ["Season"], "Ticket", "easy")                   # football season / season ticket
link("Live", ["Action"], "Replay", "medium")                     # live action / action replay
link("Hidden", ["Camera"], "Crew", "easy")                       # hidden camera / camera crew
link("Surround", ["Sound"], "Effect", "medium")                  # surround sound / sound effect
link("Centre", ["Stage"], "Door", "medium")                      # centre stage / stage door

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'text-link-10.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'word-link questions written')
