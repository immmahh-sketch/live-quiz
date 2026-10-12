# Bank session 12 Oct 2026: 3 more Categorise questions -> bank/sort-37.json. Two groups, three or four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("The North East of England", ["bridges", "Tyne", "Wear"], "medium", "A bridge over the Tyne or over the Wear?", "Tyne", "Wear",
  ["High Level Bridge", "Swing Bridge", "Redheugh Bridge", "King Edward VII Bridge"], ["Wearmouth Bridge", "Northern Spire", "Queen Alexandra Bridge", "Prebends Bridge"])
s("Music", ["Girls Aloud", "Little Mix", "North East"], "medium", "A Girls Aloud song or a Little Mix song?", "Girls Aloud", "Little Mix",
  ["Sound of the Underground", "The Promise", "Something Kinda Ooooh", "Biology"], ["Wings", "Shout Out to My Ex", "Black Magic", "Touch"])
s("TV", ["Vera", "Line of Duty", "detectives"], "medium", "A character in 'Vera' or in 'Line of Duty'?", "Vera", "Line of Duty",
  ["Joe Ashworth", "Aiden Healy", "Kenny Lockhart", "Malcolm Donahue"], ["Ted Hastings", "Steve Arnott", "Kate Fleming", "Tony Gates"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-37.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
