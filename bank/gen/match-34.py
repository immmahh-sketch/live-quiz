# Bank session 18 Oct 2026: 3 Match questions -> bank/match-34.json (game-show catchphrases to hosts, primates to their
# homes, animal body counts). Each topic probed against every match question in the live bank first (quiz shows to hosts,
# snooker values and other catchphrase sets were already there, so these use different pairs). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Television", ["catchphrases", "game shows", "hosts"], "medium", "Match each game-show catchphrase to the host who said it",
  ("Your starter for ten", "Bamber Gascoigne"), ("Super, smashing, great!", "Jim Bowen"), ("Shut that door!", "Larry Grayson"), ("Is that your final answer?", "Chris Tarrant"))
m("Nature", ["primates", "monkeys", "apes"], "medium", "Match each primate to where it lives in the wild",
  ("Ring-tailed lemur", "Madagascar"), ("Orangutan", "Borneo and Sumatra"), ("Mountain gorilla", "Central Africa"), ("Capuchin monkey", "Central and South America"))
m("Nature", ["animals", "numbers"], "easy", "Match each to the right number",
  ("Hearts in an octopus", "3"), ("Arms on a common starfish", "5"), ("Legs on a spider", "8"), ("Humps on a dromedary", "1"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-34.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
