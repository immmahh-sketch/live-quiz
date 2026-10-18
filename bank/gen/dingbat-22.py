# Bank session 18 Oct 2026: more dingbats -> bank/dingbat-22.json. Checked against every answer already in the bank (live and files).
# Elements: t text, x/y 0–100 (centre), s size 1–6, optional rot, flip "h"/"v", style strike/underline/box/outline, color #hex.
# Fit (memory: live-quiz-dingbat-fit): every line kept to (characters × size) ≤ 34; text on its side to about 19.
import json, os, glob
B = []
def d(answers, cat, diff, *els, tags=()):
    B.append({"answers": answers, "elements": [dict(e) for e in els], "category": cat, "tags": list(tags), "difficulty": diff})
def e(t, x=50, y=50, s=5, **k): return {"t": t, "x": x, "y": y, "s": s, **k}
PURPLE = "#7b2fbe"
NL = chr(10)

# candidates (the clash filter below drops any already in the bank). A first list of 30 classics (mind over matter, upside
# down, tricycle, crossroads, black sheep...) was all already in, so these were picked from phrases the bank doesn't have yet.
RED = "#d62828"
d(['Raise the bar', 'Raising the bar'], 'Phrase', 'medium', e('BAR', y=14, s=5), e('↑', y=55, s=5))
d(['Lower the tone', 'Lowering the tone'], 'Phrase', 'medium', e('↓', y=42, s=5), e('TONE', y=86, s=5))
d(['Right on time', 'Bang on time'], 'Phrase', 'medium', e('TIME', x=84, s=4))
d(['Up in the air'], 'Phrase', 'medium', e('A', x=25, s=4), e('UP', x=50, s=4, color=RED), e('IR', x=75, s=4))
d(['Down to earth'], 'Phrase', 'medium', e('D'+NL+'O'+NL+'W'+NL+'N', y=35, s=3), e('EARTH', y=88, s=4))
d(['Long story short', 'To cut a long story short'], 'Phrase', 'hard', e('STOOOOOOORY', s=1))
d(['Stand out from the crowd', 'Stand out in a crowd'], 'Phrase', 'medium', e('CROWD CROWD CROWD', y=38, s=2), e('STAND', y=70, s=4, color=RED))
d(['Paint the town red'], 'Phrase', 'easy', e('TOWN', s=6, color=RED))
d(['Going downhill'], 'Phrase', 'medium', e('GOING', s=5, rot=25))
d(['Over and over', 'Over and over again'], 'Phrase', 'easy', e('OVER'+NL+'OVER'+NL+'OVER', s=4))
d(['Step by step'], 'Phrase', 'easy', e('STEP', x=22, y=75, s=3), e('STEP', x=50, y=50, s=3), e('STEP', x=78, y=25, s=3))
d(['Wide open'], 'Phrase', 'easy', e('O   P   E   N', s=2))
d(['Short circuit'], 'Phrase', 'medium', e('CIRC', s=6))
d(['Easy as pie', 'Easy as pi'], 'Phrase', 'hard', e('EZ = π', s=5))
d(['Break a leg'], 'Phrase', 'medium', e('L     EG', s=4))
d(['Near and far'], 'Phrase', 'medium', e('NEAR', x=30, s=5), e('far', x=86, s=1))

for b in B:
    for el in b['elements']:
        for line in el['t'].split('\n'):
            assert len(line) * el['s'] <= 34, (b['answers'][0], line, el['s'])

here = os.path.dirname(os.path.abspath(__file__))
have = set()
for f in glob.glob(os.path.join(here, '..', 'dingbat*.json')):
    if f.endswith('dingbat-22.json'): continue
    for r in json.load(open(f, encoding='utf-8')): have.update(a.lower() for a in r['answers'])
live = os.path.join(here, '..', '..', '..', 'lqsql', 'ding-a.json')
if os.path.exists(live): have.update(r['a'].lower() for r in json.load(open(live, encoding='utf-8'))['rows'] if r.get('a'))
clash = [b['answers'][0] for b in B if any(a.lower() in have for a in b['answers'])]
print('clash:', clash)
B = [b for b in B if b['answers'][0] not in clash]
json.dump(B, open(os.path.join(here, '..', 'dingbat-22.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'dingbats written')
