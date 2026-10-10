# Bank session 10 Oct 2026: 2 more general races -> bank/race-81.json. 20 rows each, target 10; wrong options are
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

race("which famous 'Lane'?", "General knowledge", "medium", ["lanes", "wordplay"], [
 ("The Beatles' Liverpool street of barbers and bankers", "Penny Lane", ["Strawberry Fields", "Mathew Street", "Menlove Avenue"]), ("The London street of the Theatre Royal, where the Muffin Man lived", "Drury Lane", ["Shaftesbury Avenue", "Haymarket", "Strand"]),
 ("The East London Sunday clothes market", "Petticoat Lane", ["Brick Lane", "Columbia Road", "Roman Road"]), ("Sheffield United's ground", "Bramall Lane", ["Hillsborough", "Oakwell", "Valley Parade"]),
 ("Tottenham's home until 2017", "White Hart Lane", ["Highbury", "Upton Park", "Loftus Road"]), ("Superman's reporter girlfriend", "Lois Lane", ["Lana Lang", "Jimmy Olsen", "Perry White"]),
 ("Where you take a nostalgic trip", "Memory Lane", ["Nostalgia Street", "Yesterday Road", "Old Times Avenue"]), ("London's legal quarter and Tube station by Holborn", "Chancery Lane", ["Temple", "Fleet Street", "Gray's Inn Road"]),
 ("Where the Great Fire of London started", "Pudding Lane", ["Pie Corner", "Fish Street Hill", "Monument Street"]), ("The luxury hotel and golf resort on Barbados", "Sandy Lane", ["Sandals", "Coral Reef", "Cobblers Cove"]),
 ("The star of The Birdcage and The Producers on Broadway", "Nathan Lane", ["Matthew Broderick", "Robin Williams", "Gene Hackman"]), ("The actress who plays Martha Kent in Man of Steel", "Diane Lane", ["Amy Adams", "Michelle Pfeiffer", "Meg Ryan"]),
 ("The writer of Bread and The Liver Birds", "Carla Lane", ["Victoria Wood", "Jimmy McGovern", "Lynda La Plante"]), ("The Banks family's address in Mary Poppins", "Cherry Tree Lane", ["Privet Drive", "Spinner's End", "Acacia Avenue"]),
 ("The street in Desperate Housewives", "Wisteria Lane", ["Ramsay Street", "Melrose Place", "Elm Street"]), ("The Eagles' 1976 hit, 'Life in the ...'", "Fast Lane", ["Fast Track", "Long Run", "Express Lane"]),
 ("A quiet spot where courting couples park up", "Lovers' Lane", ["Lovers' Leap", "Kissing Gate", "Cuddle Corner"]), ("The Small Faces' bassist, nicknamed 'Plonk'", "Ronnie Lane", ["Ronnie Wood", "Kenney Jones", "Steve Marriott"]),
 ("A road lane kept for buses and taxis", "Bus lane", ["Cycle lane", "Hard shoulder", "Red route"]), ("The City street that was the centre of the world tea trade", "Mincing Lane", ["Threadneedle Street", "Lombard Street", "Cheapside"])])

race("which famous 'Tree'?", "General knowledge", "medium", ["trees", "wordplay"], [
 ("U2's 1987 album", "The Joshua Tree", ["Achtung Baby", "The Unforgettable Fire", "War"]), ("A chart of your ancestors", "Family tree", ["Birth certificate", "Census", "Heirloom"]),
 ("Where the partridge sits on the first day of Christmas", "Pear tree", ["Plum tree", "Fig tree", "Holly bush"]), ("The tree at Woolsthorpe said to have dropped fruit on Isaac Newton", "Apple tree", ["Plum tree", "Oak tree", "Fig tree"]),
 ("Northumberland's famous tree on Hadrian's Wall, felled in 2023", "Sycamore Gap tree", ["Fortingall Yew", "Ankerwycke Yew", "Allerton Oak"]), ("The tree under which the Buddha found enlightenment", "Bodhi tree", ["Banyan", "Lotus", "Sal tree"]),
 ("Enid Blyton's tree with strange lands at the top", "The Magic Faraway Tree", ["Noddy", "Malory Towers", "The Wishing-Chair"]), ("The tree in Eden whose fruit Eve ate", "Tree of Knowledge", ["Tree of Life", "Fig tree", "Olive tree"]),
 ("Tolkien's ancient Ent of Fangorn Forest", "Treebeard", ["Quickbeam", "Old Man Willow", "Skinbark"]), ("The spiky Chilean conifer found in many British gardens", "Monkey puzzle tree", ["Norway spruce", "Yew", "Cedar of Lebanon"]),
 ("A wooden form that keeps shoes in shape", "Shoe tree", ["Shoe horn", "Last", "Boot jack"]), ("London's street tree with patchy, peeling bark", "London plane", ["Silver birch", "Lime", "Sycamore"]),
 ("A slang name for an eco-protester", "Tree hugger", ["Swampy", "Crusty", "Greenie"]), ("A children's den up in the branches", "Treehouse", ["Wendy house", "Bivouac", "Tree stand"]),
 ("Someone who prunes and fells trees for a living", "Tree surgeon", ["Lumberjack", "Forester", "Woodcutter"]), ("In Aussie slang, when you're in trouble you're 'up a ...'", "Gum tree", ["Creek", "Pole", "Wattle"]),
 ("Norway's yearly gift that stands in Trafalgar Square", "Christmas tree", ["Yule log", "Advent wreath", "Maypole"]), ("The Japanese art of growing miniature trees", "Bonsai", ["Ikebana", "Origami", "Kokedama"]),
 ("The Sherwood oak said to have sheltered Robin Hood", "Major Oak", ["Royal Oak", "Bowthorpe Oak", "Allerton Oak"]), ("The tree Anne Frank could see from her hiding place", "Horse chestnut", ["Lime", "Elm", "Beech"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-81.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
