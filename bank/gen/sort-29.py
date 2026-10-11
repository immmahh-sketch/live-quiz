# Bank session 11 Oct 2026: more Categorise questions -> bank/sort-26.json. Two groups, three or four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})


s("North East", ["Tyne and Wear Metro", "London Underground"], "medium", "A Tyne and Wear Metro station or a London Tube station?", "Metro", "Tube", ["Haymarket", "Jesmond", "Pelaw", "Felling"], ["Angel", "Oval", "Temple", "Moorgate"])
s("Food and drink", ["cocktails", "gin", "whisky"], "medium", "A gin cocktail or a whisky cocktail?", "Gin", "Whisky", ["Negroni", "Tom Collins", "Gimlet", "Gin Fizz"], ["Old Fashioned", "Whisky Sour", "Manhattan", "Rob Roy"])
s("Games", ["Pokémon", "types"], "medium", "A Fire-type Pokémon or a Water-type Pokémon?", "Fire", "Water", ["Charmander", "Vulpix", "Growlithe", "Ponyta"], ["Squirtle", "Psyduck", "Magikarp", "Poliwag"])
s("Film", ["Marvel", "Avengers", "Guardians of the Galaxy"], "easy", "An original Avenger or a Guardian of the Galaxy?", "Avengers", "Guardians of the Galaxy", ["Captain America", "Thor", "Black Widow", "Hawkeye"], ["Star-Lord", "Gamora", "Drax", "Rocket"])
s("Sport", ["horse racing", "Grand National", "Cheltenham"], "hard", "A Grand National fence or a Cheltenham Festival race?", "Grand National fence", "Cheltenham race", ["Becher's Brook", "The Chair", "Canal Turn", "Valentine's"], ["Gold Cup", "Champion Hurdle", "Queen Mother Champion Chase", "Stayers' Hurdle"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-26.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
