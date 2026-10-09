# Bank session 9 Oct 2026 (fourth pass): 20 more Only One prompts appended to bank/unique-prompts.json. Each is a
# closed list with every correct answer (other accepted forms after a slash), so a fair answer is never knocked out.
import json, os
NEW = [
 ("Name one of the three wise men, or one of their gifts", ["Caspar/Gaspar/Kaspar", "Melchior", "Balthazar/Balthasar", "Gold", "Frankincense", "Myrrh"]),
 ("Name a film in the Toy Story or Shrek series", ["Toy Story", "Toy Story 2", "Toy Story 3", "Toy Story 4", "Toy Story 5", "Shrek", "Shrek 2", "Shrek the Third", "Shrek Forever After"]),
 ("Name a James Bond film starring Daniel Craig", ["Casino Royale", "Quantum of Solace", "Skyfall", "Spectre", "No Time to Die"]),
 ("Name a Spice Girl by her nickname, or a member of Steps", ["Scary Spice/Scary", "Sporty Spice/Sporty", "Baby Spice/Baby", "Ginger Spice/Ginger", "Posh Spice/Posh", "H/Ian Watkins", "Claire Richards/Claire", "Lisa Scott-Lee/Lisa", "Faye Tozer/Faye", "Lee Latchford-Evans/Lee"]),
 ("Name a Formula One team on the 2025 grid", ["Red Bull", "Ferrari", "Mercedes", "McLaren", "Aston Martin", "Alpine", "Williams", "Racing Bulls/RB/Visa Cash App RB", "Haas", "Sauber/Kick Sauber/Stake"]),
 ("Name a US state on the Pacific coast, or one that borders Mexico", ["Washington", "Oregon", "California", "Alaska", "Hawaii", "Arizona", "New Mexico", "Texas"]),
 ("Name a ground that has hosted an England men's Test match since 2000", ["Lord's/Lords", "The Oval/Oval/Kennington Oval", "Old Trafford", "Headingley", "Edgbaston", "Trent Bridge", "Rose Bowl/Ageas Bowl/Utilita Bowl/Southampton", "Riverside/Chester-le-Street/Durham", "Sophia Gardens/Cardiff"]),
 ("Name a city that has hosted the Winter Olympics since 1980", ["Lake Placid", "Sarajevo", "Calgary", "Albertville", "Lillehammer", "Nagano", "Salt Lake City", "Turin/Torino", "Vancouver", "Sochi", "PyeongChang/Pyeongchang", "Beijing", "Milan/Milano", "Cortina d'Ampezzo/Cortina"]),
 ("Name a character from The Wind in the Willows", ["Mole", "Ratty/Water Rat/Rat", "Badger", "Toad/Mr Toad", "Otter", "Portly", "Chief Weasel", "The gaoler's daughter"]),
 ("Name a character from The Lion, the Witch and the Wardrobe", ["Peter", "Susan", "Edmund", "Lucy", "Aslan", "White Witch/Jadis", "Mr Tumnus/Tumnus", "Mr Beaver", "Mrs Beaver", "Professor Kirke", "Father Christmas", "Maugrim", "Mrs Macready"]),
 ("Name one of the seven Chronicles of Narnia", ["The Lion, the Witch and the Wardrobe", "Prince Caspian", "The Voyage of the Dawn Treader", "The Silver Chair", "The Horse and His Boy", "The Magician's Nephew", "The Last Battle"]),
 ("Name a day of Holy Week, from Palm Sunday to Easter Sunday", ["Palm Sunday", "Holy Monday", "Holy Tuesday", "Holy Wednesday/Spy Wednesday", "Maundy Thursday/Holy Thursday", "Good Friday", "Holy Saturday/Easter Eve", "Easter Sunday/Easter Day"]),
 ("Name one of the 18 Pokémon types", ["Normal", "Fire", "Water", "Grass", "Electric", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]),
 ("Name a BBC television channel broadcasting in 2026", ["BBC One", "BBC Two", "BBC Three", "BBC Four", "BBC News", "BBC Parliament", "CBBC", "CBeebies", "BBC Alba", "BBC Scotland"]),
 ("Name a Quidditch position or one of the balls used in Quidditch", ["Seeker", "Keeper", "Chaser", "Beater", "Quaffle", "Bludger", "Golden Snitch/Snitch"]),
 ("Name one of Columbus's three ships of 1492, or a ship Captain Cook sailed", ["Santa María/Santa Maria", "Niña/Nina", "Pinta", "Endeavour", "Resolution", "Adventure", "Discovery"]),
 ("Name a member of Monty Python or of The Goodies", ["Graham Chapman", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones", "Michael Palin", "Tim Brooke-Taylor", "Graeme Garden", "Bill Oddie"]),
 ("Name a country with Guinea, Congo or Sudan in its name", ["Guinea", "Guinea-Bissau", "Equatorial Guinea", "Papua New Guinea", "Republic of the Congo/Congo", "Democratic Republic of the Congo/DR Congo", "Sudan", "South Sudan"]),
 ("Name one of the Deathly Hallows, or one of Voldemort's Horcruxes", ["Elder Wand", "Resurrection Stone", "Invisibility Cloak", "Tom Riddle's diary/Diary", "Marvolo Gaunt's ring/Ring", "Slytherin's locket/Locket", "Hufflepuff's cup/Cup", "Ravenclaw's diadem/Diadem", "Nagini", "Harry Potter/Harry"]),
 ("Name a planet in our Solar System that has rings", ["Jupiter", "Saturn", "Uranus", "Neptune"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
