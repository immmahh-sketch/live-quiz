# Bank session 18 Oct 2026: new Wipeout boards -> bank/wipeout-88.json (silent P, silent H). 15 right and 5 wrong each.
# Same shape as wipeout-87 (silent B and W); no other board in the bank is about silent letters. Decoys need knowledge
# (memory: live-quiz-wipeout-decoys): the same letter where you DO say it, often beside a silent twin (upbeat/cupboard, inhale/exhaust).
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words with a silent P", "Anagrams and wordplay", "medium", ["wordplay", "spelling", "silent letters"],
 ["Psychology", "Pneumonia", "Psalm", "Pterodactyl", "Raspberry", "Receipt", "Cupboard", "Corps", "Coup", "Psychic", "Pseudonym", "Ptarmigan", "Pneumatic", "Psoriasis", "Psyche"],
 ["Upbeat", "Lapse", "Capsule", "Collapse", "Pastry"])
board("Words with a silent H", "Anagrams and wordplay", "medium", ["wordplay", "spelling", "silent letters"],
 ["Hour", "Honest", "Heir", "Honour", "Ghost", "Rhyme", "Rhythm", "Rhubarb", "Ghastly", "Thames", "Thomas", "Exhaust", "Vehicle", "Shepherd", "Khaki"],
 ["Inhale", "Hotel", "Hostage", "Behave", "Hospital"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-88.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
