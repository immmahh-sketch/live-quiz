# Bank session 10 Oct 2026: 4 more general races -> bank/race-38.json. 20 rows each, target 10; wrong options are
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

race("what's the Portuguese word?", "Words and language", "medium", ["Portuguese", "languages"], [
 ("Thank you", "Obrigado", ["Gracias", "Grazie", "Merci"]), ("Hello", "Olá", ["Hola", "Ciao", "Salut"]),
 ("Please", "Por favor", ["Per favore", "S'il vous plaît", "Bitte"]), ("Good morning", "Bom dia", ["Buenos días", "Buongiorno", "Bonjour"]),
 ("Water", "Água", ["Acqua", "Eau", "Wasser"]), ("Beer", "Cerveja", ["Cerveza", "Birra", "Bière"]),
 ("Bread", "Pão", ["Pan", "Pane", "Pain"]), ("Cheese", "Queijo", ["Queso", "Formaggio", "Fromage"]),
 ("Wine", "Vinho", ["Vino", "Vin", "Wein"]), ("Beach", "Praia", ["Playa", "Spiaggia", "Plage"]),
 ("Street", "Rua", ["Calle", "Strada", "Rue"]), ("Church", "Igreja", ["Iglesia", "Chiesa", "Église"]),
 ("Dog", "Cão", ["Perro", "Cane", "Chien"]), ("Night", "Noite", ["Noche", "Notte", "Nuit"]),
 ("Yes", "Sim", ["Sí", "Oui", "Ja"]), ("No", "Não", ["Nein", "Non", "Nee"]),
 ("Today", "Hoje", ["Hoy", "Oggi", "Aujourd'hui"]), ("Tomorrow", "Amanhã", ["Mañana", "Domani", "Demain"]),
 ("Small", "Pequeno", ["Piccolo", "Petit", "Klein"]), ("Goodbye", "Adeus", ["Adiós", "Arrivederci", "Au revoir"])])

race("what's the main town of this island?", "World geography", "hard", ["islands", "capitals", "towns"], [
 ("Greenland", "Nuuk", ["Ilulissat", "Sisimiut", "Tasiilaq"]), ("The Faroe Islands", "Tórshavn", ["Klaksvík", "Runavík", "Tvøroyri"]),
 ("The Isle of Man", "Douglas", ["Ramsey", "Peel", "Castletown"]), ("Jersey", "St Helier", ["Gorey", "St Aubin", "St Brelade"]),
 ("Guernsey", "St Peter Port", ["St Sampson", "St Anne", "St Martin"]), ("Bermuda", "Hamilton", ["St George's", "Somerset", "Nassau"]),
 ("Puerto Rico", "San Juan", ["Ponce", "Mayagüez", "Santo Domingo"]), ("Tahiti", "Papeete", ["Nouméa", "Apia", "Suva"]),
 ("Hawaii (the state)", "Honolulu", ["Hilo", "Lahaina", "Kailua-Kona"]), ("Sicily", "Palermo", ["Catania", "Messina", "Syracuse"]),
 ("Sardinia", "Cagliari", ["Sassari", "Olbia", "Alghero"]), ("Corsica", "Ajaccio", ["Bastia", "Calvi", "Bonifacio"]),
 ("Crete", "Heraklion", ["Chania", "Rethymno", "Agios Nikolaos"]), ("Mallorca", "Palma", ["Alcúdia", "Sóller", "Ibiza Town"]),
 ("Madeira", "Funchal", ["Machico", "Câmara de Lobos", "Santana"]), ("The Isle of Wight", "Newport", ["Ryde", "Cowes", "Ventnor"]),
 ("Orkney", "Kirkwall", ["Stromness", "Thurso", "Wick"]), ("Shetland", "Lerwick", ["Scalloway", "Brae", "Thurso"]),
 ("The Isle of Lewis", "Stornoway", ["Tarbert", "Tobermory", "Portree"]), ("Tasmania", "Hobart", ["Launceston", "Devonport", "Burnie"])])

race("which country does this bread come from?", "Food and drink", "hard", ["bread", "countries"], [
 ("Baguette", "France", ["Belgium", "Switzerland", "Luxembourg"]), ("Ciabatta", "Italy", ["Spain", "Greece", "Malta"]),
 ("Pretzel", "Germany", ["the Netherlands", "Belgium", "Poland"]), ("Soda bread", "Ireland", ["Wales", "Iceland", "the Netherlands"]),
 ("Tortilla (the flatbread)", "Mexico", ["Peru", "Colombia", "Chile"]), ("Injera", "Ethiopia", ["Kenya", "Nigeria", "Ghana"]),
 ("Pão de queijo", "Brazil", ["Peru", "Colombia", "Chile"]), ("Bao", "China", ["Vietnam", "Thailand", "the Philippines"]),
 ("Roti canai", "Malaysia", ["Thailand", "Vietnam", "the Philippines"]), ("Stottie cake", "England", ["Wales", "Belgium", "the Netherlands"]),
 ("Knäckebröd crispbread", "Sweden", ["Iceland", "the Netherlands", "Poland"]), ("Lefse", "Norway", ["Iceland", "Poland", "the Netherlands"]),
 ("Simit", "Turkey", ["Greece", "Lebanon", "Egypt"]), ("Khachapuri", "Georgia", ["Armenia", "Azerbaijan", "Ukraine"]),
 ("Bannock", "Scotland", ["Wales", "Iceland", "Belgium"]), ("Damper", "Australia", ["South Africa", "Namibia", "Kenya"]),
 ("Melonpan", "Japan", ["Taiwan", "Vietnam", "the Philippines"]), ("Cornbread", "the USA", ["Canada", "Chile", "Kenya"]),
 ("Rugbrød", "Denmark", ["Belgium", "Iceland", "Poland"]), ("Bolo do caco", "Portugal", ["Spain", "Greece", "Chile"])])

race("what does this Yorkshire word mean?", "Words and language", "medium", ["Yorkshire", "dialect"], [
 ("Nowt", "Nothing", ["Never", "Nobody", "Nowhere"]), ("Owt", "Anything", ["Anyone", "Anywhere", "Outside"]),
 ("Summat", "Something", ["Someone", "Somewhere", "Summer"]), ("Ginnel", "Alleyway", ["Garden", "Gutter", "Cellar"]),
 ("Mardy", "Sulky", ["Tired", "Hungry", "Cheerful"]), ("Laik", "Play", ["Sleep", "Steal", "Shout"]),
 ("Spice", "Sweets", ["Curry", "Gravy", "Cake"]), ("Nesh", "Feels the cold easily", ["Greedy", "Nosy", "Lazy"]),
 ("Lug", "Ear", ["Nose", "Elbow", "Knee"]), ("Gip", "Retch", ["Sneeze", "Cough", "Hiccup"]),
 ("Mither", "Pester", ["Gossip", "Steal", "Sulk"]), ("Ey up", "Hello", ["Goodbye", "Thank you", "Good night"]),
 ("Gormless", "Clueless", ["Clever", "Cheerful", "Rich"]), ("Allus", "Always", ["Never", "Sometimes", "Already"]),
 ("Sup", "Drink", ["Eat", "Sleep", "Shout"]), ("Happen", "Perhaps", ["Never", "Already", "Quickly"]),
 ("Clarty", "Muddy", ["Tidy", "Windy", "Sunny"]), ("Mash (the tea)", "Brew tea", ["Wash up", "Sweep", "Iron clothes"]),
 ("Snap", "Packed lunch", ["Breakfast", "Supper", "Pudding"]), ("Breadcake", "Bread roll", ["Scone", "Crumpet", "Pancake"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-38.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
