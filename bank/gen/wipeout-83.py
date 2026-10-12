# Bank session 12 Oct 2026: new Wipeout boards -> bank/wipeout-83.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# decoys: presenters of other car shows (Wheeler Dealers, Car SOS, Speed)
board("People who have presented 'Top Gear' (any era)", "TV", "medium", ["Top Gear", "cars", "presenters"],
 ["Jeremy Clarkson", "Richard Hammond", "James May", "Freddie Flintoff", "Paddy McGuinness", "Chris Harris", "Matt LeBlanc", "Chris Evans", "Rory Reid", "Sabine Schmitz", "Angela Rippon", "Noel Edmonds", "William Woollard", "Quentin Willson", "Tiff Needell"],
 ["Mike Brewer", "Edd China", "Ant Anstead", "Guy Martin", "Tim Shaw"])
# decoys: The Apprentice's boss and aides, and an American Shark
board("Dragons on 'Dragons' Den' (any series)", "TV", "medium", ["Dragons' Den", "business", "North East"],
 ["Peter Jones", "Deborah Meaden", "Theo Paphitis", "Duncan Bannatyne", "Touker Suleyman", "Sara Davies", "Steven Bartlett", "Tej Lalvani", "Jenny Campbell", "Nick Jenkins", "Hilary Devey", "Kelly Hoppen", "Piers Linney", "James Caan", "Rachel Elnaugh"],
 ["Karren Brady", "Nick Hewer", "Alan Sugar", "Margaret Mountford", "Mark Cuban"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-83.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
