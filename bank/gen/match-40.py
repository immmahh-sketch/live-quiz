# Bank session 19 Oct 2026: 2 Match questions -> bank/match-40.json (sitcom writers, sitcom catchphrases to who said them).
# Each topic probed against every match question in the live bank first (Only Fools / Father Ted / Red Dwarf / Porridge
# writers were already there, so these use other shows). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Comedy", ["sitcoms", "writers"], "hard", "Match each sitcom to its writer or writers",
  ("The IT Crowd", "Graham Linehan"), ("Some Mothers Do 'Ave 'Em", "Raymond Allen"), ("Yes Minister", "Antony Jay and Jonathan Lynn"), ("The Inbetweeners", "Iain Morris and Damon Beesley"))
m("Comedy", ["sitcoms", "catchphrases"], "easy", "Match each sitcom line to the character who said it",
  ("Ooh, Betty!", "Frank Spencer"), ("I'm free!", "Mr Humphries"), ("You dirty old man!", "Harold Steptoe"), ("Have you tried turning it off and on again?", "Roy"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-40.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
