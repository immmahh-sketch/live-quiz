# Bank session 12 Oct 2026: new Wipeout boards -> bank/wipeout-85.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# decoys: jungle and savannah characters from other Disney films
board("Characters in 'The Jungle Book' (Kipling's book or the Disney film)", "Books", "medium", ["The Jungle Book", "Kipling", "Disney"],
 ["Mowgli", "Baloo", "Bagheera", "Shere Khan", "Kaa", "Akela", "Raksha", "Hathi", "Tabaqui", "Grey Brother", "Rikki-Tikki-Tavi", "Chil", "Bandar-log", "Messua", "King Louie"],
 ["Rafiki", "Timon", "Abu", "Kerchak", "Simba"])
# decoys: animal heroes from other classic children's books
board("Characters in 'The Wind in the Willows'", "Books", "medium", ["The Wind in the Willows", "Kenneth Grahame", "children's books"],
 ["Mole", "Ratty", "Mr Toad", "Badger", "Otter", "Portly", "Chief Weasel", "The gaoler's daughter", "The washerwoman", "The bargewoman", "The Sea Rat", "Pan", "Alfred the horse", "The engine driver", "The field mice"],
 ["Peter Rabbit", "Squirrel Nutkin", "Brer Rabbit", "Fantastic Mr Fox", "Hazel"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-85.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
