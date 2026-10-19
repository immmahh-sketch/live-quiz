# Bank session 19 Oct 2026: 2 Categorise questions -> bank/sort-62.json. Two groups, four items each. Each pair of categories
# was probed against every Categorise question in the live bank first (hibernates-or-migrates with the swallow, cuckoo and
# swift exists, so this uses other birds; Scottish v Welsh islands was already there and was dropped).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Nature", ["birds", "migration", "British wildlife"], "hard", "A bird that visits Britain for the summer or for the winter?", "Summer visitor", "Winter visitor",
  ["House martin", "Chiffchaff", "Willow warbler", "Nightingale"], ["Redwing", "Fieldfare", "Brambling", "Waxwing"])
s("Comedy", ["Miranda", "The Brittas Empire", "sitcoms"], "easy", "A Miranda character or a Brittas Empire character?", "Miranda", "The Brittas Empire",
  ["Stevie", "Gary", "Penny", "Tilly"], ["Gordon", "Helen", "Carole", "Laura"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-62.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
