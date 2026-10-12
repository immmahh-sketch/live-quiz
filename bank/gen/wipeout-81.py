# Bank session 12 Oct 2026: new Wipeout boards -> bank/wipeout-81.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# decoys: famous saints from elsewhere in Britain and Ireland
board("Saints of the North East of England", "History", "hard", ["saints", "Northumbria", "North East"],
 ["St Cuthbert", "St Aidan", "St Bede", "St Hilda", "St Oswald", "St Wilfrid", "St Godric", "St Benedict Biscop", "St Ceolfrith", "St Eata", "St Chad", "St Cedd", "St Oswin", "St Edwin", "St Æthelwold"],
 ["St Columba", "St Patrick", "St David", "St Augustine", "St Swithun"])
# decoys: the Danish kings who ruled England, and the one who was never crowned
board("Anglo-Saxon kings of Wessex or England (watch out for the Danes)", "History", "hard", ["Anglo-Saxons", "kings", "Wessex"],
 ["Egbert", "Æthelwulf", "Æthelbald", "Alfred the Great", "Edward the Elder", "Athelstan", "Edmund I", "Eadred", "Eadwig", "Edgar the Peaceful", "Edward the Martyr", "Æthelred the Unready", "Edmund Ironside", "Edward the Confessor", "Harold Godwinson"],
 ["Cnut", "Harold Harefoot", "Harthacnut", "Sweyn Forkbeard", "Edgar Ætheling"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-81.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
