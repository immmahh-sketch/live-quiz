# Bank session 11 Oct 2026: 3 more general races -> bank/race-190.json (antiques, ice skating and cheese words). 20 rows each, target 10; wrong options are
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

race("what's this antiques word?", "Lifestyle", "medium", ["antiques", "collecting", "words"], [
 ("The stamp proving silver or gold is genuine", "Hallmark", ["Watermark", "Postmark", "Trademark"]),
 ("The documented history of who has owned an item", "Provenance", ["Province", "Prominence", "Prophecy"]),
 ("The mellow sheen old wood or bronze gains with age", "Patina", ["Patio", "Pastiche", "Paprika"]),
 ("A modern copy made to look old", "Reproduction", ["Renovation", "Recreation", "Reception"]),
 ("Repairing an old piece to its former glory", "Restoration", ["Reformation", "Revelation", "Resignation"]),
 ("A thin layer of fine wood glued over cheaper wood", "Veneer", ["Varnish", "Venom", "Vellum"]),
 ("The interlocking joint in well-made drawers", "Dovetail", ["Pigeonhole", "Ducktail", "Fishtail"]),
 ("The 18th-century London cabinetmaker most famous for chairs", "Chippendale", ["Sheraton", "Hepplewhite", "Wedgwood"]),
 ("The bold geometric style of the 1920s and 30s", "Art Deco", ["Baroque", "Rococo", "Gothic"]),
 ("The flowing, plant-like style from around 1900", "Art Nouveau", ["Pop Art", "Cubism", "Brutalism"]),
 ("Small ornaments of little value", "Bric-a-brac", ["Abracadabra", "Tic-tac", "Brick-and-mortar"]),
 ("The BBC show where experts value the public's heirlooms", "Antiques Roadshow", ["Homes Under the Hammer", "Gardeners' World", "Countryfile"]),
 ("The show where teams buy at a fair, then sell at auction", "Bargain Hunt", ["Flog It!", "Cash in the Attic", "The Repair Shop"]),
 ("The 'cheap as chips' host with the permanent tan", "David Dickinson", ["Tim Wonnacott", "David Dimbleby", "Paul Martin"]),
 ("Fine white ceramic, often just called 'china'", "Porcelain", ["Terracotta", "Stoneware", "Enamel"]),
 ("A jug shaped like a seated man in a tricorn hat", "Toby jug", ["Toby Carvery", "Gravy boat", "Tankard"]),
 ("A tall floor-standing pendulum clock", "Grandfather clock", ["Cuckoo clock", "Carriage clock", "Body clock"]),
 ("An upholstered sofa shaped like a very long chair", "Chaise longue", ["Chesterfield", "Ottoman", "Divan"]),
 ("A thin coating of gold", "Gilt", ["Guilt", "Chrome", "Pewter"]),
 ("Selling from your car on a Sunday morning", "Car boot sale", ["Jumble sale", "Bake sale", "Fire sale"])])

race("what's this ice skating word?", "Sport", "medium", ["figure skating", "ice", "words"], [
 ("The only jump that takes off going forwards", "Axel", ["Lutz", "Salchow", "Flip"]),
 ("The jagged teeth at the front of the blade", "Toe pick", ["Toe cap", "Ice pick", "Toe ring"]),
 ("The machine that resurfaces the ice", "Zamboni", ["Zambezi", "Lamborghini", "Panini"]),
 ("Where skaters sit waiting for their scores", "Kiss and cry", ["Kiss and tell", "Hide and seek", "Rise and shine"]),
 ("The pairs move where she circles almost flat to the ice", "Death spiral", ["Death roll", "Spiral staircase", "Tailspin"]),
 ("Quick travelling turns on one foot in ice dance", "Twizzle", ["Twister", "Twiglet", "Fizzle"]),
 ("A man and woman skating together with throws and lifts", "Pairs", ["Doubles", "Duet", "Tandem"]),
 ("The discipline with no big jumps, closest to ballroom", "Ice dance", ["Ice hockey", "Ice ballet", "Curling"]),
 ("Britain's 1984 Olympic ice dance champions", "Torvill and Dean", ["Ant and Dec", "Richard and Judy", "Morecambe and Wise"]),
 ("The music of their famous routine", "Boléro", ["Swan Lake", "Carmen", "The Nutcracker"]),
 ("The ITV show where celebrities learn to skate", "Dancing on Ice", ["Strictly Come Dancing", "Ice Ice Baby", "The Jump"]),
 ("The sheet of ice you skate on", "Rink", ["Pitch", "Court", "Lane"]),
 ("Spinning with your body and free leg level with the ice", "Camel spin", ["Swan spin", "Dolphin spin", "Llama spin"]),
 ("Spinning crouched low on one leg", "Sit spin", ["Squat spin", "Stand spin", "Lie spin"]),
 ("A jump with four full turns", "Quad", ["Triple", "Double", "Single"]),
 ("The first, shorter routine of a competition", "Short programme", ["Warm-up", "Overture", "Prologue"]),
 ("The longer second routine", "Free skate", ["Free kick", "Free fall", "Free throw"]),
 ("Raising your partner above your head", "Lift", ["Hoist", "Elevator", "Throw"]),
 ("Plastic covers for the blades off the ice", "Skate guards", ["Shin guards", "Mudguards", "Fireguards"]),
 ("The metal strip under the boot", "Blade", ["Sole", "Heel", "Skid"])])

race("what's this cheese word?", "Food and drink", "medium", ["cheese", "food", "words"], [
 ("The hard outer skin of a cheese", "Rind", ["Crust", "Peel", "Shell"]),
 ("The soft white lumps that form as milk sets", "Curds", ["Clots", "Flakes", "Crumbs"]),
 ("The watery liquid strained off in cheesemaking", "Whey", ["Brine", "Buttermilk", "Syrup"]),
 ("The enzyme added to milk to make it set", "Rennet", ["Yeast", "Gelatine", "Pectin"]),
 ("What makes the blue veins in Stilton", "Mould", ["Dye", "Ink", "Rust"]),
 ("A cheddar aged for a stronger flavour", "Mature", ["Mild", "Young", "Fresh"]),
 ("Wallace and Gromit's favourite cheese", "Wensleydale", ["Stilton", "Cheshire", "Red Leicester"]),
 ("Squeaky Cypriot cheese for the grill", "Halloumi", ["Ricotta", "Mascarpone", "Gruyère"]),
 ("Salty Greek cheese kept in brine", "Feta", ["Ricotta", "Mascarpone", "Edam"]),
 ("The Indian cheese in saag and matar dishes", "Paneer", ["Ricotta", "Edam", "Gouda"]),
 ("Melted cheese in a pot for dipping bread", "Fondue", ["Fondant", "Soufflé", "Gratin"]),
 ("A selection served after dinner with crackers", "Cheeseboard", ["Breadboard", "Chessboard", "Sideboard"]),
 ("Someone who sells cheese", "Cheesemonger", ["Fishmonger", "Ironmonger", "Costermonger"]),
 ("The red coating on a Babybel", "Wax", ["Foil", "Plastic", "Paper"]),
 ("The kitchen tool for shredding cheese", "Grater", ["Peeler", "Masher", "Zester"]),
 ("Chasing a Double Gloucester down Cooper's Hill", "Cheese rolling", ["Egg rolling", "Bog snorkelling", "Shin-kicking"]),
 ("The hard Italian cheese grated over pasta", "Parmesan", ["Ricotta", "Gorgonzola", "Mascarpone"]),
 ("The stretchy white cheese on a margherita pizza", "Mozzarella", ["Stilton", "Camembert", "Gouda"]),
 ("The pub lunch of bread, cheese and pickle", "Ploughman's", ["Fisherman's", "Shepherd's", "Woodsman's"]),
 ("Cheese on toast with mustard and ale", "Welsh rarebit", ["Welsh cake", "Bara brith", "Scotch woodcock"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-190.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
