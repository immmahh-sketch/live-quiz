# Bank session 9 Oct 2026 (third pass): 4 more general races -> bank/race-4.json. 20 rows each, target 10; wrong
# options are the same kind of thing, never another row's right answer, and never also right for that row.
import json, os
R = []
def race(title, cat, diff, tags, rows):
    rights = {r[1] for r in rows}
    assert len(rows) == 20, (title, len(rows))
    assert len(rights) == 20, (title, 'duplicate right answers')
    for q, right, wrong in rows:
        assert len(wrong) == 3 and len(set(wrong)) == 3, (title, q)
        bad = [w for w in wrong if w in rights]
        assert not bad, (title, q, 'recycled', bad)
    R.append({"type": "race", "text": "The Race: " + title, "target": 10, "category": cat, "tags": tags, "difficulty": diff,
              "bank": [{"q": q, "right": right, "wrong": wrong} for q, right, wrong in rows]})

race("which English county is this town in?", "UK geography", "medium", ["counties", "towns"], [
 ("Blackpool", "Lancashire", ["Merseyside", "Greater Manchester", "West Yorkshire"]), ("Whitby", "North Yorkshire", ["East Riding of Yorkshire", "Tyne and Wear", "West Yorkshire"]),
 ("Bournemouth", "Dorset", ["Hampshire", "Isle of Wight", "West Sussex"]), ("Torquay", "Devon", ["Hampshire", "Bristol", "Isle of Wight"]),
 ("Newquay", "Cornwall", ["Hampshire", "Bristol", "Isle of Wight"]), ("Skegness", "Lincolnshire", ["Nottinghamshire", "East Riding of Yorkshire", "Rutland"]),
 ("Margate", "Kent", ["East Sussex", "Surrey", "West Sussex"]), ("Hexham", "Northumberland", ["Tyne and Wear", "South Yorkshire", "East Riding of Yorkshire"]),
 ("Darlington", "County Durham", ["Tyne and Wear", "East Riding of Yorkshire", "South Yorkshire"]), ("Stratford-upon-Avon", "Warwickshire", ["Worcestershire", "Oxfordshire", "Staffordshire"]),
 ("Windsor", "Berkshire", ["Surrey", "Buckinghamshire", "Middlesex"]), ("Cheltenham", "Gloucestershire", ["Worcestershire", "Herefordshire", "Oxfordshire"]),
 ("Bath", "Somerset", ["Bristol", "Herefordshire", "Oxfordshire"]), ("Salisbury", "Wiltshire", ["Hampshire", "Surrey", "Oxfordshire"]),
 ("Ipswich", "Suffolk", ["Cambridgeshire", "Hertfordshire", "Bedfordshire"]), ("Norwich", "Norfolk", ["Cambridgeshire", "Bedfordshire", "Hertfordshire"]),
 ("Kendal", "Cumbria", ["Merseyside", "Tyne and Wear", "Derbyshire"]), ("Chester", "Cheshire", ["Merseyside", "Staffordshire", "Derbyshire"]),
 ("Shrewsbury", "Shropshire", ["Herefordshire", "Staffordshire", "Worcestershire"]), ("Colchester", "Essex", ["Hertfordshire", "Cambridgeshire", "Bedfordshire"])])

race("what's the French word?", "Words and language", "medium", ["French", "languages"], [
 ("Cat", "Chat", ["Chapeau", "Château", "Chaise"]), ("Dog", "Chien", ["Cheval", "Chèvre", "Chou"]), ("House", "Maison", ["Mairie", "Magasin", "Matin"]),
 ("Bread", "Pain", ["Pomme de terre", "Poisson", "Poulet"]), ("Cheese", "Fromage", ["Farine", "Framboise", "Frites"]),
 ("Apple", "Pomme", ["Poire", "Prune", "Pêche"]), ("Water", "Eau", ["Vin", "Lait", "Bière"]), ("Red", "Rouge", ["Rose", "Jaune", "Bleu"]),
 ("Green", "Vert", ["Violet", "Gris", "Blanc"]), ("Friend", "Ami", ["Amour", "Âme", "Avion"]), ("Book", "Livre", ["Lit", "Lettre", "Lampe"]),
 ("Car", "Voiture", ["Vélo", "Voyage", "Ville"]), ("Sea", "Mer", ["Mère", "Montagne", "Maire"]), ("Sun", "Soleil", ["Sol", "Sel", "Ciel"]),
 ("Moon", "Lune", ["Lumière", "Lundi", "Loup"]), ("Black", "Noir", ["Nuit", "Neige", "Nez"]), ("Window", "Fenêtre", ["Feuille", "Fleur", "Forêt"]),
 ("Beach", "Plage", ["Place", "Plume", "Pluie"]), ("Butterfly", "Papillon", ["Pigeon", "Poussin", "Pingouin"]), ("Strawberry", "Fraise", ["Cerise", "Citron", "Groseille"])])

race("which country does this dish come from?", "Food and drink", "medium", ["food", "countries"], [
 ("Paella", "Spain", ["Portugal", "Italy", "Argentina"]), ("Moussaka", "Greece", ["Turkey", "Lebanon", "Italy"]), ("Goulash", "Hungary", ["Czech Republic", "Romania", "Germany"]),
 ("Sushi", "Japan", ["China", "Indonesia", "Malaysia"]), ("Kimchi", "South Korea", ["China", "Philippines", "Indonesia"]), ("Pad thai", "Thailand", ["Malaysia", "Indonesia", "China"]),
 ("Pho", "Vietnam", ["China", "Malaysia", "Philippines"]), ("Tacos", "Mexico", ["Argentina", "Cuba", "Chile"]), ("Borscht", "Ukraine", ["Russia", "Belarus", "Lithuania"]),
 ("Haggis", "Scotland", ["Ireland", "Wales", "Norway"]), ("Poutine", "Canada", ["Belgium", "USA", "Ireland"]), ("Pierogi", "Poland", ["Russia", "Czech Republic", "Germany"]),
 ("Feijoada", "Brazil", ["Portugal", "Argentina", "Cuba"]), ("Bobotie", "South Africa", ["Kenya", "Nigeria", "Egypt"]), ("Wiener schnitzel", "Austria", ["Germany", "Czech Republic", "Belgium"]),
 ("Cheese fondue", "Switzerland", ["Belgium", "Netherlands", "Germany"]), ("Ceviche", "Peru", ["Chile", "Argentina", "Cuba"]), ("Smørrebrød", "Denmark", ["Norway", "Sweden", "Netherlands"]),
 ("Tagine", "Morocco", ["Egypt", "Lebanon", "Turkey"]), ("Coq au vin", "France", ["Belgium", "Italy", "Portugal"])])

race("which city or town is this football club from?", "Football", "medium", ["football", "clubs", "places"], [
 ("Everton", "Liverpool", ["Manchester", "Chester", "Wallasey"]), ("Aston Villa", "Birmingham", ["Wolverhampton", "Coventry", "Nottingham"]),
 ("Port Vale", "Stoke-on-Trent", ["Crewe", "Derby", "Chester"]), ("Hearts", "Edinburgh", ["Aberdeen", "Dundee", "Inverness"]),
 ("Celtic", "Glasgow", ["Aberdeen", "Kilmarnock", "Ayr"]), ("Juventus", "Turin", ["Milan", "Naples", "Genoa"]), ("Ajax", "Amsterdam", ["Utrecht", "The Hague", "Antwerp"]),
 ("Benfica", "Lisbon", ["Porto", "Madrid", "Seville"]), ("Galatasaray", "Istanbul", ["Ankara", "Izmir", "Athens"]), ("Boca Juniors", "Buenos Aires", ["Montevideo", "Rosario", "Santiago"]),
 ("Feyenoord", "Rotterdam", ["Utrecht", "The Hague", "Antwerp"]), ("PSV", "Eindhoven", ["Utrecht", "Groningen", "Antwerp"]), ("Anderlecht", "Brussels", ["Antwerp", "Ghent", "Bruges"]),
 ("Zenit", "Saint Petersburg", ["Moscow", "Kyiv", "Minsk"]), ("Olympiacos", "Piraeus", ["Athens", "Thessaloniki", "Patras"]), ("Real Sociedad", "San Sebastián", ["Bilbao", "Seville", "Valencia"]),
 ("Tranmere Rovers", "Birkenhead", ["Wallasey", "Chester", "Southport"]), ("Queen of the South", "Dumfries", ["Ayr", "Stirling", "Perth"]),
 ("Arsenal", "London", ["Manchester", "Leeds", "Sheffield"]), ("Lazio", "Rome", ["Milan", "Naples", "Florence"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-4.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
