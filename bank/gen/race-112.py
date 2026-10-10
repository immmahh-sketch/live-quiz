# Bank session 10 Oct 2026: 2 more general races -> bank/race-112.json (gemstones, instruments). 20 rows each, target 10; wrong options are
# the same kind of thing, never another row's right answer, and never also right for that row.
import json, os
R = []
def race(title, cat, diff, tags, rows):
    rights = {r[1] for r in rows}
    assert len(rows) == 20, (title, len(rows))
    assert len(rights) == 20, (title, 'duplicate right answers')
    bad = [(q, w) for q, right, wrong in rows for w in wrong if w in rights]
    assert not bad, (title, 'recycled', bad)
    for q, right, wrong in rows:
        assert len(wrong) == 3 and len(set(wrong)) == 3 and right not in wrong, (title, q)
    R.append({"type": "race", "text": "The Race: " + title, "target": 10, "category": cat, "tags": tags, "difficulty": diff,
              "bank": [{"q": q, "right": right, "wrong": wrong} for q, right, wrong in rows]})

race("which gemstone is this?", "Nature", "hard", ["gemstones", "birthstones"], [
 ("January's birthstone, deep red", "Garnet", ["Spinel", "Carnelian", "Tourmaline"]),
 ("February's birthstone, purple", "Amethyst", ["Tourmaline", "Spinel", "Fluorite"]),
 ("March's birthstone, the blue of the sea", "Aquamarine", ["Zircon", "Apatite", "Fluorite"]),
 ("April's birthstone, the hardest natural material", "Diamond", ["Zircon", "Quartz", "Moissanite"]),
 ("May's birthstone, rich green", "Emerald", ["Malachite", "Tourmaline", "Agate"]),
 ("June's birthstone, made inside an oyster", "Pearl", ["Mother-of-pearl", "Coral", "Nacre"]),
 ("July's birthstone, red", "Ruby", ["Spinel", "Carnelian", "Red jasper"]),
 ("August's birthstone, olive green", "Peridot", ["Tourmaline", "Malachite", "Chrysoprase"]),
 ("September's birthstone, blue", "Sapphire", ["Zircon", "Spinel", "Iolite"]),
 ("October's birthstone, with flashes of rainbow colour", "Opal", ["Labradorite", "Quartz", "Fluorite"]),
 ("November's birthstone, golden-yellow", "Topaz", ["Citrine", "Tiger's eye", "Agate"]),
 ("December's birthstone, sky blue and loved by the Navajo", "Turquoise", ["Chrysocolla", "Larimar", "Malachite"]),
 ("Green stone prized above gold in ancient China", "Jade", ["Malachite", "Serpentine", "Aventurine"]),
 ("Deep blue stone ground into ultramarine paint", "Lapis lazuli", ["Sodalite", "Azurite", "Chrysocolla"]),
 ("Fossilised tree resin, sometimes with insects trapped inside", "Amber", ["Copal", "Citrine", "Tiger's eye"]),
 ("Black gem from Whitby, loved by Victorian mourners", "Jet", ["Black coral", "Hematite", "Black tourmaline"]),
 ("Black-and-white banded stone, carved into cameos", "Onyx", ["Agate", "Jasper", "Marble"]),
 ("Black glass made naturally by volcanoes", "Obsidian", ["Pumice", "Basalt", "Hematite"]),
 ("Blue-violet gem found only near Mount Kilimanjaro", "Tanzanite", ["Iolite", "Spinel", "Kunzite"]),
 ("Milky stone with a blue sheen, June's other birthstone", "Moonstone", ["Labradorite", "Selenite", "Quartz"])])

race("which instrument is this?", "Music", "medium", ["instruments", "music"], [
 ("Played without touching it, by waving your hands near two aerials", "Theremin", ["Synthesiser", "Melodica", "Celesta"]),
 ("A long wooden drone pipe from Aboriginal Australia", "Didgeridoo", ["Alphorn", "Pan pipes", "Bugle"]),
 ("A bag of air, a chanter and three drones", "Bagpipes", ["Concertina", "Melodica", "Harmonica"]),
 ("The biggest, lowest brass instrument in the orchestra", "Tuba", ["Euphonium", "French horn", "Trombone"]),
 ("A half-size flute, the highest instrument in the orchestra", "Piccolo", ["Recorder", "Clarinet", "Fife"]),
 ("The double-reed woodwind that gives the orchestra its tuning note", "Oboe", ["Clarinet", "Cor anglais", "Recorder"]),
 ("Long, low double-reed woodwind, the 'clown of the orchestra'", "Bassoon", ["Clarinet", "Cor anglais", "Saxophone"]),
 ("Keyboard whose strings are plucked, not hit", "Harpsichord", ["Piano", "Organ", "Celesta"]),
 ("You hum into it and it buzzes", "Kazoo", ["Harmonica", "Recorder", "Swanee whistle"]),
 ("A tuned oil drum from Trinidad", "Steelpan", ["Marimba", "Bongos", "Djembe"]),
 ("Small eight-stringed instrument played with a pick in Italian folk music", "Mandolin", ["Lute", "Banjo", "Ukulele"]),
 ("Russian stringed instrument with a triangular body", "Balalaika", ["Lute", "Banjo", "Sitar"]),
 ("A pair of Indian hand drums", "Tabla", ["Bongos", "Djembe", "Timpani"]),
 ("Irish frame drum played with a short stick", "Bodhrán", ["Tambourine", "Snare drum", "Djembe"]),
 ("Pair of shells clicked together in flamenco", "Castanets", ["Maracas", "Tambourine", "Claves"]),
 ("Small egg-shaped clay flute, made famous by a Zelda game", "Ocarina", ["Recorder", "Pan pipes", "Tin whistle"]),
 ("A bent steel bar struck with a beater", "Triangle", ["Cowbell", "Tubular bells", "Gong"]),
 ("Strings bowed by a wheel you turn with a handle", "Hurdy-gurdy", ["Barrel organ", "Lute", "Dulcimer"]),
 ("A flat box of strings plucked on the lap, heard in 'The Third Man'", "Zither", ["Dulcimer", "Lute", "Lyre"]),
 ("A tuba that wraps round the player, for marching bands", "Sousaphone", ["Euphonium", "Flugelhorn", "French horn"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-112.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
