# Bank session 10 Oct 2026: 2 more general races -> bank/race-115.json (old country names, fast food). 20 rows each, target 10; wrong options are
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

race("which country used to be called this?", "World geography", "hard", ["countries", "old names", "history"], [
 ("Rhodesia", "Zimbabwe", ["Mozambique", "South Africa", "Angola"]),
 ("Zaire", "DR Congo", ["Republic of the Congo", "Angola", "Gabon"]),
 ("Abyssinia", "Ethiopia", ["Eritrea", "Somalia", "Sudan"]),
 ("The Gold Coast", "Ghana", ["Togo", "Nigeria", "Ivory Coast"]),
 ("Dahomey", "Benin", ["Togo", "Niger", "Mali"]),
 ("Upper Volta", "Burkina Faso", ["Mali", "Niger", "Senegal"]),
 ("Kampuchea", "Cambodia", ["Laos", "Vietnam", "Thailand"]),
 ("East Pakistan", "Bangladesh", ["Pakistan", "Nepal", "Sri Lanka"]),
 ("Formosa", "Taiwan", ["Hong Kong", "Japan", "The Philippines"]),
 ("Swaziland", "Eswatini", ["South Africa", "Mozambique", "Zambia"]),
 ("Bechuanaland", "Botswana", ["Zambia", "Angola", "Mozambique"]),
 ("Basutoland", "Lesotho", ["Zambia", "Angola", "Kenya"]),
 ("Nyasaland", "Malawi", ["Zambia", "Tanzania", "Mozambique"]),
 ("British Honduras", "Belize", ["Honduras", "Guatemala", "Nicaragua"]),
 ("Dutch Guiana", "Suriname", ["Guyana", "French Guiana", "Venezuela"]),
 ("The New Hebrides", "Vanuatu", ["Fiji", "Solomon Islands", "Samoa"]),
 ("The Ellice Islands", "Tuvalu", ["Fiji", "Nauru", "Samoa"]),
 ("The Gilbert Islands", "Kiribati", ["Nauru", "Tonga", "Fiji"]),
 ("Mesopotamia, more or less", "Iraq", ["Syria", "Iran", "Jordan"]),
 ("South West Africa", "Namibia", ["Angola", "South Africa", "Zambia"])])

race("which chain sells this?", "Food and drink", "easy", ["fast food", "brands"], [
 ("The Whopper", "Burger King", ["Shake Shack", "Five Guys", "Byron"]),
 ("The Big Mac", "McDonald's", ["Five Guys", "Byron", "Carl's Jr."]),
 ("The Zinger burger", "KFC", ["Popeyes", "Chick-fil-A", "Chicken Cottage"]),
 ("The Footlong", "Subway", ["Pret A Manger", "Jimmy John's", "Quiznos"]),
 ("Butterfly chicken with peri-peri sauce", "Nando's", ["Chicken Cottage", "Popeyes", "Chick-fil-A"]),
 ("The steak bake", "Greggs", ["Pret A Manger", "Cooplands", "Warrens"]),
 ("The Frappuccino", "Starbucks", ["Costa", "Caffè Nero", "Pret A Manger"]),
 ("The Stuffed Crust pizza", "Pizza Hut", ["Papa John's", "Franco Manca", "Papa Murphy's"]),
 ("The Original Glazed doughnut", "Krispy Kreme", ["Doughnut Time", "Crosstown", "Dum Dum Donutterie"]),
 ("The Blizzard", "Dairy Queen", ["Baskin-Robbins", "Ben & Jerry's", "Häagen-Dazs"]),
 ("The Frosty", "Wendy's", ["Five Guys", "Shake Shack", "Byron"]),
 ("The Chalupa", "Taco Bell", ["Chipotle", "Tortilla", "Barburrito"]),
 ("Chicken katsu curry, served in a canteen", "Wagamama", ["Itsu", "Yo! Sushi", "Wasabi"]),
 ("The Bender in a bun", "Wimpy", ["Happy Eater", "Berni Inn", "Harvester"]),
 ("The Olympic Breakfast, by the roadside", "Little Chef", ["Happy Eater", "Harvester", "Beefeater"]),
 ("The Mighty Meaty pizza", "Domino's", ["Papa John's", "Franco Manca", "Papa Murphy's"]),
 ("Dough Balls with garlic butter", "Pizza Express", ["Prezzo", "Zizzi", "Ask Italian"]),
 ("Timbits", "Tim Hortons", ["Baskin-Robbins", "Doughnut Time", "Costa"]),
 ("Munchkins", "Dunkin'", ["Baskin-Robbins", "Doughnut Time", "Costa"]),
 ("The Double-Double", "In-N-Out", ["Shake Shack", "Five Guys", "Whataburger"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-115.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
