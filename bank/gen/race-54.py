# Bank session 10 Oct 2026: 3 more general races -> bank/race-54.json. 20 rows each, target 10; wrong options are
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

race("which country is this traditional dress from?", "Art and culture", "medium", ["traditional dress", "countries"], [
 ("The kilt", "Scotland", ["Northern Ireland", "the Isle of Man", "Brittany"]), ("The kimono", "Japan", ["Taiwan", "Thailand", "Laos"]),
 ("The hanbok", "South Korea", ["Taiwan", "Thailand", "Laos"]), ("The qipao (cheongsam)", "China", ["Thailand", "Laos", "Malaysia"]),
 ("The sombrero", "Mexico", ["Peru", "Chile", "Cuba"]), ("The áo dài", "Vietnam", ["Thailand", "Laos", "Malaysia"]),
 ("Kente cloth", "Ghana", ["Nigeria", "Kenya", "Senegal"]), ("The flamenco dress", "Spain", ["Portugal", "Italy", "Greece"]),
 ("The bunad", "Norway", ["Sweden", "Denmark", "Finland"]), ("The gho", "Bhutan", ["Nepal", "Tibet", "Myanmar"]),
 ("The sampot", "Cambodia", ["Laos", "Myanmar", "Malaysia"]), ("The barong Tagalog", "the Philippines", ["Indonesia", "Malaysia", "Thailand"]),
 ("The deel", "Mongolia", ["Kazakhstan", "Nepal", "Tibet"]), ("The Aran jumper", "Ireland", ["Northern Ireland", "the Isle of Man", "Iceland"]),
 ("Klompen, the wooden clogs", "the Netherlands", ["Belgium", "Denmark", "Luxembourg"]), ("The beret", "France", ["Belgium", "Italy", "Portugal"]),
 ("The tall black 'Welsh hat'", "Wales", ["Northern Ireland", "the Isle of Man", "Cornwall"]), ("Bombachas, the gaucho's trousers", "Argentina", ["Chile", "Peru", "Bolivia"]),
 ("The pollera, the national dress", "Panama", ["Costa Rica", "Cuba", "Jamaica"]), ("The ruana", "Colombia", ["Chile", "Cuba", "Uruguay"])])

race("which country does this martial art or wrestling style come from?", "Sport", "hard", ["martial arts", "wrestling", "countries"], [
 ("Karate", "Japan", ["Taiwan", "Mongolia", "Laos"]), ("Taekwondo", "South Korea", ["Taiwan", "Mongolia", "Laos"]),
 ("Kung fu", "China", ["Mongolia", "Laos", "Nepal"]), ("Muay Thai", "Thailand", ["Laos", "Malaysia", "Indonesia"]),
 ("Capoeira", "Brazil", ["Argentina", "Cuba", "Colombia"]), ("Krav Maga", "Israel", ["Lebanon", "Jordan", "Egypt"]),
 ("Sambo", "Russia", ["Poland", "Bulgaria", "Finland"]), ("Kalaripayattu", "India", ["Sri Lanka", "Nepal", "Bangladesh"]),
 ("Savate", "France", ["Belgium", "Italy", "Spain"]), ("Eskrima", "the Philippines", ["Indonesia", "Malaysia", "Taiwan"]),
 ("Glíma", "Iceland", ["Denmark", "Finland", "Ireland"]), ("Lethwei", "Myanmar", ["Laos", "Bangladesh", "Nepal"]),
 ("Bokator", "Cambodia", ["Laos", "Malaysia", "Indonesia"]), ("Pankration", "Greece", ["Italy", "Cyprus", "Egypt"]),
 ("Bartitsu", "England", ["Scotland", "Ireland", "Wales"]), ("Vovinam", "Vietnam", ["Laos", "Taiwan", "Malaysia"]),
 ("Laamb wrestling", "Senegal", ["Nigeria", "Ghana", "Mali"]), ("Schwingen", "Switzerland", ["Austria", "Germany", "Italy"]),
 ("Yağlı güreş (oil wrestling)", "Turkey", ["Iran", "Bulgaria", "Egypt"]), ("Jogo do pau", "Portugal", ["Spain", "Italy", "Cape Verde"])])

race("which country is this opera house or concert hall in?", "Music", "medium", ["opera houses", "concert halls"], [
 ("La Scala", "Italy", ["Switzerland", "Malta", "Croatia"]), ("The Sydney Opera House", "Australia", ["New Zealand", "Fiji", "Singapore"]),
 ("The Bolshoi Theatre", "Russia", ["Ukraine", "Belarus", "Poland"]), ("The Palais Garnier", "France", ["Belgium", "Switzerland", "Luxembourg"]),
 ("The Metropolitan Opera", "the USA", ["Canada", "Mexico", "Cuba"]), ("The Royal Opera House", "the United Kingdom", ["Belgium", "Luxembourg", "Iceland"]),
 ("The Vienna State Opera", "Austria", ["Switzerland", "Slovakia", "Slovenia"]), ("The Semperoper", "Germany", ["Poland", "Switzerland", "Luxembourg"]),
 ("The Teatro Colón", "Argentina", ["Uruguay", "Chile", "Peru"]), ("The Oslo Opera House", "Norway", ["Sweden", "Finland", "Iceland"]),
 ("The Gran Teatre del Liceu", "Spain", ["Andorra", "Malta", "Greece"]), ("The Teatro Amazonas", "Brazil", ["Peru", "Colombia", "Venezuela"]),
 ("The Teatro Nacional de São Carlos", "Portugal", ["Malta", "Greece", "Cape Verde"]), ("The Hungarian State Opera", "Hungary", ["Slovakia", "Romania", "Poland"]),
 ("The Estates Theatre, where Don Giovanni opened", "Czechia", ["Slovakia", "Poland", "Slovenia"]), ("Dubai Opera", "the UAE", ["Qatar", "Bahrain", "Oman"]),
 ("The Guangzhou Opera House", "China", ["Taiwan", "Singapore", "Vietnam"]), ("The Wexford Opera House", "Ireland", ["Wales", "Scotland", "the Isle of Man"]),
 ("The Concertgebouw", "the Netherlands", ["Belgium", "Luxembourg", "Switzerland"]), ("The Copenhagen Opera House", "Denmark", ["Sweden", "Finland", "Iceland"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-54.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
