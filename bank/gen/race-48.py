# Bank session 10 Oct 2026: 4 more general races -> bank/race-48.json. 20 rows each, target 10; wrong options are
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

race("which grape is this wine mainly made from?", "Food and drink", "hard", ["wine", "grapes"], [
 ("Chablis", "Chardonnay", ["Aligoté", "Viognier", "Pinot Grigio"]), ("Sancerre", "Sauvignon Blanc", ["Viognier", "Muscat", "Aligoté"]),
 ("Barolo", "Nebbiolo", ["Barbera", "Dolcetto", "Aglianico"]), ("Rioja", "Tempranillo", ["Touriga Nacional", "Mourvèdre", "Godello"]),
 ("Chianti", "Sangiovese", ["Montepulciano", "Aglianico", "Barbera"]), ("Beaujolais", "Gamay", ["Merlot", "Cabernet Franc", "Dolcetto"]),
 ("Red Burgundy", "Pinot Noir", ["Merlot", "Cabernet Franc", "Grenache"]), ("Prosecco", "Glera", ["Trebbiano", "Vermentino", "Pinot Grigio"]),
 ("Muscadet", "Melon de Bourgogne", ["Muscat", "Aligoté", "Trebbiano"]), ("Vouvray", "Chenin Blanc", ["Viognier", "Marsanne", "Aligoté"]),
 ("Hermitage", "Syrah", ["Grenache", "Mourvèdre", "Merlot"]), ("Cahors", "Malbec", ["Grenache", "Zinfandel", "Pinotage"]),
 ("Amarone", "Corvina", ["Nero d'Avola", "Aglianico", "Primitivo"]), ("Gavi", "Cortese", ["Vermentino", "Trebbiano", "Pinot Grigio"]),
 ("Soave", "Garganega", ["Vermentino", "Pinot Grigio", "Viognier"]), ("Tokaji", "Furmint", ["Grüner Veltliner", "Gewürztraminer", "Torrontés"]),
 ("Rías Baixas", "Albariño", ["Godello", "Torrontés", "Vermentino"]), ("Rueda", "Verdejo", ["Godello", "Viognier", "Torrontés"]),
 ("Sauternes", "Sémillon", ["Viognier", "Gewürztraminer", "Marsanne"]), ("Mosel", "Riesling", ["Grüner Veltliner", "Gewürztraminer", "Pinot Grigio"])])

race("which island group does this island belong to?", "World geography", "hard", ["islands", "archipelagos"], [
 ("Majorca", "The Balearic Islands", ["The Sporades", "The Aeolian Islands", "Cape Verde"]),
 ("Tenerife", "The Canary Islands", ["Cape Verde", "The Aeolian Islands", "The Sporades"]),
 ("Skye", "The Inner Hebrides", ["The Faroe Islands", "The Farne Islands", "The Aran Islands"]),
 ("Lewis", "The Outer Hebrides", ["The Faroe Islands", "The Aran Islands", "The Farne Islands"]),
 ("Hoy", "Orkney", ["The Faroe Islands", "The Farne Islands", "The Aran Islands"]),
 ("Unst", "Shetland", ["The Faroe Islands", "Lofoten", "The Åland Islands"]),
 ("Tresco", "The Isles of Scilly", ["The Farne Islands", "The Aran Islands", "The Frisian Islands"]),
 ("Sark", "The Channel Islands", ["The Frisian Islands", "The Farne Islands", "The Aran Islands"]),
 ("Santorini", "The Cyclades", ["The Sporades", "The Aeolian Islands", "The Saronic Islands"]),
 ("Corfu", "The Ionian Islands", ["The Sporades", "The Saronic Islands", "The Aeolian Islands"]),
 ("Rhodes", "The Dodecanese", ["The Sporades", "The Saronic Islands", "The Aeolian Islands"]),
 ("Oahu", "The Hawaiian Islands", ["The Aleutian Islands", "The Cook Islands", "The Marshall Islands"]),
 ("Tahiti", "The Society Islands", ["The Cook Islands", "The Marshall Islands", "The Marquesas"]),
 ("Mahé", "The Seychelles", ["The Maldives", "The Comoros", "The Andaman Islands"]),
 ("Porto Santo", "Madeira", ["Cape Verde", "The Aeolian Islands", "The Sporades"]),
 ("São Miguel", "The Azores", ["Cape Verde", "The Faroe Islands", "The Sporades"]),
 ("Guadalcanal", "The Solomon Islands", ["The Marshall Islands", "The Cook Islands", "The Marquesas"]),
 ("Viti Levu", "Fiji", ["The Cook Islands", "The Marshall Islands", "Tonga"]),
 ("Elba", "The Tuscan Archipelago", ["The Aeolian Islands", "The Sporades", "The Maltese Islands"]),
 ("Spitsbergen", "Svalbard", ["Lofoten", "The Faroe Islands", "Franz Josef Land"])])

race("which country does this dog breed come from?", "Animals", "medium", ["dogs", "breeds", "countries"], [
 ("Chihuahua", "Mexico", ["Peru", "Cuba", "Argentina"]), ("Great Dane", "Germany", ["Denmark", "Norway", "Sweden"]),
 ("Akita", "Japan", ["South Korea", "Taiwan", "Mongolia"]), ("Basenji", "DR Congo", ["Egypt", "Kenya", "Nigeria"]),
 ("Rhodesian Ridgeback", "Zimbabwe", ["Kenya", "Namibia", "Botswana"]), ("Pug", "China", ["Vietnam", "Thailand", "Mongolia"]),
 ("Samoyed", "Russia", ["Finland", "Norway", "Mongolia"]), ("Dalmatian", "Croatia", ["Serbia", "Slovenia", "Greece"]),
 ("Bernese Mountain Dog", "Switzerland", ["Austria", "Liechtenstein", "France"]), ("Corgi", "Wales", ["Scotland", "Ireland", "Cornwall"]),
 ("Vizsla", "Hungary", ["Romania", "Czechia", "Poland"]), ("Keeshond", "the Netherlands", ["Denmark", "Norway", "Luxembourg"]),
 ("Schipperke", "Belgium", ["Luxembourg", "Denmark", "France"]), ("Jack Russell Terrier", "England", ["Scotland", "Ireland", "Cornwall"]),
 ("Cane Corso", "Italy", ["Greece", "Portugal", "France"]), ("Pharaoh Hound", "Malta", ["Egypt", "Greece", "Cyprus"]),
 ("Ibizan Hound", "Spain", ["Portugal", "France", "Greece"]), ("Kangal", "Turkey", ["Armenia", "Greece", "Iran"]),
 ("Kelpie", "Australia", ["New Zealand", "Scotland", "Ireland"]), ("Alaskan Malamute", "the USA", ["Canada", "Greenland", "Iceland"])])

race("which country is this novel set in?", "Books", "medium", ["novels", "settings", "countries"], [
 ("Captain Corelli's Mandolin", "Greece", ["Cyprus", "Croatia", "Malta"]), ("The Kite Runner", "Afghanistan", ["Pakistan", "Iran", "Iraq"]),
 ("Wild Swans", "China", ["Taiwan", "South Korea", "Vietnam"]), ("The God of Small Things", "India", ["Sri Lanka", "Bangladesh", "Pakistan"]),
 ("One Hundred Years of Solitude", "Colombia", ["Peru", "Venezuela", "Cuba"]), ("Things Fall Apart", "Nigeria", ["Ghana", "Cameroon", "Senegal"]),
 ("Cry, the Beloved Country", "South Africa", ["Zimbabwe", "Namibia", "Botswana"]), ("The Shadow of the Wind", "Spain", ["Portugal", "Argentina", "Andorra"]),
 ("Doctor Zhivago", "Russia", ["Ukraine", "Poland", "Finland"]), ("The Name of the Rose", "Italy", ["Austria", "Switzerland", "Croatia"]),
 ("Les Misérables", "France", ["Belgium", "Switzerland", "Luxembourg"]), ("The Grapes of Wrath", "the USA", ["Canada", "Ireland", "Argentina"]),
 ("Memoirs of a Geisha", "Japan", ["South Korea", "Taiwan", "Vietnam"]), ("Out of Africa", "Kenya", ["Tanzania", "Uganda", "Ethiopia"]),
 ("Heart of Darkness", "the Congo", ["Angola", "Cameroon", "Gabon"]), ("Wolf Hall", "England", ["Wales", "Ireland", "Cornwall"]),
 ("Trainspotting", "Scotland", ["Wales", "Ireland", "Northern Ireland"]), ("The Book Thief", "Germany", ["Austria", "Poland", "Czechia"]),
 ("Like Water for Chocolate", "Mexico", ["Peru", "Cuba", "Argentina"]), ("The House of the Spirits", "Chile", ["Argentina", "Peru", "Bolivia"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-48.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
