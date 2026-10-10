# Bank session 10 Oct 2026: 2 more general races -> bank/race-61.json. 20 rows each, target 10; wrong options are
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

race("whose national motto is this?", "World geography", "hard", ["mottos", "countries"], [
 ("Liberté, égalité, fraternité", "France", ["Belgium", "Haiti", "Monaco"]), ("E pluribus unum", "the USA", ["Mexico", "Cuba", "the Philippines"]),
 ("Dieu et mon droit", "the United Kingdom", ["Ireland", "Australia", "New Zealand"]), ("Nemo me impune lacessit", "Scotland", ["Ireland", "Northern Ireland", "the Isle of Man"]),
 ("Out of many, one people", "Jamaica", ["Barbados", "Trinidad and Tobago", "the Bahamas"]), ("Einigkeit und Recht und Freiheit", "Germany", ["Austria", "Liechtenstein", "Denmark"]),
 ("Je maintiendrai", "the Netherlands", ["Belgium", "Denmark", "Norway"]), ("Mir wëlle bleiwe wat mir sinn", "Luxembourg", ["Belgium", "Liechtenstein", "Austria"]),
 ("Ordem e Progresso", "Brazil", ["Portugal", "Argentina", "Angola"]), ("A mari usque ad mare (from sea to sea)", "Canada", ["Australia", "New Zealand", "Ireland"]),
 ("Bhinneka Tunggal Ika (unity in diversity)", "Indonesia", ["Malaysia", "the Philippines", "Thailand"]), ("Satyameva Jayate (truth alone triumphs)", "India", ["Nepal", "Sri Lanka", "Bangladesh"]),
 ("Unus pro omnibus, omnes pro uno", "Switzerland", ["Austria", "Liechtenstein", "Belgium"]), ("Plus ultra", "Spain", ["Portugal", "Italy", "Mexico"]),
 ("God, Homeland, King", "Morocco", ["Algeria", "Tunisia", "Egypt"]), ("!ke e: |xarra ||ke (diverse people unite)", "South Africa", ["Namibia", "Botswana", "Zimbabwe"]),
 ("Uhuru na Umoja (freedom and unity)", "Tanzania", ["Uganda", "Rwanda", "Malawi"]), ("Harambee (let's all pull together)", "Kenya", ["Uganda", "Ethiopia", "Malawi"]),
 ("Cymru am byth (Wales for ever)", "Wales", ["Ireland", "Cornwall", "the Isle of Man"]), ("Eleftheria i thanatos (freedom or death)", "Greece", ["Cyprus", "Bulgaria", "Albania"])])

race("which town or city is this famous statue in?", "Britain", "hard", ["statues", "towns"], [
 ("Robin Hood, below the castle", "Nottingham", ["Derby", "Leicester", "Sheffield"]), ("Peter Pan in Kensington Gardens", "London", ["Oxford", "Cambridge", "Brighton"]),
 ("Greyfriars Bobby", "Edinburgh", ["Glasgow", "Stirling", "Perth"]), ("Andy Capp", "Hartlepool", ["Middlesbrough", "Sunderland", "Darlington"]),
 ("Desperate Dan", "Dundee", ["Aberdeen", "Perth", "Glasgow"]), ("Lady Godiva on horseback", "Coventry", ["Warwick", "Leicester", "Northampton"]),
 ("Earl Grey, on top of his Monument", "Newcastle", ["Sunderland", "Durham", "Gateshead"]), ("Ken Dodd, at Lime Street station", "Liverpool", ["Southport", "St Helens", "Warrington"]),
 ("Freddie Mercury by Lake Geneva", "Montreux", ["Geneva", "Lausanne", "Zurich"]), ("The Little Mermaid", "Copenhagen", ["Oslo", "Stockholm", "Aarhus"]),
 ("Manneken Pis", "Brussels", ["Antwerp", "Bruges", "Ghent"]), ("Fred Dibnah", "Bolton", ["Wigan", "Preston", "Burnley"]),
 ("Victoria Wood", "Bury", ["Rochdale", "Oldham", "Wigan"]), ("Jimi Hendrix", "Seattle", ["Portland", "San Francisco", "Tacoma"]),
 ("Les Dawson", "Lytham St Annes", ["Blackpool", "Southport", "Fleetwood"]), ("Ronnie Barker", "Aylesbury", ["Oxford", "Reading", "Luton"]),
 ("Molly Malone", "Dublin", ["Cork", "Galway", "Belfast"]), ("Rocky Balboa", "Philadelphia", ["Boston", "Pittsburgh", "New York"]),
 ("Captain Mainwaring of Dad's Army", "Thetford", ["Norwich", "Ipswich", "Bury St Edmunds"]), ("Laurel and Hardy, side by side", "Ulverston", ["Bishop Auckland", "Kendal", "Barrow-in-Furness"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-61.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
