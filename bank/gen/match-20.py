# Bank session 11 Oct 2026 (nineteenth pass): one more Match question each for 20 topics on 8 live, checked against
# the live questions in each topic. Writes bank/topics/<slug>__m20.json; import each with FILE=<slug>__m20 TOPICS=<slug> LQ_PASSWORD=… node tools/import-bank.mjs topics
import json, os
OUT = {}
def m(slug, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.setdefault(slug, []).append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff})

m("anagrams-wordplay", "medium", "Match each word to the word it makes spelled backwards",
  ("Stressed", "Desserts"), ("Diaper", "Repaid"), ("Drawer", "Reward"), ("Live", "Evil"))
m("ancient-history", "medium", "Match each Roman god to their Greek equivalent",
  ("Jupiter", "Zeus"), ("Venus", "Aphrodite"), ("Mars", "Ares"), ("Neptune", "Poseidon"))
m("animals", "easy", "Match each animal to the name for the female",
  ("Sheep", "Ewe"), ("Horse", "Mare"), ("Fox", "Vixen"), ("Pig", "Sow"))
m("books", "medium", "Match each Russian classic to its author",
  ("War and Peace", "Leo Tolstoy"), ("Crime and Punishment", "Fyodor Dostoevsky"), ("Doctor Zhivago", "Boris Pasternak"), ("Eugene Onegin", "Alexander Pushkin"))
m("british-films", "medium", "Match each Carry On film to what it sends up",
  ("Carry On Nurse", "Hospital life"), ("Carry On Camping", "A holiday campsite"), ("Carry On Up the Khyber", "The British in India"), ("Carry On Screaming!", "Horror films"))
m("british-history", "easy", "Match each English king to his nickname",
  ("Richard I", "The Lionheart"), ("Edward I", "Longshanks"), ("Æthelred", "The Unready"), ("William I", "The Conqueror"))
m("british-sitcoms", "medium", "Match each sitcom to the year it began",
  ("Fawlty Towers", "1975"), ("Only Fools and Horses", "1981"), ("Father Ted", "1995"), ("The Office", "2001"))
m("childrens-books", "medium", "Match each character to their home",
  ("Paddington", "32 Windsor Gardens"), ("Winnie-the-Pooh", "The Hundred Acre Wood"), ("The Borrowers", "Under the floorboards"), ("The Moomins", "Moominvalley"))
m("christmas", "easy", "Match each day of Christmas to its gift in the song",
  ("First day", "A partridge in a pear tree"), ("Fifth day", "Five gold rings"), ("Eighth day", "Eight maids a-milking"), ("Twelfth day", "Twelve drummers drumming"))
m("christmas-movies", "medium", "Match each Christmas film to its villain",
  ("Home Alone", "Harry and Marv"), ("Die Hard", "Hans Gruber"), ("It's a Wonderful Life", "Mr Potter"), ("Gremlins", "Stripe"))
m("christmas-music", "easy", "Match each Christmas classic to the crooner most linked with it",
  ("White Christmas", "Bing Crosby"), ("Let It Snow!", "Dean Martin"), ("The Christmas Song", "Nat King Cole"), ("Blue Christmas", "Elvis Presley"))
m("classical-music", "medium", "Match each ballet to its composer",
  ("Swan Lake", "Tchaikovsky"), ("The Rite of Spring", "Stravinsky"), ("Romeo and Juliet", "Prokofiev"), ("Giselle", "Adolphe Adam"))
m("computers-internet", "easy", "Match each keyboard shortcut to what it does",
  ("Ctrl + C", "Copy"), ("Ctrl + V", "Paste"), ("Ctrl + Z", "Undo"), ("Ctrl + P", "Print"))
m("cricket", "easy", "Match each cricket term to its meaning",
  ("Duck", "Out for nought"), ("Maiden", "An over with no runs"), ("Yorker", "A ball aimed at the batter's feet"), ("Googly", "A leg-spinner's ball that turns the other way"))
m("crime-dramas", "medium", "Match each TV detective to their first name",
  ("Morse", "Endeavour"), ("Frost", "Jack"), ("Rebus", "John"), ("Barnaby", "Tom"))
m("dc-batman", "medium", "Match each Superman actor to his first Superman film",
  ("Christopher Reeve", "Superman (1978)"), ("Brandon Routh", "Superman Returns"), ("Henry Cavill", "Man of Steel"), ("David Corenswet", "Superman (2025)"))
m("disney", "medium", "Match each Disney film to the year it came out",
  ("Snow White and the Seven Dwarfs", "1937"), ("The Little Mermaid", "1989"), ("The Lion King", "1994"), ("Frozen", "2013"))
m("doctor-who", "medium", "Match each catchphrase to its Doctor",
  ("'Fantastic!'", "The Ninth Doctor"), ("'Allons-y!'", "The Tenth Doctor"), ("'Geronimo!'", "The Eleventh Doctor"), ("'Would you like a jelly baby?'", "The Fourth Doctor"))
m("europe", "medium", "Match each international car code to its country",
  ("D", "Germany"), ("F", "France"), ("E", "Spain"), ("CH", "Switzerland"))
m("landmarks", "medium", "Match each famous bridge to its city",
  ("Golden Gate Bridge", "San Francisco"), ("Charles Bridge", "Prague"), ("Rialto Bridge", "Venice"), ("Ponte Vecchio", "Florence"))

here = os.path.dirname(os.path.abspath(__file__))
for slug, qs in OUT.items():
    json.dump(qs, open(os.path.join(here, '..', 'topics', slug + '__m20.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(sum(len(q) for q in OUT.values()), 'match questions written for', len(OUT), 'topics')
