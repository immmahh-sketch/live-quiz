# Bank session 10 Oct 2026: 2 more general races -> bank/race-138.json (make-up and skincare words, cycling and running words). 20 rows each, target 10; wrong options are
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


race("what's this make-up or skincare word?", "Fashion", "medium", ["make-up", "skincare", "beauty"], [
 ("Darkens and lengthens your eyelashes", "Mascara", ["Kajal", "Glitter", "Cold cream"]),
 ("Draws a fine line along the edge of the eyelid", "Eyeliner", ["Glitter", "Dry shampoo", "Cold cream"]),
 ("A rosy powder brushed onto the cheeks", "Blusher", ["Glitter", "Dry shampoo", "Witch hazel"]),
 ("An all-over base that evens out your skin tone", "Foundation", ["Cold cream", "Witch hazel", "SPF"]),
 ("Covers dark circles and spots", "Concealer", ["Cold cream", "Witch hazel", "Glitter"]),
 ("Colour for your lips in a twist-up tube", "Lipstick", ["Cold cream", "Witch hazel", "Dry shampoo"]),
 ("A powder for a sun-kissed glow without the sun", "Bronzer", ["Glitter", "Witch hazel", "Cold cream"]),
 ("A shimmery product dabbed on the cheekbones to catch the light", "Highlighter", ["Witch hazel", "Cold cream", "Dry shampoo"]),
 ("Goes on before your make-up so it lasts longer", "Primer", ["Witch hazel", "Cold cream", "Dry shampoo"]),
 ("Darker shading to sculpt the cheekbones and jaw", "Contour", ["Glitter", "Witch hazel", "Cold cream"]),
 ("A pencil that outlines the lips before the colour goes on", "Lip liner", ["Cuticle oil", "Glitter", "Dry shampoo"]),
 ("Painted onto fingernails and toenails", "Nail varnish", ["Cuticle oil", "Nail file", "Glitter"]),
 ("Colour brushed onto the eyelids", "Eyeshadow", ["Cold cream", "Witch hazel", "Dry shampoo"]),
 ("Stuck on to make your lashes look longer and fuller", "False eyelashes", ["Nail file", "Cuticle oil", "Glitter"]),
 ("A mist that locks your make-up in place at the end", "Setting spray", ["Dry shampoo", "Witch hazel", "Micellar water"]),
 ("A liquid swiped on after cleansing to tighten the pores", "Toner", ["Cold cream", "Dry shampoo", "Body butter"]),
 ("A daily cream that stops your face drying out", "Moisturiser", ["Dry shampoo", "Witch hazel", "Micellar water"]),
 ("A gritty scrub that clears away dead skin", "Exfoliator", ["Witch hazel", "Micellar water", "Dry shampoo"]),
 ("A light, concentrated liquid of active ingredients, used before moisturiser", "Serum", ["Dry shampoo", "Witch hazel", "Cold cream"]),
 ("Fills in and shapes your brows", "Eyebrow pencil", ["Nail file", "Cuticle oil", "Glitter"])])

race("what's this cycling or running word?", "Sport", "hard", ["cycling", "running", "athletics"], [
 ("The main pack of riders in a road race", "Peloton", ["Echelon", "Musette", "Soigneur"]),
 ("A rider who works for the team leader, fetching drinks and shielding them from the wind", "Domestique", ["Soigneur", "Directeur sportif", "Gruppetto"]),
 ("Worn by the King of the Mountains in the Tour de France", "Polka dot jersey", ["White jersey", "Rainbow jersey", "Maillot jaune"]),
 ("Worn by the leader of the Tour de France points competition", "Green jersey", ["White jersey", "Rainbow jersey", "Maillot jaune"]),
 ("A small group that escapes off the front of the race", "Breakaway", ["Gruppetto", "Echelon", "Bidon"]),
 ("Riding close behind someone else to save energy", "Slipstreaming", ["Cadence", "Tempo run", "Strides"]),
 ("Racing alone against the clock", "Time trial", ["Points race", "Scratch race", "Omnium"]),
 ("The nickname for the rider lying last overall in the Tour de France", "Lanterne rouge", ["Directeur sportif", "Soigneur", "Bidon"]),
 ("An indoor cycling track with steeply banked bends", "Velodrome", ["Omnium", "Musette", "Soigneur"]),
 ("A track race where the riders follow a little motorbike before sprinting for the line", "Keirin", ["Omnium", "Scratch race", "Team pursuit"]),
 ("The little motorbike that paces the riders in that race", "Derny", ["Bidon", "Musette", "Echelon"]),
 ("When a marathon runner suddenly runs out of energy, often around mile 20", "Hitting the wall", ["Runner's high", "Shin splints", "Taper"]),
 ("A runner who sets a fast early pace for others, then drops out", "Pacemaker", ["Strides", "Sweeper bus", "Bib"]),
 ("A free, timed 5K held every Saturday morning in parks", "Parkrun", ["Tempo run", "Hill reps", "Chip time"]),
 ("Your fastest ever time over a distance", "Personal best", ["Chip time", "Splits", "Cadence"]),
 ("Swedish 'speed play': mixing fast and slow running as you feel like it", "Fartlek", ["Tempo run", "Hill reps", "Strides"]),
 ("Running the second half of a race faster than the first", "Negative split", ["Taper", "Carb-loading", "Chip time"]),
 ("Any race longer than a marathon", "Ultramarathon", ["Taper", "Tempo run", "Hill reps"]),
 ("The NHS plan that takes beginners from the sofa to running 5K in nine weeks", "Couch to 5K", ["Tempo run", "Hill reps", "Taper"]),
 ("What relay runners hand to each other", "Baton", ["Bib", "Bidon", "Musette"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-138.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
