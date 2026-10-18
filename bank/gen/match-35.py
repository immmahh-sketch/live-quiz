# Bank session 18 Oct 2026: 3 Match questions -> bank/match-35.json (game shows' consolation prizes, the overseas shows they
# came from, presenters to the quizzes they took over). Each topic probed against every match question in the live bank first
# (none of these pairs were there). Import with: node tools/import-bank.mjs match
import json, os
OUT = []
def m(cat, tags, diff, text, *pairs):
    assert len(pairs) == 4, text
    L = [l for l, _ in pairs]; R = [r for _, r in pairs]
    assert len(set(L)) == 4 and len(set(R)) == 4, text
    OUT.append({"type": "match", "text": text, "pairs": [{"left": l, "right": r} for l, r in pairs], "difficulty": diff, "category": cat, "tags": tags})

m("Television", ["game shows", "prizes"], "medium", "Match each show to its famous consolation or booby prize",
  ("Bullseye", "Bendy Bully"), ("Crackerjack", "A Crackerjack pencil"), ("Blankety Blank", "A chequebook and pen"), ("3-2-1", "Dusty Bin"))
m("Television", ["game shows", "formats"], "hard", "Match each British show to the overseas show it was based on",
  ("Play Your Cards Right", "Card Sharks"), ("University Challenge", "College Bowl"), ("The Generation Game", "Een van de Acht"), ("Countdown", "Des chiffres et des lettres"))
m("Television", ["quiz shows", "presenters"], "medium", "Match each presenter to the long-running quiz they took over",
  ("Anne Robinson", "Countdown"), ("Jeremy Clarkson", "Who Wants to Be a Millionaire?"), ("Amol Rajan", "University Challenge"), ("Clive Myrie", "Mastermind"))

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'match-35.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'match questions written')
