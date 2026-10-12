# Bank session 12 Oct 2026: new Wipeout boards -> bank/wipeout-78.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# decoys: stars of the other big reality shows (TOWIE, Made in Chelsea)
board("Cast members of 'Geordie Shore'", "TV", "medium", ["Geordie Shore", "reality TV", "North East"],
 ["Charlotte Crosby", "Vicky Pattison", "Gaz Beadle", "Holly Hagan", "Sophie Kasaei", "Marnie Simpson", "Scotty T", "Aaron Chalmers", "Jay Gardner", "James Tindale", "Greg Lake", "Ricci Guarnaccio", "Chloe Ferry", "Nathan Henry", "Kyle Christie"],
 ["Joey Essex", "Gemma Collins", "Mark Wright", "Spencer Matthews", "Megan McKenna"])
# decoys: real Roman sites nearby that aren't on the Wall itself
board("Roman forts built on Hadrian's Wall (watch out for the ones behind it)", "History", "hard", ["Hadrian's Wall", "Romans", "North East"],
 ["Segedunum (Wallsend)", "Newcastle", "Benwell", "Rudchester", "Halton Chesters", "Chesters", "Carrawburgh", "Housesteads", "Great Chesters", "Birdoswald", "Castlesteads", "Stanwix", "Burgh by Sands", "Drumburgh", "Bowness-on-Solway"],
 ["Vindolanda", "Arbeia (South Shields)", "Corbridge", "Hexham", "Lanchester"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-78.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
