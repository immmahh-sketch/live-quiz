# Bank session 18 Oct 2026: more dingbats -> bank/dingbat-21.json. Checked against every answer already in the bank (live and files).
# Elements: t text, x/y 0–100 (centre), s size 1–6, optional rot, flip "h"/"v", style strike/underline/box/outline, color #hex.
# 11 of 14 drafts (shrinking violet, growing pains, double trouble, boxing day, thinking outside the box...) were already in.
# Fit (memory: live-quiz-dingbat-fit): every line kept to (characters × size) ≤ 34; text on its side to about 19.
import json, os, glob
B = []
def d(answers, cat, diff, *els, tags=()):
    B.append({"answers": answers, "elements": [dict(e) for e in els], "category": cat, "tags": list(tags), "difficulty": diff})
def e(t, x=50, y=50, s=5, **k): return {"t": t, "x": x, "y": y, "s": s, **k}
PURPLE = "#7b2fbe"

# candidates (the clash filter below drops any already in the bank)
d(['Sign on the dotted line'], 'Phrase', 'medium', e('SIGN', y=35, s=5), e('........', y=62, s=4))
d(['Shrinking violet'], 'Phrase', 'medium', e('VIOLET', y=25, s=5, color=PURPLE), e('VIOLET', y=52, s=3, color=PURPLE), e('VIOLET', y=74, s=2, color=PURPLE))
d(['Growing pains'], 'Phrase', 'medium', e('PAINS', y=22, s=2), e('PAINS', y=45, s=3), e('PAINS', y=72, s=5))
d(['Top of the morning'], 'Phrase', 'medium', e('MORNING', y=12, s=4))
d(['Bottom of the sea'], 'Phrase', 'medium', e('SEA', y=88, s=5))
d(['Split personality'], 'Phrase', 'medium', e('PERSON   ALITY', s=2))
d(['Break the ice', 'Breaking the ice'], 'Phrase', 'medium', e('I     CE', s=4))
d(['Double trouble'], 'Phrase', 'easy', e('TROUBLE', y=35, s=4), e('TROUBLE', y=65, s=4))
d(['Double-decker bus', 'Double decker'], 'Phrase', 'easy', e('BUS', y=35, s=6), e('BUS', y=65, s=6))
d(['Missing person'], 'Phrase', 'medium', e('PRSN', s=6))
d(['Square dance'], 'Phrase', 'medium', e('DANCE', s=6, style='box'))
d(['Boxing Day'], 'Phrase', 'easy', e('DAY', s=6, style='box'))
d(['Thinking outside the box', 'Think outside the box'], 'Phrase', 'medium', e('BOX', y=60, s=5, style='box'), e('THINKING', y=18, s=3))
d(['Left out'], 'Phrase', 'medium', e('OUT', x=12, s=5))

for b in B:
    for el in b['elements']:
        for line in el['t'].split('\n'):
            assert len(line) * el['s'] <= 34, (b['answers'][0], line, el['s'])

here = os.path.dirname(os.path.abspath(__file__))
have = set()
for f in glob.glob(os.path.join(here, '..', 'dingbat*.json')):
    if f.endswith('dingbat-21.json'): continue
    for r in json.load(open(f, encoding='utf-8')): have.update(a.lower() for a in r['answers'])
live = os.path.join(here, '..', '..', '..', 'lqsql', 'ding-a.json')
if os.path.exists(live): have.update(r['a'].lower() for r in json.load(open(live, encoding='utf-8'))['rows'] if r.get('a'))
clash = [b['answers'][0] for b in B if any(a.lower() in have for a in b['answers'])]
print('clash:', clash)
B = [b for b in B if b['answers'][0] not in clash]
json.dump(B, open(os.path.join(here, '..', 'dingbat-21.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'dingbats written')
