# Bank session 13 Oct 2026: 1 more general race -> bank/race-224.json (Punch and Judy). Checked against every race in stock;
# slapstick, clown and custard pie left out (panto and circus races); the panto race's catchphrases are used as traps here.
# 20 rows each, target 10; wrong options are the same kind of thing, never another row's right answer, and never also right for that row.
import json, os
R = []
def race(title, cat, diff, tags, rows):
    rights = {r[1] for r in rows}
    assert len(rows) == 20, (title, len(rows))
    assert len(rights) == 20, (title, 'duplicate right answers')
    bad = [(q, w) for q, right, wrong in rows for w in wrong if w in rights]
    assert not bad, (title, 'recycled', bad)
    for q, right, wrong in rows:
        assert len(wrong) == 3 and len(set(wrong)) == 3 and right not in wrong, (title, q)
    R.append({"type": "race", "text": "The Race: " + title, "target": 10, "category": cat, "tags": tags, "difficulty": diff,
              "bank": [{"q": q, "right": right, "wrong": wrong} for q, right, wrong in rows]})

race("what's this Punch and Judy word?", "Everyday life", "medium", ["Punch and Judy", "seaside", "puppets", "words"], [
 ("The hook-nosed puppet with the big stick", "Mr Punch", ["Mr Toad", "Mr Pickwick", "Mr Bumble"]),
 ("Punch's long-suffering wife", "Judy", ["Joan", "Polly", "Pearl"]),
 ("Who Punch famously throws out of the booth", "The Baby", ["The Cat", "The Parrot", "The Goose"]),
 ("Punch's dog", "Toby", ["Rover", "Spot", "Fido"]),
 ("The snapping beast after the sausages", "Crocodile", ["Shark", "Dragon", "Wolf"]),
 ("What the crocodile is after", "Sausages", ["Pies", "Kippers", "Pasties"]),
 ("The officer Punch gets the better of", "Policeman", ["Soldier", "Judge", "Sheriff"]),
 ("The clown named after the famous Grimaldi", "Joey", ["Coco", "Bozo", "Pierrot"]),
 ("Jack Ketch, whom Punch tricks into his own noose", "Hangman", ["Jailer", "Bailiff", "Gamekeeper"]),
 ("Who Punch beats at the very end of some old shows", "The Devil", ["The Bogeyman", "The Giant", "The Dragon"]),
 ("Punch's famous catchphrase", "That's the way to do it!", ["Oh no it isn't!", "Behind you!", "Nice to see you!"]),
 ("What the puppeteer is traditionally called", "Professor", ["Doctor", "Captain", "Master"]),
 ("The reed in the puppeteer's mouth that makes Punch's voice", "Swazzle", ["Kazoo", "Whistle", "Harmonica"]),
 ("The striped tent the show is played in", "Booth", ["Kiosk", "Gazebo", "Marquee"]),
 ("The assistant who collects money from the crowd", "Bottler", ["Barker", "Busker", "Rigger"]),
 ("The diarist who saw the first recorded show in England, in 1662", "Samuel Pepys", ["John Evelyn", "Daniel Defoe", "Samuel Johnson"]),
 ("Where that first recorded show took place", "Covent Garden", ["Hyde Park", "Brighton Pier", "Greenwich"]),
 ("What kind of puppet Punch is", "Glove puppet", ["Marionette", "Shadow puppet", "Ventriloquist's dummy"]),
 ("Where Punch began, as Pulcinella", "Italy", ["France", "Spain", "Greece"]),
 ("The bump on Mr Punch's back", "Hump", ["Bustle", "Rucksack", "Saddle"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-224.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
