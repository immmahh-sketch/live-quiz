# Bank session 19 Oct 2026: 8 Drop the Pin questions -> bank/pin-7.json, and their clues added to bank/pin-clues.json.
# Ancient and grand places: a Hebridean stone circle, Avebury and Silbury Hill, Blenheim, Leeds and Arundel castles, Wookey Hole and
# Dunbar. None of these places was in the live pin bank. The text never names the place; every one is on the United Kingdom or
# Scotland map. After import, check mapRegion and repin any that fell back to World.
import json, os
P = []
def pin(text, place, region, lat, lon, size, tags, diff, info):
    P.append({"type": "pin", "text": text, "place": place, "region": region, "lat": lat, "lon": lon, "sizeKm": size,
              "category": "Geography", "tags": tags, "difficulty": diff, "info": info})

pin("Which Hebridean stone circle on the Isle of Lewis, shaped like a Celtic cross, is more than 4,000 years old?", "Callanish Standing Stones", "Scotland", 58.197, -6.745, 1,
    ["stone circles", "Scotland", "prehistory"], "hard", "Callanish, on the west coast of Lewis, in the Outer Hebrides.")
pin("Which Wiltshire village sits inside the largest stone circle in Britain?", "Avebury", "United Kingdom", 51.428, -1.854, 2,
    ["stone circles", "Wiltshire", "prehistory"], "medium", "Avebury, in Wiltshire; the circle surrounds part of the village.")
pin("Which huge man-made chalk mound, the tallest prehistoric one in Europe, stands near Avebury?", "Silbury Hill", "United Kingdom", 51.416, -1.857, 1,
    ["Wiltshire", "prehistory", "landmarks"], "hard", "Silbury Hill, beside the A4 near Avebury; about 4,400 years old.")
pin("Which Oxfordshire palace, built for the Duke of Marlborough, was the birthplace of Winston Churchill?", "Blenheim Palace", "United Kingdom", 51.841, -1.361, 2,
    ["Winston Churchill", "palaces", "Oxfordshire"], "medium", "Blenheim Palace, at Woodstock in Oxfordshire.")
pin("Which moated Kent castle has been called 'the loveliest castle in the world'?", "Leeds Castle", "United Kingdom", 51.249, 0.630, 1,
    ["castles", "Kent", "moats"], "medium", "Leeds Castle, near Maidstone in Kent; it has nothing to do with Leeds in Yorkshire.")
pin("Which West Sussex castle is the home of the Duke of Norfolk?", "Arundel Castle", "United Kingdom", 50.855, -0.554, 1,
    ["castles", "Sussex", "dukes"], "medium", "Arundel Castle, in West Sussex.")
pin("Which Somerset cave system, home to the 'Witch of Wookey', is also a tourist attraction with a papermill?", "Wookey Hole", "United Kingdom", 51.228, -2.672, 1,
    ["caves", "Somerset", "attractions"], "medium", "Wookey Hole, near Wells in Somerset.")
pin("Which East Lothian harbour town was the birthplace of John Muir, the 'father of national parks'?", "Dunbar", "Scotland", 56.002, -2.516, 3,
    ["John Muir", "Scotland", "national parks"], "hard", "Dunbar, on the East Lothian coast; Muir emigrated to America as a boy.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(P, open(os.path.join(here, '..', 'pin-7.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
cp = os.path.join(here, '..', 'pin-clues.json')
clues = json.load(open(cp, encoding='utf-8'))
for p in P: clues.setdefault(p['place'], p['text'])
open(cp, 'w', encoding='utf-8').write(json.dumps(clues, ensure_ascii=False, indent=0) + chr(10))
print(len(P), 'pins written;', len(clues), 'clues')
