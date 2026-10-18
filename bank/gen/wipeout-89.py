# Bank session 18 Oct 2026: new Wipeout boards -> bank/wipeout-89.json (silent L, silent T). 15 right and 5 wrong each.
# Same shape as wipeout-87/88. Decoys need knowledge (memory: live-quiz-wipeout-decoys): the same letter where you DO say it,
# spelt like a silent twin (milk/walk, pastel/castle). 'Often' left out: half of Britain says the T.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words with a silent L", "Anagrams and wordplay", "medium", ["wordplay", "spelling", "silent letters"],
 ["Walk", "Talk", "Chalk", "Half", "Calf", "Calm", "Palm", "Salmon", "Could", "Would", "Should", "Folk", "Yolk", "Almond", "Balm"],
 ["Milk", "Film", "Bald", "Malt", "Wolf"])
board("Words with a silent T", "Anagrams and wordplay", "medium", ["wordplay", "spelling", "silent letters"],
 ["Listen", "Castle", "Whistle", "Fasten", "Christmas", "Mortgage", "Ballet", "Buffet", "Soften", "Thistle", "Rustle", "Hustle", "Glisten", "Moisten", "Gourmet"],
 ["Pastel", "Mantle", "Kettle", "Basket", "Captain"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-89.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
