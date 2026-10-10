# Bank session 10 Oct 2026: 2 more general races -> bank/race-71.json. 20 rows each, target 10; wrong options are
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

race("which famous 'Palace'?", "General knowledge", "hard", ["palaces", "wordplay"], [
 ("The football club named after the Great Exhibition's glass hall", "Crystal", ["Glass", "Diamond", "Silver"]), ("The King's London home, with the famous balcony", "Buckingham", ["Clarence", "Marlborough", "Lancaster"]),
 ("Diana's home, now William and Catherine's London office", "Kensington", ["Holland", "Chelsea", "Richmond"]), ("Churchill's birthplace in Oxfordshire", "Blenheim", ["Woodstock", "Ditchley", "Chartwell"]),
 ("Henry VIII's Thames-side palace with the famous maze", "Hampton Court", ["Richmond", "Greenwich", "Nonsuch"]), ("The Pall Mall palace where a new monarch is proclaimed", "St James's", ["Whitehall", "Marlborough", "Clarence"]),
 ("The Archbishop of Canterbury's London home", "Lambeth", ["Fulham", "Southwark", "Westminster"]), ("'Ally Pally', home of the World Darts Championship", "Alexandra", ["Victoria", "Albert", "Olympia"]),
 ("The Roman-themed Las Vegas casino", "Caesars", ["Bellagio", "Venetian", "Luxor"]), ("The St Petersburg palace stormed in 1917", "Winter", ["Catherine", "Peterhof", "Smolny"]),
 ("Beijing's imperial lakeside retreat", "Summer", ["Forbidden", "Jade", "Heavenly"]), ("The Dalai Lama's great palace in Lhasa", "Potala", ["Jokhang", "Norbulingka", "Drepung"]),
 ("Istanbul's sultans' palace, home of the Spoonmaker's Diamond", "Topkapi", ["Dolmabahçe", "Galata", "Yildiz"]), ("Vienna's Habsburg summer palace", "Schönbrunn", ["Hofburg", "Belvedere", "Nymphenburg"]),
 ("Venice's palace beside St Mark's Basilica", "Doge's", ["Rialto", "Ca' d'Oro", "Pope's"]), ("Birthplace of Mary, Queen of Scots", "Linlithgow", ["Falkland", "Stirling", "Holyrood"]),
 ("Henry VIII's boyhood palace in south-east London, with its Art Deco house", "Eltham", ["Greenwich", "Richmond", "Nonsuch"]), ("Frederick the Great's rococo palace at Potsdam", "Sanssouci", ["Charlottenburg", "Bellevue", "Nymphenburg"]),
 ("Sintra's brightly painted hilltop palace", "Pena", ["Ajuda", "Queluz", "Belém"]), ("The Paris palace beside the Louvre, burned down in 1871", "Tuileries", ["Luxembourg", "Élysée", "Palais-Royal"])])

race("which famous 'Garden'?", "General knowledge", "medium", ["gardens", "wordplay"], [
 ("The London piazza with the Royal Opera House", "Covent", ["Spitalfields", "Leadenhall", "Smithfield"]), ("London's diamond quarter, scene of the 2015 vault raid", "Hatton", ["Holborn", "Leather", "Clerkenwell"]),
 ("The Royal Botanic Gardens in south-west London", "Kew", ["Chiswick", "Syon", "Richmond"]), ("Adam and Eve's garden", "Eden", ["Babylon", "Avalon", "Arcadia"]),
 ("Ringo's song about life under the sea", "Octopus's", ["Walrus's", "Dolphin's", "Mermaid's"]), ("Frances Hodgson Burnett's novel about Mary Lennox", "Secret", ["Hidden", "Forbidden", "Lost"]),
 ("Where Peter Pan's statue stands in London", "Kensington", ["Holland", "Regent's", "Chelsea"]), ("The Wonder of the Ancient World in Babylon", "Hanging", ["Floating", "Terraced", "Royal"]),
 ("Where pub-goers drink outside in summer", "Beer", ["Ale", "Pub", "Drinking"]), ("Cornwall's 'Lost Gardens', rediscovered in 1990", "Heligan", ["Trebah", "Glendurgan", "Trelissick"]),
 ("Where Jesus prayed on the night of his arrest", "Gethsemane", ["Olives", "Golgotha", "Bethany"]), ("The White House garden used for big announcements", "Rose", ["Lily", "Tulip", "East"]),
 ("Blackpool's huge Victorian venue for party conferences and shows", "Winter", ["Spring", "Summer", "Pleasure"]), ("Edinburgh's park in the valley below the Castle", "Princes Street", ["George Street", "Royal Mile", "Queen Street"]),
 ("Copenhagen's amusement park, opened in 1843", "Tivoli", ["Bakken", "Legoland", "Liseberg"]), ("Chelsea's 1673 garden for growing medicinal plants", "Physic", ["Herb", "Apothecaries'", "Healing"]),
 ("The Goodie who still pops up on I'm Sorry I Haven't a Clue", "Graeme", ["Bill", "Tim", "Barry"]), ("A farm growing fruit and veg for sale", "Market", ["Kitchen", "Allotment", "Truck"]),
 ("The Northumberland garden with the Poison Garden and Grand Cascade", "Alnwick", ["Belsay", "Wallington", "Howick"]), ("The crammed, informal English style of flower garden", "Cottage", ["Country", "Village", "Farmhouse"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-71.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
