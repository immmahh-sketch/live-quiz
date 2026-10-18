# Bank session 18 Oct 2026: new Wipeout boards -> bank/wipeout-103.json (words that take an M in front; countries hidden in words).
# Same shapes as wipeout-92 to 94. Every decoy was checked letter by letter: no word made by putting M in front of Fish/Cup/
# Tree/Coin/Shoe, and no country (asserted against a list) hidden in Pillow/Garden/Button/Ladder/Basket.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# mice, mash, meat, maid, mother, moral, mask, many, master, march, mend, muse, moat, mink, mill
board("Words that make a new word when you put an M in front", "Anagrams and wordplay", "medium", ["wordplay", "letters"],
 ["Ice", "Ash", "Eat", "Aid", "Other", "Oral", "Ask", "Any", "Aster", "Arch", "End", "Use", "Oat", "Ink", "Ill"],
 ["Fish", "Cup", "Tree", "Coin", "Shoe"])
# wOMAN, rOMANce, rOMANtic, ottOMAN, PERUse, pIRANha, mIRANda, MALIce, MALIgn, forMALIse, aniMALIstic, inCUBAtor, sCUBA, FRANCEs, CHADwick
COUNTRIES = ["oman", "peru", "iran", "mali", "cuba", "chad", "france", "togo", "laos", "iraq", "niger", "spain", "chile", "india", "fiji", "japan",
             "china", "malta", "qatar", "nepal", "kenya", "sudan", "yemen", "wales", "italy", "benin", "gabon", "ghana", "haiti", "egypt", "syria",
             "libya", "tonga", "samoa", "nauru", "palau", "israel", "cyprus", "greece", "russia", "brazil", "canada", "mexico"]
RIGHT = ["Woman", "Romance", "Romantic", "Ottoman", "Peruse", "Piranha", "Miranda", "Malice", "Malign", "Formalise", "Animalistic", "Incubator", "Scuba", "Frances", "Chadwick"]
WRONG = ["Pillow", "Garden", "Button", "Ladder", "Basket"]
assert all(any(v in w.lower() for v in COUNTRIES) for w in RIGHT)
assert not [w for w in WRONG if any(v in w.lower() for v in COUNTRIES)]
board("Words with a country hidden inside them", "Anagrams and wordplay", "hard", ["wordplay", "hidden words", "countries"], RIGHT, WRONG)

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-103.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
