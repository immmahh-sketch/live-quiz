# Bank session 11 Oct 2026: new Wipeout boards -> bank/wipeout-67.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})


board("In England's squad at the 2022 World Cup", "Football", "medium", ["England", "Qatar 2022", "World Cup"],
 ["Jordan Pickford", "Kyle Walker", "John Stones", "Harry Maguire", "Luke Shaw", "Kieran Trippier", "Trent Alexander-Arnold", "Declan Rice", "Jude Bellingham", "Jordan Henderson", "Phil Foden", "Bukayo Saka", "Marcus Rashford", "Harry Kane", "Callum Wilson"],
 ["Tammy Abraham", "Ivan Toney", "Tyrone Mings", "Jadon Sancho", "Fikayo Tomori"])
board("In England's squad at Euro 2024", "Football", "medium", ["England", "Euro 2024"],
 ["Jordan Pickford", "Kyle Walker", "John Stones", "Marc Guéhi", "Luke Shaw", "Kieran Trippier", "Declan Rice", "Jude Bellingham", "Kobbie Mainoo", "Phil Foden", "Bukayo Saka", "Cole Palmer", "Anthony Gordon", "Harry Kane", "Ollie Watkins"],
 ["Jack Grealish", "James Maddison", "Marcus Rashford", "Harry Maguire", "Jordan Henderson"])
board("Played for Newcastle under Eddie Howe", "Football", "medium", ["Newcastle United", "Eddie Howe"],
 ["Nick Pope", "Kieran Trippier", "Sven Botman", "Fabian Schär", "Dan Burn", "Bruno Guimarães", "Joelinton", "Sandro Tonali", "Sean Longstaff", "Joe Willock", "Anthony Gordon", "Alexander Isak", "Callum Wilson", "Jacob Murphy", "Harvey Barnes"],
 ["Ayoze Pérez", "Salomón Rondón", "Christian Atsu", "Andy Carroll", "Yoshinori Muto"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-67.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
