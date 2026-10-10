# Bank session 10 Oct 2026: 4 more general races -> bank/race-15.json. 20 rows each, target 10; wrong options are
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

race("which country is this lake in?", "World geography", "medium", ["lakes", "countries"], [
 ("Loch Ness", "Scotland", ["the Isle of Man", "Norway", "Iceland"]), ("Lake Como", "Italy", ["Switzerland", "Croatia", "Spain"]),
 ("Lake Bled", "Slovenia", ["Croatia", "Slovakia", "Czechia"]), ("Lake Baikal", "Russia", ["Mongolia", "Kazakhstan", "Belarus"]),
 ("Lough Neagh", "Northern Ireland", ["the Isle of Man", "Iceland", "Norway"]), ("Lake Balaton", "Hungary", ["Slovakia", "Czechia", "Croatia"]),
 ("Lake Taupō", "New Zealand", ["Australia", "Fiji", "Samoa"]), ("Lake Louise", "Canada", ["Iceland", "Norway", "Greenland"]),
 ("Lake Tahoe", "the USA", ["Mexico", "Iceland", "Cuba"]), ("Lake Inari", "Finland", ["Estonia", "Norway", "Iceland"]),
 ("Lake Vättern", "Sweden", ["Norway", "Estonia", "Denmark"]), ("Lake Annecy", "France", ["Switzerland", "Belgium", "Luxembourg"]),
 ("The Königssee", "Germany", ["Switzerland", "Czechia", "Liechtenstein"]), ("Lake Hallstatt", "Austria", ["Switzerland", "Liechtenstein", "Czechia"]),
 ("Bala Lake (Llyn Tegid)", "Wales", ["the Isle of Man", "Norway", "Denmark"]), ("Windermere", "England", ["the Isle of Man", "Norway", "Denmark"]),
 ("Lough Corrib", "Ireland", ["the Isle of Man", "Iceland", "Denmark"]), ("Lake Toba", "Indonesia", ["Malaysia", "the Philippines", "Thailand"]),
 ("Lake Pichola, Udaipur", "India", ["Pakistan", "Nepal", "Sri Lanka"]), ("Lake Kawaguchi, below Mount Fuji", "Japan", ["South Korea", "Taiwan", "China"])])

race("which country does this cheese come from?", "Food and drink", "medium", ["cheese", "countries"], [
 ("Brie", "France", ["Belgium", "Luxembourg", "Austria"]), ("Gouda", "the Netherlands", ["Belgium", "Luxembourg", "Austria"]),
 ("Feta", "Greece", ["Turkey", "Bulgaria", "Lebanon"]), ("Mozzarella", "Italy", ["Austria", "Croatia", "Malta"]),
 ("Cheddar", "England", ["Northern Ireland", "the Isle of Man", "Belgium"]), ("Emmental", "Switzerland", ["Austria", "Luxembourg", "Belgium"]),
 ("Manchego", "Spain", ["Argentina", "Chile", "Uruguay"]), ("Halloumi", "Cyprus", ["Turkey", "Lebanon", "Malta"]),
 ("Havarti", "Denmark", ["Iceland", "Estonia", "Belgium"]), ("Jarlsberg", "Norway", ["Iceland", "Estonia", "Belgium"]),
 ("Caerphilly", "Wales", ["Northern Ireland", "the Isle of Man", "Belgium"]), ("Dunlop", "Scotland", ["Northern Ireland", "the Isle of Man", "Iceland"]),
 ("Cashel Blue", "Ireland", ["Northern Ireland", "the Isle of Man", "Iceland"]), ("Bryndza", "Slovakia", ["Czechia", "Hungary", "Austria"]),
 ("Queso Oaxaca", "Mexico", ["Argentina", "Colombia", "Peru"]), ("Västerbottensost", "Sweden", ["Iceland", "Estonia", "Latvia"]),
 ("Oscypek", "Poland", ["Czechia", "Hungary", "Lithuania"]), ("Butterkäse", "Germany", ["Austria", "Luxembourg", "Belgium"]),
 ("Queijo da Serra", "Portugal", ["Brazil", "Argentina", "Uruguay"]), ("Leipäjuusto, the 'squeaky cheese'", "Finland", ["Iceland", "Estonia", "Latvia"])])

race("what does this trade make or work with?", "Words and language", "medium", ["trades", "jobs"], [
 ("Cartographer", "Maps", ["Carts", "Cards", "Calendars"]), ("Lexicographer", "Dictionaries", ["Lectures", "Letters", "Laws"]),
 ("Cooper", "Barrels", ["Copper pots", "Chicken coops", "Baskets"]), ("Fletcher", "Arrows", ["Flutes", "Fences", "Flags"]),
 ("Milliner", "Hats", ["Mills", "Gloves", "Dresses"]), ("Cobbler", "Shoes", ["Saddles", "Belts", "Gloves"]),
 ("Farrier", "Horseshoes", ["Ferries", "Fur coats", "Fences"]), ("Chandler (originally)", "Candles", ["Chandeliers", "Soap", "Lamps"]),
 ("Sommelier", "Wine", ["Cheese", "Bread", "Coffee"]), ("Taxidermist", "Stuffed animals", ["Taxes", "Taxis", "Tattoos"]),
 ("Horologist", "Clocks and watches", ["Horoscopes", "Horses", "Horns"]), ("Luthier", "Guitars and violins", ["Drums", "Trumpets", "Pianos"]),
 ("Apiarist", "Bees", ["Apes", "Wasps", "Ants"]), ("Thatcher", "Straw roofs", ["Hedges", "Fences", "Baskets"]),
 ("Wheelwright", "Wheels", ["Wells", "Whistles", "Saddles"]), ("Glazier", "Windows", ["Ice", "Pottery", "Bricks"]),
 ("Tanner", "Leather", ["Sun tans", "Tents", "Cloth"]), ("Bowyer", "Bows", ["Bowls", "Bow ties", "Boats"]),
 ("Cutler", "Knives", ["Cutlets", "Cups", "Cloth"]), ("Mason", "Stone", ["Jars", "Bricks", "Glass"])])

race("which country did this sport come from?", "Sport", "medium", ["sports", "origins", "countries"], [
 ("Rugby", "England", ["Wales", "New Zealand", "South Africa"]), ("Golf", "Scotland", ["Wales", "Northern Ireland", "Belgium"]),
 ("Basketball", "the USA", ["Cuba", "Germany", "Spain"]), ("Judo", "Japan", ["Taiwan", "Mongolia", "Vietnam"]),
 ("Taekwondo", "South Korea", ["Taiwan", "Mongolia", "Vietnam"]), ("Ice hockey", "Canada", ["Russia", "Norway", "Czechia"]),
 ("Hurling", "Ireland", ["Wales", "Iceland", "Norway"]), ("Kabaddi", "India", ["Malaysia", "Indonesia", "Nepal"]),
 ("Capoeira", "Brazil", ["Portugal", "Argentina", "Cuba"]), ("Pétanque", "France", ["Belgium", "Monaco", "Spain"]),
 ("Australian rules football", "Australia", ["New Zealand", "South Africa", "Fiji"]), ("Bobsleigh", "Switzerland", ["Austria", "Norway", "Germany"]),
 ("Floorball", "Sweden", ["Norway", "Denmark", "Estonia"]), ("Korfball", "the Netherlands", ["Belgium", "Denmark", "Germany"]),
 ("Muay Thai", "Thailand", ["Vietnam", "Malaysia", "the Philippines"]), ("Wushu", "China", ["Taiwan", "Mongolia", "Vietnam"]),
 ("Padel", "Mexico", ["Spain", "Argentina", "Colombia"]), ("Bocce", "Italy", ["Spain", "Malta", "Greece"]),
 ("Pesäpallo (Finnish baseball)", "Finland", ["Estonia", "Norway", "Iceland"]), ("Teqball", "Hungary", ["Austria", "Czechia", "Slovakia"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-15.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
