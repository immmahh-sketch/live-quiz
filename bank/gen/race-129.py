# Bank session 10 Oct 2026: 2 more general races -> bank/race-129.json (baking words, sewing and knitting words). 20 rows each, target 10; wrong options are
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


race("what's this baking word?", "Food and drink", "medium", ["baking", "cooking", "Bake Off"], [
 ("Push, stretch and fold bread dough with the heels of your hands", "Knead", ["Baste", "Truss", "Macerate"]),
 ("Leave dough somewhere warm so it rises", "Prove", ["Reduce", "Render", "Coddle"]),
 ("Gently cut a spoon through a mixture so you keep the air in", "Fold", ["Baste", "Blanch", "Deglaze"]),
 ("Beat butter and sugar together until pale and fluffy", "Cream", ["Coddle", "Render", "Macerate"]),
 ("Work butter into flour with your fingertips until it looks like breadcrumbs", "Rub in", ["Baste", "Truss", "Deglaze"]),
 ("Bake a pastry case with no filling, weighed down with baking beans", "Blind bake", ["Flambé", "Braise", "Poach"]),
 ("Brush beaten egg or milk on top for a shiny finish", "Glaze", ["Baste", "Blanch", "Render"]),
 ("Shake flour through a sieve to get rid of lumps", "Sift", ["Reduce", "Render", "Julienne"]),
 ("Beat egg whites fast to fill them with air", "Whisk", ["Coddle", "Poach", "Truss"]),
 ("Squeeze icing or cream through a nozzle in a bag", "Pipe", ["Julienne", "Truss", "Baste"]),
 ("Heat and cool chocolate carefully so it sets glossy and snaps", "Temper", ["Reduce", "Render", "Macerate"]),
 ("Fold butter into dough again and again to make croissant layers", "Laminate", ["Truss", "Braise", "Julienne"]),
 ("Pinch the edge of a pie or pasty into a wavy pattern", "Crimp", ["Truss", "Baste", "Julienne"]),
 ("Slash the top of a loaf with a blade before it goes in the oven", "Score", ["Julienne", "Truss", "Render"]),
 ("Heat sugar until it melts and turns golden brown", "Caramelise", ["Render", "Reduce", "Deglaze"]),
 ("A bowl set over a pan of simmering water, for melting chocolate gently", "Bain-marie", ["Brûlée", "Roulade", "Streusel"]),
 ("Pastry that hasn't cooked through underneath, dreaded on Bake Off", "Soggy bottom", ["Roulade", "Streusel", "Lattice"]),
 ("Chocolate melted into warm cream, for icing or truffles", "Ganache", ["Fondant", "Frangipane", "Couverture"]),
 ("Egg whites and sugar whisked stiff and baked until crisp", "Meringue", ["Frangipane", "Streusel", "Fondant"]),
 ("The texture of the inside of a cake or loaf, as judged on Bake Off", "Crumb", ["Lattice", "Streusel", "Roulade"])])

race("what's this sewing or knitting word?", "Everyday life", "hard", ["sewing", "knitting", "crafts"], [
 ("A little metal cap that protects your finger as you push a needle", "Thimble", ["Bodkin", "Spool", "Eyelet"]),
 ("The small spool under a sewing machine that holds the lower thread", "Bobbin", ["Bodkin", "Toile", "Eyelet"]),
 ("Turn up the raw edge of a trouser leg and stitch it down", "Hem", ["Gusset", "Placket", "Yoke"]),
 ("Weaving thread back and forth across a hole in a sock to mend it", "Darning", ["Tatting", "Felting", "Ruching"]),
 ("The knitting stitch that's the opposite of plain", "Purl", ["Rib", "Cable", "Moss stitch"]),
 ("Putting the first row of stitches onto your knitting needle", "Casting on", ["Casting off", "Garter stitch", "Cable"]),
 ("Scissors with zig-zag blades that stop fabric fraying", "Pinking shears", ["Thread snips", "Bodkin", "Awl"]),
 ("Big temporary stitches that hold fabric in place before the proper sewing", "Tacking", ["Shirring", "Ruching", "Felting"]),
 ("A small hooked tool for unpicking stitches", "Seam ripper", ["Bodkin", "Awl", "Thread snips"]),
 ("The tightly woven edge of a length of fabric that doesn't fray", "Selvedge", ["Placket", "Godet", "Yoke"]),
 ("Two wooden rings that hold fabric taut while you stitch a design", "Embroidery hoop", ["Spool", "Bodkin", "Toile"]),
 ("Making fabric from yarn with a single hook", "Crochet", ["Tatting", "Macramé", "Weaving"]),
 ("A tapered fold stitched in to shape a garment to the body", "Dart", ["Gusset", "Godet", "Yoke"]),
 ("A fold pressed into fabric, as on a kilt or a school skirt", "Pleat", ["Gusset", "Placket", "Yoke"]),
 ("Stitching shapes cut from one fabric on top of another", "Appliqué", ["Batik", "Felting", "Tatting"]),
 ("X-shaped stitches on a grid that build up a picture", "Cross stitch", ["Tatting", "Macramé", "Batik"]),
 ("Stitching layers of fabric and padding together, often in patchwork", "Quilting", ["Felting", "Batik", "Weaving"]),
 ("A strip of fabric cut diagonally, used to finish curved edges", "Bias binding", ["Ric-rac", "Grosgrain", "Interfacing"]),
 ("Gathering fabric into a tight honeycomb pattern, as on the front of a child's dress", "Smocking", ["Tatting", "Batik", "Felting"]),
 ("A machine that trims a seam and wraps its edge in thread in one go", "Overlocker", ["Treadle", "Loom", "Spinning wheel"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-129.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
