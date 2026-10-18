# Bank session 19 Oct 2026: 3 Categorise questions -> bank/sort-57.json. Two groups, four items each. Each pair of categories
# was probed against every Categorise question in the live bank first (Derry Girls v Father Ted and shop v office sitcoms
# exist, but not these pairs).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Comedy", ["The IT Crowd", "Father Ted", "Graham Linehan"], "easy", "An IT Crowd character or a Father Ted character?", "The IT Crowd", "Father Ted",
  ["Roy", "Moss", "Jen", "Douglas Reynholm"], ["Dougal", "Mrs Doyle", "Father Jack", "Bishop Brennan"])
s("Comedy", ["Steptoe and Son", "Only Fools and Horses", "sitcoms"], "medium", "From Steptoe and Son or from Only Fools and Horses?", "Steptoe and Son", "Only Fools and Horses",
  ["Albert", "Harold", "Hercules the horse", "Oil Drum Lane"], ["Rodney", "Trigger", "Boycie", "Nelson Mandela House"])
s("Comedy", ["Are You Being Served?", "Some Mothers Do 'Ave 'Em", "1970s sitcoms"], "medium", "From Are You Being Served? or from Some Mothers Do 'Ave 'Em?", "Are You Being Served?", "Some Mothers Do 'Ave 'Em",
  ["Mrs Slocombe", "Captain Peacock", "Mr Humphries", "Young Mr Grace"], ["Frank Spencer", "Betty", "Baby Jessica", "The beret"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-57.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
