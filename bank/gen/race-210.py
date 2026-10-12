# Bank session 12 Oct 2026: 1 more general race -> bank/race-210.json (Hogmanay words). Checked against the Burns Night,
# Christmas, Scots words and New Year custom races: no right answer repeats theirs.
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

race("what's this Hogmanay word?", "Scotland", "medium", ["Hogmanay", "New Year", "Scotland", "words"], [
 ("The Scots name for New Year's Eve", "Hogmanay", ["Burns Night", "Martinmas", "Halloween"]),
 ("The Scots name for New Year's Day", "Ne'erday", ["Yule", "Martinmas", "Candlemas"]),
 ("What Scots call the stroke of midnight", "The Bells", ["The Gong", "The Toll", "The Countdown"]),
 ("Being the first to cross the doorstep after midnight", "First-footing", ["Gate-crashing", "Door-knocking", "Toe-tapping"]),
 ("The luckiest kind of first-footer to get", "Tall dark stranger", ["Red-haired woman", "Fair-haired man", "Short bald man"]),
 ("Carried by a first-footer to bring warmth to the house", "Lump of coal", ["Candle", "Matchbox", "Horseshoe"]),
 ("The buttery biscuit a first-footer might bring", "Shortbread", ["Ginger nut", "Custard cream", "Jaffa cake"]),
 ("Rich fruit cake baked inside pastry, eaten at New Year", "Black bun", ["Dundee cake", "Selkirk bannock", "Eccles cake"]),
 ("The traditional New Year's Day dinner in Scotland", "Steak pie", ["Haggis", "Roast goose", "Fish pie"]),
 ("Cleaning the house top to bottom before the year ends", "Redding the house", ["Spring clean", "Scrubbing up", "Turning out"]),
 ("Clearing these before midnight, so the new year starts fresh", "Paying your debts", ["Making a will", "Writing letters", "Burning bills"]),
 ("The New Year's Day dip in the freezing Firth of Forth", "Loony Dook", ["Big Splash", "Cold Snap", "Sea Shanty"]),
 ("The town where people swing balls of fire through the streets", "Stonehaven", ["Stirling", "Oban", "Inverness"]),
 ("Home of the famous Hogmanay street party below the castle", "Edinburgh", ["Glasgow", "Aberdeen", "Dundee"]),
 ("The flaming parade that opens Edinburgh's Hogmanay", "Torchlight procession", ["Lantern parade", "Carnival", "Pageant"]),
 ("The extra bank holiday Scotland gets after New Year's Day", "2 January", ["1 February", "31 December", "6 January"]),
 ("The first Monday of the year, when gifts were once given", "Handsel Monday", ["Plough Monday", "Blue Monday", "Easter Monday"]),
 ("Shetland's Viking fire festival in January", "Up Helly Aa", ["Beltane", "Samhain", "Imbolc"]),
 ("Hot spiced ale with whisky, once carried round at New Year", "Het pint", ["Hot toddy", "Mulled wine", "Snakebite"]),
 ("A promise to change your ways in the new year", "Resolution", ["Revolution", "Reflection", "Recollection"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-210.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
