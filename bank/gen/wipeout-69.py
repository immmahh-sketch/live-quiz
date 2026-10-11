# Bank session 11 Oct 2026: new Wipeout boards -> bank/wipeout-69.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})


board("Won Olympic gold for Team GB at Beijing 2008", "Sport", "hard", ["Olympics", "Beijing 2008", "Team GB"],
 ["Chris Hoy", "Rebecca Adlington", "Christine Ohuruogu", "Ben Ainslie", "Bradley Wiggins", "Victoria Pendleton", "Nicole Cooke", "James DeGale", "Tim Brabants", "Jason Kenny", "Rebecca Romero", "Geraint Thomas", "Ed Clancy", "Paul Goodison", "Zac Purchase"],
 ["Tom Daley", "Jessica Ennis", "Mo Farah", "Paula Radcliffe", "Phillips Idowu"])
board("Won Olympic gold for Team GB at Athens 2004", "Sport", "hard", ["Olympics", "Athens 2004", "Team GB"],
 ["Kelly Holmes", "Matthew Pinsent", "James Cracknell", "Steve Williams", "Ed Coode", "Bradley Wiggins", "Chris Hoy", "Ben Ainslie", "Shirley Robertson", "Sarah Webb", "Sarah Ayton", "Leslie Law", "Jason Gardener", "Mark Lewis-Francis", "Darren Campbell"],
 ["Amir Khan", "Paula Radcliffe", "Steve Redgrave", "Denise Lewis", "Jonathan Edwards"])
board("Won Olympic gold for Team GB at Sydney 2000", "Sport", "hard", ["Olympics", "Sydney 2000", "Team GB"],
 ["Steve Redgrave", "Matthew Pinsent", "James Cracknell", "Tim Foster", "Denise Lewis", "Jonathan Edwards", "Audley Harrison", "Jason Queally", "Ben Ainslie", "Iain Percy", "Shirley Robertson", "Stephanie Cook", "Richard Faulds", "Ben Hunt-Davis", "Kieran West"],
 ["Kelly Holmes", "Paula Radcliffe", "Darren Campbell", "Katharine Merry", "Chris Hoy"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-69.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
