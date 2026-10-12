# Bank session 12 Oct 2026: new Wipeout boards -> bank/wipeout-86.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# decoys: Scottish lighthouses
board("Lighthouses on the coasts of England and Wales", "UK geography", "hard", ["lighthouses", "coast", "North East"],
 ["Bishop Rock", "Wolf Rock", "Longships", "The Lizard", "Godrevy", "The Needles", "St Catherine's", "Portland Bill", "Dungeness", "North Foreland", "Flamborough Head", "Spurn", "St Mary's", "Coquet", "South Stack"],
 ["Kinnaird Head", "Cape Wrath", "Neist Point", "Mull of Galloway", "Butt of Lewis"])
# decoys: fabrics from animals, and man-made ones
board("Fabrics made from plants", "Fashion", "medium", ["fabrics", "cotton", "plants"],
 ["Cotton", "Linen", "Hemp", "Jute", "Ramie", "Bamboo", "Denim", "Corduroy", "Muslin", "Calico", "Chambray", "Seersucker", "Gingham", "Hessian", "Canvas"],
 ["Silk", "Cashmere", "Tweed", "Polyester", "Nylon"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-86.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
