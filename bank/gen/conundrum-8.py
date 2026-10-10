# Bank session 10 Oct 2026: 60 more Countdown Conundrums -> bank/conundrum-8.json. Nine-letter everyday words with no
# other nine-letter anagram (only words with a single anagram), no plurals or proper
# nouns, scrambled so no letter stays in its place. Checked against the words already in bank/conundrum*.json.
import json, os, random, glob
EASY = "SNOWBOARD SUPERSTAR STORYBOOK PIGGYBACK SCHOOLBOY TIGHTROPE SWEETSHOP SOMETIMES RAINWATER PUNCHLINE".split()
MEDIUM = ("METEORITE MIDWINTER NEWSFLASH OFFSPRING OVERWHELM PAINTBALL PARAMEDIC LITERALLY MARKETING PATRIOTIC PENFRIEND "
          "PERFECTLY PETTICOAT PITCHFORK POWERBOAT PROSECUTE PUPPETEER RECEPTION REINFORCE RIGHTEOUS SAFEGUARD SALVATION "
          "SANCTUARY SARCASTIC SCAPEGOAT SCORECARD SINGALONG SKINFLINT SLINGSHOT SPEARHEAD SPRINKLER STALEMATE STARGAZER "
          "STEAMSHIP STRONGMAN SUGARCANE").split()
HARD = "OBLIVIOUS MATRIMONY MAGNETISM MERRIMENT PLAINTIFF PROFANITY RELUCTANT SKEDADDLE SUCCULENT SPINNAKER TELEPATHY ZOOLOGIST OBSESSION NUTRITION".split()
here = os.path.dirname(os.path.abspath(__file__))
have = {x["answers"][0] for f in glob.glob(os.path.join(here, '..', 'conundrum*.json')) if not f.endswith('conundrum-8.json') for x in json.load(open(f, encoding='utf-8'))}
rng = random.Random(202610108)
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
json.dump(out, open(os.path.join(here, '..', 'conundrum-8.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'conundrums written')
