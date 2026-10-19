# Bank session 19 Oct 2026: 2 Match questions -> bank/match-47.json (British sitcom bosses to their workplaces, Scottish islands
# to what they're famous for). Each topic probed against every match question in the live bank first (Brent / Michael Scott /
# Mr Burns / Holt was there, so these are British-only). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Comedy", ["sitcoms", "bosses"], "medium", "Match each sitcom boss to the place they run",
  ("Gordon Brittas", "Whitbury Leisure Centre"), ("Brian Potter", "The Phoenix Club"), ("Ken", "The Grapes"), ("Tony", "The HWD Components canteen"))
m("UK geography", ["Scotland", "islands"], "medium", "Match each Scottish island to what it's famous for",
  ("Islay", "Whisky distilleries"), ("Iona", "Its ancient abbey"), ("Staffa", "Fingal's Cave"), ("Lewis", "The Lewis Chessmen"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-47.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
