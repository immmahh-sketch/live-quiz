# Bank session 12 Oct 2026: new Wipeout boards -> bank/wipeout-76.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# decoys: the classic "vegetables" that really aren't fruit (rhubarb is a stalk)
board("Things botanists class as fruit (cooks call most of them veg)", "Food and drink", "medium", ["fruit", "vegetables", "botany"],
 ["Tomato", "Cucumber", "Aubergine", "Courgette", "Pepper", "Pumpkin", "Avocado", "Olive", "Chilli", "Okra", "Butternut squash", "Marrow", "Green bean", "Mangetout", "Sweetcorn"],
 ["Rhubarb", "Carrot", "Potato", "Celery", "Asparagus"])
# rights reversed: desserts, reward, repaid, evil, rats, spoons, strap, reviled, pots, emit, flow, peek, plug, trams, lager
board("Words that spell a different word backwards", "Words and language", "medium", ["words", "wordplay", "backwards"],
 ["Stressed", "Drawer", "Diaper", "Live", "Star", "Snoops", "Parts", "Deliver", "Stop", "Time", "Wolf", "Keep", "Gulp", "Smart", "Regal"],
 ["Lemon", "Planet", "Garden", "Butter", "Window"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-76.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
