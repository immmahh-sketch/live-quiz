# Bank session 12 Oct 2026: 4 more Match questions -> bank/match-23.json (fictional pigs and dogs, jazz instruments, New Year traditions).
# Each title checked against every match question in the live bank. Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Books", ["pigs", "fictional animals"], "medium", "Match each fictional pig to the story it's from",
  ("Wilbur", "Charlotte's Web"), ("Napoleon", "Animal Farm"), ("Piglet", "Winnie-the-Pooh"), ("Hamm", "Toy Story"))
m("TV", ["dogs", "fictional animals"], "easy", "Match each fictional dog to its owner",
  ("Gromit", "Wallace"), ("Snowy", "Tintin"), ("Toto", "Dorothy"), ("Fang", "Hagrid"))
m("Music", ["jazz", "instruments"], "medium", "Match each jazz legend to their instrument",
  ("Miles Davis", "Trumpet"), ("Charlie Parker", "Saxophone"), ("Thelonious Monk", "Piano"), ("Benny Goodman", "Clarinet"))
m("Scotland", ["Hogmanay", "New Year", "traditions"], "hard", "Match each New Year tradition to where it happens",
  ("Swinging fireballs", "Stonehaven"), ("The Loony Dook", "South Queensferry"), ("Up Helly Aa", "Lerwick"), ("The big street party", "Edinburgh"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-23.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
