# Bank session 11 Oct 2026: more Categorise questions -> bank/sort-22.json. Two groups, three or four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})


s("Sport", ["skiing", "France", "Switzerland"], "medium", "A ski resort in France or in Switzerland?", "France", "Switzerland", ["Val d'Isère", "Chamonix", "Courchevel", "Méribel"], ["Zermatt", "Verbier", "St Moritz", "Davos"])
s("History", ["ships", "castles"], "easy", "Part of a ship or part of a castle?", "Ship", "Castle", ["Bow", "Stern", "Hull", "Keel"], ["Keep", "Moat", "Battlements", "Drawbridge"])
s("Books", ["Jacqueline Wilson", "Enid Blyton", "children's books"], "medium", "A Jacqueline Wilson book or an Enid Blyton book?", "Jacqueline Wilson", "Enid Blyton", ["The Story of Tracy Beaker", "The Illustrated Mum", "Double Act", "Hetty Feather"], ["The Magic Faraway Tree", "Malory Towers", "Five on a Treasure Island", "The Naughtiest Girl in the School"])
s("Books", ["Tolkien", "Narnia", "fantasy"], "easy", "A Tolkien character or a Narnia character?", "Tolkien", "Narnia", ["Bilbo", "Gimli", "Legolas", "Galadriel"], ["Aslan", "Mr Tumnus", "Reepicheep", "Puddleglum"])
s("World geography", ["capital cities", "USA", "Canada"], "hard", "A US state capital or a Canadian provincial capital?", "US state capital", "Canadian provincial capital", ["Sacramento", "Albany", "Austin", "Tallahassee"], ["Toronto", "Victoria", "Halifax", "Winnipeg"])
s("Sport", ["tennis", "cricket", "jargon"], "medium", "A tennis term or a cricket term?", "Tennis", "Cricket", ["Deuce", "Let", "Ace", "Tie-break"], ["Googly", "Yorker", "Maiden", "Duck"])
s("Animals", ["cats", "rabbits", "breeds"], "medium", "A breed of cat or a breed of rabbit?", "Cat", "Rabbit", ["Siamese", "Persian", "Maine Coon", "Ragdoll"], ["Netherland Dwarf", "Flemish Giant", "Lionhead", "English Lop"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-22.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
