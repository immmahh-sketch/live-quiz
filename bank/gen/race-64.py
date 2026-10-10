# Bank session 10 Oct 2026: 2 more general races -> bank/race-64.json. 20 rows each, target 10; wrong options are
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

race("which motorway?", "Britain", "hard", ["motorways", "roads"], [
 ("London to Leeds, the first full-length motorway", "M1", ["M10", "M45", "M69"]), ("The Medway towns of Kent to Faversham", "M2", ["M26", "M48", "M32"]),
 ("London to Southampton, past Winchester", "M3", ["M32", "M26", "M48"]), ("London to South Wales, via Reading and Swindon", "M4", ["M48", "M49", "M50"]),
 ("Birmingham to Exeter", "M5", ["M50", "M32", "M49"]), ("Rugby to Gretna, Britain's longest", "M6", ["M61", "M55", "M58"]),
 ("Edinburgh to Glasgow", "M8", ["M80", "M73", "M77"]), ("Edinburgh to Stirling", "M9", ["M80", "M876", "M73"]),
 ("London to Cambridge", "M11", ["M10", "M45", "M26"]), ("Rotherham to Goole", "M18", ["M180", "M181", "M621"]),
 ("London to Folkestone and the Channel Tunnel", "M20", ["M26", "M10", "M45"]), ("London to Crawley and Gatwick", "M23", ["M26", "M10", "M45"]),
 ("London's orbital motorway", "M25", ["M26", "M45", "M10"]), ("Southampton to Portsmouth", "M27", ["M271", "M275", "M32"]),
 ("London to Birmingham via Oxford", "M40", ["M42", "M45", "M69"]), ("Wolverhampton to Telford", "M54", ["M53", "M56", "M42"]),
 ("The ring road motorway around Manchester", "M60", ["M61", "M66", "M67"]), ("Liverpool to Hull, over the Pennines", "M62", ["M61", "M65", "M66"]),
 ("Glasgow to Gretna", "M74", ["M73", "M77", "M80"]), ("Edinburgh to Perth, over the Queensferry Crossing", "M90", ["M80", "M876", "M73"])])

race("which famous family?", "Famous people", "medium", ["families", "who's who"], [
 ("Kim, Khloé and Kourtney", "Kardashian", ["Jenner", "Richie", "Trump"]), ("Ozzy, Sharon, Kelly and Jack", "Osbourne", ["Richie", "Trump", "Jenner"]),
 ("Brooklyn, Romeo, Cruz and Harper", "Beckham", ["Rooney", "Lampard", "Owen"]), ("Michael, Janet, Tito and Jermaine", "Jackson", ["Osmond", "Knowles", "Carpenter"]),
 ("John, Robert and Ted, the American political brothers", "Kennedy", ["Bush", "Clinton", "Roosevelt"]), ("Charlotte, Emily, Anne and Branwell", "Brontë", ["Austen", "Mitford", "Shelley"]),
 ("Groucho, Harpo, Chico and Zeppo", "Marx", ["Ritz", "Warner", "Nicholas"]), ("Barry, Robin and Maurice", "Gibb", ["Everly", "Osmond", "Walker"]),
 ("Jack and Bobby, World Cup winners in 1966", "Charlton", ["Neville", "Ferdinand", "Lampard"]), ("Andy and Jamie, the tennis-playing brothers", "Murray", ["Henman", "Brownlee", "Bryan"]),
 ("Vanessa, Lynn and Corin, the acting dynasty", "Redgrave", ["Fiennes", "Attenborough", "Mills"]), ("Vito, Michael, Sonny and Fredo", "Corleone", ["Tattaglia", "Barzini", "Montana"]),
 ("Tony, Carmela, Meadow and A.J.", "Soprano", ["Moltisanti", "Montana", "Gambino"]), ("Frank, Fiona, Lip and Ian in Shameless", "Gallagher", ["Fisher", "Beale", "Battersby"]),
 ("Henry, Jane and Peter", "Fonda", ["Douglas", "Sheen", "Coppola"]), ("Phil, Grant and Peggy", "Mitchell", ["Beale", "Butcher", "Fowler"]),
 ("Ken, Deirdre, Peter and Tracy", "Barlow", ["Battersby", "Platt", "Webster"]), ("Zak, Cain, Charity and Marlon", "Dingle", ["Sugden", "Tate", "King"]),
 ("Alec, Stephen, William and Daniel, the acting brothers", "Baldwin", ["Wayans", "Affleck", "Hemsworth"]), ("Paris and Nicky, the hotel heiresses", "Hilton", ["Richie", "Trump", "Jenner"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-64.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
