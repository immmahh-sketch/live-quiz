# Bank session 10 Oct 2026: 2 more general races -> bank/race-123.json (kinds of shoe, British birds). 20 rows each, target 10; wrong options are
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


race("what kind of shoe is this?", "Fashion", "medium", ["shoes", "fashion", "clothes"], [
 ("A sturdy leather shoe decorated with rows of little punched holes", "Brogue", ["Derby", "Monk strap", "Chukka"]),
 ("A slip-on leather shoe with no laces, often with a 'penny' strap across the top", "Loafer", ["Monk strap", "Deck shoe", "Derby"]),
 ("A summer shoe with a canvas top and a sole of woven rope", "Espadrille", ["Huarache", "Jelly shoe", "Gladiator sandal"]),
 ("A soft leather slip-on first made by Native Americans", "Moccasin", ["Huarache", "Deck shoe", "Pump"]),
 ("A high heel as thin as a dagger", "Stiletto", ["Platform", "Peep-toe", "Pump"]),
 ("A waterproof rubber boot named after a duke", "Wellington", ["Galosh", "Wader", "Snow boot"]),
 ("A shoe carved from a single block of wood, loved in the Netherlands", "Clog", ["Geta", "Platform", "Huarache"]),
 ("A rubber sandal held on by a strap between the toes", "Flip-flop", ["Gladiator sandal", "Jelly shoe", "Slipper"]),
 ("A backless shoe that slides on at the front, sharing its name with a farm animal", "Mule", ["Pump", "Peep-toe", "Monk strap"]),
 ("A simple canvas gym shoe with a rubber sole, once a PE-lesson staple", "Plimsoll", ["Deck shoe", "Jelly shoe", "Huarache"]),
 ("An ankle boot with elastic panels at the sides, loved by the Beatles", "Chelsea boot", ["Chukka", "Jodhpur boot", "Pixie boot"]),
 ("A suede ankle boot with two eyelets and a crepe sole, made famous by Clarks", "Desert boot", ["Jodhpur boot", "Hiking boot", "Cowboy boot"]),
 ("A women's shoe held on by a strap around the back of the heel", "Slingback", ["Peep-toe", "T-bar", "Pump"]),
 ("A short, slim heel made famous by Audrey Hepburn", "Kitten heel", ["Platform", "Cuban heel", "Block heel"]),
 ("A heel that runs solid under the whole length of the foot", "Wedge", ["Block heel", "Cuban heel", "Spool heel"]),
 ("The classic plain office heel with no straps or laces", "Court shoe", ["Peep-toe", "T-bar", "Slipper"]),
 ("A flat, slipper-like women's shoe inspired by dancers", "Ballet flat", ["Jelly shoe", "Deck shoe", "Peep-toe"]),
 ("A shoe or boot with a very long, sharply pointed toe, loved by 1950s rockers", "Winklepicker", ["Pixie boot", "Cowboy boot", "Monk strap"]),
 ("A shoe with a thick crepe sole, worn by Teddy Boys and later by punks", "Brothel creeper", ["Platform", "Chukka", "Derby"]),
 ("A rounded, low-heeled shoe with a single strap across the top of the foot, often worn by girls", "Mary Jane", ["Peep-toe", "Slipper", "Derby"])])

race("which British bird is this?", "Animals", "medium", ["birds", "British wildlife", "nature"], [
 ("Red breast, sings all winter, and follows gardeners for worms", "Robin", ["Chaffinch", "Bullfinch", "Redstart"]),
 ("Black and white with a long tail: 'one for sorrow, two for joy'", "Magpie", ["Jackdaw", "Rook", "Lapwing"]),
 ("Electric blue and orange, it dives into rivers for fish", "Kingfisher", ["Bee-eater", "Dipper", "Roller"]),
 ("A seabird with a colourful striped beak, nicknamed the 'sea parrot'", "Puffin", ["Guillemot", "Razorbill", "Fulmar"]),
 ("A tiny brown bird with a cocked-up tail and a very loud song", "Wren", ["Dunnock", "Treecreeper", "Chiffchaff"]),
 ("A small garden bird with a blue cap and a yellow front", "Blue tit", ["Great tit", "Coal tit", "Nuthatch"]),
 ("Red face and a flash of yellow on the wings; a group is a 'charm'", "Goldfinch", ["Siskin", "Linnet", "Chaffinch"]),
 ("A glossy, speckled bird whose huge flocks swirl in a 'murmuration'", "Starling", ["Blackbird", "Fieldfare", "Redwing"]),
 ("A tall grey bird that stands stock-still at the water's edge, waiting for fish", "Grey heron", ["Crane", "Bittern", "Little egret"]),
 ("Lays its eggs in other birds' nests and is named after its call", "Cuckoo", ["Nightjar", "Corncrake", "Hoopoe"]),
 ("A pale, heart-faced owl that hunts silently over fields at dusk", "Barn owl", ["Tawny owl", "Little owl", "Long-eared owl"]),
 ("A small falcon often seen hovering over motorway verges", "Kestrel", ["Sparrowhawk", "Merlin", "Hobby"]),
 ("A fork-tailed summer visitor that nests in barns; one doesn't make a summer", "Swallow", ["Swift", "House martin", "Sand martin"]),
 ("A colourful crow with a blue wing flash that buries acorns", "Jay", ["Jackdaw", "Rook", "Chough"]),
 ("Green with a red cap; its laughing call is known as a 'yaffle'", "Green woodpecker", ["Great spotted woodpecker", "Wryneck", "Nuthatch"]),
 ("A huge white bird with an orange beak; the unmarked ones on open water belong to the monarch", "Mute swan", ["Whooper swan", "Bewick's swan", "Snow goose"]),
 ("A black and white shore bird with a long orange-red beak and a loud piping call", "Oystercatcher", ["Avocet", "Lapwing", "Curlew"]),
 ("A russet bird of prey with a forked tail, brought back to Gateshead's Derwent valley", "Red kite", ["Buzzard", "Marsh harrier", "Osprey"]),
 ("A big white seabird that plunges into the sea like a dart, famous on the Bass Rock", "Gannet", ["Fulmar", "Kittiwake", "Cormorant"]),
 ("A speckled bird that smashes snail shells on a stone 'anvil'", "Song thrush", ["Mistle thrush", "Fieldfare", "Redwing"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-123.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
