# Bank session 19 Oct 2026: 8 Drop the Pin questions -> bank/pin-6.json, and their clues added to bank/pin-clues.json.
# Period-drama and film locations (Poldark, Downton, Last Tango, Pride and Prejudice, Harry Potter) plus Saltaire. None of these
# places was in the live pin bank. The text never names the place; every one is on the United Kingdom map. After import, check
# mapRegion and repin any that fell back to World.
import json, os
P = []
def pin(text, place, region, lat, lon, size, tags, diff, info):
    P.append({"type": "pin", "text": text, "place": place, "region": region, "lat": lat, "lon": lon, "sizeKm": size,
              "category": "Geography", "tags": tags, "difficulty": diff, "info": info})

pin("Which Georgian harbour near St Austell has stood in for old Truro in Poldark?", "Charlestown", "United Kingdom", 50.333, -4.757, 1,
    ["Poldark", "Cornwall", "TV locations"], "hard", "Charlestown, Cornwall; its square-rigged ships and harbour were used in Poldark.")
pin("Which turquoise cove on the Lizard peninsula appeared in Poldark?", "Kynance Cove", "United Kingdom", 49.975, -5.231, 1,
    ["Poldark", "Cornwall", "coast"], "hard", "Kynance Cove, on the west side of the Lizard in Cornwall.")
pin("Which Oxfordshire village plays Downton's own village in Downton Abbey?", "Bampton", "United Kingdom", 51.725, -1.546, 1,
    ["Downton Abbey", "TV locations"], "hard", "Bampton, in west Oxfordshire; its library was Downton's cottage hospital.")
pin("Which Wiltshire National Trust village has appeared in Downton Abbey, Harry Potter and Pride and Prejudice?", "Lacock", "United Kingdom", 51.415, -2.118, 1,
    ["TV locations", "film locations", "Wiltshire"], "hard", "Lacock, near Chippenham; Lacock Abbey's cloisters were Hogwarts corridors.")
pin("Which West Yorkshire town gave its name to Sally Wainwright's 'Last Tango'?", "Halifax", "United Kingdom", 53.725, -1.863, 4,
    ["Last Tango in Halifax", "Yorkshire"], "medium", "Halifax, in Calderdale, West Yorkshire.")
pin("Which Derbyshire stately home played Mr Darcy's Pemberley in the 2005 Pride and Prejudice?", "Chatsworth House", "United Kingdom", 53.228, -1.611, 2,
    ["Pride and Prejudice", "stately homes", "Derbyshire"], "medium", "Chatsworth House, in the Peak District, home of the Dukes of Devonshire.")
pin("Which limestone cliff in the Yorkshire Dales appeared in Harry Potter and the Deathly Hallows?", "Malham Cove", "United Kingdom", 54.072, -2.158, 1,
    ["Harry Potter", "Yorkshire Dales", "landmarks"], "hard", "Malham Cove, near Settle in the Yorkshire Dales.")
pin("Which model village near Bradford did Sir Titus Salt build for his mill workers?", "Saltaire", "United Kingdom", 53.838, -1.790, 1,
    ["Victorians", "Yorkshire", "World Heritage"], "medium", "Saltaire, beside the River Aire near Shipley; a World Heritage Site.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(P, open(os.path.join(here, '..', 'pin-6.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
cp = os.path.join(here, '..', 'pin-clues.json')
clues = json.load(open(cp, encoding='utf-8'))
for p in P: clues.setdefault(p['place'], p['text'])
open(cp, 'w', encoding='utf-8').write(json.dumps(clues, ensure_ascii=False, indent=0) + chr(10))
print(len(P), 'pins written;', len(clues), 'clues')
