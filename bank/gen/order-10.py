# Bank session 10 Oct 2026: 20 more Put in order questions -> bank/order-7.json (albums, film series, novels, popes).
# Checked against every order question in the live bank (the server also skips any whose items match one already there).
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

o("Music", ["Radiohead", "albums"], "hard", "Put these Radiohead albums in order of release, earliest first", ["Pablo Honey", "The Bends", "OK Computer", "Kid A", "Hail to the Thief", "In Rainbows", "A Moon Shaped Pool"], "earliest first")
o("Music", ["Kate Bush", "albums"], "hard", "Put these Kate Bush albums in order of release, earliest first", ["The Kick Inside", "Never for Ever", "The Dreaming", "Hounds of Love", "The Sensual World", "The Red Shoes", "Aerial"], "earliest first")
o("Music", ["Fleetwood Mac", "albums"], "medium", "Put these Fleetwood Mac albums in order of release, earliest first", ["Fleetwood Mac", "Rumours", "Tusk", "Mirage", "Tango in the Night"], "earliest first")
o("Music", ["Prince", "albums"], "hard", "Put these Prince albums in order of release, earliest first", ["1999", "Purple Rain", "Around the World in a Day", "Parade", "Sign o' the Times", "Lovesexy", "Diamonds and Pearls"], "earliest first")
o("Music", ["Rolling Stones", "albums"], "hard", "Put these Rolling Stones albums in order of release, earliest first", ["Aftermath", "Beggars Banquet", "Let It Bleed", "Sticky Fingers", "Exile on Main St.", "Some Girls", "Tattoo You"], "earliest first")
o("Music", ["Bob Dylan", "albums"], "hard", "Put these Bob Dylan albums in order of release, earliest first", ["The Freewheelin' Bob Dylan", "Highway 61 Revisited", "Blonde on Blonde", "Blood on the Tracks", "Desire", "Time Out of Mind"], "earliest first")
o("Film", ["Jurassic Park", "film series"], "medium", "Put these Jurassic Park and Jurassic World films in order of release, earliest first", ["Jurassic Park", "The Lost World: Jurassic Park", "Jurassic Park III", "Jurassic World", "Jurassic World: Fallen Kingdom", "Jurassic World Dominion", "Jurassic World Rebirth"], "earliest first")
o("Film", ["Alien", "film series"], "hard", "Put these Alien films in order of release, earliest first", ["Alien", "Aliens", "Alien 3", "Alien Resurrection", "Prometheus", "Alien: Covenant", "Alien: Romulus"], "earliest first")
o("Film", ["Terminator", "film series"], "medium", "Put these Terminator films in order of release, earliest first", ["The Terminator", "Terminator 2: Judgment Day", "Terminator 3: Rise of the Machines", "Terminator Salvation", "Terminator Genisys", "Terminator: Dark Fate"], "earliest first")
o("Film", ["Indiana Jones", "film series"], "easy", "Put these Indiana Jones films in order of release, earliest first", ["Raiders of the Lost Ark", "Indiana Jones and the Temple of Doom", "Indiana Jones and the Last Crusade", "Indiana Jones and the Kingdom of the Crystal Skull", "Indiana Jones and the Dial of Destiny"], "earliest first")
o("Film", ["Despicable Me", "Minions", "animation"], "medium", "Put these Despicable Me and Minions films in order of release, earliest first", ["Despicable Me", "Despicable Me 2", "Minions", "Despicable Me 3", "Minions: The Rise of Gru", "Despicable Me 4"], "earliest first")
o("Film", ["Ice Age", "animation"], "medium", "Put these Ice Age films in order of release, earliest first", ["Ice Age", "Ice Age: The Meltdown", "Ice Age: Dawn of the Dinosaurs", "Ice Age: Continental Drift", "Ice Age: Collision Course"], "earliest first")
o("Film", ["Mad Max", "film series"], "medium", "Put these Mad Max films in order of release, earliest first", ["Mad Max", "Mad Max 2", "Mad Max Beyond Thunderdome", "Mad Max: Fury Road", "Furiosa: A Mad Max Saga"], "earliest first")
o("Film", ["Pirates of the Caribbean", "film series"], "medium", "Put these Pirates of the Caribbean films in order of release, earliest first", ["The Curse of the Black Pearl", "Dead Man's Chest", "At World's End", "On Stranger Tides", "Dead Men Tell No Tales"], "earliest first")
o("Film", ["Twilight", "film series"], "easy", "Put these Twilight films in order of release, earliest first", ["Twilight", "New Moon", "Eclipse", "Breaking Dawn – Part 1", "Breaking Dawn – Part 2"], "earliest first")
o("Film", ["Ghostbusters", "film series"], "medium", "Put these Ghostbusters films in order of release, earliest first", ["Ghostbusters (1984)", "Ghostbusters II", "Ghostbusters (2016)", "Ghostbusters: Afterlife", "Ghostbusters: Frozen Empire"], "earliest first")
o("Film", ["Superman", "actors"], "medium", "Put these actors in the order they first played Superman on film, earliest first", ["George Reeves", "Christopher Reeve", "Brandon Routh", "Henry Cavill", "David Corenswet"], "earliest first")
o("TV", ["Star Trek", "captains"], "hard", "Put these Star Trek captains in the order their series began, earliest first", ["Kirk", "Picard", "Sisko", "Janeway", "Archer"], "earliest first")
o("Books", ["Brontë sisters", "novels"], "hard", "Put these Brontë novels in order of publication, earliest first", ["Jane Eyre", "Wuthering Heights", "The Tenant of Wildfell Hall", "Shirley", "Villette"], "earliest first")
o("History", ["popes", "Catholic Church"], "hard", "Put these popes in order, earliest first", ["John XXIII", "Paul VI", "John Paul I", "John Paul II", "Benedict XVI", "Francis", "Leo XIV"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-7.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
