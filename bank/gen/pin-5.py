# Bank session 19 Oct 2026: 8 Drop the Pin questions -> bank/pin-5.json, and their clues added to bank/pin-clues.json.
# Seaside and island spots (Lundy, Brownsea, Robin Hood's Bay, Saltburn) plus North East coast villages, and Emmerdale's set.
# None of these places was in the live pin bank. The text never names the place; the map region is one the rule allows without
# naming it (United Kingdom, Tyne and Wear, Northumberland). After import, check mapRegion and repin any that fell back to World.
import json, os
P = []
def pin(text, place, region, lat, lon, size, tags, diff, info):
    P.append({"type": "pin", "text": text, "place": place, "region": region, "lat": lat, "lon": lon, "sizeKm": size,
              "category": "Geography", "tags": tags, "difficulty": diff, "info": info})

pin("On which Leeds country estate is Emmerdale's purpose-built village set?", "Harewood House", "United Kingdom", 53.897, -1.523, 3,
    ["Emmerdale", "Yorkshire", "TV locations"], "hard", "Harewood House, between Leeds and Harrogate; the set has been there since 1997.")
pin("Which island in Poole Harbour hosted Baden-Powell's first Scout camp, in 1907?", "Brownsea Island", "United Kingdom", 50.689, -1.967, 3,
    ["Scouts", "islands", "Dorset"], "hard", "Brownsea Island, in Poole Harbour, Dorset; also a red squirrel stronghold.")
pin("Which Bristol Channel island once issued its own 'puffin' coins and still has its own stamps?", "Lundy", "United Kingdom", 51.18, -4.67, 5,
    ["islands", "puffins", "Devon"], "hard", "Lundy, about 12 miles off the north Devon coast.")
pin("Which steep Yorkshire fishing village south of Whitby was a famous smugglers' haunt?", "Robin Hood's Bay", "United Kingdom", 54.434, -0.534, 2,
    ["Yorkshire", "coast", "smuggling"], "medium", "Robin Hood's Bay, on the North Yorkshire coast; also the end of the Coast to Coast walk.")
pin("Which Victorian resort near Redcar has Britain's oldest working water-powered cliff lift?", "Saltburn-by-the-Sea", "United Kingdom", 54.584, -0.968, 2,
    ["Teesside", "coast", "seaside"], "hard", "Saltburn-by-the-Sea; the cliff lift opened in 1884.")
pin("Which Northumberland fishing village is famous for its oak-smoked kippers?", "Craster", "Northumberland", 55.472, -1.593, 1,
    ["Northumberland", "coast", "food"], "medium", "Craster, on the coast below Dunstanburgh Castle.")
pin("From which Northumberland harbour do the boats leave for the Farne Islands?", "Seahouses", "Northumberland", 55.583, -1.651, 1,
    ["Northumberland", "coast", "seabirds"], "medium", "Seahouses, a few miles south of Bamburgh.")
pin("Which little bay between Tynemouth and Whitley Bay drew Victorian painters, including the American Winslow Homer?", "Cullercoats", "Tyne and Wear", 55.034, -1.433, 1,
    ["North East", "coast", "art"], "hard", "Cullercoats, on the North Tyneside coast; Homer stayed in 1881 and 1882.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(P, open(os.path.join(here, '..', 'pin-5.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
cp = os.path.join(here, '..', 'pin-clues.json')
clues = json.load(open(cp, encoding='utf-8'))
for p in P: clues.setdefault(p['place'], p['text'])
open(cp, 'w', encoding='utf-8').write(json.dumps(clues, ensure_ascii=False, indent=0) + chr(10))
print(len(P), 'pins written;', len(clues), 'clues')
