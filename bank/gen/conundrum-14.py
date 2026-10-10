# Bank session 10 Oct 2026: 30 more Countdown Conundrums -> bank/conundrum-14.json. Nine-letter everyday words with no
# other nine-letter anagram (only words with a single anagram), no plurals or proper
# nouns, scrambled so no letter stays in its place. Checked against the words already in bank/conundrum*.json.
import json, os, random, glob
# TANGERINE is left out: its letters also make ARGENTINE (silvery).
EASY = "HOUSEWORK SCHOOLBAG RAINSTORM SPOTLIGHT TRACKSUIT NIGHTCLUB FORTNIGHT FARMHOUSE".split()
MEDIUM = ("BOOKSTALL FRAMEWORK GUESSWORK BLOODSHOT HEARTBURN TEAKETTLE GINGERNUT SPEARMINT CELEBRATE BROADBAND "
          "NIGHTFALL NIGHTLIFE WEEKNIGHT GRASSLAND WAREHOUSE OVERSIGHT OVERDRAFT").split()
HARD = "CAMEMBERT METRONOME MANDOLINE OUTNUMBER OUTSPOKEN".split()
here = os.path.dirname(os.path.abspath(__file__))
have = {x["answers"][0] for f in glob.glob(os.path.join(here, '..', 'conundrum*.json')) if not f.endswith('conundrum-14.json') for x in json.load(open(f, encoding='utf-8'))}
rng = random.Random(202610114)
def scramble(w):
    # As few letters left in place as possible: none where the word allows (BEEKEEPER has too many Es to move them all).
    best, fewest = None, 99
    for _ in range(3000):
        a = list(w); rng.shuffle(a); s = ''.join(a)
        fixed = sum(x == y for x, y in zip(s, w))
        if s != w and fixed < fewest: best, fewest = s, fixed
        if fewest == 0: break
    return best
out, seen = [], set(have)
for diff, words in (("easy", EASY), ("medium", MEDIUM), ("hard", HARD)):
    for w in words:
        assert len(w) == 9 and w.isalpha() and w not in seen, w
        seen.add(w)
        out.append({"type": "conundrum", "text": "Countdown Conundrum", "answers": [w], "letters": scramble(w), "difficulty": diff, "category": "Countdown Conundrum", "tags": ["Countdown", "anagrams"]})
json.dump(out, open(os.path.join(here, '..', 'conundrum-14.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'conundrums written')
