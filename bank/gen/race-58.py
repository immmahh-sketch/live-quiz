# Bank session 10 Oct 2026: 3 more general races -> bank/race-58.json. 20 rows each, target 10; wrong options are
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

race("which country is this gorge or canyon in?", "World geography", "hard", ["gorges", "canyons", "countries"], [
 ("Antelope Canyon", "the USA", ["Canada", "Chile", "Cuba"]), ("Fish River Canyon", "Namibia", ["Botswana", "Angola", "Zimbabwe"]),
 ("Colca Canyon", "Peru", ["Bolivia", "Ecuador", "Chile"]), ("Copper Canyon", "Mexico", ["Guatemala", "Cuba", "Colombia"]),
 ("The Verdon Gorge", "France", ["Belgium", "Luxembourg", "Monaco"]), ("The Samaria Gorge", "Greece", ["Cyprus", "Croatia", "Malta"]),
 ("The Tara River Canyon", "Montenegro", ["Albania", "Serbia", "Bosnia and Herzegovina"]), ("The Avon Gorge", "England", ["Wales", "Ireland", "Northern Ireland"]),
 ("Tiger Leaping Gorge", "China", ["Nepal", "Bhutan", "Laos"]), ("Blyde River Canyon", "South Africa", ["Botswana", "Zimbabwe", "Mozambique"]),
 ("Kings Canyon", "Australia", ["Fiji", "Papua New Guinea", "Indonesia"]), ("The Todra Gorge", "Morocco", ["Algeria", "Tunisia", "Egypt"]),
 ("The Aare Gorge", "Switzerland", ["Austria", "Liechtenstein", "Germany"]), ("The Vintgar Gorge", "Slovenia", ["Croatia", "Austria", "Slovakia"]),
 ("The Takachiho Gorge", "Japan", ["South Korea", "Taiwan", "the Philippines"]), ("Charyn Canyon", "Kazakhstan", ["Uzbekistan", "Kyrgyzstan", "Mongolia"]),
 ("The Ihlara Valley", "Turkey", ["Armenia", "Syria", "Cyprus"]), ("The Rugova Canyon", "Kosovo", ["Albania", "Serbia", "North Macedonia"]),
 ("The Rakaia Gorge", "New Zealand", ["Fiji", "Papua New Guinea", "Indonesia"]), ("Fjaðrárgljúfur", "Iceland", ["Norway", "the Faroe Islands", "Greenland"])])

race("which country is this famous cave in?", "World geography", "hard", ["caves", "countries"], [
 ("The Waitomo glow-worm caves", "New Zealand", ["Fiji", "Samoa", "Tonga"]), ("Postojna Cave", "Slovenia", ["Croatia", "Slovakia", "Hungary"]),
 ("Carlsbad Caverns", "the USA", ["Canada", "Cuba", "Guatemala"]), ("Hang Sơn Đoòng, the world's biggest cave", "Vietnam", ["Laos", "Cambodia", "Myanmar"]),
 ("The Blue Grotto on Capri", "Italy", ["Cyprus", "Montenegro", "Albania"]), ("Reed Flute Cave", "China", ["Laos", "Myanmar", "Mongolia"]),
 ("Eisriesenwelt, the giant ice cave", "Austria", ["Switzerland", "Germany", "Czechia"]), ("The Cave of the Crystals", "Mexico", ["Guatemala", "Cuba", "Colombia"]),
 ("The Lascaux cave paintings", "France", ["Belgium", "Luxembourg", "Switzerland"]), ("The Altamira cave paintings", "Spain", ["Andorra", "Malta", "Morocco"]),
 ("Wookey Hole", "England", ["Wales", "Ireland", "the Isle of Man"]), ("The Ajanta Caves", "India", ["Nepal", "Sri Lanka", "Bangladesh"]),
 ("The Batu Caves", "Malaysia", ["Indonesia", "Singapore", "the Philippines"]), ("Phraya Nakhon Cave", "Thailand", ["Laos", "Cambodia", "Myanmar"]),
 ("Benagil sea cave", "Portugal", ["Morocco", "Malta", "Cape Verde"]), ("Melissani Cave", "Greece", ["Cyprus", "Albania", "Turkey"]),
 ("The Jenolan Caves", "Australia", ["Fiji", "Samoa", "Papua New Guinea"]), ("The ice caves under Vatnajökull", "Iceland", ["Norway", "Greenland", "the Faroe Islands"]),
 ("Smoo Cave", "Scotland", ["Wales", "Ireland", "the Isle of Man"]), ("Krubera Cave, the deepest known", "Georgia", ["Armenia", "Azerbaijan", "Turkey"])])

race("which country is this desert in?", "World geography", "hard", ["deserts", "countries"], [
 ("The Atacama", "Chile", ["Bolivia", "Argentina", "Ecuador"]), ("The Namib", "Namibia", ["Botswana", "Zimbabwe", "Zambia"]),
 ("The Simpson Desert", "Australia", ["Fiji", "New Zealand", "Papua New Guinea"]), ("The Taklamakan", "China", ["Mongolia", "Kyrgyzstan", "Pakistan"]),
 ("The Danakil Depression", "Ethiopia", ["Somalia", "Kenya", "Sudan"]), ("The Lut Desert", "Iran", ["Iraq", "Afghanistan", "Pakistan"]),
 ("The Negev", "Israel", ["Jordan", "Lebanon", "Syria"]), ("The Sinai", "Egypt", ["Jordan", "Lebanon", "Saudi Arabia"]),
 ("The Mojave", "the USA", ["Cuba", "Guatemala", "Belize"]), ("The Tabernas Desert, home of spaghetti westerns", "Spain", ["Portugal", "Greece", "Malta"]),
 ("The Karakum", "Turkmenistan", ["Uzbekistan", "Kazakhstan", "Afghanistan"]), ("Lençóis Maranhenses", "Brazil", ["Argentina", "Venezuela", "Uruguay"]),
 ("The Tatacoa Desert", "Colombia", ["Venezuela", "Ecuador", "Panama"]), ("The Sechura Desert", "Peru", ["Ecuador", "Bolivia", "Venezuela"]),
 ("Erg Chebbi", "Morocco", ["Algeria", "Tunisia", "Libya"]), ("The Accona Desert", "Italy", ["Greece", "Malta", "Croatia"]),
 ("The Oleshky Sands", "Ukraine", ["Belarus", "Moldova", "Romania"]), ("The Błędów Desert", "Poland", ["Czechia", "Slovakia", "Lithuania"]),
 ("The Deliblato Sands", "Serbia", ["Croatia", "Bosnia and Herzegovina", "Bulgaria"]), ("The Carcross Desert", "Canada", ["Greenland", "Iceland", "Russia"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-58.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
