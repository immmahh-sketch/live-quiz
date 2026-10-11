# Bank session 11 Oct 2026: new Wipeout boards -> bank/wipeout-68.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})


board("Won Olympic gold for Team GB at Tokyo 2020", "Sport", "hard", ["Olympics", "Tokyo 2020", "Team GB"],
 ["Tom Daley", "Adam Peaty", "Max Whitlock", "Laura Kenny", "Jason Kenny", "Tom Pidcock", "Charlotte Worthington", "Lauren Price", "Galal Yafai", "Bethany Shriever", "Matt Walls", "Tom Dean", "Duncan Scott", "Giles Scott", "Hannah Mills"],
 ["Dina Asher-Smith", "Keely Hodgkinson", "Jade Jones", "Alex Yee", "Bianca Walkden"])
board("Won Olympic gold for Team GB at Paris 2024", "Sport", "hard", ["Olympics", "Paris 2024", "Team GB"],
 ["Keely Hodgkinson", "Alex Yee", "Tom Pidcock", "Matt Richards", "Tom Dean", "Duncan Scott", "James Guy", "Emma Finucane", "Katy Marchant", "Sophie Capewell", "Ellie Aldridge", "Emily Craig", "Imogen Grant", "Lola Anderson", "Lauren Henry"],
 ["Adam Peaty", "Tom Daley", "Max Whitlock", "Jade Jones", "Dina Asher-Smith"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-68.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
