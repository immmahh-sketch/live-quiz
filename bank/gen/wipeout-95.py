# Bank session 18 Oct 2026: new Wipeout boards -> bank/wipeout-95.json (words that take a T in front; fruits hidden in words).
# Same shapes as wipeout-92 to 94. Every decoy was checked letter by letter: no word made by putting T in front of Fish/Lamp/
# Moon/Desk/Book, and no fruit hidden in Carpet/Teacup/Blanket/Ladder/Hammer.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# train, trash, that, there, twig, twin, trust, tape, tear, tall, trap, trip, tale, told, toil
board("Words that make a new word when you put a T in front", "Anagrams and wordplay", "easy", ["wordplay", "letters"],
 ["Rain", "Rash", "Hat", "Here", "Wig", "Win", "Rust", "Ape", "Ear", "All", "Rap", "Rip", "Ale", "Old", "Oil"],
 ["Fish", "Lamp", "Moon", "Desk", "Book"])
# FIGure, FIGhter, FIGment, apPEAR, sPEAR, PEARl, PLUMber, PLUMage, subLIME, LIMErick, upDATE, seDATE, candiDATE, grAPPLEd, dAPPLE
board("Words with a fruit hidden inside them", "Anagrams and wordplay", "medium", ["wordplay", "hidden words", "fruit"],
 ["Figure", "Fighter", "Figment", "Appear", "Spear", "Pearl", "Plumber", "Plumage", "Sublime", "Limerick", "Update", "Sedate", "Candidate", "Grappled", "Dapple"],
 ["Carpet", "Teacup", "Blanket", "Ladder", "Hammer"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-95.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
