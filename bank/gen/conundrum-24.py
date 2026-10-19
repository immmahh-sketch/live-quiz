# Bank session 19 Oct 2026: more Countdown Conundrums -> bank/conundrum-24.json. Nine-letter everyday words with no other
# nine-letter anagram (rare letters and doubled letters help), no plurals or proper nouns, scrambled so no letter stays in its
# place. Words already in bank/conundrum*.json are skipped, not repeated.
import json, os, random, glob
EASY = ("LUNCHTIME SKATEPARK HOUSEMATE JEWELLERY").split()
MEDIUM = ("BOWSTRING HYPNOTIST NOCTURNAL PARCHMENT THESAURUS KICKBOXER NUMBSKULL").split()
HARD = ("DEXTERITY QUICKLIME").split()
# The bank is close to full: of about 230 everyday nine-letter words tried in three batches (compounds, animals, foods, jobs,
# objects), only these 13 were new. Each checked for a second nine-letter anagram; none has one.
here = os.path.dirname(os.path.abspath(__file__))
have = {x["answers"][0] for f in glob.glob(os.path.join(here, '..', 'conundrum*.json')) if not f.endswith('conundrum-24.json') for x in json.load(open(f, encoding='utf-8'))}
rng = random.Random(202610192)
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
json.dump(out, open(os.path.join(here, '..', 'conundrum-24.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'conundrums written; already in the bank:', ' '.join(skipped))
