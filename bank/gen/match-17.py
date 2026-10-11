# Bank session 11 Oct 2026 (sixteenth pass): one more Match question each for 18 topics that had 7 live, checked against
# the live questions in each topic. Writes bank/topics/<slug>__m17.json; import each with FILE=<slug>__m17 TOPICS=<slug> LQ_PASSWORD=… node tools/import-bank.mjs topics
import json, os
OUT = {}
def m(slug, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.setdefault(slug, []).append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff})

m("breaking-bad", "easy", "Match each Breaking Bad character to who they are to Walter White",
  ("Skyler", "Wife"), ("Walter Jr", "Son"), ("Holly", "Daughter"), ("Hank", "Brother-in-law"))
m("bridgerton", "medium", "Match each Bridgerton first name to the title the character goes by",
  ("Simon", "Duke of Hastings"), ("Anthony", "Viscount Bridgerton"), ("Charlotte", "The Queen"), ("Agatha", "Lady Danbury"))
m("brighton", "medium", "Match each Brighton & Hove Albion manager to his country",
  ("Gus Poyet", "Uruguay"), ("Graham Potter", "England"), ("Roberto De Zerbi", "Italy"), ("Fabian Hürzeler", "Germany"))
m("christmas-tv", "easy", "Match each Christmas telly favourite film to its star",
  ("Elf", "Will Ferrell"), ("Home Alone", "Macaulay Culkin"), ("Scrooged", "Bill Murray"), ("Die Hard", "Bruce Willis"))
m("dexter", "medium", "Match each Miami Metro character to their job",
  ("Dexter Morgan", "Blood-spatter analyst"), ("Vince Masuka", "Forensic technician"), ("María LaGuerta", "Lieutenant"), ("Harry Morgan", "Detective"))
m("game-of-thrones", "medium", "Match each dragon to its rider",
  ("Drogon", "Daenerys"), ("Caraxes", "Daemon"), ("Vhagar", "Aemond"), ("Syrax", "Rhaenyra"))
m("newcastle-v-sunderland", "medium", "Match each Sunderland hero to his nickname",
  ("Charlie Hurley", "The King"), ("Len Shackleton", "The Clown Prince of Soccer"), ("Kevin Phillips", "Super Kev"), ("Jim Montgomery", "Monty"))
m("one-hit-wonders", "medium", "Match each number one to the act that never topped the charts again",
  ("Mouldy Old Dough", "Lieutenant Pigeon"), ("Kung Fu Fighting", "Carl Douglas"), ("Sugar, Sugar", "The Archies"), ("In the Year 2525", "Zager and Evans"))
m("quiz-shows", "easy", "Match each quiz show to the channel it's best known on",
  ("Pointless", "BBC One"), ("The Chase", "ITV"), ("Only Connect", "BBC Two"), ("Countdown", "Channel 4"))
m("scotland", "easy", "Match each Scottish city to its river",
  ("Glasgow", "Clyde"), ("Dundee", "Tay"), ("Inverness", "Ness"), ("Aberdeen", "Dee"))
m("summer-holidays", "medium", "Match each holiday destination to the money you'd take",
  ("Turkey", "Lira"), ("Morocco", "Dirham"), ("Thailand", "Baht"), ("Croatia", "Euro"))
m("the-1960s", "easy", "Match each 1960s moment to its year",
  ("The Berlin Wall goes up", "1961"), ("JFK is assassinated", "1963"), ("England win the World Cup", "1966"), ("Man lands on the Moon", "1969"))
m("the-1970s", "medium", "Match each 1970s sitcom to its setting",
  ("Porridge", "Slade Prison"), ("The Good Life", "Surbiton"), ("Fawlty Towers", "Torquay"), ("Last of the Summer Wine", "Holmfirth"))
m("the-beatles", "medium", "Match each Beatles song to the album it's on",
  ("Yesterday", "Help!"), ("Eleanor Rigby", "Revolver"), ("Come Together", "Abbey Road"), ("Twist and Shout", "Please Please Me"))
m("world-cup", "medium", "Match each World Cup to its Golden Boot winner",
  ("1986", "Gary Lineker"), ("1990", "Salvatore Schillaci"), ("2002", "Ronaldo"), ("2018", "Harry Kane"))
m("theatre", "medium", "Match each musical to the city it's set in",
  ("Les Misérables", "Paris"), ("Cabaret", "Berlin"), ("Evita", "Buenos Aires"), ("West Side Story", "New York"))
m("tudors", "medium", "Match each Tudor monarch to the year their reign began",
  ("Henry VII", "1485"), ("Henry VIII", "1509"), ("Edward VI", "1547"), ("Elizabeth I", "1558"))
m("wales", "easy", "Match each Welsh rugby legend to his position",
  ("Gareth Edwards", "Scrum-half"), ("Barry John", "Fly-half"), ("JPR Williams", "Full-back"), ("Shane Williams", "Wing"))

here = os.path.dirname(os.path.abspath(__file__))
for slug, qs in OUT.items():
    json.dump(qs, open(os.path.join(here, '..', 'topics', slug + '__m17.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(sum(len(q) for q in OUT.values()), 'match questions written for', len(OUT), 'topics')
