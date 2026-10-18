# Bank session 18 Oct 2026: new Wipeout boards -> bank/wipeout-87.json (silent B, silent W). 15 right and 5 wrong each.
# Most topics already have boards (1,300+), so these use a new shape. Decoys need knowledge, not a different set
# (memory: live-quiz-wipeout-decoys): each decoy has the same letter where you DO say it, often next to a silent twin.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# decoys: the B is said (number vs numb, timber vs climb)
board("Words with a silent B", "Anagrams and wordplay", "medium", ["wordplay", "spelling", "silent letters"],
 ["Lamb", "Comb", "Thumb", "Doubt", "Debt", "Climb", "Bomb", "Tomb", "Numb", "Crumb", "Plumber", "Subtle", "Womb", "Limb", "Dumb"],
 ["Number", "Rumble", "Tumble", "Amber", "Timber"])
# decoys: the W is said (swear vs answer, twin vs two)
board("Words with a silent W", "Anagrams and wordplay", "medium", ["wordplay", "spelling", "silent letters"],
 ["Write", "Wrong", "Wrist", "Wrap", "Wreck", "Wren", "Wrinkle", "Sword", "Answer", "Two", "Who", "Whole", "Whose", "Wrestle", "Playwright"],
 ["Swear", "Twin", "Wobble", "Award", "Tweet"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-87.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
