# Bank session 18 Oct 2026: true/false TRAPS -> bank/tf-traps-1.json.
# After the 13 Oct audit only ~5% of pickable true/false was hard, because an obscure statement is a coin flip, not hard.
# Hard here means a real trap: a common belief that is false, or a true fact that sounds wrong, so most people's
# instinct gives the wrong answer. Myths most people now know are debunked are rated medium.
# The first list's best-known myths turned out to be in the bank already, so they were taken out and a second batch added.
# Checked against every true/false statement in the bank (lqsql/audit/tf-dupcheck.py) before importing.
import json, os
OUT = []
def t(answer, diff, cat, tags, text):
    assert diff in ("easy", "medium", "hard") and text.endswith(".")
    OUT.append({"text": text, "answer": answer, "category": cat, "tags": tags, "difficulty": diff})

# --- sounds true, is false ---
t(False, "medium", "Science", ["myths", "physics"], "A penny dropped from the top of the Empire State Building could kill someone below.")
t(False, "hard", "Books and literature", ["Sherlock Holmes", "quotes"], "Sherlock Holmes says 'Elementary, my dear Watson' in Arthur Conan Doyle's stories.")
t(False, "hard", "Film quotes", ["Star Trek", "quotes"], "Captain Kirk says the exact words 'Beam me up, Scotty' in the original 'Star Trek' series.")
t(False, "hard", "Film quotes", ["Casablanca", "quotes"], "Humphrey Bogart says 'Play it again, Sam' in 'Casablanca'.")
t(False, "medium", "Books and literature", ["Frankenstein", "horror"], "In Mary Shelley's novel, the monster is called Frankenstein.")
t(False, "hard", "History", ["Morse code", "Titanic"], "The distress signal SOS stands for 'Save Our Souls'.")
t(False, "hard", "Science", ["diamonds", "geology"], "Diamonds are formed from compressed coal.")
t(False, "hard", "History", ["Columbus", "myths"], "Christopher Columbus set out to prove that the Earth was round.")
t(False, "medium", "Food and drink", ["Coca-Cola", "myths"], "Coca-Cola was originally green.")
t(False, "medium", "Nature", ["pets", "South America"], "Guinea pigs come from Guinea.")
t(False, "hard", "Geography", ["Spain", "islands", "word origins"], "The Canary Islands are named after canaries.")
t(False, "hard", "Music", ["instruments", "strings"], "Catgut, once used for violin strings, is made from cats.")
t(False, "medium", "Food and drink", ["turkey", "North America"], "Turkeys come from Turkey.")
t(False, "hard", "Maths and numbers", ["numbers", "India"], "Arabic numerals were invented by the Arabs.")
t(False, "hard", "Famous people in history", ["inventions", "toilets"], "Thomas Crapper invented the flush toilet.")
t(False, "hard", "Nature", ["lemmings", "Disney", "myths"], "Lemmings throw themselves off cliffs in mass suicides.")
t(False, "hard", "Nature", ["insects", "earwigs"], "Earwigs got their name because they crawl into people's ears to lay eggs.")
t(False, "hard", "History", ["French Revolution", "guillotine"], "The guillotine was invented by Dr Joseph-Ignace Guillotin.")
t(False, "hard", "History", ["pandemics", "1918"], "The 1918 'Spanish flu' pandemic began in Spain.")
t(False, "hard", "The human body", ["illness", "rubella"], "German measles is caused by the same virus as measles.")

# --- sounds false, is true ---
t(True, "hard", "Science and technology", ["inventions", "fax"], "The fax machine was invented before the telephone.")
t(True, "hard", "Ancient history", ["mammoths", "pyramids"], "Woolly mammoths were still alive when the Great Pyramid of Giza was built.")
t(True, "hard", "Food and drink", ["lobster", "America"], "Lobster was once thought of as food for the poor in America.")
t(True, "hard", "Food and drink", ["nuts", "South America"], "Bolivia exports more Brazil nuts than Brazil does.")
t(True, "hard", "Space and astronomy", ["Mercury", "planets"], "On average, Mercury is the closest planet to Earth.")
t(True, "hard", "Space and astronomy", ["Pluto", "Russia"], "Russia has a bigger surface area than Pluto.")
t(True, "hard", "The United States", ["Alaska", "geography"], "Alaska is both the westernmost and the easternmost US state.")
t(True, "hard", "World geography", ["Panama Canal", "oceans"], "The Atlantic end of the Panama Canal is further west than the Pacific end.")
t(True, "hard", "UK geography", ["Newcastle", "Belfast"], "Newcastle is further north than Belfast.")
t(True, "hard", "Nature", ["dinosaurs", "time"], "Tyrannosaurus rex lived closer in time to us than to Stegosaurus.")

# --- second batch (the classics above were already in the bank) ---
t(False, "hard", "World geography", ["Moscow", "Glasgow", "latitude"], "Moscow is further north than Glasgow.")
t(True, "hard", "World geography", ["London", "Canada", "latitude"], "London is further north than Calgary.")
t(True, "hard", "World geography", ["Africa", "hemispheres"], "Africa lies in all four hemispheres.")
t(True, "hard", "The United States", ["Detroit", "Canada"], "From Detroit, you travel south to reach Canada.")
t(True, "hard", "World geography", ["lakes", "Russia"], "Lake Baikal holds more fresh water than all five of North America's Great Lakes put together.")
t(False, "medium", "Science", ["gravity", "physics"], "In a vacuum, a heavy object falls faster than a light one.")
t(False, "hard", "Nature", ["cats", "dogs", "history"], "Cats were domesticated before dogs.")
t(False, "hard", "Nature", ["flamingos", "birds"], "Flamingos are pink when they hatch.")
t(True, "medium", "Nature", ["seahorses", "fish"], "Male seahorses give birth.")
t(False, "hard", "Nature", ["penguins", "Galapagos"], "Penguins live only in the southern hemisphere.")
t(False, "hard", "Nature", ["rabbits", "mammals"], "Rabbits are rodents.")
t(True, "hard", "Famous people in history", ["Churchill", "Blenheim"], "Winston Churchill was born in a palace.")
t(True, "hard", "Shakespeare", ["Shakespeare", "wills"], "Shakespeare left his wife his 'second-best bed' in his will.")
t(True, "hard", "Music", ["Beatles", "number ones"], "'Yesterday' was never a UK number one for the Beatles.")
t(False, "medium", "Eurovision", ["ABBA", "Eurovision"], "ABBA won Eurovision with 'Dancing Queen'.")
t(False, "hard", "Music", ["Elvis", "charts"], "The first UK number one single was by Elvis Presley.")
t(False, "hard", "Games and toys", ["Monopoly", "London"], "On the London Monopoly board, Old Kent Road is cheaper than Whitechapel Road.")
t(True, "hard", "World geography", ["oceans", "plate tectonics"], "The Pacific Ocean is slowly getting smaller.")

out = os.path.join(os.path.dirname(__file__), "..", "tf-traps-1.json")
json.dump(OUT, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(OUT), "items:", sum(1 for x in OUT if x["answer"]), "true,", sum(1 for x in OUT if not x["answer"]), "false;",
      sum(1 for x in OUT if x["difficulty"] == "hard"), "hard")
