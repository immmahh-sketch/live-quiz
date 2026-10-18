# Bank session 18 Oct 2026: new Wipeout boards -> bank/wipeout-98.json (words that take an F in front; seas, lakes and rivers hidden in words).
# Same shapes as wipeout-92 to 94. Every decoy was checked letter by letter: no word made by putting F in front of Cup/Pen/
# Tree/Sock/Bread, and no stretch of water (asserted against a list) hidden in Pillow/Garden/Tunnel/Button/Ladder.
import json, os
B = []
def board(text, cat, diff, tags, right, wrong):
    assert len(right) == 15 and len(set(right)) == 15, (text, len(right))
    assert len(wrong) == 5 and len(set(wrong)) == 5, (text, len(wrong))
    assert not set(right) & set(wrong), text
    B.append({"type": "wipeout", "text": text, "right": right, "wrong": wrong, "difficulty": diff, "category": cat, "tags": tags})

# flag, fear, flame, fox, face, fair, fill, farm, flake, flock, fright, fate, four, flint, frail
board("Words that make a new word when you put an F in front", "Anagrams and wordplay", "easy", ["wordplay", "letters"],
 ["Lag", "Ear", "Lame", "Ox", "Ace", "Air", "Ill", "Arm", "Lake", "Lock", "Right", "Ate", "Our", "Lint", "Rail"],
 ["Cup", "Pen", "Tree", "Sock", "Bread"])
# SEAson, SEAt, reSEArch, diSEAse, ChelSEA, SEAnce, fLAKE, sLAKE, PONDer, corresPOND, dRIVER, sPOOL, MEREly, BAYonet, TARNish
WATERS = ["sea", "lake", "pond", "river", "pool", "mere", "bay", "tarn", "loch", "lough", "burn", "beck", "brook", "stream", "ocean",
          "well", "canal", "dam", "firth", "bog", "marsh", "fen", "mire", "sound", "tide", "rill", "ria", "lagoon", "fjord", "reservoir"]
RIGHT = ["Season", "Seat", "Research", "Disease", "Chelsea", "Seance", "Flake", "Slake", "Ponder", "Correspond", "Driver", "Spool", "Merely", "Bayonet", "Tarnish"]
WRONG = ["Pillow", "Garden", "Tunnel", "Button", "Ladder"]
assert all(any(v in w.lower() for v in WATERS) for w in RIGHT)
assert not [w for w in WRONG if any(v in w.lower() for v in WATERS)]
board("Words with a stretch of water hidden inside them", "Anagrams and wordplay", "hard", ["wordplay", "hidden words", "water"], RIGHT, WRONG)

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'wipeout-98.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'wipeout boards written')
