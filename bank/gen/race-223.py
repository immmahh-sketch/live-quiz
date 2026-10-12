# Bank session 13 Oct 2026: 1 more general race -> bank/race-223.json (tailor's words). Checked against every race in stock:
# hem, dart, waistcoat, blazer and cravat left out (sewing and clothing races); Savile Row and tape measure swapped out (London
# streets and DIY tools races); Tweed and Cufflinks still appear once elsewhere, with different clues.
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

race("what's this tailor's word?", "Fashion", "medium", ["tailoring", "suits", "clothes", "words"], [
 ("Made completely to the customer's own measurements", "Bespoke", ["Ready to wear", "Second-hand", "Hand-me-down"]),
 ("Bought ready-made from the rail in a shop", "Off the peg", ["Hand-me-down", "Home-made", "Knock-off"]),
 ("The measurement from crotch to ankle", "Inside leg", ["Outside leg", "Instep", "Rise"]),
 ("The folded flap down the front of a jacket", "Lapel", ["Cuff", "Yoke", "Placket"]),
 ("Folded-back cuffs at the bottom of trousers", "Turn-ups", ["Pleats", "Flares", "Darts"]),
 ("Straps over the shoulders that hold trousers up", "Braces", ["Belt", "Sash", "Garters"]),
 ("Thin vertical lines on a City gent's suit", "Pinstripe", ["Houndstooth", "Herringbone", "Tartan"]),
 ("Rough woollen cloth from Scotland, like Harris", "Tweed", ["Denim", "Corduroy", "Linen"]),
 ("A folded handkerchief in the breast pocket", "Pocket square", ["Cravat", "Bow tie", "Tie pin"]),
 ("Used to mark the cloth before cutting", "Tailor's chalk", ["Crayon", "Charcoal", "Pastel"]),
 ("Trying on a part-made suit so it can be adjusted", "Fitting", ["Audition", "Rehearsal", "Casting"]),
 ("A jacket with two rows of buttons", "Double-breasted", ["Single-breasted", "Bomber", "Norfolk"]),
 ("The slit up the back of a jacket", "Vent", ["Gusset", "Seam", "Yoke"]),
 ("The silky layer inside a jacket", "Lining", ["Interfacing", "Wadding", "Padding"]),
 ("Tailcoat and striped trousers for a wedding", "Morning suit", ["Dinner suit", "Lounge suit", "Zoot suit"]),
 ("The black jacket worn with a bow tie", "Dinner jacket", ["Smoking jacket", "Tailcoat", "Bomber jacket"]),
 ("A suit with jacket, trousers and a waistcoat", "Three-piece", ["Two-piece", "Tracksuit", "Jumpsuit"]),
 ("They fasten the cuffs of a double-cuffed shirt", "Cufflinks", ["Studs", "Toggles", "Poppers"]),
 ("The tailor who draws and cuts the pattern", "Cutter", ["Fitter", "Presser", "Trimmer"]),
 ("The torso-shaped stand a suit is built up on", "Tailor's dummy", ["Scarecrow", "Coat stand", "Hat stand"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-223.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
