# Bank session 10 Oct 2026 (ninth pass): 1-2 more Match questions for 9 topics that had 5 or 6 live.
# Writes bank/topics/<slug>__m10.json; import each with FILE=<slug>__m10 TOPICS=<slug> LQ_PASSWORD=… node tools/import-bank.mjs topics
import json, os
OUT = {}
def m(slug, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.setdefault(slug, []).append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff})


m("christmas-tv", "medium", "Match each famous Christmas Day TV moment to its show",
  ("Den hands Angie divorce papers", "EastEnders"), ("Del Boy and Rodney finally become millionaires", "Only Fools and Horses"), ("Nessa proposes to Smithy", "Gavin & Stacey"), ("André Previn plays 'all the right notes'", "The Morecambe & Wise Show"))

m("disney", "medium", "Match each Disney heroine to where her film is set",
  ("Mulan", "China"), ("Merida", "Scotland"), ("Belle", "France"), ("Pocahontas", "Virginia"))
m("disney", "easy", "Match each character to the star who voiced them",
  ("The Genie", "Robin Williams"), ("Woody", "Tom Hanks"), ("Olaf", "Josh Gad"), ("Scar", "Jeremy Irons"))

m("food-drink", "medium", "Match each Indian dish to what it is",
  ("Korma", "A mild, creamy curry"), ("Vindaloo", "A fiery hot curry from Goa"), ("Dhal", "A lentil stew"), ("Naan", "A leavened flatbread"))
m("food-drink", "hard", "Match each beer style to the country it comes from",
  ("Pilsner", "Czech Republic"), ("Stout", "Ireland"), ("Hefeweizen", "Germany"), ("Trappist ale", "Belgium"))

m("horror-films", "medium", "Match each haunted address or hotel to its film",
  ("The Overlook Hotel", "The Shining"), ("The Bates Motel", "Psycho"), ("112 Ocean Avenue", "The Amityville Horror"), ("1428 Elm Street", "A Nightmare on Elm Street"))
m("horror-films", "medium", "Match each final girl to her film",
  ("Laurie Strode", "Halloween"), ("Sidney Prescott", "Scream"), ("Ellen Ripley", "Alien"), ("Clarice Starling", "The Silence of the Lambs"))

m("tennis-golf", "medium", "Match each Wimbledon champion to the year of their first singles title there",
  ("Roger Federer", "2003"), ("Rafael Nadal", "2008"), ("Novak Djokovic", "2011"), ("Andy Murray", "2013"))
m("tennis-golf", "medium", "Match each golf major to the month it's usually played",
  ("The Masters", "April"), ("PGA Championship", "May"), ("US Open", "June"), ("The Open", "July"))

m("the-1980s", "easy", "Match each 1980s toy craze to what it was",
  ("Rubik's Cube", "A twisting colour puzzle"), ("Cabbage Patch Kids", "Dolls that came with adoption papers"), ("Transformers", "Robots that turn into vehicles"), ("Care Bears", "Cuddly bears with a symbol on the tummy"))
m("the-1980s", "medium", "Match each 1980s TV show to its famous wheels",
  ("Knight Rider", "KITT, a talking Pontiac Trans Am"), ("The A-Team", "A black GMC van"), ("Magnum, P.I.", "A red Ferrari 308"), ("The Dukes of Hazzard", "The General Lee"))

m("usa", "easy", "Match each US city to its state",
  ("Las Vegas", "Nevada"), ("Miami", "Florida"), ("Seattle", "Washington"), ("New Orleans", "Louisiana"))
m("usa", "medium", "Match each national park to its state",
  ("Yellowstone", "Wyoming"), ("Grand Canyon", "Arizona"), ("Yosemite", "California"), ("Everglades", "Florida"))

m("breaking-bad", "easy", "Match each Breaking Bad character to the actor",
  ("Walter White", "Bryan Cranston"), ("Jesse Pinkman", "Aaron Paul"), ("Saul Goodman", "Bob Odenkirk"), ("Gus Fring", "Giancarlo Esposito"))

m("name-the-year", "hard", "Match each communication milestone to its year",
  ("The Penny Black stamp", "1840"), ("Bell's telephone patent", "1876"), ("Baird's first television demonstration", "1926"), ("The first iPhone", "2007"))
m("name-the-year", "medium", "Match each London landmark to the year it opened",
  ("Big Ben's clock tower", "1859"), ("Tower Bridge", "1894"), ("The London Eye", "2000"), ("The Shard", "2012"))

here = os.path.dirname(os.path.abspath(__file__))
for slug, items in OUT.items():
    json.dump(items, open(os.path.join(here, '..', 'topics', slug + '__m10.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(sum(map(len, OUT.values())), 'matches in', len(OUT), 'topics:', ' '.join(OUT))
