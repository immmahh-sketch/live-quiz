# Bank session 11 Oct 2026: new Wipeout boards -> bank/wipeout-50.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Mountains in Scotland (not England or Wales)", "UK geography", "medium", ["Scotland", "mountains", "Munros"],
 ["Ben Nevis", "Ben Macdui", "Braeriach", "Cairn Toul", "Cairn Gorm", "Ben Lawers", "Ben More", "Ben Lomond", "Schiehallion", "Lochnagar", "Buachaille Etive Mòr", "An Teallach", "Suilven", "Stac Pollaidh", "Sgùrr Alasdair"],
 ["Scafell Pike", "Helvellyn", "Snowdon", "Cadair Idris", "Pen y Fan"])
board("Operas by Mozart or by Puccini", "Music", "hard", ["opera", "Mozart", "Puccini"],
 ["The Magic Flute", "Don Giovanni", "The Marriage of Figaro", "Così fan tutte", "The Abduction from the Seraglio", "Idomeneo", "La clemenza di Tito", "La bohème", "Tosca", "Madama Butterfly", "Turandot", "Gianni Schicchi", "Manon Lescaut", "La fanciulla del West", "Il tabarro"],
 ["Carmen", "Aida", "La traviata", "The Barber of Seville", "Fidelio"])
board("Words that make a new word when you put 'book' in front", "Words and language", "medium", ["wordplay", "compound words"],
 ["Case", "Mark", "Shelf", "Shop", "Worm", "Keeper", "Maker", "End", "Let", "Stall", "Club", "Store", "Plate", "Binder", "Ish"],
 ["Paper", "Page", "Cover", "Spine", "Hand"])
board("Words that make a new word when you put 'house' in front", "Words and language", "medium", ["wordplay", "compound words"],
 ["Boat", "Wife", "Hold", "Work", "Keeper", "Plant", "Fly", "Coat", "Proud", "Mate", "Guest", "Warming", "Bound", "Party", "Husband"],
 ["Door", "Roof", "Window", "Garden", "Chair"])
board("Words that make a new word when you put 'night' in front", "Words and language", "medium", ["wordplay", "compound words"],
 ["Mare", "Club", "Fall", "Gown", "Cap", "Shift", "Life", "Light", "Time", "Dress", "Owl", "Shade", "Watchman", "Stand", "Jar"],
 ["Moon", "Star", "Dark", "Sleep", "Bed"])
board("Words that make a new word when you put 'home' in front", "Words and language", "medium", ["wordplay", "compound words"],
 ["Work", "Sick", "Made", "Grown", "Coming", "Land", "Page", "Town", "Owner", "Less", "Ware", "Stead", "Spun", "Brew", "Maker"],
 ["Door", "Roof", "Key", "Garden", "Wall"])
board("Words that make a new word when you put 'life' in front", "Words and language", "medium", ["wordplay", "compound words"],
 ["Boat", "Guard", "Line", "Time", "Style", "Long", "Less", "Saver", "Like", "Size", "Span", "Blood", "Belt", "Jacket", "Cycle"],
 ["Death", "Breath", "Shoe", "Book", "Day"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-50.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
