# Bank session 12 Oct 2026: new Wipeout boards -> bank/wipeout-77.json. 15 right and 5 wrong each. Decoys need
# knowledge of the subject (memory: live-quiz-wipeout-decoys): near-misses from the same world, not a different set.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# decoys: big family sagas by other writers
board("Novels by Catherine Cookson", "Books", "medium", ["Catherine Cookson", "novels", "North East"],
 ["The Fifteen Streets", "The Mallen Streak", "The Cinder Path", "Tilly Trotter", "Katie Mulholland", "The Dwelling Place", "The Gambling Man", "The Black Velvet Gown", "Colour Blind", "Kate Hannigan", "The Round Tower", "Maggie Rowan", "The Glass Virgin", "The Girl", "The Rag Nymph"],
 ["Poldark", "The Thorn Birds", "Lace", "Riders", "A Woman of Substance"])
# decoys: big entertainment shows fronted by other people
board("Shows Ant and Dec have presented or starred in", "TV", "medium", ["Ant and Dec", "TV presenters", "North East"],
 ["Byker Grove", "SMTV Live", "CD:UK", "Pop Idol", "I'm a Celebrity... Get Me Out of Here!", "Saturday Night Takeaway", "Britain's Got Talent", "Push the Button", "Limitless Win", "PokerFace", "Red or Black?", "Gameshow Marathon", "Friends Like These", "The Ant & Dec Show", "Ant & Dec Unzipped"],
 ["The X Factor", "Total Wipeout", "The Big Breakfast", "Pointless", "Gladiators"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-77.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
