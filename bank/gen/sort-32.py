# Bank session 11 Oct 2026: more Categorise questions -> bank/sort-29.json. Two groups, three or four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})


s("Football", ["Newcastle United", "Kevin Keegan", "Eddie Howe"], "medium", "Played for Newcastle under Kevin Keegan or under Eddie Howe?", "Keegan", "Howe", ["Les Ferdinand", "David Ginola", "Faustino Asprilla", "Rob Lee"], ["Bruno Guimarães", "Sven Botman", "Anthony Gordon", "Alexander Isak"])
s("History", ["Remembrance", "Bonfire Night", "November"], "easy", "Remembrance or Bonfire Night?", "Remembrance", "Bonfire Night", ["Poppy", "Cenotaph", "Last Post", "Wreath"], ["Guy", "Sparkler", "Catherine wheel", "Treacle toffee"])
s("Food and drink", ["Sunday roast", "full English breakfast"], "easy", "Part of a Sunday roast or a full English breakfast?", "Sunday roast", "Full English", ["Yorkshire pudding", "Stuffing", "Gravy", "Roast parsnips"], ["Hash brown", "Black pudding", "Baked beans", "Fried egg"])
s("Scotland", ["Burns Night", "Hogmanay", "traditions"], "medium", "A Burns Night tradition or a Hogmanay one?", "Burns Night", "Hogmanay", ["Address to a Haggis", "Selkirk Grace", "Toast to the Lassies", "Immortal Memory"], ["First-footing", "Black bun", "A lump of coal", "The bells at midnight"])
s("UK geography", ["Lake District", "North East", "lakes"], "medium", "A Lake District lake or a North East reservoir?", "Lake District", "North East reservoir", ["Windermere", "Ullswater", "Derwentwater", "Coniston Water"], ["Kielder Water", "Fontburn", "Grassholme", "Cow Green"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-29.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
