# Bank session 10 Oct 2026: 4 more general races -> bank/race-6.json. 20 rows each, target 10; wrong options are
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

race("what do you call someone from here?", "Words and language", "medium", ["demonyms", "places"], [
 ("Manchester", "Mancunian", ["Manchestrian", "Mancastrian", "Mancovian"]), ("Liverpool", "Liverpudlian", ["Liverpoolian", "Liverpudian", "Livermudlian"]),
 ("Glasgow", "Glaswegian", ["Glasgowite", "Glaswegan", "Glasgonian"]), ("Aberdeen", "Aberdonian", ["Aberdeenian", "Aberdeener", "Aberdovian"]),
 ("Dundee", "Dundonian", ["Dundeeite", "Dundovian", "Dundeeian"]), ("Birmingham", "Brummie", ["Birmie", "Brummer", "Bingie"]),
 ("Sunderland", "Mackem", ["Geordie", "Smoggie", "Sand dancer"]), ("Moscow", "Muscovite", ["Moscovian", "Moskvan", "Moscowite"]),
 ("Naples", "Neapolitan", ["Naplesian", "Napolese", "Naplitan"]), ("Venice", "Venetian", ["Venician", "Venezian", "Venesian"]),
 ("Monaco", "Monégasque", ["Monacoan", "Monegan", "Monacian"]), ("Oxford", "Oxonian", ["Oxfordian", "Oxfordite", "Oxenian"]),
 ("The Isle of Man", "Manx", ["Mannish", "Mannian", "Manese"]), ("Leeds", "Loiner", ["Leedsite", "Leedser", "Yorkie"]),
 ("The Philippines", "Filipino", ["Philippian", "Philipese", "Manilan"]), ("Cyprus", "Cypriot", ["Cyprese", "Cyprusian", "Cypran"]),
 ("Paris", "Parisian", ["Parisite", "Parisois", "Parisine"]), ("Edinburgh", "Edinburgher", ["Edinburgian", "Edinbrian", "Edinbourgher"]),
 ("Florence", "Florentine", ["Florencian", "Florentian", "Florenzan"]), ("Hamburg", "Hamburger", ["Hamburgian", "Hamburgish", "Hamburgite"])])

race("which country is this mountain or volcano in?", "World geography", "medium", ["mountains", "volcanoes", "countries"], [
 ("Kilimanjaro", "Tanzania", ["Kenya", "Uganda", "Ethiopia"]), ("Mount Fuji", "Japan", ["China", "South Korea", "Taiwan"]),
 ("Table Mountain", "South Africa", ["Namibia", "Botswana", "Zimbabwe"]), ("Mount Kosciuszko", "Australia", ["Papua New Guinea", "Fiji", "Samoa"]),
 ("Denali", "USA", ["Russia", "Iceland", "Greenland"]), ("Mount Etna", "Italy", ["Malta", "Croatia", "Portugal"]),
 ("Mount Olympus", "Greece", ["Cyprus", "Bulgaria", "Albania"]), ("Mount Ararat", "Turkey", ["Armenia", "Iran", "Georgia"]),
 ("Aconcagua", "Argentina", ["Chile", "Peru", "Bolivia"]), ("Aoraki / Mount Cook", "New Zealand", ["Samoa", "Tonga", "Vanuatu"]),
 ("Mount Teide", "Spain", ["Portugal", "Morocco", "Cape Verde"]), ("The Zugspitze", "Germany", ["Switzerland", "Poland", "Czechia"]),
 ("Snowdon (Yr Wyddfa)", "Wales", ["England", "Ireland", "the Isle of Man"]), ("Mount Sinai", "Egypt", ["Jordan", "Israel", "Saudi Arabia"]),
 ("Ben Nevis", "Scotland", ["England", "Ireland", "Northern Ireland"]), ("Popocatépetl", "Mexico", ["Peru", "Guatemala", "Colombia"]),
 ("Mount Logan", "Canada", ["Greenland", "Iceland", "Russia"]), ("Krakatoa", "Indonesia", ["Malaysia", "Thailand", "Papua New Guinea"]),
 ("Galdhøpiggen", "Norway", ["Sweden", "Finland", "Denmark"]), ("Mount Pinatubo", "Philippines", ["Malaysia", "Vietnam", "Thailand"])])

race("what's the Spanish word?", "Words and language", "medium", ["Spanish", "languages"], [
 ("Sun", "Sol", ["Sal", "Sur", "Suelo"]), ("Moon", "Luna", ["Lana", "Lunes", "Lluvia"]), ("Sea", "Mar", ["Mes", "Mil", "Miel"]),
 ("Beach", "Playa", ["Plaza", "Plata", "Planta"]), ("Fish (to eat)", "Pescado", ["Pesado", "Pecado", "Pasado"]), ("Chicken", "Pollo", ["Polvo", "Pelo", "Palo"]),
 ("Egg", "Huevo", ["Hueso", "Nuevo", "Huerto"]), ("Cheese", "Queso", ["Beso", "Peso", "Hueso"]), ("Bread", "Pan", ["Paz", "Pie", "Piso"]),
 ("Water", "Agua", ["Aguja", "Ajo", "Ala"]), ("Wine", "Vino", ["Vivo", "Vaso", "Vela"]), ("Street", "Calle", ["Cara", "Cielo", "Carne"]),
 ("Church", "Iglesia", ["Isla", "Idioma", "Iguana"]), ("Money", "Dinero", ["Diario", "Dedo", "Cordero"]), ("Today", "Hoy", ["Hoja", "Ayer", "Hora"]),
 ("Tomorrow", "Mañana", ["Manzana", "Montaña", "Semana"]), ("Big", "Grande", ["Gordo", "Grave", "Guapo"]), ("Small", "Pequeño", ["Pobre", "Pesado", "Pelado"]),
 ("Hot", "Caliente", ["Cliente", "Valiente", "Corriente"]), ("Cold", "Frío", ["Feo", "Fuego", "Frito"])])

race("which language says hello like this?", "Words and language", "medium", ["languages", "greetings"], [
 ("Bonjour", "French", ["Romanian", "Catalan", "Dutch"]), ("Ciao", "Italian", ["Spanish", "Romanian", "Maltese"]),
 ("Guten Tag", "German", ["Dutch", "Danish", "Norwegian"]), ("Konnichiwa", "Japanese", ["Cantonese", "Vietnamese", "Mongolian"]),
 ("Nǐ hǎo", "Mandarin", ["Cantonese", "Vietnamese", "Mongolian"]), ("Namaste", "Hindi", ["Urdu", "Persian", "Sinhala"]),
 ("Shalom", "Hebrew", ["Arabic", "Persian", "Amharic"]), ("Jambo", "Swahili", ["Amharic", "Yoruba", "Somali"]),
 ("Aloha", "Hawaiian", ["Samoan", "Tongan", "Fijian"]), ("Kia ora", "Māori", ["Samoan", "Tongan", "Fijian"]),
 ("Sawubona", "Zulu", ["Xhosa", "Sotho", "Shona"]), ("Merhaba", "Turkish", ["Persian", "Kurdish", "Armenian"]),
 ("Olá", "Portuguese", ["Spanish", "Catalan", "Romanian"]), ("Dzień dobry", "Polish", ["Czech", "Slovak", "Ukrainian"]),
 ("Dia dhuit", "Irish", ["Scottish Gaelic", "Manx", "Breton"]), ("Shwmae", "Welsh", ["Cornish", "Breton", "Manx"]),
 ("Annyeong", "Korean", ["Mongolian", "Vietnamese", "Cantonese"]), ("Sawasdee", "Thai", ["Lao", "Khmer", "Burmese"]),
 ("Privet", "Russian", ["Ukrainian", "Bulgarian", "Czech"]), ("Yassou", "Greek", ["Albanian", "Bulgarian", "Maltese"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-6.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
