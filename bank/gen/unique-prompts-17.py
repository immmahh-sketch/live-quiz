# Bank session 10 Oct 2026: 20 more Only One prompts (albums, directors, film series, cups, borders, sitcoms) appended to bank/unique-prompts.json.
# Each is a closed list with every correct answer (other accepted forms after a slash), so a fair answer is never knocked out.
import json, os
NEW = [
 ("Name a studio album by Arctic Monkeys", ["Whatever People Say I Am, That's What I'm Not/Whatever People Say I Am", "Favourite Worst Nightmare", "Humbug", "Suck It and See", "AM", "Tranquility Base Hotel & Casino/Tranquility Base Hotel and Casino", "The Car"]),
 ("Name a studio album by ABBA", ["Ring Ring", "Waterloo", "ABBA", "Arrival", "The Album", "Voulez-Vous", "Super Trouper", "The Visitors", "Voyage"]),
 ("Name a studio album by Take That", ["Take That & Party/Take That and Party", "Everything Changes", "Nobody Else", "Beautiful World", "The Circus", "Progress", "III", "Wonderland", "This Life"]),
 ("Name a studio album by Robbie Williams, up to 2026", ["Life thru a Lens/Life Through a Lens", "I've Been Expecting You", "Sing When You're Winning", "Swing When You're Winning", "Escapology", "Intensive Care", "Rudebox", "Reality Killed the Video Star", "Take the Crown", "Swings Both Ways", "The Heavy Entertainment Show", "The Christmas Present", "Britpop"]),
 ("Name a studio album by the Spice Girls or Girls Aloud", ["Spice", "Spiceworld", "Forever", "Sound of the Underground", "What Will the Neighbours Say?", "Chemistry", "Tangled Up", "Out of Control"]),
 ("Name a feature film directed by Danny Boyle, up to 2025", ["Shallow Grave", "Trainspotting", "A Life Less Ordinary", "The Beach", "28 Days Later", "Millions", "Sunshine", "Slumdog Millionaire", "127 Hours", "Trance", "Steve Jobs", "T2 Trainspotting/T2", "Yesterday", "28 Years Later"]),
 ("Name a feature film directed by Guy Ritchie, up to 2025", ["Lock, Stock and Two Smoking Barrels/Lock Stock", "Snatch", "Swept Away", "Revolver", "RocknRolla", "Sherlock Holmes", "Sherlock Holmes: A Game of Shadows/A Game of Shadows", "The Man from U.N.C.L.E./The Man from UNCLE", "King Arthur: Legend of the Sword/King Arthur", "Aladdin", "The Gentlemen", "Wrath of Man", "Operation Fortune: Ruse de Guerre/Operation Fortune", "The Covenant", "The Ministry of Ungentlemanly Warfare", "Fountain of Youth"]),
 ("Name a film in the Mission: Impossible series, up to 2025", ["Mission: Impossible/Mission Impossible", "Mission: Impossible 2/M:I-2", "Mission: Impossible III/M:I III", "Ghost Protocol", "Rogue Nation", "Fallout", "Dead Reckoning", "The Final Reckoning"]),
 ("Name a film in the Fast & Furious series, including the spin-off, up to 2025", ["The Fast and the Furious", "2 Fast 2 Furious", "Tokyo Drift", "Fast & Furious/Fast and Furious", "Fast Five", "Fast & Furious 6/Fast 6", "Furious 7", "The Fate of the Furious/F8", "F9", "Fast X", "Hobbs & Shaw/Hobbs and Shaw"]),
 ("Name a film in the Jurassic Park or Jurassic World series, up to 2025", ["Jurassic Park", "The Lost World", "Jurassic Park III", "Jurassic World", "Fallen Kingdom", "Dominion", "Jurassic World Rebirth/Rebirth"]),
 ("Name a country that shares a land border with Guatemala or Honduras", ["Mexico", "Belize", "El Salvador", "Honduras", "Guatemala", "Nicaragua"]),
 ("Name a US state that the Mississippi River flows through or along", ["Minnesota", "Wisconsin", "Iowa", "Illinois", "Missouri", "Kentucky", "Tennessee", "Arkansas", "Mississippi", "Louisiana"]),
 ("Name a club that won the Scottish Cup from 2000 to 2025", ["Celtic", "Rangers", "Hearts/Heart of Midlothian", "Dundee United", "Hibernian/Hibs", "St Johnstone", "Inverness Caledonian Thistle/Inverness CT/Inverness", "Aberdeen"]),
 ("Name a club that won the English League Cup from 2000 to 2025", ["Leicester City/Leicester", "Liverpool", "Blackburn Rovers/Blackburn", "Middlesbrough", "Chelsea", "Manchester United/Man United", "Tottenham Hotspur/Tottenham/Spurs", "Birmingham City/Birmingham", "Swansea City/Swansea", "Manchester City/Man City", "Newcastle United/Newcastle"]),
 ("Name a ground that has hosted a men's Rugby World Cup final", ["Eden Park", "Twickenham", "Ellis Park", "Millennium Stadium/Principality Stadium", "Stadium Australia/Accor Stadium/Telstra Stadium", "Stade de France", "International Stadium Yokohama/Nissan Stadium/Yokohama"]),
 ("Name a British Prime Minister who was born in Scotland", ["The Earl of Bute/Lord Bute", "The Earl of Aberdeen/Lord Aberdeen", "Arthur Balfour/Balfour", "Henry Campbell-Bannerman/Campbell-Bannerman", "Ramsay MacDonald/MacDonald", "Tony Blair/Blair", "Gordon Brown/Brown"]),
 ("Name a member of Radiohead or Muse", ["Thom Yorke", "Jonny Greenwood", "Colin Greenwood", "Ed O'Brien", "Philip Selway/Phil Selway", "Matt Bellamy", "Chris Wolstenholme", "Dominic Howard/Dom Howard"]),
 ("Name a member of the Royle family in The Royle Family", ["Jim", "Barbara", "Denise", "Antony", "Nana/Norma", "Baby David"]),
 ("Name one of the inhabited islands of the Isles of Scilly", ["St Mary's", "Tresco", "St Martin's", "St Agnes", "Bryher", "Gugh"]),
 ("Name the capital city of an Australian state or territory", ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide", "Hobart", "Darwin", "Canberra"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
