# Bank session 19 Oct 2026: more Countdown Conundrums -> bank/conundrum-23.json. Nine-letter everyday words with no other
# nine-letter anagram (picked for unusual letter mixes: J, Q, X, K, W, Y and doubled letters), no plurals or proper nouns,
# scrambled so no letter stays in its place. Words already in bank/conundrum*.json are skipped, not repeated.
import json, os, random, glob
EASY = ("ABANDONED ABSORBING HANDIWORK WINDBREAK WORKHOUSE GUMSHIELD").split()
MEDIUM = ("ACCLAIMED ESPLANADE KINGMAKER LIGHTSHIP PARAGLIDE ROADHOUSE TABLELAND").split()
HARD = ("ENCHANTER NIGHTHAWK SOAPSTONE WOODCHUCK").split()
# The bank is nearly full of everyday nine-letter words: of about 250 more candidates only these were new. Left out: plurals,
# proper nouns (Excalibur, Kitchener, Springbok), things usually written as two words (water butt, piggy bank), and
# MILESTONE, which is also LIMESTONE.
here = os.path.dirname(os.path.abspath(__file__))
have = {x["answers"][0] for f in glob.glob(os.path.join(here, '..', 'conundrum*.json')) if not f.endswith('conundrum-23.json') for x in json.load(open(f, encoding='utf-8'))}
rng = random.Random(202610191)
def scramble(w):
    best, fewest = None, 99
    for _ in range(3000):
        a = list(w); rng.shuffle(a); s = ''.join(a)
        fixed = sum(x == y for x, y in zip(s, w))
        if s != w and fixed < fewest: best, fewest = s, fixed
        if fewest == 0: break
    return best
out, seen, skipped = [], set(have), []
for diff, words in (("easy", EASY), ("medium", MEDIUM), ("hard", HARD)):
    for w in words:
        assert len(w) == 9 and w.isalpha(), w
        if w in seen: skipped.append(w); continue
        seen.add(w)
        out.append({"type": "conundrum", "text": "Countdown Conundrum", "answers": [w], "letters": scramble(w), "difficulty": diff, "category": "Countdown Conundrum", "tags": ["Countdown", "anagrams"]})
json.dump(out, open(os.path.join(here, '..', 'conundrum-23.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'conundrums written; already in the bank:', ' '.join(skipped))
