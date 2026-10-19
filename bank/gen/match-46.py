# Bank session 19 Oct 2026: 2 Match questions -> bank/match-46.json (sitcom catchphrases, UK and European cities' rivers). Each
# topic probed against every match question in the live bank first (a 'Lovely jubbly / I don't believe it' catchphrase set and
# Irish and capital-city rivers were there, so these use different pairs). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Comedy", ["sitcoms", "catchphrases"], "easy", "Match each sitcom line to the show it comes from",
  ("Such fun!", "Miranda"), ("Power to the people!", "Citizen Smith"), ("Stupid boy!", "Dad's Army"), ("Smoke me a kipper, I'll be back for breakfast", "Red Dwarf"))
m("World geography", ["rivers", "cities"], "hard", "Match each city to the river that runs through it",
  ("Belfast", "Lagan"), ("Munich", "Isar"), ("Swansea", "Tawe"), ("Inverness", "Ness"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-46.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
