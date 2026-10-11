# Bank session 11 Oct 2026: more Categorise questions -> bank/sort-23.json. Two groups, three or four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})


s("Music", ["dance crazes", "1990s", "2010s"], "easy", "A 1990s dance craze or a 2010s one?", "1990s", "2010s", ["Macarena", "Vogue", "Achy Breaky Heart line dance", "Cotton Eye Joe"], ["Gangnam Style", "The Floss", "The Dab", "Harlem Shake"])
s("North East", ["Newcastle", "Sunderland", "famous people"], "medium", "Born in Newcastle or born in Sunderland?", "Newcastle", "Sunderland", ["Alan Shearer", "Cheryl", "Jimmy Nail", "Hank Marvin"], ["Dave Stewart", "Kate Adie", "Jordan Pickford", "Jordan Henderson"])
s("History", ["Vikings", "Anglo-Saxons", "kings"], "medium", "A Viking king or an Anglo-Saxon king?", "Viking", "Anglo-Saxon", ["Cnut", "Sweyn Forkbeard", "Harald Hardrada", "Eric Bloodaxe"], ["Alfred the Great", "Athelstan", "Edward the Confessor", "Harold Godwinson"])
s("World geography", ["national parks", "USA", "Canada"], "medium", "A national park in the USA or in Canada?", "USA", "Canada", ["Yellowstone", "Yosemite", "Zion", "Everglades"], ["Banff", "Jasper", "Yoho", "Pacific Rim"])
s("Music", ["The Beatles", "The Rolling Stones", "wives"], "hard", "Married a Beatle or married a Rolling Stone?", "A Beatle", "A Rolling Stone", ["Yoko Ono", "Linda Eastman", "Cynthia Powell", "Barbara Bach"], ["Bianca Pérez-Mora", "Patti Hansen", "Mandy Smith", "Jo Karslake"])
s("Film", ["Carry On", "Dad's Army", "comedy actors"], "medium", "A Carry On regular or a Dad's Army star?", "Carry On", "Dad's Army", ["Sid James", "Kenneth Williams", "Barbara Windsor", "Hattie Jacques"], ["Arthur Lowe", "John Le Mesurier", "Clive Dunn", "Ian Lavender"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-23.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
