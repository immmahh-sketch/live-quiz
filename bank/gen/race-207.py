# Bank session 12 Oct 2026: 2 more general races -> bank/race-207.json (Monopoly words, whisky words). No race covers either;
# checked against the drink, Scots and board game races: only Bourbon, Islay, Go and Free Parking repeat, with different clues.
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

race("what's this Monopoly word?", "Games and toys", "easy", ["Monopoly", "board games", "words"], [
 ("The corner square where you collect £200", "Go", ["Start", "Home", "Bank"]),
 ("The first property after Go on the UK board", "Old Kent Road", ["Euston Road", "Pentonville Road", "Bow Street"]),
 ("The most expensive property on the UK board", "Mayfair", ["Regent Street", "Oxford Street", "Piccadilly"]),
 ("Mayfair's dark blue partner", "Park Lane", ["Strand", "Whitehall", "Fleet Street"]),
 ("The dearest of the three green properties", "Bond Street", ["Regent Street", "Oxford Street", "Leicester Square"]),
 ("The corner where you're 'just visiting' or locked up", "Jail", ["Court", "Police station", "Workhouse"]),
 ("The corner square where nothing happens, by the rules", "Free Parking", ["Rest Stop", "Car Park", "Lay-by"]),
 ("The card you can keep until you need to escape", "Get Out of Jail Free", ["Bail card", "Royal pardon", "Lucky break"]),
 ("The pile of cards shown as a treasure chest", "Community Chest", ["Lucky Dip", "Treasure Trove", "Bank Holiday"]),
 ("The pile of cards marked with a question mark", "Chance", ["Fortune", "Fate", "Luck"]),
 ("The first station on the UK board, after Go", "King's Cross Station", ["Marylebone Station", "Fenchurch St Station", "Liverpool Street Station"]),
 ("The utility that isn't the Electric Company", "Water Works", ["Electric Company", "Gas Board", "Sewage Works"]),
 ("The tax square just before Mayfair on the UK board", "Super Tax", ["Income Tax", "Luxury Tax", "Poll Tax"]),
 ("What you build in place of four houses", "Hotel", ["Castle", "Mansion", "Skyscraper"]),
 ("The player who looks after all the money", "Banker", ["Treasurer", "Cashier", "Accountant"]),
 ("Turning a property card over to borrow from the bank", "Mortgage", ["Loan", "Overdraft", "Pawn"]),
 ("Selling a property to the highest bidder", "Auction", ["Raffle", "Clearance", "Tender"]),
 ("The token voted out in 2013 and replaced by a cat", "Iron", ["Boot", "Top hat", "Racing car"]),
 ("The board's moustached mascot in the top hat", "Mr Monopoly", ["Mr Moneybags", "Uncle Scrooge", "Mr Banker"]),
 ("The colour of the Mayfair and Park Lane set", "Dark blue", ["Green", "Red", "Orange"])])

race("what's this whisky word?", "Beer, wine and spirits", "medium", ["whisky", "Scotland", "drinks", "words"], [
 ("Whisky from one distillery, made only from malted barley", "Single malt", ["Grain whisky", "Blend", "Moonshine"]),
 ("American whiskey made mostly from corn", "Bourbon", ["Moonshine", "Sake", "Brandy"]),
 ("The Scots word for a small measure of whisky", "Dram", ["Pint", "Jigger", "Gill"]),
 ("The wooden barrel whisky ages in", "Cask", ["Keg", "Vat", "Churn"]),
 ("Gives some whiskies their smoky taste when it's burned to dry the barley", "Peat", ["Oak", "Coal", "Charcoal"]),
 ("The building where whisky is made", "Distillery", ["Brewery", "Winery", "Refinery"]),
 ("The Scottish region around the River Spey, home to dozens of distilleries", "Speyside", ["Lowlands", "Campbeltown", "Highlands"]),
 ("The Hebridean island famous for smoky whiskies like Laphroaig", "Islay", ["Skye", "Mull", "Arran"]),
 ("Served on its own, with nothing added", "Neat", ["Dry", "Clean", "Bare"]),
 ("Served poured over ice", "On the rocks", ["Shaken", "Stirred", "Frappé"]),
 ("The whisky that evaporates from the cask as it ages", "Angel's share", ["Devil's cut", "Cellarman's tithe", "Spirit's sigh"]),
 ("What whisky made in Scotland is called", "Scotch", ["Hooch", "Grog", "Firewater"]),
 ("Whiskey made mainly from the grain in dark German bread", "Rye", ["Spelt", "Oats", "Millet"]),
 ("The grain soaked and sprouted to make malt whisky", "Malted barley", ["Sweetcorn", "Wild rice", "Buckwheat"]),
 ("The big copper kettle-shaped vessel malt whisky is distilled in", "Pot still", ["Column still", "Mash tun", "Washback"]),
 ("Smelling a whisky carefully before tasting it", "Nosing", ["Sniffing", "Breathing", "Airing"]),
 ("The old way of measuring how strong a spirit is", "Proof", ["Gauge", "Grade", "Strength"]),
 ("How the Irish and the Americans usually spell it", "Whiskey", ["Whiskie", "Wiskey", "Whisqui"]),
 ("A small flat bottle carried in a pocket", "Hip flask", ["Hipster", "Canteen", "Decanter"]),
 ("Hot water, honey, lemon and a splash of whisky", "Hot toddy", ["Hot buttered rum", "Mulled wine", "Irish coffee"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-207.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
