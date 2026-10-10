# Bank session 10 Oct 2026: 60 more Countdown Conundrums -> bank/conundrum-6.json. Nine-letter everyday words with no
# other nine-letter anagram (SLAUGHTER/LAUGHTERS left out for that reason), no plurals or proper
# nouns, scrambled so no letter stays in its place. Checked against the words already in bank/conundrum*.json.
import json, os, random, glob
EASY = "SUBMARINE SUPERHERO SPACESHIP VALENTINE BEAUTIFUL TIMETABLE SKYDIVING STARLIGHT COUNTDOWN SUNSCREEN".split()
MEDIUM = ("QUICKSTEP SANDSTONE SCULPTURE SEASONING SEMIFINAL SHORTHAND SIDEBOARD SLAPSTICK SNOWDRIFT SOLICITOR SOMEWHERE "
          "SPARKLING SPECTACLE SPOKESMAN STATEMENT STOREROOM STRETCHER SURRENDER TOMBSTONE TRANSPORT TURQUOISE VIEWPOINT "
          "WALKABOUT WHOLESALE WINDSWEPT WITHDRAWN WORKBENCH YACHTSMAN ACCORDION BEEFEATER BIOGRAPHY BLACKMAIL BOULEVARD "
          "CAFETERIA CATHEDRAL CLOAKROOM").split()
HARD = "TECHNIQUE VERTEBRAE TREACHERY ANONYMOUS BUCCANEER SECONDARY RESIDENCE SENTIMENT TEMPORARY TERRITORY UNCERTAIN ADVERTISE AMAZEMENT REHEARSAL".split()
here = os.path.dirname(os.path.abspath(__file__))
have = {x["answers"][0] for f in glob.glob(os.path.join(here, '..', 'conundrum*.json')) if not f.endswith('conundrum-6.json') for x in json.load(open(f, encoding='utf-8'))}
rng = random.Random(202610106)
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
json.dump(out, open(os.path.join(here, '..', 'conundrum-6.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'conundrums written')
