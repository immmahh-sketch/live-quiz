# Bank session 11 Oct 2026 (eleventh pass): one more Match question each for 15 topics that had 6 or 7 live.
# Writes bank/topics/<slug>__m12.json; import each with FILE=<slug>__m12 TOPICS=<slug> LQ_PASSWORD=… node tools/import-bank.mjs topics
import json, os
OUT = {}
def m(slug, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.setdefault(slug, []).append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff})


m("music-lyrics", "easy", "Match each lyric to the number that's missing",
  ("I would walk ___ miles", "500"), ("___ red balloons", "99"), ("Back in the summer of '__", "69"), ("___ days a week, I love you", "8"))
m("action-films", "medium", "Match each action film to the place that gets taken over",
  ("Die Hard", "Nakatomi Plaza"), ("Speed", "A city bus"), ("Air Force One", "The President's plane"), ("The Rock", "Alcatraz"))
m("us-tv", "medium", "Match each TV family to its show",
  ("The Bluths", "Arrested Development"), ("The Dunphys", "Modern Family"), ("The Bundys", "Married... with Children"), ("The Bankses", "The Fresh Prince of Bel-Air"))
m("anagrams-wordplay", "easy", "Match each thing to the letter that sounds like it",
  ("A hot drink", "T"), ("A green vegetable", "P"), ("A buzzing insect", "B"), ("Where fish live", "C"))
m("ancient-history", "medium", "Match each pharaoh to what he's remembered for",
  ("Tutankhamun", "A tomb found almost untouched in 1922"), ("Ramesses II", "The giant temples at Abu Simbel"), ("Khufu", "The Great Pyramid of Giza"), ("Akhenaten", "Worshipping a single sun god, the Aten"))
m("animals", "easy", "Match each creature to how many legs or arms it has",
  ("Spider", "8"), ("Ant", "6"), ("Lobster", "10"), ("Starfish", "5"))
m("pixar-animation", "medium", "Match each Pixar film to the year it came out",
  ("Toy Story", "1995"), ("Finding Nemo", "2003"), ("Up", "2009"), ("Inside Out", "2015"))
m("art", "easy", "Match each artist to what they loved to paint",
  ("Claude Monet", "Water lilies"), ("Edgar Degas", "Ballet dancers"), ("George Stubbs", "Horses"), ("L. S. Lowry", "Matchstick figures in mill towns"))
m("australia", "medium", "Match each Australian landmark to its state or territory",
  ("Uluru", "Northern Territory"), ("Great Barrier Reef", "Queensland"), ("Sydney Opera House", "New South Wales"), ("The Twelve Apostles", "Victoria"))
m("beer-wine-spirits", "easy", "Match each spirit to its home country",
  ("Ouzo", "Greece"), ("Sake", "Japan"), ("Tequila", "Mexico"), ("Grappa", "Italy"))
m("bonfire-night", "easy", "Match each autumn festival to its country",
  ("Diwali", "India"), ("Thanksgiving", "USA"), ("Day of the Dead", "Mexico"), ("Oktoberfest", "Germany"))
m("books", "medium", "Match each novel to the character who tells the story",
  ("Moby-Dick", "Ishmael"), ("The Great Gatsby", "Nick Carraway"), ("Treasure Island", "Jim Hawkins"), ("To Kill a Mockingbird", "Scout Finch"))
m("boxing-combat", "medium", "Match each British boxer to his home town",
  ("Ricky Hatton", "Manchester"), ("Anthony Joshua", "Watford"), ("Joe Calzaghe", "Newbridge"), ("Amir Khan", "Bolton"))
m("boy-bands-girl-groups", "medium", "Match each group to how it was put together",
  ("One Direction", "The X Factor"), ("Girls Aloud", "Popstars: The Rivals"), ("Hear'Say", "Popstars"), ("Spice Girls", "An advert in The Stage newspaper"))
m("brands-logos", "easy", "Match each brand to its slogan",
  ("Nike", "Just Do It"), ("L'Oréal", "Because you're worth it"), ("Carlsberg", "Probably the best lager in the world"), ("Tesco", "Every little helps"))

here = os.path.dirname(os.path.abspath(__file__))
for slug, qs in OUT.items():
    json.dump(qs, open(os.path.join(here, '..', 'topics', slug + '__m12.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(sum(len(q) for q in OUT.values()), 'match questions written for', len(OUT), 'topics')
