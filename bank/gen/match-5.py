# Bank session 9 Oct 2026 (fourth pass): 2 more Match questions for 13 broad topics that had 5 live.
# Writes bank/topics/<slug>__m5.json; import each with FILE=<slug>__m5 TOPICS=<slug> LQ_PASSWORD=… node tools/import-bank.mjs topics
import json, os
OUT = {}
def m(slug, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.setdefault(slug, []).append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff})

m("north-east-england", "medium", "Match each North East landmark to the place it stands",
  ("The Angel of the North", "Gateshead"), ("Penshaw Monument", "Sunderland"), ("The Transporter Bridge", "Middlesbrough"), ("Locomotion railway museum", "Shildon"))
m("north-east-england", "medium", "Match each star to the North East drama they're known for",
  ("Brenda Blethyn", "Vera"), ("Jimmy Nail", "Spender"), ("Tim Healy", "Auf Wiedersehen, Pet"), ("Declan Donnelly", "Byker Grove"))

m("harry-potter", "medium", "Match each actor to the Hogwarts teacher they played",
  ("Emma Thompson", "Sybill Trelawney"), ("Kenneth Branagh", "Gilderoy Lockhart"), ("David Thewlis", "Remus Lupin"), ("Imelda Staunton", "Dolores Umbridge"))
m("harry-potter", "easy", "Match each spell to what it does",
  ("Expelliarmus", "Knocks the wand out of an enemy's hand"), ("Lumos", "Lights up the tip of your wand"), ("Wingardium Leviosa", "Makes things float"), ("Expecto Patronum", "Conjures a Patronus"))

m("james-bond", "medium", "Match each Bond film to its main villain",
  ("Skyfall", "Raoul Silva"), ("Casino Royale", "Le Chiffre"), ("GoldenEye", "Alec Trevelyan"), ("Live and Let Die", "Mr. Big"))
m("james-bond", "medium", "Match each Bond henchman to their trademark",
  ("Oddjob", "A steel-rimmed bowler hat"), ("Jaws", "Steel teeth"), ("Rosa Klebb", "A poisoned blade in her shoe"), ("Xenia Onatopp", "Crushing victims with her thighs"))

m("london", "medium", "Match each London terminus to a city its trains go to",
  ("King's Cross", "Newcastle"), ("Paddington", "Bristol"), ("Euston", "Manchester"), ("St Pancras", "Paris"))
m("london", "medium", "Match each London museum or gallery to something it's famous for",
  ("The British Museum", "The Rosetta Stone"), ("The National Gallery", "The Hay Wain"), ("Tate Modern", "The Turbine Hall"), ("The Natural History Museum", "Hope the blue whale skeleton"))

m("musicals", "easy", "Match each song to its musical",
  ("Memory", "Cats"), ("Don't Cry for Me Argentina", "Evita"), ("I Dreamed a Dream", "Les Misérables"), ("Defying Gravity", "Wicked"))
m("musicals", "medium", "Match each musical to the person who wrote its songs",
  ("Hamilton", "Lin-Manuel Miranda"), ("Mamma Mia!", "Benny Andersson and Björn Ulvaeus"), ("Billy Elliot", "Elton John"), ("Matilda", "Tim Minchin"))

m("soaps", "medium", "Match each soap to where it's set",
  ("Emmerdale", "The Yorkshire Dales"), ("Hollyoaks", "Chester"), ("Brookside", "Liverpool"), ("Doctors", "The Midlands"))
m("soaps", "easy", "Match each actor to their EastEnders character",
  ("Barbara Windsor", "Peggy Mitchell"), ("June Brown", "Dot Cotton"), ("Ross Kemp", "Grant Mitchell"), ("Danny Dyer", "Mick Carter"))

m("royal-family", "medium", "Match each royal to their title",
  ("Prince Edward", "Duke of Edinburgh"), ("Princess Anne", "Princess Royal"), ("Catherine", "Princess of Wales"), ("Prince Harry", "Duke of Sussex"))
m("royal-family", "easy", "Match each royal residence to where it is",
  ("Balmoral", "Aberdeenshire"), ("Sandringham", "Norfolk"), ("Windsor Castle", "Berkshire"), ("Holyroodhouse", "Edinburgh"))

m("tudors", "medium", "Match each Tudor to their nickname",
  ("Mary I", "Bloody Mary"), ("Elizabeth I", "The Virgin Queen"), ("Edward VI", "The Boy King"), ("Lady Jane Grey", "The Nine Days' Queen"))
m("tudors", "hard", "Match each Tudor to the place they died",
  ("Anne Boleyn", "The Tower of London"), ("Henry VIII", "Whitehall Palace"), ("Elizabeth I", "Richmond Palace"), ("Jane Seymour", "Hampton Court"))

m("world-wars", "medium", "Match each wartime operation to what it was",
  ("Operation Overlord", "The D-Day landings"), ("Operation Dynamo", "The Dunkirk evacuation"), ("Operation Barbarossa", "Germany's invasion of the USSR"), ("Operation Market Garden", "The airborne attack on Arnhem"))
m("world-wars", "medium", "Match each First World War battle to its year",
  ("Mons", "1914"), ("The Somme", "1916"), ("Passchendaele", "1917"), ("Amiens", "1918"))

m("olympics", "easy", "Match each British Olympian to their sport",
  ("Chris Hoy", "Cycling"), ("Ben Ainslie", "Sailing"), ("Tom Daley", "Diving"), ("Adam Peaty", "Swimming"))
m("olympics", "medium", "Match each Summer Olympics to its year",
  ("Barcelona", "1992"), ("Atlanta", "1996"), ("Sydney", "2000"), ("Athens", "2004"))

m("doctor-who", "easy", "Match each Doctor to the actor who played them",
  ("The Ninth Doctor", "Christopher Eccleston"), ("The Tenth Doctor", "David Tennant"), ("The Twelfth Doctor", "Peter Capaldi"), ("The Thirteenth Doctor", "Jodie Whittaker"))
m("doctor-who", "medium", "Match each companion to their Doctor",
  ("Donna Noble", "The Tenth Doctor"), ("Amy Pond", "The Eleventh Doctor"), ("Bill Potts", "The Twelfth Doctor"), ("Yasmin Khan", "The Thirteenth Doctor"))

m("friends", "easy", "Match each Friend to their surname",
  ("Monica", "Geller"), ("Chandler", "Bing"), ("Joey", "Tribbiani"), ("Phoebe", "Buffay"))
m("friends", "easy", "Match each line to the Friend who says it",
  ("'How you doin'?'", "Joey"), ("'We were on a break!'", "Ross"), ("'Could I BE wearing any more clothes?'", "Chandler"), ("'Smelly cat, smelly cat…'", "Phoebe"))

m("pop-music", "medium", "Match each act to their first UK number one",
  ("Spice Girls", "Wannabe"), ("Westlife", "Swear It Again"), ("Girls Aloud", "Sound of the Underground"), ("Little Mix", "Cannonball"))
m("pop-music", "medium", "Match each star to their real name",
  ("Lady Gaga", "Stefani Germanotta"), ("Elton John", "Reginald Dwight"), ("Freddie Mercury", "Farrokh Bulsara"), ("Sting", "Gordon Sumner"))

here = os.path.dirname(os.path.abspath(__file__))
for slug, items in OUT.items():
    json.dump(items, open(os.path.join(here, '..', 'topics', slug + '__m5.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(sum(map(len, OUT.values())), 'matches in', len(OUT), 'topics:', ' '.join(OUT))
