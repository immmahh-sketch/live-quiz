# Bank session 19 Oct 2026: 2 Categorise questions -> bank/sort-55.json. Two groups, four items each. Each pair of categories
# was probed against every Categorise question in the live bank first (old units of length v weight was already there).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

# snow leopards, like cheetahs and pumas, can't roar
s("Nature", ["big cats", "roaring"], "hard", "A cat that can roar or one that can't?", "Can roar", "Can't roar",
  ["Lion", "Tiger", "Jaguar", "Leopard"], ["Cheetah", "Puma", "Lynx", "Snow leopard"])
s("Nature", ["poultry", "breeds", "farming"], "medium", "A breed of hen or a breed of duck?", "Hen", "Duck",
  ["Rhode Island Red", "Leghorn", "Orpington", "Silkie"], ["Aylesbury", "Indian Runner", "Khaki Campbell", "Pekin"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-55.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
