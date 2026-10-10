# Bank session 10 Oct 2026: 3 more general races -> bank/race-62.json. 20 rows each, target 10; wrong options are
# the same kind of thing, never another row's right answer, and never also right for that row.
import json, os
R = []
def race(title, cat, diff, tags, rows):
    rights = {r[1] for r in rows}
    assert len(rows) == 20, (title, len(rows))
    assert len(rights) == 20, (title, 'duplicate right answers')
    bad = [(q, w) for q, right, wrong in rows for w in wrong if w in rights]
    assert not bad, (title, 'recycled', bad)
    for q, right, wrong in rows:
        assert len(wrong) == 3 and len(set(wrong)) == 3 and right not in wrong, (title, q)
    R.append({"type": "race", "text": "The Race: " + title, "target": 10, "category": cat, "tags": tags, "difficulty": diff,
              "bank": [{"q": q, "right": right, "wrong": wrong} for q, right, wrong in rows]})

race("which US state is this national park in?", "World geography", "hard", ["national parks", "USA"], [
 ("Yosemite", "California", ["Nevada", "Idaho", "Nebraska"]), ("Petrified Forest", "Arizona", ["Nevada", "Oklahoma", "Kansas"]),
 ("Zion", "Utah", ["Nevada", "Idaho", "Nebraska"]), ("Dry Tortugas", "Florida", ["Georgia", "Louisiana", "South Carolina"]),
 ("Acadia", "Maine", ["Vermont", "New Hampshire", "Massachusetts"]), ("Glacier", "Montana", ["Idaho", "Nevada", "Nebraska"]),
 ("Olympic", "Washington", ["Idaho", "Nevada", "Nebraska"]), ("Crater Lake", "Oregon", ["Idaho", "Nevada", "Kansas"]),
 ("Kenai Fjords", "Alaska", ["Idaho", "Nevada", "Nebraska"]), ("Grand Teton", "Wyoming", ["Idaho", "Nevada", "Nebraska"]),
 ("Mesa Verde", "Colorado", ["Nevada", "Kansas", "Nebraska"]), ("Big Bend", "Texas", ["Oklahoma", "Louisiana", "Kansas"]),
 ("Shenandoah", "Virginia", ["West Virginia", "Maryland", "North Carolina"]), ("Mammoth Cave", "Kentucky", ["Tennessee", "Ohio", "Indiana"]),
 ("Carlsbad Caverns", "New Mexico", ["Oklahoma", "Nevada", "Kansas"]), ("Badlands", "South Dakota", ["Nebraska", "Iowa", "Kansas"]),
 ("Hot Springs", "Arkansas", ["Missouri", "Oklahoma", "Louisiana"]), ("Theodore Roosevelt", "North Dakota", ["Nebraska", "Iowa", "Wisconsin"]),
 ("Isle Royale", "Michigan", ["Wisconsin", "Ohio", "Illinois"]), ("Voyageurs", "Minnesota", ["Wisconsin", "Iowa", "Illinois"])])

race("which city is this cathedral in?", "Britain", "hard", ["cathedrals", "cities"], [
 ("The Mappa Mundi and a chained library", "Hereford", ["Shrewsbury", "Exeter", "Chester"]), ("The Imp, a little stone devil carved in the Angel Choir", "Lincoln", ["Southwell", "Ripon", "Carlisle"]),
 ("Britain's tallest spire and the best-kept Magna Carta", "Salisbury", ["Exeter", "Bath", "Truro"]), ("The great 'scissor arches' under the tower", "Wells", ["Bath", "Bristol", "Exeter"]),
 ("Thomas Becket was murdered here in 1170", "Canterbury", ["Rochester", "Guildford", "St Albans"]), ("The tombs of St Cuthbert and the Venerable Bede", "Durham", ["Carlisle", "Ripon", "Newcastle"]),
 ("The Great East Window in the Minster, the size of a tennis court", "York", ["Ripon", "Beverley", "Carlisle"]), ("Jane Austen's grave", "Winchester", ["Guildford", "Rochester", "Exeter"]),
 ("Richard III was reburied here in 2015", "Leicester", ["Nottingham", "Derby", "Southwell"]), ("The 'Ship of the Fens'", "Ely", ["Cambridge", "Bury St Edmunds", "St Albans"]),
 ("Basil Spence's building beside the ruins bombed in 1940", "Coventry", ["Birmingham", "Manchester", "Sheffield"]), ("The Catholic cathedral nicknamed 'Paddy's Wigwam'", "Liverpool", ["Manchester", "Bradford", "Sheffield"]),
 ("Wren's dome and the Whispering Gallery", "London", ["St Albans", "Oxford", "Rochester"]), ("Edward II's tomb, and cloisters used as Hogwarts corridors", "Gloucester", ["Bristol", "Bath", "Oxford"]),
 ("King John's tomb", "Worcester", ["Shrewsbury", "Bristol", "Chester"]), ("England's largest monastic cloisters, with Edith Cavell buried outside", "Norwich", ["Bury St Edmunds", "Cambridge", "Ipswich"]),
 ("Catherine of Aragon's grave", "Peterborough", ["Oxford", "Southwell", "St Albans"]), ("The only medieval English cathedral with three spires", "Lichfield", ["Derby", "Southwell", "Shrewsbury"]),
 ("St Mungo's tomb in the crypt", "Glasgow", ["Edinburgh", "St Andrews", "Aberdeen"]), ("A Marc Chagall window, and a spire you can see from the sea", "Chichester", ["Truro", "Exeter", "Rochester"])])

race("which famous Lord?", "Famous people", "medium", ["lords", "who's who"], [
 ("Vanished in 1974 after his children's nanny was murdered", "Lucan", ["Lichfield", "Snowdon", "Montagu"]), ("His column stands in Trafalgar Square", "Nelson", ["Raglan", "Palmerston", "Mountbatten"]),
 ("The Romantic poet called 'mad, bad and dangerous to know'", "Byron", ["Rochester", "Palmerston", "Montagu"]), ("His face pointed out from the 'Your Country Needs You' poster", "Kitchener", ["Haig", "Raglan", "Mountbatten"]),
 ("'You're fired!' on The Apprentice", "Sugar", ["Archer", "Sainsbury", "Bragg"]), ("He Who Must Not Be Named", "Voldemort", ["Asriel", "Summerisle", "Business"]),
 ("The nickname of William Joyce, who broadcast Nazi propaganda to Britain", "Haw-Haw", ["Beaverbrook", "Rothermere", "Reith"]), ("The short-tempered ruler of Duloc in Shrek", "Farquaad", ["Business", "Asriel", "Summerisle"]),
 ("Ran the London 2012 Olympics after winning 1500m gold twice", "Coe", ["Botham", "Bragg", "Winston"]), ("The Poet Laureate who wrote 'The Charge of the Light Brigade'", "Tennyson", ["Rochester", "Lister", "Rayleigh"]),
 ("The top-hatted toff of the Beano, 'and His Pals'", "Snooty", ["Percy", "Emsworth", "Marchmain"]), ("Robert Crawley, head of the family in Downton Abbey", "Grantham", ["Marchmain", "Emsworth", "Summerisle"]),
 ("Took the Parthenon marbles to London", "Elgin", ["Montagu", "Lichfield", "Palmerston"]), ("Led the Charge of the Light Brigade and gave his name to a knitted jacket", "Cardigan", ["Raglan", "Mountbatten", "Palmerston"]),
 ("Said to have put meat between bread so he needn't leave the card table", "Sandwich", ["Raglan", "Lichfield", "Rochester"]), ("Paid for Howard Carter's hunt for Tutankhamun's tomb", "Carnarvon", ["Montagu", "Rothermere", "Beaverbrook"]),
 ("The absolute temperature scale is named after him", "Kelvin", ["Rayleigh", "Lister", "Rutherford"]), ("Founded the Scouts", "Baden-Powell", ["Reith", "Mountbatten", "Lister"]),
 ("Stephen Fry's Elizabethan courtier in Blackadder II", "Melchett", ["Percy", "Emsworth", "Marchmain"]), ("Rik Mayall's 'Woof!' ladies' man in Blackadder", "Flashheart", ["Percy", "Emsworth", "Asriel"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-62.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
