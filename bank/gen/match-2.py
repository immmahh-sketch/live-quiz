# Bank session 9 Oct 2026: 3 more Match questions for each topic with fewer than 5 unused in the live bank.
# Writes bank/topics/<slug>__m2.json (the importer reads <slug>__*.json as a top-up of <slug>), then:
#   TOPICS=<slugs> LQ_PASSWORD=… node tools/import-bank.mjs topics
import json, os
OUT = {}
def m(slug, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.setdefault(slug, []).append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff})

m("general-knowledge", "medium", "Match each phobia to what it is a fear of",
  ("Arachnophobia", "Spiders"), ("Claustrophobia", "Enclosed spaces"), ("Acrophobia", "Heights"), ("Agoraphobia", "Open or crowded places"))
m("general-knowledge", "medium", "Match each group name to its animal",
  ("A pride", "Lions"), ("A murder", "Crows"), ("A parliament", "Owls"), ("A gaggle", "Geese"))
m("general-knowledge", "medium", "Match each Roman god to his or her Greek equivalent",
  ("Jupiter", "Zeus"), ("Mars", "Ares"), ("Venus", "Aphrodite"), ("Neptune", "Poseidon"))

m("name-the-year", "medium", "Match each TV first to its year",
  ("First episode of Coronation Street", "1960"), ("First episode of Doctor Who", "1963"), ("First episode of EastEnders", "1985"), ("First series of Big Brother in the UK", "2000"))
m("name-the-year", "hard", "Match each launch to its year",
  ("Google is founded", "1998"), ("Facebook launches", "2004"), ("Twitter launches", "2006"), ("The first iPhone goes on sale", "2007"))
m("name-the-year", "medium", "Match each royal occasion to its year",
  ("Coronation of Elizabeth II", "1953"), ("Wedding of Charles and Diana", "1981"), ("Death of Diana, Princess of Wales", "1997"), ("Coronation of Charles III", "2023"))

m("tennis-golf", "easy", "Match each golfer to his country",
  ("Rory McIlroy", "Northern Ireland"), ("Seve Ballesteros", "Spain"), ("Tiger Woods", "USA"), ("Colin Montgomerie", "Scotland"))
m("tennis-golf", "easy", "Match each tennis term to its meaning",
  ("Love", "Zero"), ("Deuce", "40–40"), ("Ace", "A serve the opponent can't touch"), ("Let", "A serve that clips the net and is replayed"))
m("tennis-golf", "medium", "Match each famous golf course to its country",
  ("St Andrews", "Scotland"), ("Augusta National", "USA"), ("Royal Birkdale", "England"), ("Valderrama", "Spain"))

m("the-1980s", "medium", "Match each classic gadget to the company that made it",
  ("Walkman", "Sony"), ("ZX Spectrum", "Sinclair"), ("BBC Micro", "Acorn"), ("Game Boy", "Nintendo"))
m("the-1980s", "easy", "Match each 1980s soap to where it is set",
  ("EastEnders", "Albert Square"), ("Brookside", "A Liverpool cul-de-sac"), ("Dallas", "Southfork Ranch"), ("Neighbours", "Ramsay Street"))
m("the-1980s", "easy", "Match each 1980s number one to its act",
  ("Come On Eileen", "Dexys Midnight Runners"), ("Relax", "Frankie Goes to Hollywood"), ("Do They Know It's Christmas?", "Band Aid"), ("Never Gonna Give You Up", "Rick Astley"))

m("boy-bands-girl-groups", "easy", "Match each song to its group",
  ("Back for Good", "Take That"), ("Flying Without Wings", "Westlife"), ("Wannabe", "Spice Girls"), ("The Promise", "Girls Aloud"))
m("boy-bands-girl-groups", "easy", "Match each singer to their group",
  ("Ronan Keating", "Boyzone"), ("Beyoncé", "Destiny's Child"), ("Nicole Scherzinger", "The Pussycat Dolls"), ("Cheryl", "Girls Aloud"))
m("boy-bands-girl-groups", "medium", "Match each group to its Christmas number one",
  ("East 17", "Stay Another Day"), ("Spice Girls", "2 Become 1"), ("Westlife", "I Have a Dream"), ("Girls Aloud", "Sound of the Underground"))

m("british-sitcoms", "easy", "Match each catchphrase to its sitcom",
  ("'Lovely jubbly!'", "Only Fools and Horses"), ("'I don't believe it!'", "One Foot in the Grave"), ("'Don't panic!'", "Dad's Army"), ("'I have a cunning plan'", "Blackadder"))
m("british-sitcoms", "medium", "Match each sitcom family to its show",
  ("The Trotters", "Only Fools and Horses"), ("The Royles", "The Royle Family"), ("The Boswells", "Bread"), ("The Goods", "The Good Life"))
m("british-sitcoms", "hard", "Match each sitcom to the company its characters work for",
  ("The Office", "Wernham Hogg"), ("The IT Crowd", "Reynholm Industries"), ("Are You Being Served?", "Grace Brothers"), ("Drop the Dead Donkey", "Globelink News"))

m("days-that-shook-the-world", "medium", "Match each assassination to the year it happened",
  ("Archduke Franz Ferdinand", "1914"), ("John F. Kennedy", "1963"), ("Martin Luther King", "1968"), ("John Lennon", "1980"))
m("days-that-shook-the-world", "easy", "Match each event to its city",
  ("The Great Fire of 1666", "London"), ("The Storming of the Bastille", "Paris"), ("The great earthquake of 1906", "San Francisco"), ("The Tiananmen Square protests", "Beijing"))
m("days-that-shook-the-world", "easy", "Match each person to the moment they are remembered for",
  ("Rosa Parks", "Refusing to give up her bus seat"), ("Nelson Mandela", "Walking free from prison in 1990"), ("Yuri Gagarin", "First person in space"), ("Neil Armstrong", "First steps on the Moon"))

m("dexter", "medium", "Match each killer to his nickname",
  ("Brian Moser", "The Ice Truck Killer"), ("Arthur Mitchell", "The Trinity Killer"), ("Travis Marshall", "The Doomsday Killer"), ("Dexter Morgan", "The Bay Harbor Butcher"))
m("dexter", "easy", "Match each character to who they are to Dexter",
  ("Harry", "Adoptive father"), ("Debra", "Sister"), ("Rita", "Wife"), ("Harrison", "Son"))
m("dexter", "hard", "Match each character to the season of Dexter they first appear in",
  ("Lila Tournay", "Season 2"), ("Jordan Chase", "Season 5"), ("Isaak Sirko", "Season 7"), ("Oliver Saxon, the Brain Surgeon", "Season 8"))

m("film-quotes", "easy", "Match each famous movie line to the film it comes from",
  ("'Here's looking at you, kid'", "Casablanca"), ("'May the Force be with you'", "Star Wars"), ("'There's no place like home'", "The Wizard of Oz"), ("'Houston, we have a problem'", "Apollo 13"))
m("film-quotes", "easy", "Match each catchphrase to the film character who says it",
  ("'Hasta la vista, baby'", "The Terminator"), ("'Bond. James Bond.'", "James Bond"), ("'My precious'", "Gollum"), ("'Life is like a box of chocolates'", "Forrest Gump"))
m("film-quotes", "easy", "Match each famous line to its film",
  ("'Nobody puts Baby in a corner'", "Dirty Dancing"), ("'You're gonna need a bigger boat'", "Jaws"), ("'Keep the change, ya filthy animal'", "Home Alone"), ("'I see dead people'", "The Sixth Sense"))

m("football", "easy", "Match each English club to its nickname",
  ("Newcastle United", "The Magpies"), ("Sunderland", "The Black Cats"), ("Arsenal", "The Gunners"), ("West Ham United", "The Hammers"))
m("football", "medium", "Match each England manager to the tournament he took England deep into",
  ("Alf Ramsey", "1966 World Cup"), ("Bobby Robson", "Italia 90"), ("Terry Venables", "Euro 96"), ("Gareth Southgate", "Euro 2020"))
m("football", "medium", "Match each stadium to its city",
  ("Camp Nou", "Barcelona"), ("San Siro", "Milan"), ("Santiago Bernabéu", "Madrid"), ("Maracanã", "Rio de Janeiro"))

m("halloween-music", "medium", "Match each spooky song to its act",
  ("Somebody's Watching Me", "Rockwell"), ("Bark at the Moon", "Ozzy Osbourne"), ("Werewolves of London", "Warren Zevon"), ("Bat Out of Hell", "Meat Loaf"))
m("halloween-music", "hard", "Match each film to the song or tune it is known for",
  ("The Exorcist", "Tubular Bells"), ("Hocus Pocus", "I Put a Spell on You"), ("Beetlejuice", "Day-O (The Banana Boat Song)"), ("The Lost Boys", "Cry Little Sister"))
m("halloween-music", "easy", "Match each song to its act",
  ("Highway to Hell", "AC/DC"), ("Superstition", "Stevie Wonder"), ("Zombie", "The Cranberries"), ("Witchy Woman", "Eagles"))

m("newcastle-v-sunderland", "hard", "Match each North East club to its old ground",
  ("Sunderland", "Roker Park"), ("Middlesbrough", "Ayresome Park"), ("Darlington", "Feethams"), ("Gateshead", "Redheugh Park"))
m("newcastle-v-sunderland", "medium", "Match each Newcastle hero to his nickname",
  ("Jackie Milburn", "Wor Jackie"), ("Malcolm Macdonald", "Supermac"), ("Paul Gascoigne", "Gazza"), ("Kevin Keegan", "King Kev"))
m("newcastle-v-sunderland", "easy", "Match each home kit to its North East club",
  ("Black and white stripes", "Newcastle United"), ("Red and white stripes", "Sunderland"), ("All red", "Middlesbrough"), ("Blue and white", "Hartlepool United"))

m("record-breakers", "easy", "Match each first to the person who did it",
  ("First mile run in under four minutes", "Roger Bannister"), ("First to the top of Everest (with Tenzing Norgay)", "Edmund Hillary"), ("First woman to fly solo across the Atlantic", "Amelia Earhart"), ("First person in space", "Yuri Gagarin"))
m("record-breakers", "medium", "Match each record to the country that holds it",
  ("Largest country by area", "Russia"), ("Most people", "India"), ("Smallest country", "Vatican City"), ("Most Summer Olympic medals", "USA"))
m("record-breakers", "medium", "Match each record to the planet that holds it",
  ("Largest planet", "Jupiter"), ("Hottest planet", "Venus"), ("Smallest planet", "Mercury"), ("Most moons", "Saturn"))

m("religion-festivals", "medium", "Match each festival to what it marks",
  ("Christmas", "The birth of Jesus"), ("Easter", "The resurrection of Jesus"), ("Hanukkah", "The rededication of the Temple in Jerusalem"), ("Eid al-Fitr", "The end of Ramadan"))
m("religion-festivals", "easy", "Match each patron saint to his country",
  ("St George", "England"), ("St Andrew", "Scotland"), ("St David", "Wales"), ("St Patrick", "Ireland"))
m("religion-festivals", "easy", "Match each title to its faith",
  ("The Pope", "Catholic Church"), ("The Dalai Lama", "Tibetan Buddhism"), ("Rabbi", "Judaism"), ("Imam", "Islam"))

m("rock-music", "easy", "Match each singer to his band",
  ("Freddie Mercury", "Queen"), ("Robert Plant", "Led Zeppelin"), ("Brian Johnson", "AC/DC"), ("Ozzy Osbourne", "Black Sabbath"))
m("rock-music", "easy", "Match each song to its band",
  ("Smoke on the Water", "Deep Purple"), ("Stairway to Heaven", "Led Zeppelin"), ("Paranoid", "Black Sabbath"), ("Back in Black", "AC/DC"))
m("rock-music", "medium", "Match each drummer to his band",
  ("Keith Moon", "The Who"), ("John Bonham", "Led Zeppelin"), ("Dave Grohl", "Nirvana"), ("Lars Ulrich", "Metallica"))

m("rom-coms", "medium", "Match each rom-com to its stars",
  ("Notting Hill", "Julia Roberts and Hugh Grant"), ("Pretty Woman", "Julia Roberts and Richard Gere"), ("When Harry Met Sally", "Billy Crystal and Meg Ryan"), ("Sleepless in Seattle", "Tom Hanks and Meg Ryan"))
m("rom-coms", "hard", "Match each rom-com to its writer",
  ("Four Weddings and a Funeral", "Richard Curtis"), ("When Harry Met Sally", "Nora Ephron"), ("Clueless", "Amy Heckerling"), ("The Holiday", "Nancy Meyers"))
m("rom-coms", "hard", "Match each actor to his rom-com character",
  ("Hugh Grant", "William Thacker (Notting Hill)"), ("Richard Gere", "Edward Lewis (Pretty Woman)"), ("Colin Firth", "Mark Darcy (Bridget Jones's Diary)"), ("Matthew McConaughey", "Benjamin Barry (How to Lose a Guy in 10 Days)"))

m("summer-holidays", "medium", "Match each seaside town to its county",
  ("Blackpool", "Lancashire"), ("Whitby", "North Yorkshire"), ("Newquay", "Cornwall"), ("Skegness", "Lincolnshire"))
m("summer-holidays", "easy", "Match each airport code to its airport",
  ("LHR", "Heathrow"), ("NCL", "Newcastle"), ("LGW", "Gatwick"), ("MAN", "Manchester"))
m("summer-holidays", "medium", "Match each holiday country to its main language",
  ("Portugal", "Portuguese"), ("Croatia", "Croatian"), ("Cyprus", "Greek"), ("Malta", "Maltese"))

m("the-1990s", "easy", "Match each 1990s number one to its act",
  ("Gangsta's Paradise", "Coolio"), ("Barbie Girl", "Aqua"), ("Believe", "Cher"), ("...Baby One More Time", "Britney Spears"))
m("the-1990s", "easy", "Match each 1990s TV show to its presenter",
  ("Noel's House Party", "Noel Edmonds"), ("TFI Friday", "Chris Evans"), ("Blind Date", "Cilla Black"), ("Gladiators", "Ulrika Jonsson"))
m("the-1990s", "medium", "Match each 1990s event to its year",
  ("Nelson Mandela walks free", "1990"), ("The Channel Tunnel opens", "1994"), ("Diana, Princess of Wales dies", "1997"), ("The Good Friday Agreement", "1998"))

m("the-2000s", "easy", "Match each 2000s gadget to its maker",
  ("iPod", "Apple"), ("Razr", "Motorola"), ("PlayStation 2", "Sony"), ("Wii", "Nintendo"))
m("the-2000s", "hard", "Match each 2000s moment to its year",
  ("Euro notes and coins arrive", "2002"), ("Concorde's last flight", "2003"), ("Smoking banned in pubs in England", "2007"), ("Barack Obama is elected", "2008"))
m("the-2000s", "easy", "Match each show to its host",
  ("Who Wants to Be a Millionaire?", "Chris Tarrant"), ("The Weakest Link", "Anne Robinson"), ("Deal or No Deal", "Noel Edmonds"), ("Big Brother", "Davina McCall"))

here = os.path.dirname(os.path.abspath(__file__))
for slug, items in OUT.items():
    json.dump(items, open(os.path.join(here, '..', 'topics', slug + '__m2.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(sum(map(len, OUT.values())), 'matches in', len(OUT), 'topics:', ','.join(OUT))
