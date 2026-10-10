# Bank session 10 Oct 2026: new Wipeout boards -> bank/wipeout-7.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

board("Characters in Gavin & Stacey (watch for impostors)", "Film and TV", "medium", ["Gavin & Stacey", "sitcoms"],
 ["Gavin", "Stacey", "Smithy", "Nessa", "Bryn", "Pam", "Mick", "Gwen", "Dawn", "Pete", "Doris", "Jason", "Dave Coaches", "Rudi", "Neil the Baby"],
 ["Dai Coaches", "Uncle Glyn", "Rhian", "Kenny", "Barbara"])
board("Clubs in the 2025–26 Premier League", "Football", "medium", ["Premier League", "clubs"],
 ["Arsenal", "Aston Villa", "Bournemouth", "Brentford", "Brighton", "Burnley", "Chelsea", "Crystal Palace", "Everton", "Fulham", "Leeds United", "Liverpool", "Newcastle United", "Sunderland", "Nottingham Forest"],
 ["Leicester City", "Ipswich Town", "Southampton", "Luton Town", "Sheffield United"])
board("Pokémon from the original 151", "Games and toys", "medium", ["Pokémon", "games"],
 ["Pikachu", "Bulbasaur", "Charmander", "Squirtle", "Jigglypuff", "Meowth", "Psyduck", "Snorlax", "Mewtwo", "Gengar", "Eevee", "Magikarp", "Gyarados", "Onix", "Machamp"],
 ["Lucario", "Togepi", "Pichu", "Marill", "Greninja"])
board("Real Mr. Men (watch for made-up ones)", "Books", "medium", ["Mr. Men", "children's books"],
 ["Mr. Tickle", "Mr. Greedy", "Mr. Happy", "Mr. Nosey", "Mr. Sneeze", "Mr. Bump", "Mr. Snow", "Mr. Messy", "Mr. Topsy-Turvy", "Mr. Silly", "Mr. Uppity", "Mr. Small", "Mr. Daydream", "Mr. Forgetful", "Mr. Jelly"],
 ["Mr. Grubby", "Mr. Hiccup", "Mr. Fidget", "Mr. Snooze", "Mr. Sniffle"])
board("Thunderbirds characters and craft (watch for impostors)", "Film and TV", "medium", ["Thunderbirds", "Gerry Anderson"],
 ["Scott Tracy", "Virgil Tracy", "Alan Tracy", "Gordon Tracy", "John Tracy", "Jeff Tracy", "Lady Penelope", "Parker", "Brains", "Tin-Tin", "Kyrano", "The Hood", "Grandma Tracy", "FAB 1", "Tracy Island"],
 ["Michael Tracy", "Lady Persephone", "Dexter Tracy", "Colonel White", "Kenny Tracy"])
board("Gladiators from the original 1990s ITV series", "Film and TV", "hard", ["Gladiators", "TV"],
 ["Wolf", "Jet", "Lightning", "Shadow", "Saracen", "Cobra", "Hunter", "Rhino", "Trojan", "Warrior", "Ace", "Panther", "Flame", "Amazon", "Nightshade"],
 ["Legend", "Giant", "Fury", "Atlas", "Tornado"])
board("Lakes and waters in the Lake District", "Britain", "medium", ["Lake District", "lakes"],
 ["Windermere", "Ullswater", "Derwentwater", "Coniston Water", "Buttermere", "Crummock Water", "Wastwater", "Thirlmere", "Haweswater", "Ennerdale Water", "Bassenthwaite Lake", "Grasmere", "Rydal Water", "Loweswater", "Elterwater"],
 ["Kielder Water", "Ladybower Reservoir", "Rutland Water", "Bala Lake", "Semerwater"])
board("Bridges over the River Tyne", "The North East", "hard", ["Tyne", "bridges", "North East"],
 ["Tyne Bridge", "Swing Bridge", "High Level Bridge", "Gateshead Millennium Bridge", "Redheugh Bridge", "King Edward VII Bridge", "Queen Elizabeth II Metro Bridge", "Scotswood Bridge", "Blaydon Bridge", "Newburn Bridge", "Wylam Bridge", "Hagg Bank Bridge", "Ovingham Bridge", "Corbridge Bridge", "Hexham Bridge"],
 ["Wearmouth Bridge", "Northern Spire", "Queen Alexandra Bridge", "Transporter Bridge", "Infinity Bridge"])
board("Actresses who played a 'Bond girl'", "James Bond", "medium", ["Bond", "actresses"],
 ["Ursula Andress", "Honor Blackman", "Diana Rigg", "Jane Seymour", "Britt Ekland", "Barbara Bach", "Grace Jones", "Halle Berry", "Eva Green", "Léa Seydoux", "Famke Janssen", "Michelle Yeoh", "Denise Richards", "Teri Hatcher", "Gemma Arterton"],
 ["Kate Winslet", "Keira Knightley", "Emma Thompson", "Helen Mirren", "Catherine Zeta-Jones"])
board("People who have been Chancellor of the Exchequer", "Politics", "medium", ["Chancellors", "politics"],
 ["Gordon Brown", "George Osborne", "Rishi Sunak", "Rachel Reeves", "Philip Hammond", "Sajid Javid", "Kwasi Kwarteng", "Jeremy Hunt", "Nadhim Zahawi", "Alistair Darling", "Kenneth Clarke", "Norman Lamont", "Nigel Lawson", "Geoffrey Howe", "Denis Healey"],
 ["Michael Gove", "Theresa May", "Ed Balls", "John Prescott", "Priti Patel"])
board("People who have been Home Secretary", "Politics", "hard", ["Home Secretaries", "politics"],
 ["Theresa May", "Amber Rudd", "Sajid Javid", "Priti Patel", "Suella Braverman", "Grant Shapps", "James Cleverly", "Yvette Cooper", "Shabana Mahmood", "Jack Straw", "David Blunkett", "John Reid", "Jacqui Smith", "Alan Johnson", "Michael Howard"],
 ["Dominic Raab", "Michael Gove", "Ed Miliband", "Boris Johnson", "Liz Truss"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-7.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'boards written')
