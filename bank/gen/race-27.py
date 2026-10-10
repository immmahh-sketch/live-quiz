# Bank session 10 Oct 2026: 4 more general races -> bank/race-27.json. 20 rows each, target 10; wrong options are
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

race("which river or water does this bridge cross?", "Famous landmarks", "hard", ["bridges", "rivers"], [
 ("Tower Bridge", "The Thames", ["The Lea", "The Medway", "The Mersey"]), ("The Tyne Bridge", "The Tyne", ["The Tweed", "The Derwent", "The Blyth"]),
 ("The Charles Bridge, Prague", "The Vltava", ["The Elbe", "The Oder", "The Morava"]), ("The Ponte Vecchio, Florence", "The Arno", ["The Tiber", "The Po", "The Adige"]),
 ("The Pont Neuf, Paris", "The Seine", ["The Loire", "The Marne", "The Garonne"]), ("Brooklyn Bridge", "The East River", ["The Hudson", "The Potomac", "The Delaware"]),
 ("The Chain Bridge, Budapest", "The Danube", ["The Tisza", "The Drava", "The Sava"]), ("The Clifton Suspension Bridge", "The Avon", ["The Frome", "The Usk", "The Exe"]),
 ("The Severn Bridge", "The Severn", ["The Wye", "The Usk", "The Dee"]), ("The Humber Bridge", "The Humber", ["The Ouse", "The Trent", "The Aire"]),
 ("Telford's Menai Bridge", "The Menai Strait", ["The Conwy", "The Dee", "The Clwyd"]), ("The Rialto Bridge, Venice", "The Grand Canal", ["The Giudecca Canal", "The Brenta", "The Piave"]),
 ("Stari Most, Mostar", "The Neretva", ["The Drina", "The Sava", "The Bosna"]), ("The Wearmouth Bridge", "The Wear", ["The Tweed", "The Derwent", "The Blyth"]),
 ("Middlesbrough's Transporter Bridge", "The Tees", ["The Swale", "The Ure", "The Esk"]), ("The Pont d'Avignon", "The Rhône", ["The Loire", "The Garonne", "The Saône"]),
 ("Heidelberg's Old Bridge", "The Neckar", ["The Main", "The Moselle", "The Weser"]), ("Cologne's Hohenzollern Bridge", "The Rhine", ["The Moselle", "The Main", "The Weser"]),
 ("The Kapellbrücke, Lucerne", "The Reuss", ["The Aare", "The Limmat", "The Inn"]), ("The Galata Bridge, Istanbul", "The Golden Horn", ["The Bosphorus", "The Dardanelles", "The Sea of Marmara"])])

race("what is this on a Spanish menu?", "Food and drink", "medium", ["Spanish food", "tapas"], [
 ("Gazpacho", "Cold tomato soup", ["Hot fish stew", "Chicken broth", "Lentil soup"]), ("Churros", "Fried dough sticks", ["Cheese twists", "Pancakes", "Waffles"]),
 ("Tortilla española", "Potato omelette", ["Corn wrap", "Pancake", "Pizza"]), ("Chorizo", "Spicy sausage", ["Ham", "Pork chop", "Meatloaf"]),
 ("Jamón", "Cured ham", ["Bacon", "Beef", "Sausage"]), ("Patatas bravas", "Spicy fried potatoes", ["Chips with cheese", "Mashed potato", "Potato salad"]),
 ("Calamares", "Fried squid rings", ["Battered cod", "Fried prawns", "Onion rings"]), ("Albóndigas", "Meatballs", ["Dumplings", "Fishcakes", "Burgers"]),
 ("Pulpo", "Octopus", ["Squid", "Lobster", "Crab"]), ("Gambas", "Prawns", ["Crab", "Mussels", "Lobster"]),
 ("Pimientos de Padrón", "Little green peppers", ["Stuffed olives", "Pickled onions", "Jalapeños"]), ("Boquerones", "Anchovies", ["Sardines", "Mackerel", "Whitebait"]),
 ("Crema catalana", "Custard with a burnt-sugar top", ["Rice pudding", "Trifle", "Sponge cake"]), ("Turrón", "Nougat", ["Marzipan", "Fudge", "Toffee"]),
 ("Sangría", "Red wine punch", ["White wine spritzer", "Sherry", "Cider"]), ("Fabada", "Bean and pork stew", ["Chickpea soup", "Fish stew", "Vegetable soup"]),
 ("Pan con tomate", "Bread rubbed with tomato", ["Garlic bread", "Cheese on toast", "Tomato soup"]), ("Paella", "Saffron rice dish", ["Risotto", "Fried rice", "Rice pudding"]),
 ("Flan", "Crème caramel", ["Cheesecake", "Bread pudding", "Jelly"]), ("Morcilla", "Black pudding", ["White pudding", "Haggis", "Liver sausage"])])

race("what is this mythical creature?", "Myths and legends", "medium", ["mythical creatures", "legends"], [
 ("A griffin", "Eagle and lion", ["Horse and eagle", "Lion and scorpion", "Winged lion"]), ("A centaur", "Man and horse", ["Man and lion", "Man and stag", "Man and wolf"]),
 ("The Minotaur", "Man and bull", ["Man and lion", "Man and stag", "Man and wolf"]), ("A mermaid", "Woman and fish", ["Woman and snake", "Bull and fish", "Woman and swan"]),
 ("A harpy", "Woman and bird", ["Woman and snake", "Woman and swan", "Lion and scorpion"]), ("The Sphinx", "Lion with a human head", ["Winged lion", "Lion and scorpion", "Dog-headed man"]),
 ("Pegasus", "Winged horse", ["Horned rabbit", "Winged lion", "Horse and eagle"]), ("The Chimera", "Lion, goat and serpent", ["Lion and scorpion", "Winged serpent", "Horse and eagle"]),
 ("A satyr", "Man and goat", ["Man and stag", "Man and wolf", "Man and lion"]), ("The Kraken", "Giant squid", ["Giant whale", "Sea serpent", "Giant crab"]),
 ("The Hydra", "Many-headed serpent", ["Winged serpent", "Two-headed dog", "Sea serpent"]), ("A Cyclops", "One-eyed giant", ["Many-armed giant", "Dog-headed man", "Giant wolf"]),
 ("A unicorn", "Horse with a single horn", ["Horned rabbit", "Horse and eagle", "Winged lion"]), ("A kelpie", "Shape-shifting water horse", ["Giant whale", "Water-dwelling goblin", "Sea serpent"]),
 ("A banshee", "Wailing spirit", ["Headless horseman", "Water-dwelling goblin", "Shape-shifting fox"]), ("A selkie", "Seal that becomes human", ["Shape-shifting fox", "Woman and swan", "Water-dwelling goblin"]),
 ("The phoenix", "Bird reborn from its ashes", ["Winged serpent", "Fire-breathing lizard", "Woman and swan"]), ("A basilisk", "Serpent whose gaze kills", ["Fire-breathing lizard", "Sea serpent", "Winged serpent"]),
 ("Cerberus", "Three-headed dog", ["Two-headed dog", "Giant wolf", "Dog-headed man"]), ("The yeti", "Snowy ape-man", ["Giant wolf", "Many-armed giant", "Headless horseman"])])

race("which country does this pudding or sweet come from?", "Food and drink", "hard", ["puddings", "sweets", "countries"], [
 ("Tiramisu", "Italy", ["Malta", "Croatia", "Spain"]), ("Crème brûlée", "France", ["Monaco", "Switzerland", "Luxembourg"]),
 ("Black Forest gâteau", "Germany", ["Switzerland", "Luxembourg", "Denmark"]), ("Sachertorte", "Austria", ["Switzerland", "Czechia", "Slovakia"]),
 ("Pastel de nata", "Portugal", ["Spain", "Mexico", "Argentina"]), ("Mochi", "Japan", ["China", "South Korea", "Taiwan"]),
 ("Mango sticky rice", "Thailand", ["Vietnam", "Malaysia", "Cambodia"]), ("Brigadeiro", "Brazil", ["Argentina", "Mexico", "Colombia"]),
 ("The lamington", "Australia", ["New Zealand", "Fiji", "Singapore"]), ("Kladdkaka", "Sweden", ["Norway", "Denmark", "Finland"]),
 ("Dobos torte", "Hungary", ["Slovakia", "Romania", "Czechia"]), ("Stroopwafel", "the Netherlands", ["Denmark", "Luxembourg", "Norway"]),
 ("The Liège waffle", "Belgium", ["Luxembourg", "Switzerland", "Denmark"]), ("Bara brith", "Wales", ["Northern Ireland", "the Isle of Man", "Iceland"]),
 ("Cranachan", "Scotland", ["Northern Ireland", "the Isle of Man", "Iceland"]), ("Spotted dick", "England", ["Northern Ireland", "the Isle of Man", "Iceland"]),
 ("Barmbrack", "Ireland", ["the Isle of Man", "Iceland", "Denmark"]), ("Malva pudding", "South Africa", ["Namibia", "Zimbabwe", "Kenya"]),
 ("The Nanaimo bar", "Canada", ["Iceland", "Denmark", "New Zealand"]), ("Key lime pie", "the USA", ["Cuba", "Jamaica", "Mexico"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-27.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
