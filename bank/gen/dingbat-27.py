# Bank session 19 Oct 2026: more dingbats -> bank/dingbat-27.json. Checked against every answer already in the bank (live and files).
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
# candidates (the clash filter below drops any already in the bank); about 200 phrases were checked first and only free ones
# drawn. Inner circle and End of the line were left out because the drawing would depend on letters overlapping.
d(['Forty winks', '40 winks'], 'Phrase', 'easy', e('WINKS', y=40, s=5), e('× 40', y=70, s=4))
d(['Seeing double'], 'Phrase', 'easy', e('SEEING', y=35, s=5), e('SEEING', y=65, s=5))
d(['Cold shoulder', 'The cold shoulder', 'Give the cold shoulder'], 'Phrase', 'medium', e('SHOULDER', s=4, color=BLUE))
d(['Hot water', 'In hot water'], 'Phrase', 'medium', e('H2O', s=6, color=RED))
d(['Split up'], 'Phrase', 'medium', e('U     P', s=4))
d(['Out of place'], 'Phrase', 'medium', e('PLA E', y=45, s=5), e('C', x=85, y=85, s=4))
d(['Generation gap'], 'Phrase', 'medium', e('GENER     ATION', s=2))
d(['Ups and downs'], 'Phrase', 'medium', e('UPS', y=35, s=5), e('DOWNS', y=65, s=5, flip='v'))
d(['Look before you leap'], 'Phrase', 'medium', e('LOOK', y=50, x=28, s=4), e('LEAP', y=50, x=72, s=4))
d(['Corner shop'], 'Phrase', 'easy', e('SHOP', x=14, y=10, s=3))
d(['Uphill', 'Up hill'], 'Phrase', 'medium', e('L'+NL+'L'+NL+'I'+NL+'H', y=50, s=3))

for b in B:
    for el in b['elements']:
        for line in el['t'].split('\n'):
            assert len(line) * el['s'] <= 34, (b['answers'][0], line, el['s'])

here = os.path.dirname(os.path.abspath(__file__))
have = set()
for f in glob.glob(os.path.join(here, '..', 'dingbat*.json')):
    if f.endswith('dingbat-27.json'): continue
    for r in json.load(open(f, encoding='utf-8')): have.update(a.lower() for a in r['answers'])
live = os.path.join(here, '..', '..', '..', 'lqsql', 'ding-a.json')
if os.path.exists(live): have.update(r['a'].lower() for r in json.load(open(live, encoding='utf-8'))['rows'] if r.get('a'))
clash = [b['answers'][0] for b in B if any(a.lower() in have for a in b['answers'])]
print('clash:', clash)
B = [b for b in B if b['answers'][0] not in clash]
json.dump(B, open(os.path.join(here, '..', 'dingbat-27.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'dingbats written')
