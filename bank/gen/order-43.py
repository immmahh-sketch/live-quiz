# Bank session 18 Oct 2026: 1 Put in order question -> bank/order-43.json (dinosaurs by when they lived).
# Probed against every order question in the live bank first. Later sitcoms, Royal Navy ranks, tempo markings, famous ships
# and geological periods were all already there, so this session adds only the one.
import json, os
OUT = []
def o(cat, tags, diff, text, items, hint):
    assert 3 <= len(items) <= 7 and len(set(items)) == len(items), text
    OUT.append({"type": "order", "text": text, "items": items, "hint": hint, "category": cat, "tags": tags, "difficulty": diff})

# about 231, 150, 125, 75 and 67 million years ago
o("Nature", ["dinosaurs", "prehistory"], "hard", "Put these dinosaurs in the order they lived, earliest first",
  ["Eoraptor", "Stegosaurus", "Iguanodon", "Velociraptor", "Tyrannosaurus rex"], "earliest first")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'order-43.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'order questions written')
