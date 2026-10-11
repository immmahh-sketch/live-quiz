# Bank session 11 Oct 2026 (twelfth pass): one more Match question each for 15 more topics that had 7 live.
# Writes bank/topics/<slug>__m13.json; import each with FILE=<slug>__m13 TOPICS=<slug> LQ_PASSWORD=… node tools/import-bank.mjs topics
import json, os
OUT = {}
def m(slug, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.setdefault(slug, []).append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff})


m("british-films", "medium", "Match each British film to the year it came out",
  ("Four Weddings and a Funeral", "1994"), ("Trainspotting", "1996"), ("Billy Elliot", "2000"), ("The King's Speech", "2010"))
m("british-food", "easy", "Match each dish to its main ingredient",
  ("Bubble and squeak", "Leftover potato and cabbage"), ("Toad in the hole", "Sausages"), ("Cullen skink", "Smoked haddock"), ("Laverbread", "Seaweed"))
m("british-history", "easy", "Match each Prime Minister to a war they led Britain through",
  ("Winston Churchill", "The Second World War"), ("David Lloyd George", "The First World War"), ("Margaret Thatcher", "The Falklands War"), ("Tony Blair", "The Iraq War"))
m("british-sitcoms", "easy", "Match each sitcom character to their job",
  ("Basil Fawlty", "Hotel owner"), ("Del Boy", "Market trader"), ("David Brent", "Office manager at a paper company"), ("Father Ted", "Priest"))
m("capital-cities", "easy", "Match each capital to its famous landmark",
  ("Paris", "The Eiffel Tower"), ("Rome", "The Colosseum"), ("Athens", "The Acropolis"), ("Moscow", "Red Square"))
m("cars-motoring", "medium", "Match each car to the decade it was launched",
  ("Mini", "1950s"), ("Ford Capri", "1960s"), ("Ford Sierra", "1980s"), ("Ford Ka", "1990s"))
m("childrens-books", "easy", "Match each magical land to its book",
  ("Narnia", "The Lion, the Witch and the Wardrobe"), ("Neverland", "Peter Pan"), ("Wonderland", "Alice's Adventures in Wonderland"), ("Oz", "The Wonderful Wizard of Oz"))
m("kids-tv", "hard", "Match each children's show to its famous narrator",
  ("Thomas the Tank Engine", "Ringo Starr"), ("Paddington (1975)", "Michael Hordern"), ("Postman Pat", "Ken Barrie"), ("Roobarb", "Richard Briers"))
m("christmas", "easy", "Match each word for Christmas to its language",
  ("Noël", "French"), ("Navidad", "Spanish"), ("Weihnachten", "German"), ("Natale", "Italian"))
m("christmas-movies", "medium", "Match each Christmas film to the year it came out",
  ("It's a Wonderful Life", "1946"), ("Home Alone", "1990"), ("Elf", "2003"), ("The Holiday", "2006"))
m("christmas-music", "medium", "Match each Christmas song to the film it comes from",
  ("White Christmas", "Holiday Inn"), ("Walking in the Air", "The Snowman"), ("Christmas Is All Around", "Love Actually"), ("Somewhere in My Memory", "Home Alone"))
m("crime-dramas", "easy", "Match each TV detective to the place they work",
  ("Inspector Morse", "Oxford"), ("Rebus", "Edinburgh"), ("Vera", "Northumberland"), ("Taggart", "Glasgow"))
m("classical-music", "hard", "Match each composer to how many symphonies they wrote",
  ("Haydn", "104"), ("Mozart", "41"), ("Beethoven", "9"), ("Brahms", "4"))
m("computers-internet", "medium", "Match each website to the year it launched",
  ("Google", "1998"), ("Facebook", "2004"), ("YouTube", "2005"), ("Twitter", "2006"))
m("cricket", "easy", "Match each cricket legend to his country",
  ("Brian Lara", "West Indies"), ("Sachin Tendulkar", "India"), ("Shane Warne", "Australia"), ("Muttiah Muralitharan", "Sri Lanka"))

here = os.path.dirname(os.path.abspath(__file__))
for slug, qs in OUT.items():
    json.dump(qs, open(os.path.join(here, '..', 'topics', slug + '__m13.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(sum(len(q) for q in OUT.values()), 'match questions written for', len(OUT), 'topics')
