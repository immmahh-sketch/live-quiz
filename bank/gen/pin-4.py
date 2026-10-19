# Bank session 19 Oct 2026: 8 Drop the Pin questions -> bank/pin-4.json, and their clues added to bank/pin-clues.json.
# Places tied to today's rewilding and TV sessions (beavers, sea eagles, bison, Taggart, Bergerac) plus North East coast spots.
# None of these places was in the live pin bank. The text never names the place; the map region is one the rule allows without
# naming it (United Kingdom, Scotland, Tyne and Wear, Northumberland). After import, check mapRegion: last time the server fell
# back to the World map, and tools' bank_repin put them right.
import json, os
P = []
def pin(text, place, region, lat, lon, size, tags, diff, info):
    P.append({"type": "pin", "text": text, "place": place, "region": region, "lat": lat, "lon": lon, "sizeKm": size,
              "category": "Geography", "tags": tags, "difficulty": diff, "info": info})

pin("In which Argyll forest were beavers officially released in 2009, the first wild ones in Britain for 400 years?", "Knapdale", "Scotland", 56.03, -5.55, 10,
    ["beavers", "rewilding", "Scotland"], "hard", "Knapdale Forest, in mid-Argyll between Lochgilphead and the Sound of Jura.")
pin("Onto which small Hebridean island were white-tailed eagles first released in 1975?", "Isle of Rum", "Scotland", 57.00, -6.33, 12,
    ["white-tailed eagles", "rewilding", "islands"], "hard", "Rum, in the Small Isles south of Skye.")
pin("Where were European bison let loose in 2022, in woods just outside Canterbury?", "West Blean Woods", "United Kingdom", 51.32, 1.06, 5,
    ["bison", "rewilding", "Kent"], "hard", "West Blean and Thornden Woods, north of Canterbury in Kent.")
pin("Which island's capital, St Helier, was Jim Bergerac's patch?", "Jersey", "United Kingdom", 49.21, -2.13, 12,
    ["Bergerac", "Channel Islands", "TV locations"], "medium", "Jersey, the largest Channel Island, off the coast of Normandy.")
pin("Which Glasgow district gave its name to the CID in Taggart?", "Maryhill", "Scotland", 55.89, -4.29, 3,
    ["Taggart", "Glasgow", "TV locations"], "hard", "Maryhill, in the north-west of Glasgow.")
pin("Which island off Amble is home to England's only colony of roseate terns?", "Coquet Island", "Northumberland", 55.334, -1.539, 1,
    ["seabirds", "islands", "North East"], "hard", "Coquet Island, an RSPB reserve a mile off Amble.")
pin("Which village at the river's mouth has a ruined priory and castle on its headland and the Longsands beach?", "Tynemouth", "Tyne and Wear", 55.017, -1.420, 2,
    ["North East", "coast"], "medium", "Tynemouth, on the north side of the mouth of the Tyne.")
pin("Which sea stack off South Shields had a staircase cut into it, with a pub in a cave in the cliffs nearby?", "Marsden Rock", "Tyne and Wear", 54.984, -1.383, 1,
    ["North East", "coast", "landmarks"], "hard", "Marsden Rock, in Marsden Bay; the Marsden Grotto pub is cut into the cliff.")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(P, open(os.path.join(here, '..', 'pin-4.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
cp = os.path.join(here, '..', 'pin-clues.json')
clues = json.load(open(cp, encoding='utf-8'))
for p in P: clues.setdefault(p['place'], p['text'])
open(cp, 'w', encoding='utf-8').write(json.dumps(clues, ensure_ascii=False, indent=0) + chr(10))
print(len(P), 'pins written;', len(clues), 'clues')
