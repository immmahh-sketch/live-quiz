# Bank session 11 Oct 2026: 9 more Categorise questions -> bank/sort-17.json. Two groups, three or four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Music", ["The Beatles", "The Monkees"], "medium", "A Beatle or a Monkee?", "Beatle", "Monkee", ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr"], ["Davy Jones", "Micky Dolenz", "Peter Tork", "Mike Nesmith"])
s("Science", ["gemstones", "metals"], "easy", "A gemstone or a metal?", "Gemstone", "Metal", ["Ruby", "Emerald", "Sapphire", "Topaz"], ["Copper", "Zinc", "Nickel", "Titanium"])
s("Books", ["Shakespeare", "Christopher Marlowe", "plays"], "hard", "A play by Shakespeare or by Christopher Marlowe?", "Shakespeare", "Marlowe", ["Hamlet", "King Lear", "Twelfth Night", "Coriolanus"], ["Doctor Faustus", "Tamburlaine", "The Jew of Malta", "Edward II"])
s("Music", ["Oasis", "Blur", "Britpop"], "medium", "In Oasis or in Blur?", "Oasis", "Blur", ["Liam Gallagher", "Noel Gallagher", "Bonehead", "Guigsy"], ["Damon Albarn", "Graham Coxon", "Alex James", "Dave Rowntree"])
s("Games and toys", ["Pokémon", "Transformers"], "easy", "A Pokémon or a Transformer?", "Pokémon", "Transformer", ["Pikachu", "Charizard", "Squirtle", "Jigglypuff"], ["Optimus Prime", "Megatron", "Bumblebee", "Starscream"])
s("TV", ["soaps", "Australia", "UK"], "easy", "An Australian soap or a British soap?", "Australian", "British", ["Neighbours", "Home and Away", "Sons and Daughters", "Prisoner: Cell Block H"], ["EastEnders", "Emmerdale", "Hollyoaks", "Doctors"])
s("Books", ["Harry Potter", "Hogwarts"], "easy", "A Hogwarts subject or a spell?", "Subject", "Spell", ["Potions", "Herbology", "Divination", "Transfiguration"], ["Expelliarmus", "Lumos", "Accio", "Alohomora"])
s("Film", ["Doctor Who", "Star Wars", "villains"], "easy", "A Doctor Who villain or a Star Wars villain?", "Doctor Who", "Star Wars", ["Davros", "The Master", "Missy", "The Rani"], ["Darth Vader", "Palpatine", "Kylo Ren", "Jabba the Hutt"])
s("Mythology", ["Roman gods", "Norse gods"], "easy", "A Roman god or a Norse god?", "Roman", "Norse", ["Jupiter", "Mars", "Mercury", "Neptune"], ["Odin", "Thor", "Loki", "Freya"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-17.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
