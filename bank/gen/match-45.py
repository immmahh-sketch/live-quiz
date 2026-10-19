# Bank session 19 Oct 2026: 3 Match questions -> bank/match-45.json (Rik Mayall's characters, Blackadder's cast, garden
# birds' colourful features). Each topic probed against every match question in the live bank first (none of these pairs
# were there). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Comedy", ["Rik Mayall", "characters"], "medium", "Match each Rik Mayall character to the show he's from",
  ("Rick", "The Young Ones"), ("Richie", "Bottom"), ("Lord Flashheart", "Blackadder"), ("Alan B'Stard", "The New Statesman"))
m("Comedy", ["Blackadder", "actors"], "easy", "Match each actor to their Blackadder role",
  ("Rowan Atkinson", "Blackadder"), ("Tony Robinson", "Baldrick"), ("Hugh Laurie", "Prince George"), ("Stephen Fry", "Lord Melchett"))
m("Nature", ["birds", "British wildlife", "colours"], "medium", "Match each garden bird to its splash of colour",
  ("Robin", "Orange-red breast"), ("Goldfinch", "Red face"), ("Blue tit", "Blue cap"), ("Bullfinch", "Rosy-pink chest"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-45.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
