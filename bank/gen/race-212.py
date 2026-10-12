# Bank session 12 Oct 2026: 1 more general race -> bank/race-212.json (allotment words). Checked against the gardening, farm
# and fruit-and-veg variety races: no right answer repeats theirs.
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

race("what's this allotment word?", "Nature", "medium", ["allotments", "gardening", "vegetables", "words"], [
 ("The little wooden hut on every plot", "Shed", ["Gazebo", "Pergola", "Summerhouse"]),
 ("Your own patch of ground at the allotments", "Plot", ["Paddock", "Croft", "Acre"]),
 ("A big barrel collecting rainwater off the shed roof", "Water butt", ["Cistern", "Sump", "Trough"]),
 ("A tall clay pot put over a crown to grow pale, tender stalks", "Rhubarb forcer", ["Bell jar", "Plant pot", "Chimney pot"]),
 ("Climbing beans with scarlet flowers, grown up canes", "Runner beans", ["Broad beans", "Kidney beans", "Butter beans"]),
 ("The thick-stemmed giant grown for North East shows", "Pot leek", ["Spring onion", "Shallot", "Celeriac"]),
 ("The old measure of a standard plot: ten of these", "Rod", ["Chain", "Furlong", "Yard"]),
 ("Mesh draped over the cabbages to keep the pigeons off", "Netting", ["Bunting", "Tarpaulin", "Muslin"]),
 ("A long, curved plastic greenhouse", "Polytunnel", ["Orangery", "Conservatory", "Gazebo"]),
 ("A bed built up inside wooden boards", "Raised bed", ["Flower bed", "Sunbed", "Water bed"]),
 ("Spuds you plant to grow next year's crop", "Seed potatoes", ["New potatoes", "Jacket potatoes", "Mash"]),
 ("Leaving seed potatoes on a windowsill to sprout first", "Chitting", ["Thinning", "Sowing", "Pricking out"]),
 ("Piling soil up round the potato stems", "Earthing up", ["Digging in", "Turning over", "Bedding down"]),
 ("Growing a different crop in each bed every year", "Crop rotation", ["Crop circle", "Companion planting", "Succession sowing"]),
 ("Plants like clover grown to be dug back in and feed the soil", "Green manure", ["Bone meal", "Blood, fish and bone", "Wood ash"]),
 ("Rotted-down autumn leaves used to improve the soil", "Leaf mould", ["Peat", "Bark chips", "Gravel"]),
 ("What you join to get a plot in many towns", "Waiting list", ["Guest list", "Wish list", "Shortlist"]),
 ("Little blue pellets that stop slimy pests", "Slug pellets", ["Bird seed", "Mothballs", "Weedkiller"]),
 ("The cabbage, sprout and kale family", "Brassicas", ["Legumes", "Alliums", "Cucurbits"]),
 ("Hairy green berries on a prickly bush", "Gooseberry", ["Blackcurrant", "Redcurrant", "Cranberry"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-212.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
