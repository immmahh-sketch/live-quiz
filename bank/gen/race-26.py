# Bank session 10 Oct 2026: 4 more general races -> bank/race-26.json. 20 rows each, target 10; wrong options are
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

race("what is this on an Indian menu?", "Food and drink", "medium", ["Indian food", "words"], [
 ("Aloo", "Potato", ["Onion", "Carrot", "Cabbage"]), ("Gobi", "Cauliflower", ["Cabbage", "Broccoli", "Carrot"]), ("Saag", "Spinach", ["Lettuce", "Cabbage", "Kale"]),
 ("Paneer", "Cheese", ["Butter", "Cream", "Tofu"]), ("Murgh", "Chicken", ["Duck", "Beef", "Pork"]), ("Gosht", "Meat (lamb or mutton)", ["Duck", "Pork", "Rabbit"]),
 ("Dal", "Lentils", ["Rice", "Beans", "Barley"]), ("Chana", "Chickpeas", ["Beans", "Corn", "Peanuts"]), ("Bhindi", "Okra", ["Courgette", "Green beans", "Celery"]),
 ("Baingan", "Aubergine", ["Courgette", "Pepper", "Pumpkin"]), ("Matar", "Peas", ["Beans", "Corn", "Broad beans"]), ("Jhinga", "Prawns", ["Crab", "Lobster", "Squid"]),
 ("Machli", "Fish", ["Squid", "Crab", "Duck"]), ("Keema", "Minced meat", ["Sausage", "Bacon", "Liver"]), ("Raita", "Yoghurt dip", ["Pickle", "Chutney", "Gravy"]),
 ("Lassi", "Yoghurt drink", ["Tea", "Lemonade", "Coconut water"]), ("Tikka", "Chunks", ["Sauce", "Stew", "Soup"]), ("Tandoor", "Clay oven", ["Frying pan", "Steamer", "Wok"]),
 ("Pani", "Water", ["Bread", "Milk", "Tea"]), ("Mirch", "Chilli", ["Garlic", "Ginger", "Lime"])])

race("which country is this natural wonder in?", "World geography", "medium", ["natural wonders", "countries"], [
 ("The Great Barrier Reef", "Australia", ["Papua New Guinea", "Fiji", "Indonesia"]), ("The Grand Canyon", "the USA", ["Mexico", "Peru", "Argentina"]),
 ("Ha Long Bay", "Vietnam", ["Thailand", "Cambodia", "Malaysia"]), ("The Giant's Causeway", "Northern Ireland", ["Wales", "the Isle of Man", "the Faroe Islands"]),
 ("Salar de Uyuni, the salt flats", "Bolivia", ["Peru", "Argentina", "Paraguay"]), ("Pamukkale's white terraces", "Turkey", ["Greece", "Cyprus", "Georgia"]),
 ("The Geirangerfjord", "Norway", ["Sweden", "Finland", "Denmark"]), ("Zhangjiajie's stone pillars", "China", ["Taiwan", "Mongolia", "South Korea"]),
 ("Milford Sound", "New Zealand", ["Fiji", "Samoa", "Tonga"]), ("The Bay of Fundy", "Canada", ["Greenland", "Denmark", "Portugal"]),
 ("The Cliffs of Moher", "Ireland", ["Wales", "the Isle of Man", "the Faroe Islands"]), ("Fingal's Cave", "Scotland", ["Wales", "the Isle of Man", "the Faroe Islands"]),
 ("Cheddar Gorge", "England", ["Wales", "the Isle of Man", "Belgium"]), ("The red dunes of Sossusvlei", "Namibia", ["Botswana", "Angola", "Zimbabwe"]),
 ("The Chocolate Hills", "the Philippines", ["Indonesia", "Malaysia", "Thailand"]), ("The Jeita Grotto", "Lebanon", ["Syria", "Israel", "Cyprus"]),
 ("The Blue Lagoon", "Iceland", ["Greenland", "the Faroe Islands", "Denmark"]), ("Wadi Rum", "Jordan", ["Saudi Arabia", "Egypt", "Israel"]),
 ("Socotra's dragon's blood trees", "Yemen", ["Oman", "Somalia", "Eritrea"]), ("Torres del Paine", "Chile", ["Argentina", "Peru", "Uruguay"])])

race("what does this British slang mean?", "Words and language", "easy", ["slang", "British English"], [
 ("Gobsmacked", "Amazed", ["Punched", "Hungry", "Drunk"]), ("Knackered", "Exhausted", ["Angry", "Hungry", "Drunk"]), ("Chuffed", "Pleased", ["Out of breath", "Embarrassed", "Bored"]),
 ("Skint", "Broke", ["Thin", "Sunburnt", "Drunk"]), ("Gutted", "Very disappointed", ["Hungry", "Relieved", "Angry"]), ("Minging", "Disgusting", ["Moaning", "Lucky", "Excellent"]),
 ("A faff", "A fuss about nothing", ["A bit of gossip", "A white lie", "A quick nap"]), ("A bodge", "A botched repair", ["A bribe", "A clumsy dance", "A shortcut"]),
 ("A kerfuffle", "A commotion", ["A hairstyle", "A hiccup", "A sponge cake"]), ("A chinwag", "A chat", ["A beard", "A joke", "An argument"]),
 ("Naff", "Uncool", ["Rude", "Hungry", "Lucky"]), ("Throw a wobbly", "Have a tantrum", ["Fall over", "Get drunk", "Dance badly"]),
 ("Gone pear-shaped", "Gone wrong", ["Got fat", "Gone mouldy", "Gone well"]), ("Dodgy", "Suspicious", ["Lucky", "Quick", "Hidden"]),
 ("The lurgy", "An illness", ["A hangover", "A bad mood", "A parking fine"]), ("A cuppa", "A cup of tea", ["A biscuit", "A pint", "A sandwich"]),
 ("Full of beans", "Lively", ["Full up", "Lying", "Grumpy"]), ("Hunky-dory", "Fine", ["Handsome", "Dull", "Lucky"]),
 ("A bevvy", "A drink", ["A crowd", "A bet", "A bath"]), ("Chock-a-block", "Packed full", ["Locked out", "Upside down", "Empty"])])

race("which country does this drink come from?", "Food and drink", "hard", ["spirits", "liqueurs", "countries"], [
 ("Cointreau", "France", ["Belgium", "Switzerland", "Luxembourg"]), ("Baileys", "Ireland", ["Wales", "Northern Ireland", "Iceland"]),
 ("Amaretto", "Italy", ["Malta", "Croatia", "Portugal"]), ("Jägermeister", "Germany", ["Switzerland", "Denmark", "Luxembourg"]),
 ("Ouzo", "Greece", ["Cyprus", "Bulgaria", "Malta"]), ("Tequila", "Mexico", ["Cuba", "Colombia", "Peru"]),
 ("Sake", "Japan", ["China", "Taiwan", "Vietnam"]), ("Soju", "South Korea", ["China", "Taiwan", "Vietnam"]),
 ("Becherovka", "Czechia", ["Slovakia", "Slovenia", "Croatia"]), ("Unicum", "Hungary", ["Slovakia", "Romania", "Croatia"]),
 ("Rakı", "Turkey", ["Cyprus", "Lebanon", "Bulgaria"]), ("Cachaça", "Brazil", ["Portugal", "Argentina", "Colombia"]),
 ("Malibu", "Barbados", ["Jamaica", "Cuba", "Trinidad and Tobago"]), ("Drambuie", "Scotland", ["Iceland", "Wales", "Northern Ireland"]),
 ("Pimm's", "England", ["Wales", "Northern Ireland", "the Isle of Man"]), ("Southern Comfort", "the USA", ["Canada", "Cuba", "Jamaica"]),
 ("Advocaat", "the Netherlands", ["Belgium", "Denmark", "Luxembourg"]), ("Krupnik", "Poland", ["Slovakia", "Ukraine", "Belarus"]),
 ("Licor 43", "Spain", ["Portugal", "Andorra", "Argentina"]), ("Stroh rum", "Austria", ["Switzerland", "Liechtenstein", "Slovenia"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-26.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
