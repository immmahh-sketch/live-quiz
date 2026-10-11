# Bank session 11 Oct 2026 (thirteenth pass): one more Match question each for 15 more topics that had 7 live.
# Writes bank/topics/<slug>__m14.json; import each with FILE=<slug>__m14 TOPICS=<slug> LQ_PASSWORD=… node tools/import-bank.mjs topics
import json, os
OUT = {}
def m(slug, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.setdefault(slug, []).append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff})


m("days-that-shook-the-world", "easy", "Match each famous line to the leader who said it",
  ("I have a dream", "Martin Luther King"), ("We shall fight on the beaches", "Winston Churchill"), ("Ich bin ein Berliner", "John F. Kennedy"), ("The lady's not for turning", "Margaret Thatcher"))
m("dc-batman", "easy", "Match each Batman villain to their trademark",
  ("The Riddler", "Question-mark puzzles"), ("Two-Face", "Flipping a coin"), ("Mr Freeze", "An ice gun"), ("Poison Ivy", "Deadly plants"))
m("games-toys", "medium", "Match each toy to the decade it first went on sale",
  ("Barbie", "1950s"), ("Rubik's Cube", "1970s"), ("Cabbage Patch Kids", "1980s"), ("Tamagotchi", "1990s"))
m("doctor-who", "easy", "Match each monster to its famous cry",
  ("Daleks", "Exterminate!"), ("Cybermen", "Delete!"), ("Sontarans", "Sontar-ha!"), ("Weeping Angels", "Don't blink"))
m("easter-spring", "easy", "Match each spring date to what it marks",
  ("1 March", "St David's Day"), ("1 April", "April Fools' Day"), ("23 April", "St George's Day"), ("1 May", "May Day"))
m("europe", "medium", "Match each country to its money before the euro",
  ("France", "Franc"), ("Germany", "Deutschmark"), ("Italy", "Lira"), ("Spain", "Peseta"))
m("eurovision", "medium", "Match each UK Eurovision winner to their year",
  ("Sandie Shaw", "1967"), ("Brotherhood of Man", "1976"), ("Bucks Fizz", "1981"), ("Katrina and the Waves", "1997"))
m("famous-firsts", "hard", "Match each famous first to where it happened",
  ("The first powered flight", "Kitty Hawk"), ("The first test-tube baby", "Oldham"), ("The first public steam railway", "Stockton-on-Tees"), ("The first four-minute mile", "Oxford"))
m("landmarks", "medium", "Match each ancient wonder to its country",
  ("Petra", "Jordan"), ("Angkor Wat", "Cambodia"), ("Machu Picchu", "Peru"), ("Chichén Itzá", "Mexico"))
m("famous-people", "easy", "Match each famous figure to their nickname",
  ("Florence Nightingale", "The Lady with the Lamp"), ("Margaret Thatcher", "The Iron Lady"), ("Elvis Presley", "The King"), ("The Duke of Wellington", "The Iron Duke"))
m("fashion", "easy", "Match each designer to their home country",
  ("Coco Chanel", "France"), ("Giorgio Armani", "Italy"), ("Vivienne Westwood", "England"), ("Calvin Klein", "USA"))
m("film-quotes", "easy", "Match each 1980s line to its film",
  ("E.T. phone home", "E.T. the Extra-Terrestrial"), ("Nobody puts Baby in a corner", "Dirty Dancing"), ("I'll be back", "The Terminator"), ("Where we're going, we don't need roads", "Back to the Future"))
m("flags", "medium", "Match each country to the symbol on its flag",
  ("Canada", "A maple leaf"), ("Lebanon", "A cedar tree"), ("Cyprus", "A map of the island"), ("Brazil", "A starry globe"))
m("football", "medium", "Match each football nickname to its owner",
  ("Gazza", "Paul Gascoigne"), ("Psycho", "Stuart Pearce"), ("The Special One", "José Mourinho"), ("Supermac", "Malcolm Macdonald"))
m("friends", "medium", "Match each Friend to one of their siblings",
  ("Ross", "Monica"), ("Phoebe", "Ursula"), ("Rachel", "Jill"), ("Joey", "Gina"))

here = os.path.dirname(os.path.abspath(__file__))
for slug, qs in OUT.items():
    json.dump(qs, open(os.path.join(here, '..', 'topics', slug + '__m14.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(sum(len(q) for q in OUT.values()), 'match questions written for', len(OUT), 'topics')
