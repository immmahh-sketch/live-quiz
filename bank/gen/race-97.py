# Bank session 10 Oct 2026: 2 more general races -> bank/race-97.json (motorways, Muppets). 20 rows each, target 10; wrong options are
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

race("which motorway is this?", "Britain", "hard", ["motorways", "roads", "travel"], [
 ("London to Leeds, Britain's first full intercity motorway", "M1", ["M18", "M42", "M69"]),
 ("Liverpool to Hull, right over the Pennines", "M62", ["M65", "M58", "M56"]),
 ("London to south Wales, over the Severn", "M4", ["M32", "M49", "M50"]),
 ("Birmingham to Exeter, past Bristol", "M5", ["M50", "M42", "M32"]),
 ("Rugby to the Scottish border: Britain's longest motorway", "M6", ["M61", "M55", "M54"]),
 ("The orbital ring road round London", "M25", ["M26", "M10", "M45"]),
 ("Edinburgh to Glasgow", "M8", ["M73", "M80", "M77"]),
 ("London to Folkestone and the Channel Tunnel", "M20", ["M2", "M26", "M10"]),
 ("London to Cambridge", "M11", ["M10", "M45", "M18"]),
 ("London to Southampton", "M3", ["M27", "M2", "M26"]),
 ("Down past Gatwick on the way to Brighton", "M23", ["M26", "M2", "M27"]),
 ("Manchester's orbital ring road", "M60", ["M66", "M56", "M61"]),
 ("London to Birmingham by way of Oxford", "M40", ["M42", "M45", "M54"]),
 ("The road you pay to use to get round Birmingham", "M6 Toll", ["M42", "M54", "M69"]),
 ("Glasgow down to Carlisle and the border", "M74", ["M77", "M73", "M80"]),
 ("Edinburgh to Perth, over the Queensferry Crossing", "M90", ["M80", "M876", "M73"]),
 ("Doncaster towards Grimsby and the Humber", "M180", ["M18", "M621", "M606"]),
 ("Over the old Severn Bridge to Chepstow", "M48", ["M49", "M32", "M50"]),
 ("Through County Durham up to Newcastle", "A1(M)", ["A19", "A167", "A66(M)"]),
 ("Edinburgh to Stirling", "M9", ["M80", "M876", "M73"])])

race("which Muppet is this?", "TV", "medium", ["Muppets", "puppets", "children's TV"], [
 ("Frog who hosts the show and sings 'Rainbow Connection'", "Kermit", ["Walter", "Clifford", "Bobo"]),
 ("Pig with a karate chop, madly in love with a frog", "Miss Piggy", ["Annie Sue", "Foo-Foo", "Bobo"]),
 ("Bear comic whose catchphrase is 'Wocka wocka!'", "Fozzie Bear", ["Big Mean Carl", "Bobo", "Thog"]),
 ("Blue 'whatever' with a hooked nose and a passion for chickens", "Gonzo", ["Uncle Deadly", "Lew Zealand", "Bobo"]),
 ("Wild drummer of the Electric Mayhem, kept on a chain", "Animal", ["Floyd Pepper", "Zoot", "Lips"]),
 ("The dog who plays the piano", "Rowlf", ["Foo-Foo", "Sprocket", "Bobo"]),
 ("Cook who babbles in mock Swedish and fights his food", "Swedish Chef", ["Lew Zealand", "Marvin Suggs", "Bobo"]),
 ("Meeping lab assistant who always gets hurt", "Beaker", ["Walter", "Clifford", "Bobo"]),
 ("Bald scientist with no eyes who runs Muppet Labs", "Dr Bunsen Honeydew", ["Uncle Deadly", "Marvin Suggs", "Lew Zealand"]),
 ("The two grumpy old hecklers up in the theatre box", "Statler and Waldorf", ["Bert and Ernie", "Bob and Doug", "Wayne and Wanda"]),
 ("Stern bald eagle who disapproves of everything", "Sam Eagle", ["Uncle Deadly", "Big Mean Carl", "Lew Zealand"]),
 ("Young stage manager in glasses whose uncle owns the theatre", "Scooter", ["Walter", "Clifford", "Bobo"]),
 ("Wisecracking rat, Gonzo's sidekick in The Muppet Christmas Carol", "Rizzo", ["Sprocket", "Clifford", "Foo-Foo"]),
 ("King prawn who insists he is not a shrimp", "Pepe", ["Lew Zealand", "Clifford", "Bobo"]),
 ("Gonzo's beloved chicken", "Camilla", ["Annie Sue", "Foo-Foo", "Bobo"]),
 ("Gold-toothed leader of the Electric Mayhem, on keyboards", "Dr Teeth", ["Floyd Pepper", "Zoot", "Lips"]),
 ("Laid-back Electric Mayhem guitarist who says 'Fer sure'", "Janice", ["Floyd Pepper", "Zoot", "Lips"]),
 ("Kermit's young nephew", "Robin", ["Walter", "Clifford", "Bobo"]),
 ("Big hairy monster who towers over everyone", "Sweetums", ["Big Mean Carl", "Thog", "Uncle Deadly"]),
 ("Muppet who loves to blow things up with explosives", "Crazy Harry", ["Lew Zealand", "Marvin Suggs", "Uncle Deadly"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-97.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
