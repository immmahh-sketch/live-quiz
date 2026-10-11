# Bank session 11 Oct 2026: more Categorise questions -> bank/sort-31.json. Two groups, three or four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})


s("Football", ["England", "1966", "Italia 90"], "medium", "Played for England in the 1966 final or the 1990 semi-final?", "1966 final", "1990 semi-final", ["Bobby Moore", "Geoff Hurst", "Nobby Stiles", "Gordon Banks"], ["Gary Lineker", "Paul Gascoigne", "Chris Waddle", "Peter Shilton"])
s("TV", ["Gavin & Stacey", "EastEnders"], "easy", "A Gavin & Stacey character or an EastEnders character?", "Gavin & Stacey", "EastEnders", ["Nessa", "Smithy", "Uncle Bryn", "Doris"], ["Dot Cotton", "Phil Mitchell", "Peggy Mitchell", "Ian Beale"])
s("TV", ["The Simpsons", "Family Guy", "places"], "medium", "A place in The Simpsons or in Family Guy?", "The Simpsons", "Family Guy", ["Springfield", "Moe's Tavern", "Kwik-E-Mart", "Shelbyville"], ["Quahog", "The Drunken Clam", "Pawtucket Brewery", "Spooner Street"])
s("Sport", ["England captains", "football", "cricket"], "easy", "Captained England at football or at cricket?", "Football", "Cricket", ["Bobby Moore", "Alan Shearer", "Harry Kane", "Steven Gerrard"], ["Michael Vaughan", "Joe Root", "Alastair Cook", "Ben Stokes"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-31.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
