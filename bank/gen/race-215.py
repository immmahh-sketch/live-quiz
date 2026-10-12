# Bank session 12 Oct 2026: 1 more general race -> bank/race-215.json (school dinners). Checked against the school words, sweet
# shop, classic sweets, pudding and 1970s races: tuck shop and dinner lady left out, as the school words race has them.
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

race("what's this school dinner word?", "Food and drink", "easy", ["school dinners", "nostalgia", "food", "words"], [
 ("Lumpy tapioca pudding, nicknamed after pond life", "Frogspawn", ["Snails", "Tadpoles", "Slime"]),
 ("Rock-hard chocolate traybake served with pink custard", "Chocolate concrete", ["Rocky road", "Tiffin", "Brownie"]),
 ("The custard that came in a strange bright colour", "Pink custard", ["Green custard", "Blue custard", "Purple custard"]),
 ("Spiral turkey sticks Jamie Oliver campaigned against", "Turkey Twizzlers", ["Chicken nuggets", "Turkey dinosaurs", "Sausage rolls"]),
 ("The TV chef behind the 2005 school food campaign", "Jamie Oliver", ["Gordon Ramsay", "Delia Smith", "Hugh Fearnley-Whittingstall"]),
 ("Pastry case of jam topped with syrupy cornflakes", "Cornflake tart", ["Bakewell tart", "Treacle tart", "Custard tart"]),
 ("Tart of jam, custard and desiccated coconut, from the North West", "Manchester tart", ["Liverpool tart", "Gypsy tart", "Yorkshire curd tart"]),
 ("Milky wheat pudding, often with a blob of jam in the middle", "Semolina", ["Porridge", "Polenta", "Couscous"]),
 ("Suet pudding rolled up with jam", "Jam roly-poly", ["Swiss roll", "Bread pudding", "Sticky toffee pudding"]),
 ("Ice cream wrapped in sponge, a 1970s favourite", "Arctic roll", ["Viennetta", "Choc ice", "Baked Alaska"]),
 ("Plain sponge drowned in runny custard", "Sponge and custard", ["Trifle", "Eton mess", "Knickerbocker glory"]),
 ("Going back up for more", "Seconds", ["Extras", "Afters", "Leftovers"]),
 ("Breaded fish strips, a Friday favourite", "Fish fingers", ["Fish cakes", "Scampi", "Goujons"]),
 ("Smiley-faced potato shapes", "Potato smileys", ["Hash browns", "Potato waffles", "Croquettes"]),
 ("Fried slices of luncheon meat in batter", "Spam fritters", ["Corned beef hash", "Faggots", "Scotch eggs"]),
 ("Instant pudding whisked up with milk", "Angel Delight", ["Instant Whip", "Bird's Trifle", "Ready Brek"]),
 ("Lunch brought from home in a box", "Packed lunch", ["Takeaway", "Picnic", "Doggy bag"]),
 ("Meals paid for by the state for poorer pupils", "Free school meals", ["Meal deals", "Food parcels", "Luncheon vouchers"]),
 ("The big room where everyone ate", "Dinner hall", ["Staff room", "Common room", "Cloakroom"]),
 ("The free third-of-a-pint drink taken away from most pupils in 1971", "Milk", ["Orange squash", "Water", "Ribena"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-215.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
