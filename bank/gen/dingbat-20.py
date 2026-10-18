# Bank session 18 Oct 2026: more dingbats -> bank/dingbat-20.json. Checked against every answer already in the bank (live and files).
# Elements: t text, x/y 0–100 (centre), s size 1–6, optional rot, flip "h"/"v", style strike/underline/box/outline, color #hex.
# Fit (memory: live-quiz-dingbat-fit): no wrapping, so every line is kept to (characters × size) ≤ 34, the safe width at the
# board's calc(size × 2.4cqw); the assert below enforces it. Text turned on its side must also fit the board's height
# (16:9), so a vertical word keeps (characters × size) to about 19.
import json, os, glob
B = []
def d(answers, cat, diff, *els, tags=()):
    B.append({"answers": answers, "elements": [dict(e) for e in els], "category": cat, "tags": list(tags), "difficulty": diff})
def e(t, x=50, y=50, s=5, **k): return {"t": t, "x": x, "y": y, "s": s, **k}
RED, GREY, GOLD, SILVER, YELLOW = "#d42020", "#8a8f94", "#c9a227", "#9aa0a6", "#e0b400"
BLUE, BROWN, PURPLE, GREEN, PINK, ORANGE = "#1f5fd4", "#7a4a1e", "#7b2fbe", "#1f9a3a", "#e8579a", "#e07a00"

# candidates (the clash filter below drops any already in the bank)
d(['Split second'], 'Phrase', 'medium', e('SEC   OND', s=3))
d(['Broken heart'], 'Phrase', 'medium', e('HE   ART', s=4))
d(['Upside down'], 'Phrase', 'medium', e('DOWN', s=6, flip='v'))
d(['Backfire'], 'Phrase', 'medium', e('ERIF', s=6))
d(['Downtown'], 'Phrase', 'medium', e('TOWN', s=5, rot=90))
d(['Top secret'], 'Phrase', 'medium', e('SECRET', y=15, s=4))
d(['Bottom line'], 'Phrase', 'medium', e('LINE', y=85, s=5))
d(['Small talk'], 'Phrase', 'easy', e('talk', s=1))
d(['Tea for two'], 'Phrase', 'medium', e('T 4 2', s=6))
d(['Cancelled flight'], 'Phrase', 'medium', e('FLIGHT', s=5, style='strike'))
d(['Mixed feelings'], 'Phrase', 'medium', e('FGEELINS', s=4))
d(['Green with envy'], 'Phrase', 'easy', e('ENVY', s=6, color=GREEN))
d(['Feeling blue'], 'Phrase', 'easy', e('FEELING', s=4, color=BLUE))
d(['Red alert'], 'Phrase', 'easy', e('ALERT', s=6, color=RED))
d(['Gold medal'], 'Phrase', 'easy', e('MEDAL', s=6, color=GOLD))
d(['Pink Panther', 'The Pink Panther'], 'Phrase', 'easy', e('PANTHER', s=4, color=PINK))
d(['Purple patch'], 'Phrase', 'medium', e('PATCH', s=6, color=PURPLE))
d(['Silver screen'], 'Phrase', 'medium', e('SCREEN', s=5, color=SILVER))
d(['Yellow Submarine'], 'Phrase', 'easy', e('SUBMARINE', s=3, color=YELLOW))
d(['Orange juice'], 'Phrase', 'easy', e('JUICE', s=6, color=ORANGE))
d(['Brown sauce'], 'Phrase', 'easy', e('SAUCE', s=6, color=BROWN))
d(['Grey area'], 'Phrase', 'medium', e('AREA', s=6, color=GREY))
d(['Lower case'], 'Phrase', 'medium', e('case', s=6))
d(['Big deal'], 'Phrase', 'easy', e('DEAL', s=6))
d(['High tea'], 'Phrase', 'medium', e('TEA', y=12, s=5))
d(['Long time no see'], 'Phrase', 'hard', e('T I M E', y=35, s=4), e('NO C', y=65, s=4))
d(['Head start'], 'Phrase', 'medium', e('START', y=12, s=5))
d(['Fall behind'], 'Phrase', 'hard', e('BEHIND', s=3, rot=90))

d(['Over the moon'], 'Phrase', 'medium', e('ME', y=33, s=5), e('MOON', y=67, s=5))
d(['Walking on air'], 'Phrase', 'medium', e('WALKING', y=33, s=4), e('AIR', y=67, s=5))
d(['Sleeping on the job'], 'Phrase', 'medium', e('SLEEPING', y=33, s=4), e('JOB', y=67, s=5))
d(['Square meal'], 'Phrase', 'medium', e('MEAL', s=6, style='box'))
d(['Out of order'], 'Phrase', 'medium', e('RODER', s=6))
d(['Undercover agent'], 'Phrase', 'medium', e('COVER', y=33, s=5), e('AGENT', y=67, s=5))
d(['Once in a blue moon'], 'Phrase', 'hard', e('MOONCEON', s=4, color=BLUE))
d(['Uphill struggle'], 'Phrase', 'medium', e('STRUGGLE', s=4, rot=-25))
d(['Small print'], 'Phrase', 'easy', e('print', s=1))

for b in B:
    for el in b['elements']:
        for line in el['t'].split('\n'):
            assert len(line) * el['s'] <= 34, (b['answers'][0], line, el['s'])

here = os.path.dirname(os.path.abspath(__file__))
have = set()
for f in glob.glob(os.path.join(here, '..', 'dingbat*.json')):
    if f.endswith('dingbat-20.json'): continue
    for r in json.load(open(f, encoding='utf-8')): have.update(a.lower() for a in r['answers'])
live = os.path.join(here, '..', '..', '..', 'lqsql', 'ding-a.json')
if os.path.exists(live): have.update(r['a'].lower() for r in json.load(open(live, encoding='utf-8'))['rows'] if r.get('a'))
clash = [b['answers'][0] for b in B if any(a.lower() in have for a in b['answers'])]
print('clash:', clash)
B = [b for b in B if b['answers'][0] not in clash]
json.dump(B, open(os.path.join(here, '..', 'dingbat-20.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'dingbats written')
