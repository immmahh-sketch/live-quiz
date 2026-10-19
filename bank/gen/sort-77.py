# Bank session 19 Oct 2026: 2 Categorise questions -> bank/sort-77.json. Each pair of categories was probed against every
# Categorise question in the live bank first (no Sweeney v Bill character sort; a hibernates-or-migrates sort exists, so this one
# sets hibernators against animals that stay active all winter, and only the hedgehog and dormouse are shared).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Television", ["The Sweeney", "The Bill", "police"], "medium", "A character from The Sweeney or from The Bill?", "The Sweeney", "The Bill",
  ["Jack Regan", "George Carter", "Frank Haskins"], ["June Ackland", "Reg Hollis", "Tosh Lines", "Bob Cryer"])
# badgers slow down in cold spells but don't truly hibernate; red squirrels and moles stay active
s("Nature", ["hibernation", "winter", "British wildlife"], "medium", "Does it hibernate, or stay active all winter?", "Hibernates", "Stays active",
  ["Hedgehog", "Dormouse", "Adder", "Common toad"], ["Fox", "Badger", "Red squirrel", "Mole"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-77.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
