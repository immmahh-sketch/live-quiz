# Bank session 10 Oct 2026: 2 more general races -> bank/race-105.json (famous graves, universities). 20 rows each, target 10; wrong options are
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

race("where is this famous person buried?", "History", "hard", ["graves", "famous people", "history"], [
 ("Karl Marx", "Highgate Cemetery", ["Kensal Green Cemetery", "Brompton Cemetery", "Golders Green"]),
 ("Jim Morrison of the Doors", "Père Lachaise, Paris", ["Montmartre Cemetery", "Hollywood Forever", "Montparnasse"]),
 ("Elvis Presley", "Graceland", ["Forest Lawn", "Sun Studio", "Hollywood Forever"]),
 ("William Shakespeare", "Holy Trinity Church, Stratford", ["Southwark Cathedral", "St Giles' Cathedral", "Canterbury Cathedral"]),
 ("Winston Churchill", "Bladon churchyard", ["Chartwell", "Blenheim Palace", "Hampstead"]),
 ("Diana, Princess of Wales", "Althorp", ["Sandringham", "Kensington Palace", "Balmoral"]),
 ("Richard III, after being found under a car park", "Leicester Cathedral", ["York Minster", "Bosworth Field", "Fotheringhay"]),
 ("Admiral Lord Nelson", "St Paul's Cathedral", ["Greenwich", "Portsmouth Cathedral", "Trafalgar Square"]),
 ("Isaac Newton", "Westminster Abbey", ["Trinity College, Cambridge", "Woolsthorpe Manor", "Southwark Cathedral"]),
 ("Henry VIII", "St George's Chapel, Windsor", ["Hampton Court", "Canterbury Cathedral", "The Tower of London"]),
 ("Napoleon", "Les Invalides, Paris", ["Notre-Dame", "The Panthéon", "Versailles"]),
 ("John F. Kennedy", "Arlington National Cemetery", ["Dallas", "Boston", "Hyannis Port"]),
 ("Lenin, embalmed in a mausoleum", "Red Square, Moscow", ["Novodevichy Cemetery", "St Petersburg", "Volgograd"]),
 ("Robert the Bruce's body", "Dunfermline Abbey", ["Scone Palace", "Stirling Castle", "Iona"]),
 ("Robert Burns", "Dumfries", ["Alloway", "Ayr", "Edinburgh"]),
 ("Grace Darling, the lighthouse heroine", "Bamburgh", ["Seahouses", "The Farne Islands", "Whitby"]),
 ("Charlotte and Emily Brontë", "Haworth", ["Scarborough", "Thornton", "York"]),
 ("The Venerable Bede", "Durham Cathedral", ["Jarrow", "Lindisfarne", "Whitby Abbey"]),
 ("Jane Austen", "Winchester Cathedral", ["Bath Abbey", "Chawton", "Salisbury Cathedral"]),
 ("Dylan Thomas", "Laugharne", ["Swansea", "Cardiff", "New York"])])

race("which country is this famous university in?", "World geography", "medium", ["universities", "countries"], [
 ("Harvard", "The USA", ["Mexico", "England", "Scotland"]),
 ("Sciences Po", "France", ["Greece", "Austria", "Hungary"]),
 ("Trinity College, home of the Book of Kells", "Ireland", ["Scotland", "Wales", "England"]),
 ("Heidelberg", "Germany", ["Austria", "Luxembourg", "Hungary"]),
 ("Bologna, the oldest university in the world", "Italy", ["Greece", "Malta", "Austria"]),
 ("Salamanca", "Spain", ["Mexico", "Argentina", "Chile"]),
 ("Leiden", "The Netherlands", ["Luxembourg", "Austria", "Norway"]),
 ("Uppsala", "Sweden", ["Norway", "Finland", "Iceland"]),
 ("KU Leuven", "Belgium", ["Luxembourg", "Austria", "Hungary"]),
 ("ETH, where Einstein studied", "Switzerland", ["Austria", "Hungary", "Liechtenstein"]),
 ("Todai, the University of Tokyo", "Japan", ["Malaysia", "Thailand", "Vietnam"]),
 ("NUS, the National University", "Singapore", ["Malaysia", "Indonesia", "Thailand"]),
 ("McMaster", "Canada", ["Scotland", "England", "Mexico"]),
 ("Monash", "Australia", ["England", "Scotland", "Malaysia"]),
 ("Otago", "New Zealand", ["Scotland", "Wales", "Fiji"]),
 ("Wits, in Johannesburg", "South Africa", ["Kenya", "Nigeria", "Morocco"]),
 ("Al-Azhar, in Cairo", "Egypt", ["Turkey", "Morocco", "Israel"]),
 ("Aarhus", "Denmark", ["Norway", "Iceland", "Finland"]),
 ("Coimbra", "Portugal", ["Brazil", "Greece", "Malta"]),
 ("KAIST", "South Korea", ["Malaysia", "Thailand", "Vietnam"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-105.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
