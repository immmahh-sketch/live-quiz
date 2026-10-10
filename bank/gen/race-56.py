# Bank session 10 Oct 2026: 3 more general races -> bank/race-56.json. 20 rows each, target 10; wrong options are
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

race("which country is this racecourse in?", "Sport", "medium", ["horse racing", "racecourses"], [
 ("Longchamp", "France", ["Belgium", "Switzerland", "Monaco"]), ("Flemington", "Australia", ["Fiji", "Singapore", "Malaysia"]),
 ("Churchill Downs", "the USA", ["Mexico", "Bermuda", "the Bahamas"]), ("Meydan", "the UAE", ["Qatar", "Bahrain", "Oman"]),
 ("Sha Tin", "Hong Kong", ["Singapore", "Macau", "Taiwan"]), ("The Curragh", "Ireland", ["Northern Ireland", "the Isle of Man", "Iceland"]),
 ("Aintree", "England", ["Northern Ireland", "the Isle of Man", "Iceland"]), ("Ayr", "Scotland", ["Northern Ireland", "the Isle of Man", "Iceland"]),
 ("Chepstow", "Wales", ["Northern Ireland", "the Isle of Man", "Iceland"]), ("Tokyo Racecourse, home of the Japan Cup", "Japan", ["South Korea", "Taiwan", "Singapore"]),
 ("Woodbine", "Canada", ["Mexico", "Bermuda", "Iceland"]), ("The Ippodromo San Siro", "Italy", ["Switzerland", "Monaco", "Malta"]),
 ("Iffezheim, near Baden-Baden", "Germany", ["Austria", "Switzerland", "Poland"]), ("Jägersro", "Sweden", ["Denmark", "Finland", "Iceland"]),
 ("Øvrevoll", "Norway", ["Denmark", "Finland", "Iceland"]), ("Ellerslie", "New Zealand", ["Fiji", "Singapore", "Malaysia"]),
 ("Kenilworth", "South Africa", ["Namibia", "Zimbabwe", "Kenya"]), ("The Hipódromo de Palermo", "Argentina", ["Uruguay", "Chile", "Peru"]),
 ("The Gávea racecourse", "Brazil", ["Uruguay", "Peru", "Colombia"]), ("Pardubice, home of the Velká pardubická", "Czechia", ["Slovakia", "Poland", "Hungary"])])

race("which country did this explorer come from?", "History", "hard", ["explorers", "countries"], [
 ("Christopher Columbus", "Italy", ["Malta", "Greece", "Croatia"]), ("Ferdinand Magellan", "Portugal", ["Brazil", "Malta", "Greece"]),
 ("Roald Amundsen", "Norway", ["Finland", "Estonia", "Austria"]), ("Captain James Cook", "England", ["Wales", "the Isle of Man", "Northern Ireland"]),
 ("Abel Tasman", "the Netherlands", ["Luxembourg", "Austria", "Poland"]), ("Vitus Bering", "Denmark", ["Finland", "Estonia", "Poland"]),
 ("Ibn Battuta", "Morocco", ["Algeria", "Tunisia", "Egypt"]), ("Zheng He", "China", ["Mongolia", "Korea", "Vietnam"]),
 ("Hernán Cortés", "Spain", ["Mexico", "Malta", "Andorra"]), ("Jacques Cartier", "France", ["Canada", "Luxembourg", "Switzerland"]),
 ("Leif Erikson", "Iceland", ["Greenland", "Finland", "the Faroe Islands"]), ("Ernest Shackleton", "Ireland", ["Wales", "the Isle of Man", "Northern Ireland"]),
 ("Edmund Hillary", "New Zealand", ["Australia", "Fiji", "South Africa"]), ("Sven Hedin", "Sweden", ["Finland", "Estonia", "Austria"]),
 ("Alexander von Humboldt", "Germany", ["Austria", "Switzerland", "Luxembourg"]), ("David Livingstone", "Scotland", ["Wales", "the Isle of Man", "Northern Ireland"]),
 ("Robert Peary", "the USA", ["Canada", "Australia", "Greenland"]), ("Yuri Gagarin", "Russia", ["Ukraine", "Belarus", "Kazakhstan"]),
 ("Junko Tabei, first woman up Everest", "Japan", ["South Korea", "Taiwan", "Mongolia"]), ("Adrien de Gerlache, of the Belgica", "Belgium", ["Luxembourg", "Austria", "Switzerland"])])

race("which country hosts this famous race or event?", "Sport", "hard", ["races", "events", "countries"], [
 ("The Comrades Marathon", "South Africa", ["Namibia", "Zimbabwe", "Kenya"]), ("The Marathon des Sables", "Morocco", ["Algeria", "Tunisia", "Egypt"]),
 ("The Great North Run", "England", ["Wales", "Scotland", "the Isle of Man"]), ("The Athens Classic Marathon", "Greece", ["Cyprus", "Turkey", "Bulgaria"]),
 ("The Vasaloppet ski race", "Sweden", ["Finland", "Denmark", "Iceland"]), ("The Giro d'Italia", "Italy", ["Malta", "Croatia", "Slovenia"]),
 ("The Vuelta", "Spain", ["Portugal", "Andorra", "Malta"]), ("The Tour of Flanders", "Belgium", ["Luxembourg", "Denmark", "Germany"]),
 ("The Dakar Rally, since 2020", "Saudi Arabia", ["Senegal", "Egypt", "Jordan"]), ("The Bathurst 1000", "Australia", ["Fiji", "Singapore", "Malaysia"]),
 ("The Indianapolis 500", "the USA", ["Canada", "Mexico", "Bermuda"]), ("The Monte Carlo Rally", "Monaco", ["Andorra", "Luxembourg", "San Marino"]),
 ("The Cresta Run", "Switzerland", ["Liechtenstein", "Luxembourg", "Czechia"]), ("The Hahnenkamm downhill", "Austria", ["Liechtenstein", "Slovenia", "Czechia"]),
 ("The Elfstedentocht skating race", "the Netherlands", ["Denmark", "Luxembourg", "Germany"]), ("The Tour de France", "France", ["Luxembourg", "Andorra", "Denmark"]),
 ("The Birkebeinerrennet", "Norway", ["Finland", "Denmark", "Iceland"]), ("The Rás Tailteann cycle race", "Ireland", ["Wales", "Scotland", "the Isle of Man"]),
 ("The Hakone Ekiden relay", "Japan", ["South Korea", "Taiwan", "China"]), ("The Coast to Coast multisport race", "New Zealand", ["Fiji", "Singapore", "Malaysia"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-56.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
