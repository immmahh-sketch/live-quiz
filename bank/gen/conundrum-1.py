# Bank session 10 Oct 2026: the first Countdown Conundrums -> bank/conundrum.json. Nine-letter everyday words with
# no other nine-letter anagram, scrambled so no letter stays in its place. Marked exactly, so no plurals or proper nouns.
import json, os, random
EASY = "CHOCOLATE BUTTERFLY PINEAPPLE TELEPHONE SPAGHETTI HAMBURGER CROCODILE CHAMPAGNE SNOWFLAKE JELLYFISH BREAKFAST WATERFALL BUMBLEBEE".split()
MEDIUM = "SAXOPHONE PARACHUTE MARMALADE ADVENTURE BLUEBERRY CHEMISTRY GEOGRAPHY HURRICANE LIGHTNING ALLIGATOR ASTRONAUT DANDELION HAIRBRUSH HANDSHAKE MICROWAVE NIGHTMARE PANTOMIME VEGETABLE XYLOPHONE YESTERDAY ZOOKEEPER CASSEROLE DETECTIVE MOUSETRAP SCARECROW TELESCOPE CROSSWORD LIBRARIAN".split()
HARD = "DIRECTORY KNOWLEDGE LABYRINTH OBJECTIVE QUICKSAND FORTUNATE PERFORMER GARDENING SCRAMBLED".split()
rng = random.Random(20261010)
def scramble(w):
    while True:
        a = list(w); rng.shuffle(a); s = ''.join(a)
        if all(x != y for x, y in zip(s, w)): return s
out, seen = [], set()
for diff, words in (("easy", EASY), ("medium", MEDIUM), ("hard", HARD)):
    for w in words:
        assert len(w) == 9 and w.isalpha() and w not in seen, w
        seen.add(w)
        out.append({"type": "conundrum", "text": "Countdown Conundrum", "answers": [w], "letters": scramble(w), "difficulty": diff, "category": "Countdown Conundrum", "tags": ["Countdown", "anagrams"]})
here = os.path.dirname(os.path.abspath(__file__))
json.dump(out, open(os.path.join(here, '..', 'conundrum.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'conundrums written')
