# Bank session 10 Oct 2026: 60 more Countdown Conundrums -> bank/conundrum-4.json. Nine-letter everyday words with no
# other nine-letter anagram (only words with a single anagram), no plurals or proper
# nouns, scrambled so no letter stays in its place. Checked against the words already in bank/conundrum*.json.
import json, os, random, glob
EASY = "ASPARAGUS LAWNMOWER BRIEFCASE PAPERCLIP HEARTBEAT WONDERFUL BOOMERANG FURNITURE SOMETHING DANGEROUS".split()
MEDIUM = ("AUBERGINE COURGETTE GUACAMOLE PISTACHIO BUTTERNUT CHAMELEON WOLVERINE TARANTULA ANGELFISH BARRACUDA ARMADILLO "
          "ALBATROSS CLIPBOARD DRAINPIPE HANDBRAKE LAMPSHADE WASHBASIN WRISTBAND ABUNDANCE CHARACTER CHILDHOOD CONFUSION "
          "DIFFICULT DISCOVERY ENCOURAGE EXCELLENT SCIENTIST TELEGRAPH YOUNGSTER IMPORTANT BACKSTAGE BEDSPREAD ASTRONOMY "
          "LANDSCAPE SANDPAPER VOLUNTEER").split()
HARD = "CORIANDER CHIPOLATA CENTIPEDE CORMORANT WOODLOUSE MAGNITUDE NARRATIVE VARIATION SECRETARY ENDURANCE OPERATION DIRECTION SENSATION AGREEMENT".split()
here = os.path.dirname(os.path.abspath(__file__))
have = {x["answers"][0] for f in glob.glob(os.path.join(here, '..', 'conundrum*.json')) if not f.endswith('conundrum-4.json') for x in json.load(open(f, encoding='utf-8'))}
rng = random.Random(202610104)
def scramble(w):
    while True:
        a = list(w); rng.shuffle(a); s = ''.join(a)
        if all(x != y for x, y in zip(s, w)): return s
out, seen = [], set(have)
for diff, words in (("easy", EASY), ("medium", MEDIUM), ("hard", HARD)):
    for w in words:
        assert len(w) == 9 and w.isalpha() and w not in seen, w
        seen.add(w)
        out.append({"type": "conundrum", "text": "Countdown Conundrum", "answers": [w], "letters": scramble(w), "difficulty": diff, "category": "Countdown Conundrum", "tags": ["Countdown", "anagrams"]})
json.dump(out, open(os.path.join(here, '..', 'conundrum-4.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'conundrums written')
