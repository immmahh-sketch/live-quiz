# Bank session 18 Oct 2026: new Wipeout boards -> bank/wipeout-91.json (silent U, silent C). 15 right and 5 wrong each.
# Same shape as wipeout-87 to 90. Decoys need knowledge (memory: live-quiz-wipeout-decoys): the same letter where you DO say it,
# spelt like a silent twin (penguin/guitar, language/tongue; scone/scene, discuss/discipline).
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words with a silent U", "Anagrams and wordplay", "hard", ["wordplay", "spelling", "silent letters"],
 ["Guess", "Guitar", "Guest", "Guard", "Guide", "Biscuit", "Build", "Circuit", "Colleague", "League", "Tongue", "Rogue", "Vague", "Plague", "Catalogue"],
 ["Penguin", "Language", "Linguist", "Guava", "Argue"])
board("Words with a silent C", "Anagrams and wordplay", "hard", ["wordplay", "spelling", "silent letters"],
 ["Scissors", "Muscle", "Scene", "Science", "Scent", "Descend", "Fascinate", "Ascend", "Crescent", "Discipline", "Indict", "Yacht", "Acquire", "Acquaint", "Scenic"],
 ["Scarf", "Scone", "Mascot", "Escape", "Discuss"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-91.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
