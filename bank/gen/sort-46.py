# Bank session 18 Oct 2026: 4 Categorise questions -> bank/sort-46.json. Two groups, four items each. Each pair of categories
# was probed against every Categorise question in the live bank first (planets with rings or without was dropped: it splits
# exactly like the existing 'rocky planet or gas giant').
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Maths and numbers", ["shapes", "geometry", "Platonic solids"], "hard", "A Platonic solid (every face the same regular shape) or not?", "Platonic solid", "Not Platonic",
  ["Cube", "Tetrahedron", "Octahedron", "Icosahedron"], ["Cuboid", "Cylinder", "Square-based pyramid", "Triangular prism"])
s("British sitcoms", ["Roy Clarke", "David Croft", "sitcoms"], "medium", "A sitcom written by Roy Clarke or by David Croft?", "Roy Clarke", "David Croft",
  ["Last of the Summer Wine", "Open All Hours", "Keeping Up Appearances", "Rosie"], ["Dad's Army", "Hi-de-Hi!", "'Allo 'Allo!", "Are You Being Served?"])
s("British sitcoms", ["One Foot in the Grave", "Porridge", "sitcoms"], "easy", "A character from One Foot in the Grave or from Porridge?", "One Foot in the Grave", "Porridge",
  ["Victor Meldrew", "Margaret", "Mrs Warboys", "Nick Swainey"], ["Fletcher", "Godber", "Mr Mackay", "Mr Barrowclough"])
s("Television", ["cartoons", "dogs", "Hanna-Barbera", "Disney"], "medium", "A Hanna-Barbera cartoon dog or a Disney dog?", "Hanna-Barbera", "Disney",
  ["Scooby-Doo", "Muttley", "Huckleberry Hound", "Astro"], ["Pluto", "Goofy", "Lady", "Bolt"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-46.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
