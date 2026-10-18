# Bank session 18 Oct 2026: new Wipeout boards -> bank/wipeout-90.json (silent G, silent K). 15 right and 5 wrong each.
# (A Nearest Wins draft of North East dates came back 12 out of 12 already in the bank, so this session moved to the
# other lowest type.) Decoys need knowledge (memory: live-quiz-wipeout-decoys): the G is said in signal, signature,
# designate, resignation and malignant, though not in sign, design, resign or benign.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Words with a silent G", "Anagrams and wordplay", "hard", ["wordplay", "spelling", "silent letters"],
 ["Gnome", "Gnat", "Gnaw", "Sign", "Design", "Foreign", "Reign", "Campaign", "Champagne", "Cologne", "Align", "Benign", "Resign", "Feign", "Diaphragm"],
 ["Signal", "Signature", "Designate", "Resignation", "Malignant"])
board("Words with a silent K", "Anagrams and wordplay", "easy", ["wordplay", "spelling", "silent letters"],
 ["Knee", "Knife", "Knight", "Knock", "Knot", "Know", "Knuckle", "Knit", "Knob", "Knack", "Knead", "Knelt", "Knickers", "Knapsack", "Knowledge"],
 ["Kiln", "Kettle", "Kayak", "Ankle", "Kingdom"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-90.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
