# Bank session 11 Oct 2026 (fourteenth pass): one more Match question each for 15 more topics that had 7 live.
# Writes bank/topics/<slug>__m15.json; import each with FILE=<slug>__m15 TOPICS=<slug> LQ_PASSWORD=… node tools/import-bank.mjs topics
import json, os
OUT = {}
def m(slug, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.setdefault(slug, []).append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff})


m("game-of-thrones", "medium", "Match each Westeros castle to the house that rules it",
  ("Winterfell", "Stark"), ("Casterly Rock", "Lannister"), ("Highgarden", "Tyrell"), ("Sunspear", "Martell"))
m("halloween", "easy", "Match each horror villain to their film",
  ("Michael Myers", "Halloween"), ("Freddy Krueger", "A Nightmare on Elm Street"), ("Jason Voorhees", "Friday the 13th"), ("Ghostface", "Scream"))
m("halloween-music", "medium", "Match each spooky song or tune to its film",
  ("Time Warp", "The Rocky Horror Picture Show"), ("This Is Halloween", "The Nightmare Before Christmas"), ("Tubular Bells", "The Exorcist"), ("I Put a Spell on You", "Hocus Pocus"))
m("harry-potter", "medium", "Match each Hogwarts ghost to their house",
  ("Nearly Headless Nick", "Gryffindor"), ("The Bloody Baron", "Slytherin"), ("The Fat Friar", "Hufflepuff"), ("The Grey Lady", "Ravenclaw"))
m("horse-racing", "medium", "Match each racecourse to its county",
  ("Aintree", "Merseyside"), ("Ascot", "Berkshire"), ("Cheltenham", "Gloucestershire"), ("Newmarket", "Suffolk"))
m("ireland", "medium", "Match each city to its Irish province",
  ("Dublin", "Leinster"), ("Cork", "Munster"), ("Galway", "Connacht"), ("Belfast", "Ulster"))
m("james-bond", "medium", "Match each Bond film to the year it came out",
  ("Dr. No", "1962"), ("Goldfinger", "1964"), ("GoldenEye", "1995"), ("Skyfall", "2012"))
m("london", "medium", "Match each London park to something you'll find there",
  ("Hyde Park", "Speakers' Corner"), ("Regent's Park", "London Zoo"), ("Greenwich Park", "The Royal Observatory"), ("Richmond Park", "Wild deer"))
m("maths-numbers", "easy", "Match each number to its special name",
  ("12", "A dozen"), ("13", "A baker's dozen"), ("20", "A score"), ("144", "A gross"))
m("motorsport", "medium", "Match each famous race to its country",
  ("Le Mans 24 Hours", "France"), ("Indianapolis 500", "USA"), ("Bathurst 1000", "Australia"), ("Monte Carlo Rally", "Monaco"))
m("musicals", "medium", "Match each musical to its leading character",
  ("Les Misérables", "Jean Valjean"), ("Wicked", "Elphaba"), ("Miss Saigon", "Kim"), ("The Phantom of the Opera", "Christine Daaé"))
m("mythology", "easy", "Match each Greek monster to the hero who beat it",
  ("Medusa", "Perseus"), ("The Minotaur", "Theseus"), ("The Hydra", "Heracles"), ("Polyphemus the Cyclops", "Odysseus"))
m("nature-environment", "easy", "Match each animal to its main food",
  ("Giant panda", "Bamboo"), ("Koala", "Eucalyptus leaves"), ("Anteater", "Ants and termites"), ("Blue whale", "Krill"))
m("new-year", "easy", "Match each New Year word to its meaning",
  ("Hogmanay", "Scotland's New Year's Eve"), ("First-footing", "Being the first visitor after midnight"), ("Auld Lang Syne", "Days long gone"), ("Resolution", "A promise to change"))
m("newcastle-v-sunderland", "medium", "Match each club to its fans' nickname",
  ("Newcastle United", "The Toon Army"), ("Sunderland", "Mackems"), ("Middlesbrough", "Smoggies"), ("Hartlepool United", "Monkey Hangers"))

here = os.path.dirname(os.path.abspath(__file__))
for slug, qs in OUT.items():
    json.dump(qs, open(os.path.join(here, '..', 'topics', slug + '__m15.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(sum(len(q) for q in OUT.values()), 'match questions written for', len(OUT), 'topics')
