# Bank session 11 Oct 2026: more Categorise questions -> bank/sort-21.json. Two groups, three or four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})


s("Film", ["Ghostbusters", "The Goonies", "1980s films"], "medium", "A Ghostbuster or a Goonie?", "Ghostbusters", "The Goonies", ["Peter Venkman", "Ray Stantz", "Egon Spengler", "Winston Zeddemore"], ["Mikey", "Data", "Chunk", "Mouth"])
s("TV", ["Grange Hill", "Byker Grove", "children's TV"], "medium", "A Grange Hill character or a Byker Grove character?", "Grange Hill", "Byker Grove", ["Tucker", "Zammo", "Gonch", "Roland"], ["PJ", "Duncan", "Spuggie", "Geoff"])
s("North East", ["Tyne and Wear Metro", "Newcastle", "Gateshead"], "medium", "A Metro station north of the Tyne or south of it?", "North of the Tyne", "South of the Tyne", ["Haymarket", "Monument", "Jesmond", "Tynemouth"], ["Gateshead", "Heworth", "Jarrow", "Pelaw"])
s("TV", ["Porridge", "Only Fools and Horses", "sitcoms"], "easy", "A Porridge character or an Only Fools and Horses character?", "Porridge", "Only Fools and Horses", ["Fletcher", "Godber", "Mr Mackay", "Lukewarm"], ["Trigger", "Boycie", "Denzil", "Uncle Albert"])
s("Games", ["chess", "ballet"], "medium", "A chess opening or a ballet move?", "Chess opening", "Ballet move", ["Sicilian", "Ruy Lopez", "King's Gambit", "Queen's Gambit"], ["Pirouette", "Plié", "Arabesque", "Jeté"])
s("Animals", ["chickens", "sheep", "breeds"], "medium", "A breed of chicken or a breed of sheep?", "Chicken", "Sheep", ["Rhode Island Red", "Leghorn", "Orpington", "Silkie"], ["Suffolk", "Texel", "Herdwick", "Swaledale"])
s("Music", ["Taylor Swift", "Adele"], "easy", "A Taylor Swift song or an Adele song?", "Taylor Swift", "Adele", ["Shake It Off", "Blank Space", "Love Story", "Anti-Hero"], ["Hello", "Someone Like You", "Rolling in the Deep", "Skyfall"])
s("TV", ["The Goodies", "Monty Python", "comedy"], "medium", "One of the Goodies or one of the Pythons?", "The Goodies", "Monty Python", ["Tim Brooke-Taylor", "Graeme Garden", "Bill Oddie"], ["John Cleese", "Michael Palin", "Eric Idle", "Terry Jones"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-21.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
