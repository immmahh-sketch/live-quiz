# Bank session 19 Oct 2026: more dingbats -> bank/dingbat-26.json. Checked against every answer already in the bank (live and files).
# Elements: t text, x/y 0–100 (centre), s size 1–6, optional rot, flip "h"/"v", style strike/underline/box/outline, color #hex.
# Fit (memory: live-quiz-dingbat-fit): every line kept to (characters × size) ≤ 34; text on its side to about 19.
import json, os, glob
B = []
def d(answers, cat, diff, *els, tags=()):
    B.append({"answers": answers, "elements": [dict(e) for e in els], "category": cat, "tags": list(tags), "difficulty": diff})
def e(t, x=50, y=50, s=5, **k): return {"t": t, "x": x, "y": y, "s": s, **k}
PURPLE = "#7b2fbe"
NL = chr(10)

# candidates (the clash filter below drops any already in the bank); about 65 phrases were checked first and only the free
# ones were drawn (bottom line, low key, crossover, first class and others were already in). Step back and Overturn
# then clashed on their alternative answers and were dropped by the filter, so 9 went in.
d(['Middle class'], 'Phrase', 'medium', e('upper', y=20, s=2), e('CLASS', y=50, s=5), e('lower', y=80, s=2))
d(['Breakfast', 'Break fast'], 'Phrase', 'medium', e('FA    ST', s=4))
d(['Overdue'], 'Phrase', 'easy', e('OVER', y=22, s=3), e('DUE', y=60, s=6))
d(['Walk the line'], 'Phrase', 'medium', e('WALK', y=40, s=5), e('__________', y=58, s=3))
d(['Sidestep', 'Side step'], 'Phrase', 'medium', e('STEP', x=88, s=3, rot=90))
d(['Step back', 'Step backwards'], 'Phrase', 'medium', e('PETS', s=6))
d(['Overturn', 'Turn over'], 'Phrase', 'medium', e('TURN', s=6, flip='v'))
d(['Backwards'], 'Phrase', 'easy', e('SDRAWKCAB', s=3))
d(['Look over', 'Overlook'], 'Phrase', 'medium', e('LOOK', y=28, s=4), e('OVER', y=62, s=5))
d(['Income'], 'Phrase', 'medium', e('COME', s=5, style='box'))
d(['Downtime'], 'Phrase', 'medium', e('T'+NL+'I'+NL+'M'+NL+'E', y=50, s=3))

for b in B:
    for el in b['elements']:
        for line in el['t'].split('\n'):
            assert len(line) * el['s'] <= 34, (b['answers'][0], line, el['s'])

here = os.path.dirname(os.path.abspath(__file__))
have = set()
for f in glob.glob(os.path.join(here, '..', 'dingbat*.json')):
    if f.endswith('dingbat-26.json'): continue
    for r in json.load(open(f, encoding='utf-8')): have.update(a.lower() for a in r['answers'])
live = os.path.join(here, '..', '..', '..', 'lqsql', 'ding-a.json')
if os.path.exists(live): have.update(r['a'].lower() for r in json.load(open(live, encoding='utf-8'))['rows'] if r.get('a'))
clash = [b['answers'][0] for b in B if any(a.lower() in have for a in b['answers'])]
print('clash:', clash)
B = [b for b in B if b['answers'][0] not in clash]
json.dump(B, open(os.path.join(here, '..', 'dingbat-26.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'dingbats written')
