# Bank session 10 Oct 2026: 2 more general races -> bank/race-60.json. 20 rows each, target 10; wrong options are
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

race("which country is this glacier in?", "World geography", "hard", ["glaciers", "countries"], [
 ("The Perito Moreno Glacier", "Argentina", ["Uruguay", "Bolivia", "Paraguay"]), ("The Aletsch Glacier", "Switzerland", ["Liechtenstein", "Slovenia", "Germany"]),
 ("Jostedalsbreen", "Norway", ["Sweden", "Finland", "Denmark"]), ("Vatnajökull", "Iceland", ["the Faroe Islands", "Denmark", "Sweden"]),
 ("The Franz Josef Glacier", "New Zealand", ["Fiji", "Australia", "Papua New Guinea"]), ("The Mendenhall Glacier", "the USA", ["Russia", "Mexico", "Japan"]),
 ("The Athabasca Glacier", "Canada", ["Russia", "Mexico", "Japan"]), ("The Mer de Glace", "France", ["Belgium", "Luxembourg", "Germany"]),
 ("The Pasterze", "Austria", ["Germany", "Slovenia", "Liechtenstein"]), ("The Grey Glacier", "Chile", ["Uruguay", "Bolivia", "Paraguay"]),
 ("The Khumbu Glacier, below Everest", "Nepal", ["Bhutan", "Bangladesh", "Tibet"]), ("The Baltoro Glacier, below K2", "Pakistan", ["Afghanistan", "Kyrgyzstan", "Bhutan"]),
 ("The Ilulissat Icefjord", "Greenland", ["the Faroe Islands", "Denmark", "Sweden"]), ("The Fedchenko Glacier", "Tajikistan", ["Kyrgyzstan", "Uzbekistan", "Afghanistan"]),
 ("The Pastoruri Glacier", "Peru", ["Bolivia", "Ecuador", "Colombia"]), ("The Furtwängler Glacier on Kilimanjaro", "Tanzania", ["Uganda", "Rwanda", "Ethiopia"]),
 ("The Gangotri Glacier, source of the Ganges", "India", ["Bhutan", "Bangladesh", "Afghanistan"]), ("The Baishui Glacier on Jade Dragon Snow Mountain", "China", ["Mongolia", "Laos", "Myanmar"]),
 ("The Calderone, a glacier in the Apennines", "Italy", ["Slovenia", "Croatia", "Greece"]), ("The Lewis Glacier on Mount Kenya", "Kenya", ["Uganda", "Ethiopia", "Rwanda"])])

race("which country is this famous rock formation in?", "World geography", "hard", ["rock formations", "countries"], [
 ("Uluru", "Australia", ["Fiji", "Papua New Guinea", "Indonesia"]), ("Sugarloaf Mountain", "Brazil", ["Argentina", "Uruguay", "Chile"]),
 ("Table Mountain", "South Africa", ["Namibia", "Botswana", "Zimbabwe"]), ("Delicate Arch", "the USA", ["Mexico", "Cuba", "Guatemala"]),
 ("Sigiriya, the Lion Rock", "Sri Lanka", ["India", "the Maldives", "Bangladesh"]), ("The monasteries of Meteora", "Greece", ["Cyprus", "Bulgaria", "Albania"]),
 ("The cliffs of Étretat", "France", ["Belgium", "Luxembourg", "the Netherlands"]), ("The Bastei rocks", "Germany", ["Austria", "Poland", "Denmark"]),
 ("The fairy chimneys of Cappadocia", "Turkey", ["Cyprus", "Armenia", "Syria"]), ("Preikestolen (Pulpit Rock)", "Norway", ["Sweden", "Finland", "Denmark"]),
 ("The Moeraki Boulders", "New Zealand", ["Fiji", "Samoa", "Tonga"]), ("The Stone Forest of Shilin", "China", ["Vietnam", "Laos", "Mongolia"]),
 ("Ben Bulben", "Ireland", ["Wales", "Northern Ireland", "the Isle of Man"]), ("The Drumheller hoodoos", "Canada", ["Mexico", "Greenland", "Russia"]),
 ("The Ciudad Encantada", "Spain", ["Portugal", "Andorra", "Italy"]), ("Old Harry Rocks", "England", ["Wales", "Northern Ireland", "the Isle of Man"]),
 ("The Old Man of Hoy", "Scotland", ["Wales", "Northern Ireland", "the Faroe Islands"]), ("'James Bond Island' in Phang Nga Bay", "Thailand", ["Vietnam", "Malaysia", "Myanmar"]),
 ("Elephant Rock on Heimaey", "Iceland", ["the Faroe Islands", "Greenland", "Denmark"]), ("Auyán-tepui, the table mountain behind Angel Falls", "Venezuela", ["Colombia", "Ecuador", "Peru"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-60.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
