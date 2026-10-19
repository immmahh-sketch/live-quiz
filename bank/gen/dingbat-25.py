# Bank session 19 Oct 2026: more dingbats -> bank/dingbat-25.json. Checked against every answer already in the bank (live and files).
# Elements: t text, x/y 0–100 (centre), s size 1–6, optional rot, flip "h"/"v", style strike/underline/box/outline, color #hex.
# Fit (memory: live-quiz-dingbat-fit): every line kept to (characters × size) ≤ 34; text on its side to about 19.
import json, os, glob
B = []
def d(answers, cat, diff, *els, tags=()):
    B.append({"answers": answers, "elements": [dict(e) for e in els], "category": cat, "tags": list(tags), "difficulty": diff})
def e(t, x=50, y=50, s=5, **k): return {"t": t, "x": x, "y": y, "s": s, **k}
PURPLE = "#7b2fbe"
NL = chr(10)

# candidates (the clash filter below drops any already in the bank); about 70 phrases were checked first and only the free
# ones were drawn (over the moon, side by side, underdog and others were already in).
RED = "#d62828"
d(['On the house'], 'Phrase', 'easy', e('ON', y=25, s=3), e('HOUSE', y=65, s=5))
d(['Under the counter'], 'Phrase', 'medium', e('COUNTER', y=30, s=4), e('£ £ £', y=70, s=4))
d(['Overweight'], 'Phrase', 'easy', e('OVER', y=22, s=3), e('WEIGHT', y=60, s=5))
d(['Wall to wall'], 'Phrase', 'medium', e('WALL 2 WALL', s=3))
d(['Second chance'], 'Phrase', 'medium', e('CHANCE', y=32, s=4), e('CHANCE', y=68, s=4, color=RED))
d(['Split the bill'], 'Phrase', 'easy', e('BI    LL', s=4))
d(['Look back'], 'Phrase', 'easy', e('KOOL', s=6))
d(['Fingers crossed', 'Crossed fingers'], 'Phrase', 'medium', e('FINGERS', s=2), e('FINGERS', s=2, rot=90))
d(['Sign of the times'], 'Phrase', 'hard', e('×', s=6))

for b in B:
    for el in b['elements']:
        for line in el['t'].split('\n'):
            assert len(line) * el['s'] <= 34, (b['answers'][0], line, el['s'])

here = os.path.dirname(os.path.abspath(__file__))
have = set()
for f in glob.glob(os.path.join(here, '..', 'dingbat*.json')):
    if f.endswith('dingbat-25.json'): continue
    for r in json.load(open(f, encoding='utf-8')): have.update(a.lower() for a in r['answers'])
live = os.path.join(here, '..', '..', '..', 'lqsql', 'ding-a.json')
if os.path.exists(live): have.update(r['a'].lower() for r in json.load(open(live, encoding='utf-8'))['rows'] if r.get('a'))
clash = [b['answers'][0] for b in B if any(a.lower() in have for a in b['answers'])]
print('clash:', clash)
B = [b for b in B if b['answers'][0] not in clash]
json.dump(B, open(os.path.join(here, '..', 'dingbat-25.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'dingbats written')
