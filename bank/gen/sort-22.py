# Bank session 11 Oct 2026: 7 more Categorise questions -> bank/sort-19.json. Two groups, three or four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Film", ["Hollywood", "Bollywood", "actors"], "medium", "A Hollywood star or a Bollywood star?", "Hollywood", "Bollywood", ["Tom Cruise", "Julia Roberts", "Denzel Washington", "Meryl Streep"], ["Shah Rukh Khan", "Amitabh Bachchan", "Aamir Khan", "Deepika Padukone"])
s("World geography", ["Alps", "Himalayas", "mountains"], "medium", "A peak in the Alps or in the Himalayas?", "Alps", "Himalayas", ["Mont Blanc", "Matterhorn", "Eiger", "Jungfrau"], ["Everest", "Annapurna", "Kangchenjunga", "Lhotse"])
s("World geography", ["deserts", "Africa", "Asia"], "medium", "A desert in Africa or in Asia?", "Africa", "Asia", ["Sahara", "Kalahari", "Namib", "Nubian"], ["Gobi", "Thar", "Taklamakan", "Karakum"])
s("Animals", ["famous animals", "horses", "dogs"], "easy", "A famous horse or a famous dog?", "Horse", "Dog", ["Red Rum", "Black Beauty", "Shergar", "Desert Orchid"], ["Lassie", "Greyfriars Bobby", "Snoopy", "Gromit"])
s("Food and drink", ["Thai food", "Indian food"], "easy", "A Thai dish or an Indian dish?", "Thai", "Indian", ["Pad Thai", "Tom yum", "Massaman curry", "Som tam"], ["Biryani", "Dal", "Tandoori chicken", "Saag aloo"])
s("Sport", ["golf", "Formula One"], "easy", "A golf course or a Formula One circuit?", "Golf course", "F1 circuit", ["St Andrews", "Augusta", "Carnoustie", "Wentworth"], ["Silverstone", "Monza", "Suzuka", "Interlagos"])
s("Music", ["instruments"], "easy", "Played with a bow, or blown?", "Bowed", "Blown", ["Violin", "Viola", "Cello", "Double bass"], ["Flute", "Oboe", "Trumpet", "Bassoon"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-19.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
