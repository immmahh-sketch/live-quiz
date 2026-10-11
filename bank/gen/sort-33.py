# Bank session 11 Oct 2026: more Categorise questions -> bank/sort-30.json. Two groups, three or four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})


s("TV", ["The Crystal Maze", "Gladiators", "game shows"], "medium", "A Crystal Maze zone or a Gladiators event?", "Crystal Maze zone", "Gladiators event", ["Aztec", "Industrial", "Futuristic", "Medieval"], ["Hang Tough", "Atlaspheres", "Duel", "The Eliminator"])
s("TV", ["The Chase", "Eggheads", "quizzers"], "medium", "A Chaser or an Egghead?", "Chaser", "Egghead", ["Mark Labbett", "Anne Hegerty", "Shaun Wallace", "Paul Sinha"], ["Judith Keppel", "Kevin Ashman", "Daphne Fowler", "CJ de Mooi"])
s("TV", ["Only Fools and Horses", "Fawlty Towers", "sitcoms"], "easy", "An Only Fools and Horses character or a Fawlty Towers character?", "Only Fools and Horses", "Fawlty Towers", ["Rodney", "Trigger", "Boycie", "Marlene"], ["Sybil", "Manuel", "Polly", "Major Gowen"])
s("TV", ["Love Island", "I'm a Celebrity", "reality TV"], "easy", "Something from Love Island or from I'm a Celebrity?", "Love Island", "I'm a Celebrity", ["Casa Amor", "Recoupling", "Beach Hut", "Hideaway"], ["Bushtucker trial", "Dingo Dollar challenge", "Bush Telegraph", "Kiosk Keith"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-30.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
