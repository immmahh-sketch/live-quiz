# Bank session 19 Oct 2026: 3 Match questions -> bank/match-38.json (odd units of measurement, big cats' coats, quiz-show
# creators). Each topic probed against every match question in the live bank first (none of these pairs were there).
# Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Everyday life", ["units", "measurement"], "medium", "Match each unit to what it's used to measure",
  ("Hand", "A horse's height"), ("Knot", "Speed at sea"), ("Carat", "A gemstone's weight"), ("Furlong", "A horse race's distance"))
m("Nature", ["big cats", "patterns"], "medium", "Match each big cat to its coat",
  ("Leopard", "Rosettes"), ("Cheetah", "Solid black spots"), ("Tiger", "Stripes"), ("Lion", "Plain tawny"))
m("Television", ["game shows", "creators"], "hard", "Match each game show to the person who created it",
  ("Wheel of Fortune", "Merv Griffin"), ("Mastermind", "Bill Wright"), ("Pointless", "Richard Osman"), ("Robot Wars", "Marc Thorpe"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-38.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
