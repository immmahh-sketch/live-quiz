# Bank session 19 Oct 2026: 3 Categorise questions -> bank/sort-58.json. Two groups, four items each. Each pair of categories
# was probed against every Categorise question in the live bank first (none of these pairs were there).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Comedy", ["Black Books", "Phoenix Nights", "sitcoms"], "easy", "From Black Books or from Phoenix Nights?", "Black Books", "Phoenix Nights",
  ["Bernard Black", "Manny", "Fran", "Nifty Gifty"], ["Brian Potter", "Max and Paddy", "Den Perry", "Les Alanos"])
s("Comedy", ["Yes Minister", "The Thick of It", "politics"], "medium", "A Yes Minister character or a Thick of It character?", "Yes Minister", "The Thick of It",
  ["Jim Hacker", "Sir Humphrey Appleby", "Bernard Woolley", "Sir Arnold Robinson"], ["Malcolm Tucker", "Nicola Murray", "Hugh Abbot", "Ollie Reeder"])
s("Comedy", ["Peter Kay", "Ricky Gervais"], "medium", "A Peter Kay show or a Ricky Gervais show?", "Peter Kay", "Ricky Gervais",
  ["Phoenix Nights", "Car Share", "That Peter Kay Thing", "Britain's Got the Pop Factor"], ["The Office", "Extras", "Derek", "After Life"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-58.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
