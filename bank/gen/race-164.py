# Bank session 11 Oct 2026: 3 more general races -> bank/race-164.json (fairground, Victorian and pottery words). 20 rows each, target 10; wrong options are
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

race("what's this fairground word?", "Everyday life", "easy", ["fairs", "rides", "words"], [
 ("Little electric cars you bump into each other", "Dodgems", ["Go-karts", "Bumper boats", "Teacups"]),
 ("Spinning cars on a rolling track, whirled round by the operators", "Waltzer", ["Teacups", "Octopus", "Pirate ship"]),
 ("A spiral slide down a tower, sitting on a mat", "Helter-skelter", ["Log flume", "Drop tower", "Bouncy castle"]),
 ("A giant wheel with seats around the rim", "Big wheel", ["Drop tower", "Pirate ship", "Swingboats"]),
 ("A merry-go-round of painted horses", "Carousel", ["Swingboats", "Teacups", "Octopus"]),
 ("A dark ride full of skeletons and screams", "Ghost train", ["Log flume", "Pirate ship", "Drop tower"]),
 ("The stall where you fish plastic ducks out of the water", "Hook-a-duck", ["Crazy golf", "Shooting gallery", "Bagatelle"]),
 ("Throw balls to knock nuts off their posts", "Coconut shy", ["Shooting gallery", "Skittles", "Crazy golf"]),
 ("Pink spun sugar on a stick", "Candyfloss", ["Toffee apple", "Rock", "Nougat"]),
 ("Cars racing round loops and steep drops", "Rollercoaster", ["Log flume", "Monorail", "Cable car"]),
 ("A room of wobbly glass that makes you look tall or wide", "Hall of mirrors", ["Hall of fame", "Hall of residence", "Music hall"]),
 ("Draw tickets from a spinning drum to win prizes", "Tombola", ["Kitty", "Pools", "Roulette"]),
 ("Hit the pad with a hammer to ring the bell", "Test your strength", ["Arm wrestle", "Tug of war", "Whack-a-mole"]),
 ("The prize once won in a plastic bag of water", "Goldfish", ["Hamster", "Tortoise", "Budgie"]),
 ("Swings on chains that fly outwards as they spin", "Chair-o-planes", ["Swingboats", "Pirate ship", "Teacups"]),
 ("Throw rings over the prizes", "Hoopla", ["Skittles", "Bagatelle", "Bowls"]),
 ("The travelling families who run the fairs", "Showmen", ["Roadies", "Drovers", "Bargees"]),
 ("Newcastle's huge June fair on the Town Moor", "The Hoppings", ["Hull Fair", "Appleby Fair", "Scarborough Fair"]),
 ("Nottingham's famous October fair", "Goose Fair", ["Hull Fair", "Appleby Fair", "Scarborough Fair"]),
 ("The arcade game where coins tip over a moving shelf", "Penny falls", ["Pinball", "Fruit machine", "Claw machine"])])

race("what's this Victorian word?", "History", "medium", ["Victorians", "19th century", "words"], [
 ("The grim institution where the poor were made to live and work", "Workhouse", ["Almshouse", "Asylum", "Orphanage"]),
 ("The world's first postage stamp", "Penny Black", ["Penny Red", "Twopenny Blue", "Penny Farthing"]),
 ("The bicycle with a huge front wheel", "Penny-farthing", ["Boneshaker", "Hobby horse", "Tandem"]),
 ("The 1851 show in a giant glasshouse in Hyde Park", "Great Exhibition", ["Festival of Britain", "Ideal Home Show", "Expo"]),
 ("The Queen's husband, who died in 1861", "Prince Albert", ["Prince Edward", "Prince Leopold", "Lord Melbourne"]),
 ("The job that sent small boys up the flues", "Chimney sweep", ["Lamplighter", "Costermonger", "Muffin man"]),
 ("A child who scavenged the Thames mud at low tide", "Mudlark", ["Lamplighter", "Costermonger", "Muffin man"]),
 ("Woke workers by tapping their windows with a long pole", "Knocker-upper", ["Lamplighter", "Costermonger", "Muffin man"]),
 ("The never-caught killer of Whitechapel, 1888", "Jack the Ripper", ["Sweeney Todd", "Dick Turpin", "Burke and Hare"]),
 ("The engineer of the Great Western Railway and the Clifton bridge", "Isambard Kingdom Brunel", ["Thomas Telford", "George Stephenson", "Robert Stephenson"]),
 ("The engineer who built London's sewers", "Joseph Bazalgette", ["Thomas Telford", "John Snow", "Robert Stephenson"]),
 ("The summer of 1858 when the Thames smelt so bad Parliament nearly fled", "Great Stink", ["Great Smog", "Great Fire", "Great Plague"]),
 ("'The Lady with the Lamp' in the Crimean War", "Florence Nightingale", ["Mary Seacole", "Edith Cavell", "Elizabeth Fry"]),
 ("A hooped petticoat for a wide skirt", "Crinoline", ["Bustle", "Corset", "Bloomers"]),
 ("The author who'd worked in a blacking factory as a boy", "Charles Dickens", ["Thomas Hardy", "Wilkie Collins", "Anthony Trollope"]),
 ("'The ___ on which the sun never sets'", "Empire", ["Kingdom", "Commonwealth", "Republic"]),
 ("A cheap, gory serial story", "Penny dreadful", ["Penny whistle", "Penny arcade", "Penny loafer"]),
 ("The street light lit each evening by a lamplighter", "Gas lamp", ["Torch", "Neon sign", "Chandelier"]),
 ("Celebrated Victoria's 60 years on the throne in 1897", "Diamond Jubilee", ["Golden Jubilee", "Silver Jubilee", "Ruby Jubilee"]),
 ("A free school for the poorest children", "Ragged school", ["Grammar school", "Public school", "Boarding school"])])

race("what's this pottery word?", "Art", "medium", ["pottery", "ceramics", "crafts"], [
 ("The oven that fires the clay", "Kiln", ["Forge", "Smelter", "Range"]),
 ("The spinning disc for shaping clay", "Potter's wheel", ["Spinning wheel", "Catherine wheel", "Waterwheel"]),
 ("The glassy coating added before the second firing", "Glaze", ["Varnish", "Lacquer", "Wax"]),
 ("Shaping clay on the wheel", "Throwing", ["Bowling", "Pitching", "Tossing"]),
 ("Porous, low-fired pottery, like a flowerpot", "Earthenware", ["Pewter", "Glassware", "Silverware"]),
 ("Dense, hard pottery fired at a high heat", "Stoneware", ["Pewter", "Glassware", "Tinware"]),
 ("Fine, white, see-through ware, also called china", "Porcelain", ["Pewter", "Glassware", "Tinware"]),
 ("Pottery fired once, before any glaze", "Biscuit", ["Wafer", "Cracker", "Rusk"]),
 ("Liquid clay used to stick pieces together", "Slip", ["Slurp", "Sludge", "Slick"]),
 ("Reddish-brown fired clay: 'baked earth' in Italian", "Terracotta", ["Majolica", "Faience", "Raku"]),
 ("Blue-and-white pottery from the Netherlands", "Delft", ["Majolica", "Faience", "Raku"]),
 ("The firm famous for pale-blue jasperware", "Wedgwood", ["Royal Doulton", "Spode", "Moorcroft"]),
 ("'The Potteries' city in Staffordshire", "Stoke-on-Trent", ["Stockport", "Stafford", "Stourbridge"]),
 ("Designer of the bright Art Deco 'Bizarre' ware", "Clarice Cliff", ["Susie Cooper", "Lucie Rie", "Grayson Perry"]),
 ("The blue design with a bridge, two birds and a willow tree", "Willow pattern", ["Chintz", "Paisley", "Toile"]),
 ("A pot built from rolled-up sausages of clay", "Coil pot", ["Pinch pot", "Slab pot", "Chimney pot"]),
 ("The Japanese art of mending cracks with gold", "Kintsugi", ["Origami", "Ikebana", "Bonsai"]),
 ("The TV contest where judge Keith Brymer Jones cries", "The Great Pottery Throw Down", ["The Great British Sewing Bee", "The Repair Shop", "Grand Designs"]),
 ("The general word for objects made of fired clay", "Ceramics", ["Textiles", "Metallurgy", "Lacquerware"]),
 ("Baking the pottery in the kiln", "Firing", ["Smelting", "Tempering", "Roasting"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-164.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
