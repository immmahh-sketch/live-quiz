# Bank session 11 Oct 2026 (fifteenth pass): one more Match question each for 15 more topics that had 7 live.
# Writes bank/topics/<slug>__m16.json; import each with FILE=<slug>__m16 TOPICS=<slug> LQ_PASSWORD=… node tools/import-bank.mjs topics
import json, os
OUT = {}
def m(slug, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.setdefault(slug, []).append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff})


m("space", "hard", "Match each space telescope to the year it was launched",
  ("Hubble", "1990"), ("Spitzer", "2003"), ("Kepler", "2009"), ("James Webb", "2021"))
m("pop-music", "medium", "Match each singer to their home town",
  ("Ed Sheeran", "Framlingham"), ("Adele", "Tottenham"), ("Lewis Capaldi", "Bathgate"), ("Sam Fender", "North Shields"))
m("star-wars", "medium", "Match each character to their home planet",
  ("Luke Skywalker", "Tatooine"), ("Princess Leia", "Alderaan"), ("Chewbacca", "Kashyyyk"), ("Padmé Amidala", "Naboo"))
m("reality-tv", "easy", "Match each 'Great British' contest to its craft",
  ("The Great British Bake Off", "Baking"), ("The Great Pottery Throw Down", "Pottery"), ("The Great British Sewing Bee", "Sewing"), ("MasterChef", "Cooking"))
m("record-breakers", "easy", "Match each skyscraper to its city",
  ("Burj Khalifa", "Dubai"), ("Shanghai Tower", "Shanghai"), ("The Shard", "London"), ("Petronas Towers", "Kuala Lumpur"))
m("religion-festivals", "easy", "Match each place of worship to its faith",
  ("Church", "Christianity"), ("Mosque", "Islam"), ("Synagogue", "Judaism"), ("Gurdwara", "Sikhism"))
m("rock-music", "medium", "Match each classic rock album to its band",
  ("Nevermind", "Nirvana"), ("Rumours", "Fleetwood Mac"), ("Back in Black", "AC/DC"), ("Appetite for Destruction", "Guns N' Roses"))
m("rom-coms", "medium", "Match each rom-com to the year it came out",
  ("Pretty Woman", "1990"), ("Four Weddings and a Funeral", "1994"), ("Notting Hill", "1999"), ("Love Actually", "2003"))
m("rugby", "hard", "Match each rugby ground to its club",
  ("Welford Road", "Leicester Tigers"), ("Kingsholm", "Gloucester"), ("The Rec", "Bath"), ("Sandy Park", "Exeter Chiefs"))
m("science-technology", "medium", "Match each invention to the century it appeared",
  ("The printing press", "15th century"), ("James Watt's steam engine", "18th century"), ("The telephone", "19th century"), ("The World Wide Web", "20th century"))
m("scotland", "medium", "Match each Scottish city to its nickname",
  ("Edinburgh", "Auld Reekie"), ("Aberdeen", "The Granite City"), ("Dundee", "City of Discovery"), ("Glasgow", "Dear Green Place"))
m("shakespeare", "hard", "Match each play to a famous prop or stage direction",
  ("The Winter's Tale", "Exit, pursued by a bear"), ("Hamlet", "Yorick's skull"), ("Macbeth", "A floating dagger"), ("Othello", "A lost handkerchief"))
m("soaps", "medium", "Match each soap to the year it began",
  ("Coronation Street", "1960"), ("Emmerdale", "1972"), ("EastEnders", "1985"), ("Hollyoaks", "1995"))

here = os.path.dirname(os.path.abspath(__file__))
for slug, qs in OUT.items():
    json.dump(qs, open(os.path.join(here, '..', 'topics', slug + '__m16.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(sum(len(q) for q in OUT.values()), 'match questions written for', len(OUT), 'topics')
