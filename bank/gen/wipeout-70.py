# Bank session 11 Oct 2026: new Wipeout boards -> bank/wipeout-70.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})


board("Won Olympic gold for Team GB at Rio 2016", "Sport", "hard", ["Olympics", "Rio 2016", "Team GB"],
 ["Mo Farah", "Jason Kenny", "Laura Kenny", "Max Whitlock", "Adam Peaty", "Nicola Adams", "Andy Murray", "Alistair Brownlee", "Charlotte Dujardin", "Joe Clarke", "Liam Heath", "Jade Jones", "Giles Scott", "Helen Glover", "Kate Richardson-Walsh"],
 ["Tom Daley", "Jessica Ennis-Hill", "Greg Rutherford", "Bryony Page", "Jonny Brownlee"])
board("In England's squad at the 2023 Women's World Cup", "Football", "medium", ["Lionesses", "England", "World Cup"],
 ["Mary Earps", "Lucy Bronze", "Jess Carter", "Alex Greenwood", "Millie Bright", "Keira Walsh", "Georgia Stanway", "Ella Toone", "Lauren James", "Lauren Hemp", "Alessia Russo", "Chloe Kelly", "Rachel Daly", "Niamh Charles", "Laura Coombs"],
 ["Beth Mead", "Leah Williamson", "Fran Kirby", "Beth England", "Jill Scott"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-70.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
