# Bank session 19 Oct 2026: 8 Drop the Pin questions -> bank/pin-3.json, and their clues added to bank/pin-clues.json.
# Places tied to today's TV and wildlife sessions (Heartbeat, Doc Martin, All Creatures, Hamish Macbeth, gannets) plus North East
# landmarks. None of these places was in the live pin bank. The text never names the place; the map region is one the rule
# allows without naming it (United Kingdom, Scotland, Tyne and Wear, Northumberland). sizeKm sets how close a pin must be.
import json, os
P = []
def pin(text, place, region, lat, lon, size, tags, diff, info):
    P.append({"type": "pin", "text": text, "place": place, "region": region, "lat": lat, "lon": lon, "sizeKm": size,
              "category": "Geography", "tags": tags, "difficulty": diff, "info": info})

pin("Which North York Moors village played Aidensfield in ITV's Heartbeat?", "Goathland", "United Kingdom", 54.400, -0.718, 3,
    ["Heartbeat", "Yorkshire", "TV locations"], "hard", "Goathland, on the North York Moors; its station was also Hogsmeade in the Harry Potter films.")
pin("Which island in the Firth of Forth holds the world's biggest colony of northern gannets?", "Bass Rock", "Scotland", 56.077, -2.641, 1,
    ["gannets", "seabirds", "islands"], "hard", "The Bass Rock, off North Berwick in East Lothian; it turns white with around 150,000 gannets.")
pin("Which Cornish fishing village plays Portwenn in Doc Martin?", "Port Isaac", "United Kingdom", 50.593, -4.830, 2,
    ["Doc Martin", "Cornwall", "TV locations"], "medium", "Port Isaac, on Cornwall's north coast.")
pin("In which North Yorkshire market town did the real James Herriot, Alf Wight, have his vet's practice?", "Thirsk", "United Kingdom", 54.232, -1.341, 3,
    ["James Herriot", "All Creatures Great and Small", "Yorkshire"], "hard", "Thirsk; the old surgery at 23 Kirkgate is now The World of James Herriot.")
pin("Which Highland village on Loch Carron played Lochdubh in Hamish Macbeth?", "Plockton", "Scotland", 57.337, -5.652, 2,
    ["Hamish Macbeth", "Highlands", "TV locations"], "hard", "Plockton, in Wester Ross, looking out to Skye.")
pin("Where on Hadrian's Wall did a famous tree, seen in Robin Hood: Prince of Thieves, get cut down overnight in 2023?", "Sycamore Gap", "Northumberland", 55.0035, -2.3737, 1,
    ["Hadrian's Wall", "Northumberland", "trees"], "medium", "Sycamore Gap, between Housesteads and Steel Rigg; the tree was felled in September 2023.")
pin("Which seaside landmark did Dire Straits sing about in 'Tunnel of Love'?", "Spanish City", "Tyne and Wear", 55.0450, -1.4450, 1,
    ["Dire Straits", "North East", "landmarks"], "medium", "The Spanish City, Whitley Bay, restored and reopened in 2018.")
pin("Which red-and-white striped lighthouse near Whitburn was the first in the world built to use alternating current?", "Souter Lighthouse", "Tyne and Wear", 54.9707, -1.3638, 1,
    ["lighthouses", "North East", "landmarks"], "hard", "Souter Lighthouse, on the cliffs at Marsden between South Shields and Whitburn; it opened in 1871.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(P, open(os.path.join(here, '..', 'pin-3.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
cp = os.path.join(here, '..', 'pin-clues.json')
clues = json.load(open(cp, encoding='utf-8'))
for p in P: clues.setdefault(p['place'], p['text'])
open(cp, 'w', encoding='utf-8').write(json.dumps(clues, ensure_ascii=False, indent=0) + chr(10))
print(len(P), 'pins written;', len(clues), 'clues')
