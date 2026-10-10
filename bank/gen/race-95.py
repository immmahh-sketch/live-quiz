# Bank session 10 Oct 2026: 2 more general races -> bank/race-95.json (herbs and spices, hats). 20 rows each, target 10; wrong options are
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

race("which herb or spice is this?", "Food and drink", "medium", ["herbs", "spices", "cooking"], [
 ("Dried stigmas of a crocus flower, the dearest spice in the world by weight", "Saffron", ["Sumac", "Allspice", "Fenugreek"]),
 ("Bark from a tree, sold rolled up into quills", "Cinnamon", ["Allspice", "Caraway", "Sumac"]),
 ("The seed of a fruit whose lacy red coat gives a second spice, mace", "Nutmeg", ["Allspice", "Caraway", "Fenugreek"]),
 ("Pods of a climbing orchid, scraped into custard and ice cream", "Vanilla", ["Tonka bean", "Carob", "Allspice"]),
 ("Bright yellow root powder that colours most curries", "Turmeric", ["Galangal", "Fenugreek", "Asafoetida"]),
 ("Dried unopened flower buds, pushed into a ham or an orange", "Cloves", ["Allspice", "Capers", "Caraway"]),
 ("Ground dried red peppers, smoked in Spain and the star of Hungarian goulash", "Paprika", ["Sumac", "Harissa", "Allspice"]),
 ("The main herb in Italian pesto", "Basil", ["Oregano", "Parsley", "Tarragon"]),
 ("The herb muddled into a classic mojito", "Mint", ["Lemon balm", "Parsley", "Lemongrass"]),
 ("Needle-like herb that's 'for remembrance' in Hamlet, classic with roast lamb", "Rosemary", ["Thyme", "Tarragon", "Marjoram"]),
 ("Soft grey-green leaves, mixed with onion in Christmas stuffing", "Sage", ["Thyme", "Parsley", "Marjoram"]),
 ("Called cilantro in America; some people say it tastes of soap", "Coriander", ["Parsley", "Chervil", "Fennel"]),
 ("Knobbly root grated into stir-fries and brewed into a fizzy beer", "Ginger", ["Galangal", "Lemongrass", "Wasabi"]),
 ("The world's most traded spice: berries picked green, then dried until black", "Black pepper", ["Allspice", "Cayenne", "Mustard seed"]),
 ("Eight-pointed brown pod tasting of liquorice, a key part of Chinese five-spice", "Star anise", ["Fennel", "Caraway", "Liquorice root"]),
 ("Green pods crushed into Indian chai and Scandinavian buns", "Cardamom", ["Fenugreek", "Allspice", "Caraway"]),
 ("Earthy seed that's the backbone of chilli con carne and most curry powders", "Cumin", ["Caraway", "Fennel", "Fenugreek"]),
 ("Blue-black berries from a conifer that give gin its flavour", "Juniper", ["Sloe", "Elderberry", "Allspice"]),
 ("Feathery herb cured with salmon in Scandinavian gravlax", "Dill", ["Fennel", "Chervil", "Tarragon"]),
 ("Fiery root grated into the sauce served with roast beef", "Horseradish", ["Wasabi", "Mustard", "Radish"])])

race("what kind of hat is this?", "Fashion", "medium", ["hats", "clothes"], [
 ("Hard round felt hat of old City gents, worn by Laurel and Hardy", "Bowler", ["Trilby", "Homburg", "Busby"]),
 ("Tall flat-topped silk hat of Abraham Lincoln and the Mad Hatter", "Top hat", ["Homburg", "Bicorne", "Tricorn"]),
 ("Tweed cap peaked front and back, forever linked with Sherlock Holmes", "Deerstalker", ["Newsboy cap", "Trapper hat", "Glengarry"]),
 ("Red felt with a black tassel, Tommy Cooper's trademark", "Fez", ["Kufi", "Skullcap", "Turban"]),
 ("Very wide-brimmed hat from Mexico", "Sombrero", ["Akubra", "Sun hat", "Conical hat"]),
 ("The classic cowboy hat, named after its Philadelphia maker", "Stetson", ["Akubra", "Homburg", "Boonie hat"]),
 ("Woven straw hat named after one country but made in Ecuador", "Panama", ["Trilby", "Sun hat", "Bucket hat"]),
 ("Stiff flat-topped straw hat of Henley Regatta and barbershop quartets", "Boater", ["Trilby", "Sun hat", "Bucket hat"]),
 ("Soft round flat cap, linked with French onion sellers and the Paras", "Beret", ["Kepi", "Beanie", "Toque"]),
 ("Tall black fur hat of the guards outside Buckingham Palace", "Bearskin", ["Busby", "Shako", "Kepi"]),
 ("Square flat cap with a tassel, thrown in the air at graduation", "Mortarboard", ["Biretta", "Zucchetto", "Kepi"]),
 ("Rounded cloth cap with a small stiff peak, Andy Capp's trademark", "Flat cap", ["Newsboy cap", "Beanie", "Baseball cap"]),
 ("Soft felt hat pinched at the front, worn by Indiana Jones", "Fedora", ["Trilby", "Homburg", "Akubra"]),
 ("Scottish woollen bonnet with a pompom, named after a Burns poem", "Tam o'shanter", ["Glengarry", "Balmoral", "Bobble hat"]),
 ("Tall pointed hat worn by a bishop", "Mitre", ["Biretta", "Zucchetto", "Skullcap"]),
 ("Oilskin rain hat with a long brim at the back, worn by fishermen", "Sou'wester", ["Bucket hat", "Trapper hat", "Boonie hat"]),
 ("Small flat-topped hat worn by Walter White as Heisenberg", "Pork pie hat", ["Trilby", "Homburg", "Bucket hat"]),
 ("Close-fitting bell-shaped hat of 1920s flappers", "Cloche", ["Fascinator", "Bonnet", "Turban"]),
 ("Small round brimless hat made famous by Jackie Kennedy", "Pillbox hat", ["Fascinator", "Bonnet", "Beanie"]),
 ("Russian fur hat with ear flaps that tie up on top", "Ushanka", ["Busby", "Papakha", "Beanie"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-95.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
