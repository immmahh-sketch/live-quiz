# Bank session 11 Oct 2026: new Wipeout boards -> bank/wipeout-66.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})


board("In England's squad at the 2018 World Cup", "Football", "medium", ["England", "Russia 2018", "World Cup"],
 ["Jordan Pickford", "Kyle Walker", "John Stones", "Harry Maguire", "Kieran Trippier", "Ashley Young", "Danny Rose", "Gary Cahill", "Jordan Henderson", "Eric Dier", "Jesse Lingard", "Dele Alli", "Harry Kane", "Raheem Sterling", "Jamie Vardy"],
 ["Joe Hart", "Jack Wilshere", "Adam Lallana", "Chris Smalling", "Wayne Rooney"])
board("In England's squad at Euro 2020", "Football", "medium", ["England", "Euro 2020"],
 ["Jordan Pickford", "Kyle Walker", "John Stones", "Harry Maguire", "Luke Shaw", "Kieran Trippier", "Declan Rice", "Kalvin Phillips", "Mason Mount", "Jude Bellingham", "Jack Grealish", "Bukayo Saka", "Raheem Sterling", "Harry Kane", "Marcus Rashford"],
 ["Jesse Lingard", "Fikayo Tomori", "Eric Dier", "James Ward-Prowse", "Ollie Watkins"])
board("Professional dancers on Strictly Come Dancing", "TV", "medium", ["Strictly Come Dancing", "dancers"],
 ["Anton Du Beke", "Brendan Cole", "Karen Hauer", "Kevin Clifton", "Gorka Márquez", "Giovanni Pernice", "Aljaž Škorjanec", "Janette Manrara", "Oti Mabuse", "Johannes Radebe", "Dianne Buswell", "Nadiya Bychkova", "Amy Dowden", "Nikita Kuzmin", "Vito Coppola"],
 ["Shirley Ballas", "Motsi Mabuse", "Craig Revel Horwood", "Arlene Phillips", "Bruno Tonioli"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-66.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
