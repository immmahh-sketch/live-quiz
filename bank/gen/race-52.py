# Bank session 10 Oct 2026: 3 more general races -> bank/race-52.json. 20 rows each, target 10; wrong options are
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

race("which country is this famous hotel in?", "Travel", "medium", ["hotels", "countries"], [
 ("The Burj Al Arab", "the UAE", ["Qatar", "Bahrain", "Oman"]), ("Raffles", "Singapore", ["Malaysia", "Indonesia", "Hong Kong"]),
 ("The Savoy", "England", ["Wales", "Northern Ireland", "the Isle of Man"]), ("The Waldorf Astoria", "the USA", ["Mexico", "Bermuda", "the Bahamas"]),
 ("The Taj Mahal Palace", "India", ["Pakistan", "Sri Lanka", "Bangladesh"]), ("The Mena House, by the Pyramids", "Egypt", ["Jordan", "Lebanon", "Tunisia"]),
 ("The Château Frontenac", "Canada", ["Belgium", "Luxembourg", "Monaco"]), ("The Gellért, with its famous baths", "Hungary", ["Czechia", "Slovakia", "Romania"]),
 ("The Hotel Sacher", "Austria", ["Switzerland", "Czechia", "Slovenia"]), ("The Hotel Adlon", "Germany", ["Switzerland", "Poland", "Luxembourg"]),
 ("The Pera Palace", "Turkey", ["Greece", "Cyprus", "Bulgaria"]), ("La Mamounia", "Morocco", ["Tunisia", "Algeria", "Jordan"]),
 ("The Copacabana Palace", "Brazil", ["Argentina", "Uruguay", "Chile"]), ("Gleneagles", "Scotland", ["Wales", "Northern Ireland", "the Isle of Man"]),
 ("The Grand Hotel Tremezzo, on Lake Como", "Italy", ["Switzerland", "Monaco", "Croatia"]), ("The Mandarin Oriental, Bangkok", "Thailand", ["Vietnam", "Malaysia", "Cambodia"]),
 ("The Hôtel de Crillon", "France", ["Belgium", "Luxembourg", "Monaco"]), ("The Icehotel", "Sweden", ["Norway", "Finland", "Iceland"]),
 ("Reid's Palace, on Madeira", "Portugal", ["Spain", "Cape Verde", "Malta"]), ("Ashford Castle", "Ireland", ["Wales", "Northern Ireland", "the Isle of Man"])])

race("which studio or company made this film?", "Film", "hard", ["film studios", "films"], [
 ("Toy Story", "Pixar", ["Sony Pictures Animation", "Warner Bros.", "Universal"]), ("Shrek", "DreamWorks", ["Sony Pictures Animation", "Warner Bros.", "Paramount"]),
 ("Spirited Away", "Studio Ghibli", ["Toei Animation", "Sunrise", "Madhouse"]), ("Chicken Run", "Aardman", ["BBC Films", "Film4", "StudioCanal"]),
 ("Despicable Me", "Illumination", ["Sony Pictures Animation", "Warner Bros.", "Paramount"]), ("Ice Age", "Blue Sky", ["Sony Pictures Animation", "Paramount", "Warner Bros."]),
 ("Coraline", "Laika", ["Warner Bros.", "Paramount", "Annapurna"]), ("Frozen", "Walt Disney Animation", ["Sony Pictures Animation", "Universal", "Paramount"]),
 ("Dracula (1958), with Christopher Lee", "Hammer", ["Rank", "MGM", "Universal"]), ("The Ladykillers (1955)", "Ealing", ["Rank", "MGM", "Gainsborough"]),
 ("Four Weddings and a Funeral", "Working Title", ["Film4", "BBC Films", "Miramax"]), ("Dr. No", "Eon Productions", ["MGM", "Rank", "Paramount"]),
 ("Iron Man", "Marvel Studios", ["Warner Bros.", "Sony Pictures", "20th Century Fox"]), ("Star Wars (1977)", "Lucasfilm", ["Paramount", "Universal", "MGM"]),
 ("E.T. the Extra-Terrestrial", "Amblin", ["Paramount", "MGM", "Columbia"]), ("Everything Everywhere All at Once", "A24", ["Neon", "Annapurna", "Focus Features"]),
 ("Get Out", "Blumhouse", ["Neon", "Annapurna", "Focus Features"]), ("The Secret of Kells", "Cartoon Saloon", ["StudioCanal", "BBC Films", "Film4"]),
 ("The Hunger Games", "Lionsgate", ["Paramount", "Universal", "Columbia"]), ("The Lord of the Rings films", "New Line Cinema", ["Paramount", "Universal", "Miramax"])])

race("which country does this department store come from?", "Shopping", "medium", ["department stores", "countries"], [
 ("Macy's", "the USA", ["Canada", "New Zealand", "Puerto Rico"]), ("Galeries Lafayette", "France", ["Luxembourg", "Monaco", "Portugal"]),
 ("KaDeWe", "Germany", ["Austria", "Poland", "Czechia"]), ("El Corte Inglés", "Spain", ["Portugal", "Argentina", "Andorra"]),
 ("La Rinascente", "Italy", ["Malta", "Greece", "Croatia"]), ("GUM", "Russia", ["Ukraine", "Belarus", "Kazakhstan"]),
 ("Isetan", "Japan", ["Taiwan", "China", "Thailand"]), ("Myer", "Australia", ["New Zealand", "Canada", "South Africa"]),
 ("Brown Thomas", "Ireland", ["Scotland", "Wales", "Northern Ireland"]), ("Stockmann", "Finland", ["Estonia", "Latvia", "Iceland"]),
 ("Illum", "Denmark", ["Iceland", "Estonia", "Latvia"]), ("NK (Nordiska Kompaniet)", "Sweden", ["Iceland", "Estonia", "Latvia"]),
 ("De Bijenkorf", "the Netherlands", ["Luxembourg", "Austria", "Poland"]), ("Steen & Strøm", "Norway", ["Iceland", "Estonia", "Latvia"]),
 ("Harrods", "England", ["Scotland", "Wales", "Northern Ireland"]), ("El Puerto de Liverpool", "Mexico", ["Colombia", "Peru", "Argentina"]),
 ("Falabella", "Chile", ["Uruguay", "Bolivia", "Paraguay"]), ("Shinsegae", "South Korea", ["Taiwan", "China", "Thailand"]),
 ("Inno", "Belgium", ["Luxembourg", "Austria", "Poland"]), ("Manor", "Switzerland", ["Austria", "Liechtenstein", "Luxembourg"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-52.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
