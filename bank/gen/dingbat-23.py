# Bank session 18 Oct 2026: more dingbats -> bank/dingbat-23.json. Checked against every answer already in the bank (live and files).
# Elements: t text, x/y 0–100 (centre), s size 1–6, optional rot, flip "h"/"v", style strike/underline/box/outline, color #hex.
# Fit (memory: live-quiz-dingbat-fit): every line kept to (characters × size) ≤ 34; text on its side to about 19.
import json, os, glob
B = []
def d(answers, cat, diff, *els, tags=()):
    B.append({"answers": answers, "elements": [dict(e) for e in els], "category": cat, "tags": list(tags), "difficulty": diff})
def e(t, x=50, y=50, s=5, **k): return {"t": t, "x": x, "y": y, "s": s, **k}
PURPLE = "#7b2fbe"
NL = chr(10)

# candidates (the clash filter below drops any already in the bank), picked from the free phrases found last time.
RED = "#d62828"
d(['Over the top'], 'Phrase', 'easy', e('OVER', y=22, s=3), e('TOP', y=60, s=6))
d(["You're under arrest", 'Under arrest'], 'Phrase', 'medium', e('ARREST', y=35, s=5), e('YOU', y=70, s=4))
d(['Second hand', 'Second-hand'], 'Phrase', 'medium', e('HAND', x=27, s=4), e('HAND', x=73, s=4, color=RED))
d(['Big fish in a small pond'], 'Phrase', 'hard', e('FISH', y=38, s=6), e('pond', y=75, s=1))
d(['Far away'], 'Phrase', 'medium', e('away', x=90, y=90, s=1))
d(['Rock the boat', 'Rocking the boat'], 'Phrase', 'hard', e('BOAT', x=28, s=4, rot=-20), e('BOAT', x=72, s=4, rot=20))
d(['Cross the line', 'Crossing the line'], 'Phrase', 'easy', e('LINE', s=6, style='strike'))
d(['In the long run', 'Long run'], 'Phrase', 'medium', e('RUUUUUUUN', s=3))
d(['High and dry'], 'Phrase', 'medium', e('DRY', y=10, s=5))
d(['First among equals'], 'Phrase', 'hard', e('=  =  1  =  =', s=2))
d(['Fly by night', 'Fly-by-night'], 'Phrase', 'hard', e('FLY', x=28, s=4), e('NIGHT', x=70, s=3, color='#1d2b6b'))

for b in B:
    for el in b['elements']:
        for line in el['t'].split('\n'):
            assert len(line) * el['s'] <= 34, (b['answers'][0], line, el['s'])

here = os.path.dirname(os.path.abspath(__file__))
have = set()
for f in glob.glob(os.path.join(here, '..', 'dingbat*.json')):
    if f.endswith('dingbat-23.json'): continue
    for r in json.load(open(f, encoding='utf-8')): have.update(a.lower() for a in r['answers'])
live = os.path.join(here, '..', '..', '..', 'lqsql', 'ding-a.json')
if os.path.exists(live): have.update(r['a'].lower() for r in json.load(open(live, encoding='utf-8'))['rows'] if r.get('a'))
clash = [b['answers'][0] for b in B if any(a.lower() in have for a in b['answers'])]
print('clash:', clash)
B = [b for b in B if b['answers'][0] not in clash]
json.dump(B, open(os.path.join(here, '..', 'dingbat-23.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'dingbats written')
