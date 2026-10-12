# Bank session 12 Oct 2026: 1 more general race -> bank/race-208.json (laundry words). Checked against the cleaning race
# (bleach, fabric conditioner and lint roller left out so nothing repeats).
# 20 rows each, target 10; wrong options are the same kind of thing, never another row's right answer, and never also right for that row.
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

race("what's this laundry word?", "Everyday life", "easy", ["laundry", "washing", "home", "words"], [
 ("The fast whirl at the end of a wash that wrings the water out", "Spin cycle", ["Rinse cycle", "Soak", "Eco mode"]),
 ("A machine that dries clothes in a turning drum of warm air", "Tumble dryer", ["Twin tub", "Trouser press", "Steamer"]),
 ("A folding frame you hang washing on indoors", "Clothes horse", ["Washboard", "Dolly tub", "Laundry basket"]),
 ("Old hand-cranked rollers for squeezing the water out", "Mangle", ["Washboard", "Dolly tub", "Twin tub"]),
 ("Clips the washing onto the line", "Clothes peg", ["Safety pin", "Bulldog clip", "Hair grip"]),
 ("The rope or wire strung across the garden", "Washing line", ["Clothes rail", "Bunting", "Guy rope"]),
 ("The spinning, umbrella-shaped washing line", "Rotary dryer", ["Maypole", "Parasol", "Carousel"]),
 ("The hot, flat-bottomed tool that takes out creases", "Iron", ["Crimper", "Curling tongs", "Toastie maker"]),
 ("The narrow padded table you press clothes on", "Ironing board", ["Drawing board", "Chopping board", "Surfboard"]),
 ("Sprayed on shirt collars to make them stiff", "Starch", ["Glue", "Varnish", "Lacquer"]),
 ("A shop full of coin-operated washing machines", "Launderette", ["Dry cleaner's", "Tailor's", "Haberdashery"]),
 ("The pile of black and navy clothes washed together", "Darks", ["Brights", "Lights", "Shades"]),
 ("Silky and lacy things that need a gentle wash", "Delicates", ["Smalls", "Fineries", "Softs"]),
 ("When one red sock turns the whole load pink", "Colour run", ["Fade", "Bobble", "Fray"]),
 ("What wool can do if it's washed too hot", "Shrink", ["Fade", "Bobble", "Stretch"]),
 ("The fluff that collects in the dryer's filter", "Lint", ["Dust", "Felt", "Down"]),
 ("Washing powder or liquid", "Detergent", ["Descaler", "Degreaser", "Solvent"]),
 ("The care label showing a hand in a tub", "Hand wash", ["Do not wash", "Tumble dry", "Cold rinse"]),
 ("The care label showing a plain circle", "Dry clean only", ["Tumble dry", "Do not iron", "Do not bleach"]),
 ("The little bag that hangs on the line holding the clips", "Peg bag", ["Kit bag", "Tote bag", "Bum bag"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-208.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
