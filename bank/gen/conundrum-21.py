# Bank session 18 Oct 2026: more Countdown Conundrums -> bank/conundrum-21.json. Nine-letter everyday words with no other
# nine-letter anagram (picked for unusual letter mixes: J, Q, X, K, W, Y and doubled letters), no plurals or proper nouns,
# scrambled so no letter stays in its place. Words already in bank/conundrum*.json are skipped, not repeated.
import json, os, random, glob
EASY = ("AFTERLIFE BALANCING BROTHERLY COMPUTING DREAMLAND EXPENSIVE GRADUALLY HANDLEBAR MEMORABLE PROGRAMME SUNBURNED "
        "THUNDERED FEATHERED").split()
MEDIUM = ("AERODROME ALONGSIDE BAKEHOUSE EDITORIAL EIDERDOWN EXHIBITOR GRUMBLING HYPOCRITE INFLUENCE INNKEEPER LAUGHABLE "
          "MASTERFUL NORTHWARD PLENTIFUL PROMENADE SOUTHWARD TRIUMPHED BARBECUED MAGNIFIED JOURNEYED AWARENESS").split()
HARD = ("ELBOWROOM NAUGHTILY OBSTINATE PRIVILEGE RESTFULLY SIGHTSEER SQUEAMISH SYMPHONIC WORDSMITH ZIGZAGGED MODERNISE "
        "DEADLIEST").split()
# Left out: everyday words already in the bank (jellyfish, crossword, snowflake and 30 more), plurals, and words with a
# second anagram: LIMESTONE (MILESTONE), COASTLINE (SECTIONAL), ORCHESTRA (CARTHORSE).
here = os.path.dirname(os.path.abspath(__file__))
have = {x["answers"][0] for f in glob.glob(os.path.join(here, '..', 'conundrum*.json')) if not f.endswith('conundrum-21.json') for x in json.load(open(f, encoding='utf-8'))}
rng = random.Random(202610180)
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
json.dump(out, open(os.path.join(here, '..', 'conundrum-21.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'conundrums written; already in the bank:', ' '.join(skipped))
