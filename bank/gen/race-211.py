# Bank session 12 Oct 2026: 1 more general race -> bank/race-211.json (St Patrick's Day words). Checked against the Irish towns,
# Irish words and Irish acts races: no right answer repeats theirs.
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

race("what's this St Patrick's Day word?", "Ireland", "easy", ["St Patrick's Day", "Ireland", "words"], [
 ("The three-leafed plant worn on St Patrick's Day", "Shamrock", ["Thistle", "Leek", "Rose"]),
 ("The little bearded shoemaker of Irish folklore", "Leprechaun", ["Banshee", "Pixie", "Goblin"]),
 ("What the leprechaun hides at the end of the rainbow", "Pot of gold", ["Chest of silver", "Bag of jewels", "Box of shillings"]),
 ("The date of St Patrick's Day", "17 March", ["17 April", "1 March", "23 April"]),
 ("The creatures St Patrick is said to have driven out of Ireland", "Snakes", ["Wolves", "Rats", "Frogs"]),
 ("The colour everyone wears on the day", "Green", ["Orange", "White", "Gold"]),
 ("Ireland's nickname, for its green fields", "Emerald Isle", ["Jade Coast", "Green Land", "Shamrock Shore"]),
 ("The American river dyed green every year", "Chicago River", ["Hudson", "Mississippi", "Potomac"]),
 ("The dark stout poured by the million that day", "Guinness", ["Newcastle Brown", "Old Speckled Hen", "Bishop's Finger"]),
 ("The stone you kiss for the gift of the gab", "Blarney Stone", ["Stone of Destiny", "Rosetta Stone", "Hag Stone"]),
 ("A lively Irish folk dance", "Jig", ["Waltz", "Polka", "Tango"]),
 ("The 1994 Eurovision interval act that made Irish dancing a worldwide hit", "Riverdance", ["Lord of the Dance", "Feet of Flames", "Stomp"]),
 ("The Irish loaf raised with bicarbonate instead of yeast", "Soda bread", ["Sourdough", "Brioche", "Barm cake"]),
 ("The musical instrument that's Ireland's national emblem", "Harp", ["Lyre", "Fiddle", "Bagpipes"]),
 ("The Irish frame drum played with a short stick", "Bodhrán", ["Tambourine", "Snare drum", "Bongo"]),
 ("Where St Patrick was actually born", "Britain", ["Ireland", "France", "Italy"]),
 ("The holy mountain pilgrims climb, many of them barefoot", "Croagh Patrick", ["Ben Nevis", "Snowdon", "Carrauntoohil"]),
 ("The New York street the big parade marches up", "Fifth Avenue", ["Broadway", "Park Avenue", "Madison Avenue"]),
 ("The Irish whiskey made at Midleton in County Cork", "Jameson", ["Glenfiddich", "Jack Daniel's", "Johnnie Walker"]),
 ("Mashed potato and cabbage, an Irish favourite", "Colcannon", ["Champ", "Bubble and squeak", "Rumbledethumps"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-211.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
