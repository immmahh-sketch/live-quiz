# Bank session 11 Oct 2026: more Categorise questions -> bank/sort-24.json. Two groups, three or four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})


s("Football", ["Sunderland", "Middlesbrough", "legends"], "medium", "A Sunderland legend or a Middlesbrough legend?", "Sunderland", "Middlesbrough", ["Charlie Hurley", "Kevin Phillips", "Niall Quinn", "Jim Montgomery"], ["Juninho", "Wilf Mannion", "George Camsell", "Tony Mowbray"])
s("Music", ["The Kinks", "Small Faces", "1960s"], "medium", "A Kinks song or a Small Faces song?", "The Kinks", "Small Faces", ["Lola", "Waterloo Sunset", "Sunny Afternoon", "You Really Got Me"], ["Itchycoo Park", "Lazy Sunday", "All or Nothing", "Tin Soldier"])
s("Words and language", ["Geordie", "Scouse", "dialect"], "medium", "A Geordie word or a Scouse word?", "Geordie", "Scouse", ["Hinny", "Canny", "Howay", "Clarts"], ["Boss", "Sound", "Made up", "Antwacky"])
s("Food and drink", ["Yorkshire", "Lancashire", "regional food"], "medium", "A Yorkshire dish or a Lancashire dish?", "Yorkshire", "Lancashire", ["Yorkshire pudding", "Parkin", "Fat rascal", "Wensleydale with fruit cake"], ["Hotpot", "Eccles cake", "Chorley cake", "Butter pie"])
s("Books", ["Charles Dickens", "Oliver Twist", "A Christmas Carol"], "easy", "From Oliver Twist or from A Christmas Carol?", "Oliver Twist", "A Christmas Carol", ["Fagin", "Bill Sikes", "Nancy", "The Artful Dodger"], ["Ebenezer Scrooge", "Bob Cratchit", "Tiny Tim", "Jacob Marley"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-24.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
