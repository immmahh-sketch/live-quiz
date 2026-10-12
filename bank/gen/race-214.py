# Bank session 12 Oct 2026: 1 more general race -> bank/race-214.json (British breads). Checked against the bread-by-country,
# cake and biscuit, baking, Bake Off and Pancake Day races: no right answer repeats theirs.
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

race("which British bread is this?", "Food and drink", "medium", ["bread", "British food", "North East"], [
 ("Flat, round, heavy North East loaf, often filled with ham and pease pudding", "Stottie", ["Focaccia", "Naan", "Pitta"]),
 ("Lancashire's word for a soft round bread roll", "Barm cake", ["Bap", "Batch", "Breadcake"]),
 ("The East Midlands word for a crusty round roll", "Cob", ["Bap", "Batch", "Breadcake"]),
 ("A long loaf with diagonal slashes across the top", "Bloomer", ["Baguette", "Ciabatta", "Challah"]),
 ("Two round loaves, a small one sat on top of a big one", "Cottage loaf", ["Brioche", "Bagel", "Pretzel"]),
 ("A tin loaf with a long split down the middle", "Split tin", ["Ciabatta", "Focaccia", "Rye bread"]),
 ("Spongy round griddle bread full of holes, eaten toasted", "Crumpet", ["Scone", "Pancake", "Waffle"]),
 ("A thin, flat crumpet made without a ring", "Pikelet", ["Oatcake", "Pancake", "Drop scone"]),
 ("A flat round bun split and toasted, as in eggs Benedict", "English muffin", ["Bagel", "Scone", "Brioche"]),
 ("A Northern Irish griddle bread cut into quarters", "Farl", ["Bap", "Oatcake", "Scone"]),
 ("A flat Scottish oat or barley loaf baked on a griddle", "Bannock", ["Pancake", "Pitta", "Croissant"]),
 ("Northumbria's griddle scone that sizzles as it cooks", "Singin' hinny", ["Fat rascal", "Welsh cake", "Rock cake"]),
 ("Sticky Wiltshire bread made with lard, sugar and dried fruit", "Lardy cake", ["Fruit loaf", "Bara brith", "Panettone"]),
 ("A flat Lancashire roll baked on the floor of the oven", "Oven bottom muffin", ["Bap", "Batch", "Breadcake"]),
 ("Brown bread with malted wheat grains, a famous trade name", "Granary", ["Rye bread", "Challah", "Pumpernickel"]),
 ("Bread made from the whole wheat grain", "Wholemeal", ["White", "Rye bread", "Sourdough"]),
 ("A sweet fruited bun, split, toasted and buttered", "Teacake", ["Brioche", "Croissant", "Iced bun"]),
 ("A very thick slice of bread", "Doorstep", ["Wedge", "Slab", "Brick"]),
 ("The crusty end slice of a loaf", "Heel", ["Butt", "Elbow", "Knob"]),
 ("Strips of toast for dipping into a boiled egg", "Soldiers", ["Sticks", "Twigs", "Ladders"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-214.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
