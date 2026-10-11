# Bank session 11 Oct 2026: more Categorise questions -> bank/sort-20.json. Two groups, three or four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})


s("Film", ["Disney", "villains", "sidekicks"], "easy", "A Disney villain or a Disney sidekick?", "Villain", "Sidekick", ["Scar", "Ursula", "Jafar", "Cruella de Vil"], ["Timon", "Sebastian", "Abu", "Mushu"])
s("Food and drink", ["cheese", "France", "Italy"], "easy", "A French cheese or an Italian cheese?", "France", "Italy", ["Brie", "Camembert", "Roquefort", "Comté"], ["Parmesan", "Gorgonzola", "Mozzarella", "Pecorino"])
s("Sport", ["cricket", "golf", "jargon"], "medium", "A cricket term or a golf term?", "Cricket", "Golf", ["Googly", "Yorker", "Maiden", "Silly mid-on"], ["Birdie", "Bogey", "Albatross", "Mulligan"])
s("UK geography", ["London Underground", "Monopoly"], "easy", "A London Underground line or a Monopoly property?", "Tube line", "Monopoly", ["Jubilee", "Central", "Northern", "Bakerloo"], ["Mayfair", "Old Kent Road", "Pall Mall", "Whitechapel Road"])
s("Religion and myth", ["Norse gods", "Egyptian gods", "mythology"], "medium", "A Norse god or an Egyptian god?", "Norse", "Egyptian", ["Odin", "Thor", "Loki", "Freya"], ["Ra", "Anubis", "Osiris", "Horus"])
s("Film", ["Batman", "Spider-Man", "villains"], "easy", "A Batman villain or a Spider-Man villain?", "Batman", "Spider-Man", ["The Joker", "The Penguin", "The Riddler", "Bane"], ["Green Goblin", "Doctor Octopus", "Venom", "Sandman"])
s("Music", ["Spice Girls", "Sugababes", "girl groups"], "medium", "A Spice Girl or a Sugababe?", "Spice Girls", "Sugababes", ["Mel B", "Emma Bunton", "Geri Halliwell", "Victoria Beckham"], ["Keisha Buchanan", "Mutya Buena", "Siobhán Donaghy", "Heidi Range"])
s("Sport", ["horse racing", "Grand National", "Derby"], "hard", "A Grand National winner or a Derby winner?", "Grand National", "Derby", ["Red Rum", "Aldaniti", "Tiger Roll", "Corbiere"], ["Shergar", "Nijinsky", "Galileo", "Mill Reef"])
s("TV", ["Strictly Come Dancing", "Dancing on Ice", "judges"], "medium", "Judged Strictly or judged Dancing on Ice?", "Strictly", "Dancing on Ice", ["Craig Revel Horwood", "Shirley Ballas", "Motsi Mabuse", "Anton Du Beke"], ["Christopher Dean", "Jayne Torvill", "Ashley Banjo", "Oti Mabuse"])
s("TV", ["Gladiators", "1990s TV"], "medium", "An original 1990s Gladiator: a man or a woman?", "Man", "Woman", ["Wolf", "Saracen", "Shadow", "Hunter"], ["Jet", "Lightning", "Panther", "Flame"])
s("TV", ["Gerry Anderson", "Thunderbirds", "Captain Scarlet"], "medium", "A Thunderbirds character or a Captain Scarlet character?", "Thunderbirds", "Captain Scarlet", ["Lady Penelope", "Parker", "Brains", "Scott Tracy"], ["Captain Blue", "Colonel White", "Captain Black", "Destiny Angel"])
s("Religion and myth", ["Chinese zodiac", "star signs"], "medium", "A Chinese zodiac animal or a Western star sign's creature?", "Chinese zodiac", "Star sign", ["Rat", "Dragon", "Monkey", "Rooster"], ["Scorpion", "Crab", "Lion", "Fish"])
s("TV", ["Sesame Street", "The Muppet Show"], "medium", "A Sesame Street character or a Muppet Show character?", "Sesame Street", "The Muppet Show", ["Big Bird", "Elmo", "Cookie Monster", "Oscar the Grouch"], ["Fozzie Bear", "Miss Piggy", "Gonzo", "Animal"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-20.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
