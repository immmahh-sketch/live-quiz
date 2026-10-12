# Bank session 12 Oct 2026: 1 more general race -> bank/race-206.json (fish and chip shop words). No other race covers chippies;
# only Haddock (seafood race) and Gravy (Sunday roast race) appear in other races, with different clues.
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

race("what's this fish and chip shop word?", "Food and drink", "easy", ["fish and chips", "chippy", "food", "words"], [
 ("Crispy bits of fried batter, scooped from the fryer", "Scraps", ["Crumbs", "Flakes", "Shavings"]),
 ("Soft green side made from marrowfat peas", "Mushy peas", ["Petits pois", "Garden peas", "Split peas"]),
 ("Britain's most popular chip shop fish", "Cod", ["Hake", "Pollock", "Whiting"]),
 ("The chippy fish Yorkshire and Scotland prefer", "Haddock", ["Hake", "Pollock", "Whiting"]),
 ("A flat fish with orange spots", "Plaice", ["Turbot", "Halibut", "Sole"]),
 ("A flat, wing-shaped fish, served on the bone", "Skate", ["Turbot", "Halibut", "Sole"]),
 ("The bright red, smoked sausage sold in chippies", "Saveloy", ["Chorizo", "Frankfurter", "Black pudding"]),
 ("A sausage dipped in batter and deep-fried", "Battered sausage", ["Toad in the hole", "Corn dog", "Sausage roll"]),
 ("A whole onion kept in vinegar in a jar on the counter", "Pickled onion", ["Spring onion", "Red onion", "Onion ring"]),
 ("Mashed fish and potato, shaped and fried", "Fishcake", ["Fish finger", "Goujon", "Fish pie"]),
 ("Scotland's famous chippy pudding: a chocolate bar in batter", "Deep-fried Mars bar", ["Deep-fried Twix", "Deep-fried Snickers", "Deep-fried Bounty"]),
 ("Malt, or 'non-brewed condiment': what you shake on your chips", "Vinegar", ["Brown sauce", "Ketchup", "Mayonnaise"]),
 ("Thick brown sauce poured over chips in the North", "Gravy", ["Brown sauce", "Bread sauce", "Custard"]),
 ("Yellowy-brown spicy sauce, a chippy classic", "Curry sauce", ["Tikka masala", "Korma", "Satay"]),
 ("What chips were famously wrapped in, back in the day", "Newspaper", ["Tracing paper", "Wallpaper", "Parchment"]),
 ("A buttered bread roll stuffed with chips", "Chip butty", ["Bacon butty", "Toastie", "Sausage roll"]),
 ("A slice of potato dipped in batter and fried", "Potato fritter", ["Hash brown", "Rösti", "Croquette"]),
 ("The fat many Northern chippies still fry in", "Beef dripping", ["Olive oil", "Butter", "Coconut oil"]),
 ("Scotland's orange fizzy drink, a chippy favourite", "Irn-Bru", ["Vimto", "Tizer", "Dandelion and burdock"]),
 ("The North East's yellow split-pea spread, great with a saveloy", "Pease pudding", ["Hummus", "Black pudding", "Polenta"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-206.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
