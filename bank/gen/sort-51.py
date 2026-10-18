# Bank session 18 Oct 2026: 4 Categorise questions -> bank/sort-51.json. Two groups, three or four items each. Each pair of
# categories was probed against every Categorise question in the live bank first (Forsyth-hosted or not, Tarrant v Edmonds and
# Top Gear v Countryfile exist, but not these pairs).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Television", ["University Challenge", "Mastermind", "quiz hosts"], "medium", "A University Challenge host or a Mastermind host?", "University Challenge", "Mastermind",
  ["Bamber Gascoigne", "Jeremy Paxman", "Amol Rajan"], ["Magnus Magnusson", "John Humphrys", "Clive Myrie", "Peter Snow"])
s("Children's TV", ["Thunderbirds", "Stingray", "Gerry Anderson"], "medium", "A Thunderbirds character or a Stingray character?", "Thunderbirds", "Stingray",
  ["Lady Penelope", "Brains", "Parker", "Jeff Tracy"], ["Troy Tempest", "Marina", "Phones", "Commander Shore"])
s("Nature", ["apes", "monkeys", "primates"], "medium", "An ape or a monkey?", "Ape", "Monkey",
  ["Gorilla", "Orangutan", "Chimpanzee", "Gibbon"], ["Baboon", "Mandrill", "Capuchin", "Marmoset"])
# wild turkeys and peacocks can both fly short distances
s("Nature", ["birds", "flightless birds"], "hard", "Can this bird fly or not?", "Can fly", "Can't fly",
  ["Turkey", "Peacock", "Pheasant", "Puffin"], ["Kiwi", "Kakapo", "Cassowary", "Rhea"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-51.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
