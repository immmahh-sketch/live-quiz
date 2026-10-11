# Bank session 11 Oct 2026: 3 more general races -> bank/race-188.json (wartime home front, yoga and martial arts words). 20 rows each, target 10; wrong options are
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

race("what's this wartime home front word?", "History", "medium", ["Second World War", "home front", "words"], [
 ("Children sent to the countryside for safety", "Evacuees", ["Refugees", "Orphans", "Cadets"]),
 ("Limiting food so everyone got a fair share", "Rationing", ["Means testing", "Budgeting", "Fasting"]),
 ("The German bombing of British cities in 1940 and 1941", "The Blitz", ["Blitzkrieg", "The Battle of Britain", "The Doodlebugs"]),
 ("Switching off every light so bombers couldn't see the city", "Blackout", ["Curfew", "Lockdown", "Shutdown"]),
 ("The curved corrugated-iron shelter dug into the garden", "Anderson shelter", ["Nissen hut", "Bus shelter", "Lean-to"]),
 ("The cage-like indoor shelter that doubled as a table", "Morrison shelter", ["Nissen hut", "Dresser", "Larder"]),
 ("Older volunteers defending Britain, the real Dad's Army", "Home Guard", ["Coastguard", "Old Guard", "Life Guards"]),
 ("Young women sent to work on the farms", "Land Girls", ["Spice Girls", "Wrens", "Brownies"]),
 ("Wardens who made sure the blackout was kept", "ARP wardens", ["Traffic wardens", "Church wardens", "Prison warders"]),
 ("The nickname for the V-1 flying bomb", "Doodlebug", ["Ladybird", "Bedbug", "Humbug"]),
 ("The campaign to grow your own vegetables", "Dig for Victory", ["Keep Calm and Carry On", "Grow Your Own", "Plough On"]),
 ("The campaign urging people to repair old clothes", "Make Do and Mend", ["Waste Not Want Not", "Sew What", "Darn It"]),
 ("The poster warning that gossip could help spies", "Careless talk costs lives", ["Keep Calm and Carry On", "Your Country Needs You", "Mind the Gap"]),
 ("Carried everywhere in a cardboard box in case of gas", "Gas mask", ["Tin hat", "Torch", "Whistle"]),
 ("The booklet of coupons for food", "Ration book", ["Identity card", "Passbook", "Phrasebook"]),
 ("The mass rescue from the French beaches in 1940", "Dunkirk", ["Arnhem", "Calais", "Normandy"]),
 ("'The Forces' Sweetheart'", "Vera Lynn", ["Gracie Fields", "Anne Shelton", "Cilla Black"]),
 ("The day the war in Europe ended", "VE Day", ["VJ Day", "D-Day", "Armistice Day"]),
 ("Eggs that came as a powder in a tin", "Powdered egg", ["Scotch egg", "Easter egg", "Pickled egg"]),
 ("The fighter that flew alongside the Hurricane in the Battle of Britain", "Spitfire", ["Lancaster", "Mosquito", "Wellington"])])

race("what's this yoga word?", "Lifestyle", "medium", ["yoga", "wellbeing", "words"], [
 ("The greeting said with palms together", "Namaste", ["Shalom", "Aloha", "Ciao"]),
 ("The upside-down V pose", "Downward dog", ["Sleeping dog", "Hot dog", "Top dog"]),
 ("Cross-legged with each foot on the opposite thigh", "Lotus position", ["Rose position", "Pole position", "Recovery position"]),
 ("One of the body's seven energy centres", "Chakra", ["Karma", "Dharma", "Nirvana"]),
 ("The sacred sound chanted at the start", "Om", ["Ah", "Shh", "Ooh"]),
 ("The 'corpse pose', lying flat at the end", "Savasana", ["Siesta", "Sauna", "Samsara"]),
 ("A flowing sequence of poses that greets the morning", "Sun salutation", ["Moon landing", "Sun dance", "Sunrise"]),
 ("Balancing on one leg with the other foot on your thigh", "Tree pose", ["Flamingo", "Scarecrow", "Lamppost"]),
 ("Kneeling and folding forward to rest", "Child's pose", ["Baby step", "Kneeler", "Prayer"]),
 ("Lying face down and lifting the chest like a snake", "Cobra", ["Python", "Viper", "Adder"]),
 ("Lunging with arms outstretched, in poses I, II and III", "Warrior", ["Soldier", "Knight", "Gladiator"]),
 ("Yoga breathing exercises", "Pranayama", ["Panorama", "Pyjama", "Piranha"]),
 ("The Sanskrit word for a yoga pose", "Asana", ["Ashram", "Avatar", "Arena"]),
 ("A word or phrase repeated over and over in meditation", "Mantra", ["Mascot", "Manta", "Matrix"]),
 ("Yoga in a room heated to around 40°C", "Hot yoga", ["Steam yoga", "Sauna yoga", "Power yoga"]),
 ("A spiritual teacher", "Guru", ["Guinea", "Gurkha", "Gnu"]),
 ("Someone who practises yoga", "Yogi", ["Yokel", "Yeti", "Yodeller"]),
 ("The non-slip rubber thing you practise on", "Mat", ["Pad", "Tile", "Plinth"]),
 ("Paying calm attention to the present moment", "Mindfulness", ["Forgetfulness", "Wistfulness", "Playfulness"]),
 ("The Japanese school of meditative Buddhism", "Zen", ["Zion", "Zed", "Zest"])])

race("what's this martial arts word?", "Sport", "medium", ["martial arts", "karate", "words"], [
 ("The training hall", "Dojo", ["Dynamo", "Disco", "Depot"]),
 ("The instructor", "Sensei", ["Samurai", "Shogun", "Sushi"]),
 ("The top level of belt", "Black belt", ["Brown belt", "Green belt", "Bible belt"]),
 ("The white cotton training suit", "Gi", ["Toga", "Sari", "Kilt"]),
 ("A set sequence of moves practised on your own", "Kata", ["Kart", "Kebab", "Kayak"]),
 ("The shout when you strike", "Kiai", ["Banzai", "Aloha", "Yeehaw"]),
 ("Two sticks joined by a chain", "Nunchucks", ["Chopsticks", "Drumsticks", "Maracas"]),
 ("Straw mats covering the floor", "Tatami", ["Tiramisu", "Origami", "Tamagotchi"]),
 ("A grade within the black belt, as in '3rd ___'", "Dan", ["Kyu", "Pip", "Rank"]),
 ("A strike with the edge of the hand", "Karate chop", ["Lamb chop", "Pork chop", "Chop suey"]),
 ("The Olympic sport of throws and holds, from Japan", "Judo", ["Kendo", "Aikido", "Hapkido"]),
 ("Huge wrestlers pushing each other out of a ring", "Sumo", ["Kendo", "Origami", "Kabuki"]),
 ("The Korean kicking sport at the Olympics", "Taekwondo", ["Karate", "Hapkido", "Krav Maga"]),
 ("The Chinese fighting arts made famous by Bruce Lee", "Kung fu", ["Karate", "Kendo", "Capoeira"]),
 ("Thailand's 'art of eight limbs'", "Muay Thai", ["Pad Thai", "Tai chi", "Thai green"]),
 ("A black-clad Japanese spy and assassin", "Ninja", ["Samurai", "Geisha", "Shogun"]),
 ("The Karate Kid's wise teacher", "Mr Miyagi", ["Mr Motivator", "Mr Bean", "Mr T"]),
 ("His car-polishing lesson", "Wax on, wax off", ["Wash and go", "Rinse and repeat", "Spit and polish"]),
 ("What you do as you step into the training hall", "Bow", ["Curtsy", "Salute", "Wave"]),
 ("What changes colour as you go up the grades", "Belt", ["Headband", "Gloves", "Socks"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-188.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
