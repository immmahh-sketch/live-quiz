# Bank session 18 Oct 2026: 4 Categorise questions -> bank/sort-45.json. Two groups, four items each. Each pair of
# categories was probed against every Categorise question already in the live bank (Thunderbirds v Captain Scarlet,
# Shipping Forecast areas and Greek v Norse gods were already there).
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

# the trap: skirt (Norse) and shirt (Old English) began as the same word
s("Anagrams and wordplay", ["word origins", "Vikings", "Old English"], "hard", "Did this English word come from Old Norse or Old English?", "Old Norse", "Old English",
  ["Skirt", "Sky", "Egg", "Knife"], ["Shirt", "Heaven", "House", "Bread"])
s("Television", ["cartoons", "Hanna-Barbera", "Looney Tunes"], "medium", "A Hanna-Barbera character or a Looney Tunes character?", "Hanna-Barbera", "Looney Tunes",
  ["Yogi Bear", "Top Cat", "Huckleberry Hound", "Snagglepuss"], ["Bugs Bunny", "Daffy Duck", "Foghorn Leghorn", "Wile E. Coyote"])
s("British sitcoms", ["'Allo 'Allo", "Dad's Army", "David Croft"], "easy", "A character from 'Allo 'Allo! or from Dad's Army?", "'Allo 'Allo!", "Dad's Army",
  ["René", "Herr Flick", "Officer Crabtree", "Yvette"], ["Captain Mainwaring", "Private Pike", "Corporal Jones", "Private Godfrey"])
s("Television", ["Gladiators", "game shows"], "medium", "A gladiator from the 1990s ITV show or from the 2024 BBC revival?", "1990s", "2024",
  ["Wolf", "Jet", "Lightning", "Shadow"], ["Fury", "Legend", "Giant", "Sabre"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-45.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
