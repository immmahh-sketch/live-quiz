# Bank session 18 Oct 2026: 4 Categorise questions -> bank/sort-47.json. Two groups, four items each. Each pair of categories
# was probed against every Categorise question in the live bank first (Northumberland or County Durham was already there).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("History", ["steam", "railways", "LNER", "GWR"], "hard", "A steam engine built for the LNER or for the Great Western?", "LNER", "Great Western",
  ["Flying Scotsman", "Mallard", "Green Arrow", "Sir Nigel Gresley"], ["City of Truro", "King George V", "Caerphilly Castle", "Pendennis Castle"])
s("Money", ["old money", "coins", "pre-decimal"], "medium", "Old money: worth more than a shilling or less?", "More than a shilling", "Less than a shilling",
  ["Florin", "Half-crown", "Crown", "Guinea"], ["Farthing", "Ha'penny", "Threepenny bit", "Sixpence"])
s("British sitcoms", ["Men Behaving Badly", "Rising Damp", "sitcoms"], "easy", "A character from Men Behaving Badly or from Rising Damp?", "Men Behaving Badly", "Rising Damp",
  ["Gary", "Tony", "Dorothy", "Deborah"], ["Rigsby", "Miss Jones", "Alan", "Philip"])
s("British sitcoms", ["Red Dwarf", "The Vicar of Dibley", "sitcoms"], "easy", "A character from Red Dwarf or from The Vicar of Dibley?", "Red Dwarf", "The Vicar of Dibley",
  ["Lister", "Rimmer", "Kryten", "Holly"], ["Geraldine", "Alice", "Owen", "Jim Trott"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-47.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
