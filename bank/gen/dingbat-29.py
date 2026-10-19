# Bank session 19 Oct 2026: more dingbats -> bank/dingbat-29.json. Checked against every answer already in the bank (live and files).
# Elements: t text, x/y 0–100 (centre), s size 1–6, optional rot, flip "h"/"v", style strike/underline/box/outline, color #hex.
# Fit (memory: live-quiz-dingbat-fit): every line kept to (characters × size) ≤ 34; text on its side to about 19.
import json, os, glob
B = []
def d(answers, cat, diff, *els, tags=()):
    B.append({"answers": answers, "elements": [dict(e) for e in els], "category": cat, "tags": list(tags), "difficulty": diff})
def e(t, x=50, y=50, s=5, **k): return {"t": t, "x": x, "y": y, "s": s, **k}
PURPLE = "#7b2fbe"
NL = chr(10)

# candidates (the clash filter below drops any already in the bank); about 80 phrases were checked and only free ones drawn
# (crossword, square root, small print and most 'size' phrases were already in, and Fine print was left out as it would look like
# Small print). New mechanics this time: rotation, flips, a tick, a list and an anagram.
d(['Upright', 'Up right'], 'Phrase', 'medium', e('RIGHT', s=3, rot=-90))
d(['Weak link'], 'Phrase', 'medium', e('CHAIN link CHAIN', s=2))
d(['Topsy turvy', 'Topsy-turvy'], 'Phrase', 'medium', e('TOPSY', y=35, s=5, flip='v'), e('TURVY', y=65, s=5, flip='h'))
d(['Check in', 'Check-in'], 'Phrase', 'medium', e('IN ✓', s=5))
d(['Short list', 'Shortlist'], 'Phrase', 'medium', e('1 EGGS' + NL + '2 MILK', s=3))
d(['Half asleep'], 'Phrase', 'hard', e('ASL', s=6))
d(['Bigger picture', 'The bigger picture'], 'Phrase', 'medium', e('picture', y=30, s=2), e('PICTURE', y=65, s=4))
d(['Change of heart'], 'Phrase', 'medium', e('HEART → EARTH', s=2))
d(['Dot com', 'Dotcom', '.com'], 'Phrase', 'easy', e('.COM', s=5))
d(['One-way street', 'One way street'], 'Phrase', 'medium', e('STREET →', s=4))
d(['Three-piece suite', 'Three piece suite'], 'Phrase', 'medium', e('SU   I   TE', s=3))

for b in B:
    for el in b['elements']:
        for line in el['t'].split('\n'):
            assert len(line) * el['s'] <= 34, (b['answers'][0], line, el['s'])

here = os.path.dirname(os.path.abspath(__file__))
have = set()
for f in glob.glob(os.path.join(here, '..', 'dingbat*.json')):
    if f.endswith('dingbat-29.json'): continue
    for r in json.load(open(f, encoding='utf-8')): have.update(a.lower() for a in r['answers'])
live = os.path.join(here, '..', '..', '..', 'lqsql', 'ding-a.json')
if os.path.exists(live): have.update(r['a'].lower() for r in json.load(open(live, encoding='utf-8'))['rows'] if r.get('a'))
clash = [b['answers'][0] for b in B if any(a.lower() in have for a in b['answers'])]
print('clash:', clash)
B = [b for b in B if b['answers'][0] not in clash]
json.dump(B, open(os.path.join(here, '..', 'dingbat-29.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'dingbats written')
