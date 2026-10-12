# Bank session 12 Oct 2026: new Wipeout boards -> bank/wipeout-84.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# decoys: great Benedictine houses, the other big order
board("Cistercian abbeys in England and Wales", "History", "hard", ["monasteries", "Cistercians", "abbeys"],
 ["Fountains", "Rievaulx", "Tintern", "Furness", "Byland", "Jervaulx", "Kirkstall", "Roche", "Buildwas", "Beaulieu", "Whalley", "Valle Crucis", "Strata Florida", "Waverley", "Newminster"],
 ["Whitby", "Durham", "Westminster", "Glastonbury", "Bury St Edmunds"])
# rights: Iron Curtain, Iron Man, Iron Lady, Ironside, Ironbridge, Iron Maiden, Iron Age, iron lung, the Iron Duke, the Iron Throne,
# The Iron Giant, ironclad, ironmonger, iron fist, ironworks
board("Words that make a new word or phrase when you put 'iron' in front", "Words and language", "medium", ["words", "wordplay", "iron"],
 ["Curtain", "Man", "Lady", "Side", "Bridge", "Maiden", "Age", "Lung", "Duke", "Throne", "Giant", "Clad", "Monger", "Fist", "Works"],
 ["Silk", "Feather", "Cloud", "Pillow", "Velvet"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-84.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
