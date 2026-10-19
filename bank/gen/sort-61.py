# Bank session 19 Oct 2026: 3 Categorise questions -> bank/sort-61.json. Two groups, four items each. Each pair of categories
# was probed against every Categorise question in the live bank first (insect-or-not and Dinnerladies v Still Game exist,
# but not these pairs).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Comedy", ["Rab C. Nesbitt", "Still Game", "Scotland"], "easy", "A Rab C. Nesbitt character or a Still Game character?", "Rab C. Nesbitt", "Still Game",
  ["Rab", "Mary Doll", "Gash", "Jamesie"], ["Jack", "Victor", "Winston", "Navid"])
# the weever fish and lion's mane jellyfish sting; the grass and smooth snakes are harmless
s("Nature", ["British wildlife", "venom"], "hard", "A British creature that can poison or sting you, or a harmless one?", "Venomous", "Harmless",
  ["Adder", "Weever fish", "Lion's mane jellyfish", "Wasp"], ["Grass snake", "Slow worm", "Smooth snake", "Newt"])
s("Comedy", ["Benidorm", "Phoenix Nights", "sitcoms"], "easy", "From Benidorm or from Phoenix Nights?", "Benidorm", "Phoenix Nights",
  ["The Solana", "Madge", "Mateo", "The Garveys"], ["Brian Potter", "Max and Paddy", "Den Perry", "Les Alanos"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-61.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
