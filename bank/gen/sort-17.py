# Bank session 11 Oct 2026: 11 more Categorise questions -> bank/sort-14.json. Two groups, three or four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Cars and motoring", ["Ford", "Vauxhall"], "easy", "A Ford or a Vauxhall?", "Ford", "Vauxhall", ["Fiesta", "Focus", "Mondeo", "Escort"], ["Corsa", "Astra", "Vectra", "Cavalier"])
s("Food and drink", ["Italian food", "pasta", "bread"], "easy", "A pasta or an Italian bread?", "Pasta", "Bread", ["Penne", "Fusilli", "Farfalle", "Linguine"], ["Focaccia", "Ciabatta", "Grissini", "Panettone"])
s("Books", ["Shakespeare", "Charles Dickens"], "easy", "A Shakespeare play or a Dickens novel?", "Shakespeare", "Dickens", ["Hamlet", "Othello", "Macbeth", "The Tempest"], ["Bleak House", "Hard Times", "Great Expectations", "Little Dorrit"])
s("World geography", ["volcanoes", "mountains"], "medium", "A volcano, or a mountain that isn't one?", "Volcano", "Not a volcano", ["Etna", "Vesuvius", "Kilimanjaro", "Mount Fuji"], ["Everest", "K2", "Matterhorn", "Mont Blanc"])
s("World geography", ["USA", "Canada"], "medium", "A US state or a Canadian province?", "US state", "Canadian province", ["Oregon", "Ohio", "Idaho", "Maine"], ["Ontario", "Quebec", "Alberta", "Manitoba"])
s("Games and toys", ["board games", "video games"], "easy", "A board game or a video game?", "Board game", "Video game", ["Cluedo", "Risk", "Ludo", "Trivial Pursuit"], ["Tetris", "Minecraft", "Sonic the Hedgehog", "Fortnite"])
s("Science and nature", ["clouds", "rocks"], "easy", "A type of cloud or a type of rock?", "Cloud", "Rock", ["Cumulus", "Stratus", "Cirrus", "Nimbostratus"], ["Granite", "Basalt", "Slate", "Marble"])
s("Football", ["London", "Manchester"], "medium", "A club from Greater London or from Greater Manchester?", "London", "Manchester", ["Arsenal", "Chelsea", "Fulham", "Brentford"], ["Bolton Wanderers", "Wigan Athletic", "Salford City", "Stockport County"])
s("Animals", ["horses", "dogs", "breeds"], "medium", "A horse breed or a dog breed?", "Horse", "Dog", ["Shire", "Clydesdale", "Appaloosa", "Arabian"], ["Dalmatian", "Weimaraner", "Saluki", "Akita"])
s("Film", ["James Bond", "Sean Connery", "Daniel Craig"], "easy", "A Sean Connery Bond film or a Daniel Craig one?", "Sean Connery", "Daniel Craig", ["Goldfinger", "Thunderball", "Dr. No", "From Russia with Love"], ["Skyfall", "Casino Royale", "Spectre", "No Time to Die"])
s("Sport", ["Formula One", "horse racing"], "easy", "A Formula One driver or a jockey?", "F1 driver", "Jockey", ["Lewis Hamilton", "Jenson Button", "Nigel Mansell", "Damon Hill"], ["Frankie Dettori", "Tony McCoy", "Lester Piggott", "Hollie Doyle"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-14.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
