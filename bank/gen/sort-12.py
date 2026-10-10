# Bank session 10 Oct 2026: 14 more Categorise questions -> bank/sort-9.json. Two groups, four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Music", ["Nirvana", "Pearl Jam", "grunge"], "medium", "A Nirvana song or a Pearl Jam song?", "Nirvana", "Pearl Jam", ["Smells Like Teen Spirit", "Come as You Are", "Lithium", "Heart-Shaped Box"], ["Alive", "Jeremy", "Even Flow", "Black"])
s("Music", ["opera", "Mozart", "Wagner"], "hard", "An opera by Mozart or by Wagner?", "Mozart", "Wagner", ["The Magic Flute", "Don Giovanni", "The Marriage of Figaro", "Così fan tutte"], ["Tristan und Isolde", "Parsifal", "Lohengrin", "Tannhäuser"])
s("Art", ["Picasso", "Dalí", "painting"], "hard", "Painted by Picasso or by Dalí?", "Picasso", "Dalí", ["Guernica", "Les Demoiselles d'Avignon", "The Old Guitarist", "The Weeping Woman"], ["The Persistence of Memory", "The Elephants", "Swans Reflecting Elephants", "Christ of Saint John of the Cross"])
s("Art", ["Leonardo da Vinci", "Michelangelo", "Renaissance"], "medium", "A work by Leonardo da Vinci or by Michelangelo?", "Leonardo", "Michelangelo", ["Mona Lisa", "The Last Supper", "Lady with an Ermine", "Vitruvian Man"], ["The Creation of Adam", "The Last Judgment", "David", "Pietà"])
s("Film", ["Pixar", "Toy Story", "Monsters, Inc."], "easy", "A 'Toy Story' character or a 'Monsters, Inc.' character?", "Toy Story", "Monsters, Inc.", ["Woody", "Rex", "Hamm", "Slinky Dog"], ["Sulley", "Mike Wazowski", "Boo", "Randall"])
s("Books", ["Harry Potter"], "medium", "A Hogwarts teacher or someone who worked at the Ministry of Magic?", "Hogwarts teacher", "Ministry of Magic", ["Minerva McGonagall", "Filius Flitwick", "Pomona Sprout", "Horace Slughorn"], ["Cornelius Fudge", "Arthur Weasley", "Kingsley Shacklebolt", "Barty Crouch Sr"])
s("Children's books", ["comics", "The Beano", "The Dandy"], "medium", "A 'Beano' character or a 'Dandy' character?", "The Beano", "The Dandy", ["Dennis the Menace", "Minnie the Minx", "Roger the Dodger", "The Bash Street Kids"], ["Desperate Dan", "Korky the Cat", "Bananaman", "Beryl the Peril"])
s("Football", ["European Cup", "Champions League"], "medium", "Has won the European Cup or Champions League, or never has?", "Has won it", "Never", ["Nottingham Forest", "Aston Villa", "Celtic", "Liverpool"], ["Arsenal", "Tottenham Hotspur", "Newcastle United", "Everton"])
s("TV", ["Netflix", "Prime Video", "streaming"], "medium", "A Netflix series or an Amazon Prime Video series?", "Netflix", "Prime Video", ["Stranger Things", "The Crown", "Bridgerton", "Squid Game"], ["The Boys", "Reacher", "The Grand Tour", "Clarkson's Farm"])
s("World geography", ["capital cities", "Latin America"], "hard", "A capital in South America or in Central America?", "South America", "Central America", ["Lima", "Bogotá", "Quito", "Santiago"], ["Managua", "Tegucigalpa", "San José", "Guatemala City"])
s("Words and language", ["loanwords", "Italian", "Spanish"], "medium", "A word English borrowed from Italian or from Spanish?", "Italian", "Spanish", ["Opera", "Piano", "Graffiti", "Fiasco"], ["Patio", "Mosquito", "Tornado", "Siesta"])
s("Music", ["Queen", "Led Zeppelin", "rock"], "medium", "A member of Queen or a member of Led Zeppelin?", "Queen", "Led Zeppelin", ["Freddie Mercury", "Brian May", "Roger Taylor", "John Deacon"], ["Robert Plant", "Jimmy Page", "John Paul Jones", "John Bonham"])
s("TV", ["Bake Off", "MasterChef", "cookery"], "medium", "Has fronted or judged 'Bake Off' or 'MasterChef'?", "Bake Off", "MasterChef", ["Mary Berry", "Paul Hollywood", "Mel Giedroyc", "Sue Perkins"], ["Loyd Grossman", "John Torode", "Gregg Wallace", "Monica Galetti"])
s("Travel", ["London Underground", "London Overground"], "hard", "A London Underground line or a London Overground line?", "Underground", "Overground", ["Bakerloo", "Jubilee", "Victoria", "Piccadilly"], ["Lioness", "Mildmay", "Windrush", "Suffragette"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-9.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
