# Bank session 18 Oct 2026: 3 Categorise questions -> bank/sort-53.json. Two groups, three or four items each. Each pair of
# categories was probed against every Categorise question in the live bank first (Cluedo suspect v weapon, Monopoly square v
# Cluedo room and Crystal Maze zone v Gladiators event exist, but not these pairs).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Everyday life", ["cars", "Ford", "Vauxhall"], "medium", "A Ford or a Vauxhall?", "Ford", "Vauxhall",
  ["Fiesta", "Focus", "Escort", "Capri"], ["Corsa", "Astra", "Nova", "Cavalier"])
s("Games and puzzles", ["Monopoly", "Cluedo", "board games"], "medium", "A Monopoly token or a Cluedo weapon?", "Monopoly token", "Cluedo weapon",
  ["Top hat", "Boot", "Thimble", "Iron"], ["Candlestick", "Rope", "Dagger", "Lead pipe"])
s("Nature", ["birds", "seabirds", "garden birds"], "easy", "A garden bird or a seabird?", "Garden bird", "Seabird",
  ["Robin", "Blue tit", "Wren", "Blackbird"], ["Puffin", "Gannet", "Guillemot", "Kittiwake"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-53.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
