# Bank session 11 Oct 2026 (seventeenth pass): one more Match question each for 19 topics that had 7 live, checked against
# the live questions in each topic. Writes bank/topics/<slug>__m18.json; import each with FILE=<slug>__m18 TOPICS=<slug> LQ_PASSWORD=… node tools/import-bank.mjs topics
import json, os
OUT = {}
def m(slug, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.setdefault(slug, []).append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff})

m("music-lyrics", "easy", "Match each lyric or song title to the missing day",
  ("I don't like ___s", "Monday"), ("___ I'm in Love", "Friday"), ("Ruby ___", "Tuesday"), ("___ Bloody ___", "Sunday"))
m("the-1990s", "easy", "Match each 1990s boy band to one of its members",
  ("Take That", "Robbie Williams"), ("Boyzone", "Ronan Keating"), ("Westlife", "Shane Filan"), ("East 17", "Brian Harvey"))
m("the-2000s", "medium", "Match each 2000s sitcom to one of its stars",
  ("Peep Show", "David Mitchell"), ("Gavin & Stacey", "James Corden"), ("The Inbetweeners", "Simon Bird"), ("Extras", "Ricky Gervais"))
m("the-2010s", "easy", "Match each 2010s number one to its act",
  ("Shape of You", "Ed Sheeran"), ("Happy", "Pharrell Williams"), ("Uptown Funk", "Mark Ronson and Bruno Mars"), ("Someone You Loved", "Lewis Capaldi"))
m("20th-century", "medium", "Match each 20th-century first to its year",
  ("First powered aeroplane flight", "1903"), ("First FA Cup final at Wembley", "1923"), ("BBC starts its TV service", "1936"), ("First test-tube baby born", "1978"))
m("human-body", "medium", "Match each bone to where you'd find it",
  ("Femur", "Thigh"), ("Humerus", "Upper arm"), ("Mandible", "Jaw"), ("Tibia", "Shin"))
m("lord-of-the-rings", "medium", "Match each fantasy wizard to their story",
  ("Gandalf", "The Lord of the Rings"), ("Merlin", "The legend of King Arthur"), ("Rincewind", "Discworld"), ("Ged", "Earthsea"))
m("marvel", "easy", "Match each Marvel hero to their signature weapon",
  ("Thor", "Hammer"), ("Captain America", "Shield"), ("Hawkeye", "Bow and arrow"), ("Wolverine", "Claws"))
m("north-east-england", "medium", "Match each North East castle to what it's known for",
  ("Alnwick Castle", "Hogwarts in the Harry Potter films"), ("Bamburgh Castle", "Seat of the ancient kings of Northumbria"), ("Durham Castle", "A university college"), ("Dunstanburgh Castle", "Clifftop ruins on the coast path"))
m("the-office", "easy", "Match each character from the UK Office to the actor",
  ("David Brent", "Ricky Gervais"), ("Tim Canterbury", "Martin Freeman"), ("Gareth Keenan", "Mackenzie Crook"), ("Dawn Tinsley", "Lucy Davis"))
m("olympics", "medium", "Match each Olympian to their nickname",
  ("Usain Bolt", "Lightning Bolt"), ("Michael Phelps", "The Baltimore Bullet"), ("Eddie Edwards", "The Eagle"), ("Ian Thorpe", "The Thorpedo"))
m("oscars", "medium", "Match each actress to the film that won her Best Actress",
  ("Frances McDormand", "Fargo"), ("Emma Stone", "La La Land"), ("Olivia Colman", "The Favourite"), ("Julia Roberts", "Erin Brockovich"))
m("royal-family", "medium", "Match each royal to the year they were born",
  ("King Charles III", "1948"), ("Prince William", "1982"), ("Prince Harry", "1984"), ("Princess Charlotte", "2015"))
m("world-wars", "easy", "Match each wartime figure or poster to the famous words",
  ("Winston Churchill", "We shall fight on the beaches"), ("Neville Chamberlain", "Peace for our time"), ("Vera Lynn", "We'll meet again"), ("Lord Kitchener's poster", "Your country needs you"))
m("uk-geography", "medium", "Match each island to the part of the UK it belongs to",
  ("Anglesey", "Wales"), ("Arran", "Scotland"), ("Lundy", "England"), ("Rathlin Island", "Northern Ireland"))
m("number-ones", "medium", "Match each Christmas number one to its year",
  ("Do They Know It's Christmas?", "1984"), ("Mistletoe and Wine", "1988"), ("Mr Blobby", "1993"), ("Killing in the Name", "2009"))
m("video-games", "easy", "Match each game character to what kind of creature they are",
  ("Sonic", "Hedgehog"), ("Crash", "Bandicoot"), ("Spyro", "Dragon"), ("Yoshi", "Dinosaur"))
m("words-language", "easy", "Match each phobia to what it's a fear of",
  ("Arachnophobia", "Spiders"), ("Claustrophobia", "Tight, enclosed spaces"), ("Acrophobia", "Heights"), ("Agoraphobia", "Open or crowded places"))
m("world-geography", "easy", "Match each capital to the river that runs through it",
  ("Paris", "Seine"), ("Rome", "Tiber"), ("Budapest", "Danube"), ("Cairo", "Nile"))

here = os.path.dirname(os.path.abspath(__file__))
for slug, qs in OUT.items():
    json.dump(qs, open(os.path.join(here, '..', 'topics', slug + '__m18.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(sum(len(q) for q in OUT.values()), 'match questions written for', len(OUT), 'topics')
