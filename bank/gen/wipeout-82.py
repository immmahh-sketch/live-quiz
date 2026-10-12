# Bank session 12 Oct 2026: new Wipeout boards -> bank/wipeout-82.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# decoys: old coins from the rest of Europe
board("Old British coins (before decimal day, or long before)", "History", "medium", ["coins", "money", "pre-decimal"],
 ["Farthing", "Halfpenny", "Penny", "Threepenny bit", "Sixpence", "Shilling", "Florin", "Half crown", "Crown", "Groat", "Guinea", "Sovereign", "Half sovereign", "Noble", "Angel"],
 ["Ducat", "Doubloon", "Thaler", "Franc", "Groschen"])
# decoys: the kings just either side of the dates, a Scottish king, and a queen who was never crowned
board("Kings of England between 1066 and 1485", "History", "medium", ["kings", "Normans", "Plantagenets"],
 ["William the Conqueror", "William Rufus", "Henry I", "Stephen", "Henry II", "Richard the Lionheart", "King John", "Henry III", "Edward I", "Edward II", "Edward III", "Richard II", "Henry V", "Edward IV", "Richard III"],
 ["Henry VII", "Harold Godwinson", "Edward VI", "Robert the Bruce", "Empress Matilda"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-82.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
