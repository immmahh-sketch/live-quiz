# Bank session 19 Oct 2026: more dingbats -> bank/dingbat-28.json. Checked against every answer already in the bank (live and files).
# Elements: t text, x/y 0–100 (centre), s size 1–6, optional rot, flip "h"/"v", style strike/underline/box/outline, color #hex.
# Fit (memory: live-quiz-dingbat-fit): every line kept to (characters × size) ≤ 34; text on its side to about 19.
import json, os, glob
B = []
def d(answers, cat, diff, *els, tags=()):
    B.append({"answers": answers, "elements": [dict(e) for e in els], "category": cat, "tags": list(tags), "difficulty": diff})
def e(t, x=50, y=50, s=5, **k): return {"t": t, "x": x, "y": y, "s": s, **k}
PURPLE = "#7b2fbe"
NL = chr(10)

# candidates (the clash filter below drops any already in the bank); about 230 phrases were checked first and only free ones
# drawn, avoiding the mechanics used last time (colour, a missing letter, stacked letters going up). Lying low was then
# dropped by the filter (Low lying is already in), so 10 went in.
d(['One after another'], 'Phrase', 'medium', e('ANOTHER ONE', s=3))
d(['Second to none'], 'Phrase', 'medium', e('SECOND → NONE', s=2))
d(['Lying low', 'Low lying'], 'Phrase', 'medium', e('LYING', y=90, s=4))
d(['Feeling down'], 'Phrase', 'medium', e(NL.join('FEELING'), y=50, s=2))
d(['Repeat'], 'Phrase', 'medium', e('PEAT', y=35, s=5), e('PEAT', y=65, s=5))
d(['Cut back', 'Cutback'], 'Phrase', 'medium', e('BA   CK', s=4))
d(['Big talk'], 'Phrase', 'easy', e('TALK', s=6))
d(['Raise the roof'], 'Phrase', 'medium', e('ROOF', y=15, s=4), e('HOUSE', y=72, s=5))
d(['Sleep on it'], 'Phrase', 'easy', e('SLEEP', y=35, s=4), e('IT', y=65, s=5))
d(['Lie in', 'Lie-in'], 'Phrase', 'medium', e('I LIE N', s=4))
d(['Reverse', 'In reverse'], 'Phrase', 'easy', e('ESREVER', s=4))

for b in B:
    for el in b['elements']:
        for line in el['t'].split('\n'):
            assert len(line) * el['s'] <= 34, (b['answers'][0], line, el['s'])

here = os.path.dirname(os.path.abspath(__file__))
have = set()
for f in glob.glob(os.path.join(here, '..', 'dingbat*.json')):
    if f.endswith('dingbat-28.json'): continue
    for r in json.load(open(f, encoding='utf-8')): have.update(a.lower() for a in r['answers'])
live = os.path.join(here, '..', '..', '..', 'lqsql', 'ding-a.json')
if os.path.exists(live): have.update(r['a'].lower() for r in json.load(open(live, encoding='utf-8'))['rows'] if r.get('a'))
clash = [b['answers'][0] for b in B if any(a.lower() in have for a in b['answers'])]
print('clash:', clash)
B = [b for b in B if b['answers'][0] not in clash]
json.dump(B, open(os.path.join(here, '..', 'dingbat-28.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'dingbats written')
