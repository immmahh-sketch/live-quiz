# Bank session 19 Oct 2026: more dingbats -> bank/dingbat-30.json. Checked against every answer already in the bank (live and files).
# Elements: t text, x/y 0–100 (centre), s size 1–6, optional rot, flip "h"/"v", style strike/underline/box/outline, color #hex.
# Fit (memory: live-quiz-dingbat-fit): every line kept to (characters × size) ≤ 34; text on its side to about 19.
import json, os, glob
B = []
def d(answers, cat, diff, *els, tags=()):
    B.append({"answers": answers, "elements": [dict(e) for e in els], "category": cat, "tags": list(tags), "difficulty": diff})
def e(t, x=50, y=50, s=5, **k): return {"t": t, "x": x, "y": y, "s": s, **k}
PURPLE = "#7b2fbe"
NL = chr(10)

RED = "#d62828"
BLUE = "#3fa9f5"
PINK = "#ff69b4"
BROWN = "#8b4513"
# candidates (the clash filter below drops any already in the bank); about 85 phrases were checked and only free ones drawn.
# This batch leans on colour (hot/cold/pink/brown) and symbols (>> << ||), which earlier batches used less.
d(['Time out', 'Timeout'], 'Phrase', 'easy', e('TIME', y=40, s=5, style='box'), e('OUT', x=88, y=88, s=3))
d(['Fast forward', 'Fast-forward'], 'Phrase', 'easy', e('FAST >>', s=4))
d(['Rewind'], 'Phrase', 'easy', e('<< REWIND', s=3))
d(['Pause'], 'Phrase', 'easy', e('PA||SE', s=5))
d(['Cold turkey'], 'Phrase', 'medium', e('TURKEY', s=5, color=BLUE))
d(['Hot potato'], 'Phrase', 'easy', e('POTATO', s=5, color=RED))
d(['Warm up', 'Warm-up', 'Warmup'], 'Phrase', 'easy', e('UP', s=6, color=RED))
d(['Cool down', 'Cooldown', 'Cool-down'], 'Phrase', 'easy', e('DOWN', y=75, s=5, color=BLUE))
d(['Pop up', 'Popup', 'Pop-up'], 'Phrase', 'medium', e('POP', y=75, s=3), e('UP', y=18, s=6))
d(['Run away', 'Runaway'], 'Phrase', 'easy', e('RUN', x=16, s=4), e('AWAY', x=76, s=4))
d(['Pink slip'], 'Phrase', 'medium', e('SLIP', s=6, color=PINK))
d(['Brown nose', 'Brownnose', 'Brown-nose'], 'Phrase', 'medium', e('NOSE', s=6, color=BROWN))

for b in B:
    for el in b['elements']:
        for line in el['t'].split('\n'):
            assert len(line) * el['s'] <= 34, (b['answers'][0], line, el['s'])

here = os.path.dirname(os.path.abspath(__file__))
have = set()
for f in glob.glob(os.path.join(here, '..', 'dingbat*.json')):
    if f.endswith('dingbat-30.json'): continue
    for r in json.load(open(f, encoding='utf-8')): have.update(a.lower() for a in r['answers'])
live = os.path.join(here, '..', '..', '..', 'lqsql', 'ding-a.json')
if os.path.exists(live): have.update(r['a'].lower() for r in json.load(open(live, encoding='utf-8'))['rows'] if r.get('a'))
clash = [b['answers'][0] for b in B if any(a.lower() in have for a in b['answers'])]
print('clash:', clash)
B = [b for b in B if b['answers'][0] not in clash]
json.dump(B, open(os.path.join(here, '..', 'dingbat-30.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'dingbats written')
