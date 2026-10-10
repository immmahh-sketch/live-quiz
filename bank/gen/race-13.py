# Bank session 10 Oct 2026: 4 more general races -> bank/race-13.json. 20 rows each, target 10; wrong options are
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

race("name the famous dragon", "Film, TV and books", "medium", ["dragons", "characters"], [
 ("The Hobbit's gold-hoarding dragon", "Smaug", ["Glaurung", "Ancalagon", "Scatha"]), ("The magic dragon who lived by the sea", "Puff", ["Jackie Paper", "Honalee", "Fluff"]),
 ("Hiccup's Night Fury", "Toothless", ["Stormfly", "Hookfang", "Meatlug"]), ("Daenerys's biggest dragon", "Drogon", ["Rhaegal", "Viserion", "Balerion"]),
 ("Hagrid's baby Norwegian Ridgeback", "Norbert", ["Fluffy", "Aragog", "Buckbeak"]), ("The NeverEnding Story's luckdragon", "Falkor", ["Artax", "Atreyu", "Gmork"]),
 ("Mulan's tiny guardian dragon", "Mushu", ["Cri-Kee", "Khan", "Shan Yu"]), ("The dragon in Pete's Dragon", "Elliott", ["Lampie", "Nora", "Doc Terminus"]),
 ("The purple video-game dragon", "Spyro", ["Sparx", "Crash", "Gnasty Gnorc"]), ("Eragon's blue dragon", "Saphira", ["Thorn", "Glaedr", "Shruikan"]),
 ("Spirited Away's river spirit who can turn into a dragon", "Haku", ["No-Face", "Kamaji", "Yubaba"]), ("The dragon Sean Connery voices in Dragonheart", "Draco", ["Bowen", "Einon", "Gilbert"]),
 ("The fire Pokémon that evolves from Charmeleon", "Charizard", ["Charmander", "Dragonite", "Gyarados"]), ("Dragon Ball's wish-granting dragon on Earth", "Shenron", ["Porunga", "Piccolo", "Goku"]),
 ("Ivor the Engine's little dragon", "Idris", ["Jones the Steam", "Dai Station", "Evans the Song"]), ("Raya and the Last Dragon's water dragon", "Sisu", ["Namaari", "Tuk Tuk", "Boun"]),
 ("The dragon Sigurd slays in Norse legend", "Fafnir", ["Sleipnir", "Fenrir", "Ratatoskr"]), ("The dragon Harry faces in the Triwizard Tournament", "Hungarian Horntail", ["Chinese Fireball", "Swedish Short-Snout", "Common Welsh Green"]),
 ("The Sleeping Beauty villain who turns into a dragon", "Maleficent", ["Diablo", "Aurora", "Merryweather"]), ("The dragon on the Welsh flag", "Y Ddraig Goch", ["Y Ddraig Wen", "Dewi", "Merlin"])])

race("which country is this palace or castle in?", "Famous landmarks", "medium", ["palaces", "castles", "countries"], [
 ("Versailles", "France", ["Luxembourg", "Switzerland", "Monaco"]), ("The Alhambra", "Spain", ["Morocco", "Egypt", "Greece"]),
 ("Topkapı Palace", "Turkey", ["Greece", "Iran", "Egypt"]), ("Schönbrunn Palace", "Austria", ["Switzerland", "Czechia", "Slovakia"]),
 ("The Forbidden City", "China", ["Mongolia", "Taiwan", "Vietnam"]), ("Peterhof", "Russia", ["Ukraine", "Finland", "Romania"]),
 ("Blenheim Palace", "England", ["Wales", "Ireland", "the Netherlands"]), ("Mysore Palace", "India", ["Pakistan", "Nepal", "Sri Lanka"]),
 ("Sanssouci", "Germany", ["Switzerland", "Czechia", "the Netherlands"]), ("Pena Palace", "Portugal", ["Brazil", "Greece", "Croatia"]),
 ("Holyroodhouse", "Scotland", ["Wales", "Ireland", "Norway"]), ("Christiansborg Palace", "Denmark", ["Norway", "Finland", "the Netherlands"]),
 ("Drottningholm Palace", "Sweden", ["Norway", "Finland", "Iceland"]), ("The Doge's Palace", "Italy", ["Croatia", "Greece", "Malta"]),
 ("Gyeongbokgung Palace", "South Korea", ["North Korea", "Taiwan", "Mongolia"]), ("The Grand Palace, home of the Emerald Buddha", "Thailand", ["Cambodia", "Laos", "Myanmar"]),
 ("Himeji Castle", "Japan", ["Taiwan", "North Korea", "Vietnam"]), ("Buda Castle", "Hungary", ["Czechia", "Romania", "Slovakia"]),
 ("Wawel Castle", "Poland", ["Czechia", "Slovakia", "Ukraine"]), ("The Royal Palace of Laeken", "Belgium", ["Luxembourg", "the Netherlands", "Switzerland"])])

race("what does this Latin phrase mean?", "Words and language", "medium", ["Latin", "phrases"], [
 ("Carpe diem", "Seize the day", ["Seize the fish", "Care for the day", "Rest for a day"]), ("Tempus fugit", "Time flies", ["Time stands still", "The storm is coming", "Time heals"]),
 ("In vino veritas", "In wine, there is truth", ["Wine makes you wise", "Truth in the vineyard", "Wine is life"]), ("Mea culpa", "My fault", ["My cup", "My secret", "My pleasure"]),
 ("Quid pro quo", "Something for something", ["Money for nothing", "A pound for a pound", "Take it or leave it"]), ("Pro bono", "For the public good", ["For a bone", "For the professionals", "For good luck"]),
 ("Caveat emptor", "Let the buyer beware", ["Beware of empty promises", "The empty cave", "Let the seller beware"]), ("Bona fide", "In good faith", ["Good dog", "Faithful bones", "Well made"]),
 ("Ad hoc", "For this purpose", ["To the hill", "For ever", "After the fact"]), ("Terra firma", "Solid ground", ["Terrible farm", "Earth's edge", "Shaky ground"]),
 ("Vice versa", "The other way round", ["A bad poem", "Against the law", "Twice over"]), ("Post mortem", "After death", ["After the post", "Before death", "After the war"]),
 ("Magnum opus", "Great work", ["A big gun", "A great opera", "A large opening"]), ("Non sequitur", "It does not follow", ["No second chances", "Not secure", "Without a sequel"]),
 ("Persona non grata", "An unwelcome person", ["An ungrateful person", "A person of no importance", "A nameless person"]), ("Habeas corpus", "You should have the body", ["Have a heart", "Bring the money", "A healthy body"]),
 ("Per annum", "Per year", ["Per person", "Per hour", "Per month"]), ("Ad infinitum", "To infinity", ["To the finish", "In the end", "Up to a point"]),
 ("Alma mater", "Nourishing mother", ["Old flame", "Mother's soul", "Dear friend"]), ("Et tu, Brute?", "You too, Brutus?", ["And now, brute?", "And you, Caesar?", "Even the brutes?"])])

race("which country is this island part of?", "World geography", "medium", ["islands", "countries"], [
 ("Corsica", "France", ["Malta", "Monaco", "Croatia"]), ("Sardinia", "Italy", ["Malta", "Croatia", "Tunisia"]),
 ("Mallorca", "Spain", ["Malta", "Morocco", "Cyprus"]), ("Crete", "Greece", ["Cyprus", "Turkey", "Malta"]),
 ("Gotland", "Sweden", ["Finland", "Estonia", "Latvia"]), ("Bornholm", "Denmark", ["Germany", "Poland", "Finland"]),
 ("Madeira", "Portugal", ["Morocco", "Cape Verde", "Brazil"]), ("Tasmania", "Australia", ["New Zealand", "Papua New Guinea", "Fiji"]),
 ("Hokkaido", "Japan", ["Russia", "North Korea", "Taiwan"]), ("Bali", "Indonesia", ["Malaysia", "the Philippines", "Thailand"]),
 ("Zanzibar", "Tanzania", ["Kenya", "Mozambique", "Madagascar"]), ("Hawaii", "the USA", ["Mexico", "Fiji", "Canada"]),
 ("Svalbard", "Norway", ["Finland", "Iceland", "Russia"]), ("The Galápagos Islands", "Ecuador", ["Peru", "Colombia", "Mexico"]),
 ("Easter Island", "Chile", ["Peru", "New Zealand", "Argentina"]), ("Jeju", "South Korea", ["North Korea", "Taiwan", "Vietnam"]),
 ("Hainan", "China", ["Taiwan", "Vietnam", "the Philippines"]), ("Anglesey", "Wales", ["Ireland", "the Isle of Man", "Northern Ireland"]),
 ("Lindisfarne", "England", ["Ireland", "Northern Ireland", "the Isle of Man"]), ("Skye", "Scotland", ["Ireland", "Northern Ireland", "Iceland"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-13.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
