# Bank session 19 Oct 2026: more dingbats -> bank/dingbat-24.json. Checked against every answer already in the bank (live and files).
# Elements: t text, x/y 0–100 (centre), s size 1–6, optional rot, flip "h"/"v", style strike/underline/box/outline, color #hex.
# Fit (memory: live-quiz-dingbat-fit): every line kept to (characters × size) ≤ 34; text on its side to about 19.
import json, os, glob
B = []
def d(answers, cat, diff, *els, tags=()):
    B.append({"answers": answers, "elements": [dict(e) for e in els], "category": cat, "tags": list(tags), "difficulty": diff})
def e(t, x=50, y=50, s=5, **k): return {"t": t, "x": x, "y": y, "s": s, **k}
PURPLE = "#7b2fbe"
NL = chr(10)

# candidates (the clash filter below drops any already in the bank); a list of 40 phrases was checked first and only the
# free ones were drawn (heartbreak, crossword, split ends and others were already in).
RED = "#d62828"
d(['Close call'], 'Phrase', 'medium', e('CALLCALL', s=3))
d(['Day by day'], 'Phrase', 'medium', e('DAY', x=28, s=4), e('DAY', x=72, s=4))
d(['One for the road'], 'Phrase', 'medium', e('1  4', y=25, s=4), e('ROAD', y=65, s=5))
d(['Seventh heaven'], 'Phrase', 'hard', e('HEAVEN', x=45, s=5), e('7th', x=90, y=22, s=2))
d(['Spread the word'], 'Phrase', 'medium', e('W   O   R   D', s=2))
d(['Rat race'], 'Phrase', 'hard', e('RAT RAT RAT →', s=2))
d(['Overflow'], 'Phrase', 'easy', e('OVER', y=22, s=3), e('FLOW', y=60, s=6))
d(['Lowdown', 'The lowdown'], 'Phrase', 'medium', e('L'+NL+'O'+NL+'W', y=68, s=3))

for b in B:
    for el in b['elements']:
        for line in el['t'].split('\n'):
            assert len(line) * el['s'] <= 34, (b['answers'][0], line, el['s'])

here = os.path.dirname(os.path.abspath(__file__))
have = set()
for f in glob.glob(os.path.join(here, '..', 'dingbat*.json')):
    if f.endswith('dingbat-24.json'): continue
    for r in json.load(open(f, encoding='utf-8')): have.update(a.lower() for a in r['answers'])
live = os.path.join(here, '..', '..', '..', 'lqsql', 'ding-a.json')
if os.path.exists(live): have.update(r['a'].lower() for r in json.load(open(live, encoding='utf-8'))['rows'] if r.get('a'))
clash = [b['answers'][0] for b in B if any(a.lower() in have for a in b['answers'])]
print('clash:', clash)
B = [b for b in B if b['answers'][0] not in clash]
json.dump(B, open(os.path.join(here, '..', 'dingbat-24.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'dingbats written')
