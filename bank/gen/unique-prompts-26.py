# Bank session 11 Oct 2026: 8 more Only One prompts (album lists and film series not yet in the file) appended to bank/unique-prompts.json.
# Each is a closed list with every correct answer (other accepted forms after a slash), so a fair answer is never knocked out.
import json, os
NEW = [
 ("Name a studio album by Pulp", ["It", "Freaks", "Separations", "His 'n' Hers/His n Hers", "Different Class", "This Is Hardcore", "We Love Life", "More"]),
 ("Name a studio album by Led Zeppelin", ["Led Zeppelin/Led Zeppelin I", "Led Zeppelin II", "Led Zeppelin III", "Led Zeppelin IV/Untitled/Four Symbols/Zoso", "Houses of the Holy", "Physical Graffiti", "Presence", "In Through the Out Door", "Coda"]),
 ("Name a studio album by the Smiths or by the Stone Roses", ["The Smiths", "Meat Is Murder", "The Queen Is Dead", "Strangeways, Here We Come/Strangeways", "The Stone Roses", "Second Coming"]),
 ("Name a studio album by Kylie Minogue, up to 2025", ["Kylie", "Enjoy Yourself", "Rhythm of Love", "Let's Get to It", "Kylie Minogue", "Impossible Princess", "Light Years", "Fever", "Body Language", "X", "Aphrodite", "Kiss Me Once", "Kylie Christmas", "Golden", "Disco", "Tension", "Tension II"]),
 ("Name a film in the Alien or Terminator series (the Predator crossovers count), up to 2025", ["Alien", "Aliens", "Alien 3/Alien³", "Alien Resurrection", "Prometheus", "Alien: Covenant/Alien Covenant", "Alien: Romulus/Alien Romulus/Romulus", "Alien vs. Predator/AVP/Alien vs Predator", "Aliens vs. Predator: Requiem/AVP Requiem", "The Terminator/Terminator", "Terminator 2: Judgment Day/Terminator 2/T2", "Terminator 3: Rise of the Machines/Terminator 3/T3", "Terminator Salvation", "Terminator Genisys", "Terminator: Dark Fate/Dark Fate"]),
 ("Name a Pirates of the Caribbean film or a Men in Black film", ["The Curse of the Black Pearl/Curse of the Black Pearl", "Dead Man's Chest", "At World's End", "On Stranger Tides", "Dead Men Tell No Tales/Salazar's Revenge", "Men in Black", "Men in Black II/Men in Black 2", "Men in Black 3", "Men in Black: International/Men in Black International"]),
 ("Name a film in the Mad Max or Matrix series", ["Mad Max", "Mad Max 2/The Road Warrior", "Mad Max Beyond Thunderdome/Beyond Thunderdome", "Mad Max: Fury Road/Fury Road", "Furiosa/Furiosa: A Mad Max Saga", "The Matrix/Matrix", "The Matrix Reloaded/Matrix Reloaded", "The Matrix Revolutions/Matrix Revolutions", "The Matrix Resurrections/Matrix Resurrections"]),
 ("Name a film in the Ice Age, Kung Fu Panda or Despicable Me/Minions series, up to 2025", ["Ice Age", "Ice Age: The Meltdown/The Meltdown", "Ice Age: Dawn of the Dinosaurs/Dawn of the Dinosaurs", "Ice Age: Continental Drift/Continental Drift", "Ice Age: Collision Course/Collision Course", "The Ice Age Adventures of Buck Wild/Buck Wild", "Kung Fu Panda", "Kung Fu Panda 2", "Kung Fu Panda 3", "Kung Fu Panda 4", "Despicable Me", "Despicable Me 2", "Despicable Me 3", "Despicable Me 4", "Minions", "Minions: The Rise of Gru/The Rise of Gru"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
