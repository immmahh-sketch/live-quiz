# Bank session 12 Oct 2026: new Wipeout boards -> bank/wipeout-75.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# decoys: Old English or French words that feel just as old
board("English words that came from the Vikings' Old Norse", "Words and language", "hard", ["Vikings", "Old Norse", "words"],
 ["Sky", "Egg", "Knife", "Window", "Husband", "Law", "Skin", "Skirt", "They", "Cake", "Ugly", "Leg", "Anger", "Berserk", "Ransack"],
 ["Shirt", "Bread", "House", "Beef", "Castle"])
# decoys: things from just before or just after her reign
board("Invented or first seen in Queen Victoria's reign (1837 to 1901)", "History", "medium", ["Victorians", "inventions"],
 ["Telephone", "Postage stamp", "Christmas card", "Christmas cracker", "Motor car", "Phonograph", "Radio", "Typewriter", "Traffic lights", "London Underground", "Dishwasher", "Escalator", "Diesel engine", "X-ray", "Light bulb"],
 ["Television", "Aeroplane", "Steam locomotive", "Tank", "Electric guitar"])
# decoys: words named after places, not people
board("Words named after a real person (watch out for places)", "Words and language", "medium", ["eponyms", "words"],
 ["Sandwich", "Saxophone", "Diesel", "Boycott", "Guillotine", "Nicotine", "Braille", "Silhouette", "Jacuzzi", "Mausoleum", "Sideburns", "Shrapnel", "Nachos", "Mesmerise", "Zeppelin"],
 ["Hamburger", "Denim", "Bikini", "Tuxedo", "Champagne"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-75.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
