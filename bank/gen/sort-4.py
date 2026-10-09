# Bank session 9 Oct 2026 (third pass): 2 more Categorise (sort) questions for 12 topics that had 5 live (Christmas first).
# Writes bank/topics/<slug>__s4.json; import with FILE=<slug>__s4 TOPICS=<slug> LQ_PASSWORD=… node tools/import-bank.mjs topics
import json, os
OUT = {}
def s(slug, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.setdefault(slug, []).append({"type": "sort", "text": text, "categories": [a, b],
        "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B], "difficulty": diff})

s("christmas", "easy", "From 'A Christmas Carol' or from the Nativity story?", "A Christmas Carol", "The Nativity",
  ["Scrooge", "Jacob Marley", "Tiny Tim", "Bob Cratchit"], ["Joseph", "The angel Gabriel", "King Herod", "The shepherds"])
s("christmas", "easy", "A Christmas treat or an Easter treat?", "Christmas", "Easter",
  ["Mince pie", "Christmas pudding", "Stollen", "Panettone"], ["Hot cross bun", "Simnel cake", "Creme Egg", "Easter biscuits"])
s("christmas-movies", "medium", "A Christmas film released before 1990, or from 1990 on?", "Before 1990", "1990 on",
  ["It's a Wonderful Life", "White Christmas", "Scrooged", "Gremlins"], ["Home Alone", "Elf", "Love Actually", "Klaus"])
s("christmas-movies", "medium", "Is Father Christmas a main character, or not?", "Santa's a main character", "Not a main character",
  ["Elf", "The Santa Clause", "Miracle on 34th Street", "Arthur Christmas"], ["Home Alone", "Die Hard", "It's a Wonderful Life", "Love Actually"])
s("christmas-music", "medium", "A Christmas hit from the 1970s or the 1980s?", "1970s", "1980s",
  ["Merry Xmas Everybody", "I Wish It Could Be Christmas Everyday", "Lonely This Christmas", "Wonderful Christmastime"], ["Last Christmas", "Do They Know It's Christmas?", "Fairytale of New York", "Merry Christmas Everyone"])
s("christmas-music", "easy", "A Christmas song sung by a man or by a woman?", "Man", "Woman",
  ["Driving Home for Christmas", "White Christmas", "Last Christmas", "Step into Christmas"], ["All I Want for Christmas Is You", "Santa Baby", "Underneath the Tree", "Rockin' Around the Christmas Tree"])

s("boxing-combat", "medium", "World heavyweight champion, or champion at a lighter weight?", "Heavyweight", "Lighter weight",
  ["Muhammad Ali", "Lennox Lewis", "Tyson Fury", "Mike Tyson"], ["Naseem Hamed", "Floyd Mayweather", "Ricky Hatton", "Amir Khan"])
s("boxing-combat", "easy", "A boxing term or a wrestling term?", "Boxing", "Wrestling",
  ["Uppercut", "Jab", "Southpaw", "Haymaker"], ["Body slam", "Suplex", "Pinfall", "Half nelson"])

s("capital-cities", "medium", "A capital in the Northern or the Southern Hemisphere?", "Northern", "Southern",
  ["Ottawa", "Oslo", "Cairo", "Tokyo"], ["Canberra", "Wellington", "Buenos Aires", "Pretoria"])
s("capital-cities", "medium", "The capital of an island nation, or not?", "Island nation", "Not an island nation",
  ["Reykjavík", "Dublin", "Valletta", "Manila"], ["Vienna", "Madrid", "Prague", "Lima"])

s("cars-motoring", "medium", "A brand that only makes electric cars, or not?", "Electric only", "Not electric only",
  ["Tesla", "Polestar", "Rivian", "Lucid"], ["Ford", "Vauxhall", "Peugeot", "Kia"])
s("cars-motoring", "medium", "A Formula One world champion or a World Rally champion?", "Formula One", "World Rally",
  ["Lewis Hamilton", "Nigel Mansell", "Jenson Button", "Damon Hill"], ["Colin McRae", "Sébastien Loeb", "Richard Burns", "Walter Röhrl"])

s("kids-tv", "medium", "A BBC children's show or an ITV one?", "BBC", "ITV",
  ["Blue Peter", "Newsround", "Grange Hill", "Byker Grove"], ["Art Attack", "SM:tv Live", "Rainbow", "Press Gang"])
s("kids-tv", "medium", "A Postman Pat character or a Fireman Sam character?", "Postman Pat", "Fireman Sam",
  ["Mrs Goggins", "Jess", "Ted Glen", "PC Selby"], ["Norman Price", "Dilys Price", "Station Officer Steele", "Elvis Cridlington"])

s("childrens-books", "easy", "Written by Roald Dahl or by David Walliams?", "Roald Dahl", "David Walliams",
  ["The Twits", "The Witches", "Danny the Champion of the World", "Esio Trot"], ["Gangsta Granny", "Mr Stink", "Billionaire Boy", "The Boy in the Dress"])
s("childrens-books", "easy", "A Beatrix Potter character or a Winnie-the-Pooh character?", "Beatrix Potter", "Winnie-the-Pooh",
  ["Peter Rabbit", "Jemima Puddle-Duck", "Mrs Tiggy-Winkle", "Squirrel Nutkin"], ["Eeyore", "Piglet", "Kanga", "Tigger"])

s("classical-music", "medium", "Written by Beethoven or by Mozart?", "Beethoven", "Mozart",
  ["Moonlight Sonata", "Für Elise", "Ode to Joy", "Fidelio"], ["The Magic Flute", "Eine kleine Nachtmusik", "Don Giovanni", "The Marriage of Figaro"])
s("classical-music", "medium", "A Baroque composer or a Romantic composer?", "Baroque", "Romantic",
  ["Bach", "Handel", "Vivaldi", "Purcell"], ["Chopin", "Schumann", "Liszt", "Brahms"])

s("computers-internet", "easy", "Made by Apple or by Microsoft?", "Apple", "Microsoft",
  ["iTunes", "Safari", "Keynote", "FaceTime"], ["Excel", "Outlook", "Teams", "Xbox"])
s("computers-internet", "medium", "A programming language or a social media app?", "Programming language", "Social media app",
  ["Python", "Java", "Ruby", "Swift"], ["TikTok", "Snapchat", "Pinterest", "Reddit"])

s("cricket", "medium", "A way for a batter to be out, or not?", "Out", "Not out",
  ["Bowled", "Caught", "LBW", "Stumped"], ["Wide", "Maiden", "No-ball", "Bye"])
s("cricket", "medium", "Captained England or captained Australia?", "England", "Australia",
  ["Michael Vaughan", "Alastair Cook", "Joe Root", "Ben Stokes"], ["Ricky Ponting", "Steve Waugh", "Michael Clarke", "Pat Cummins"])

s("crime-dramas", "medium", "Set in Oxford or in London?", "Oxford", "London",
  ["Inspector Morse", "Lewis", "Endeavour"], ["Luther", "The Bill", "Prime Suspect", "Sherlock"])
s("crime-dramas", "medium", "A BBC crime drama or an ITV crime drama?", "BBC", "ITV",
  ["Line of Duty", "Luther", "Happy Valley", "Shetland"], ["Vera", "Broadchurch", "Midsomer Murders", "Endeavour"])

here = os.path.dirname(os.path.abspath(__file__))
for slug, items in OUT.items():
    json.dump(items, open(os.path.join(here, '..', 'topics', slug + '__s4.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(sum(map(len, OUT.values())), 'sorts in', len(OUT), 'topics:', ' '.join(OUT))
