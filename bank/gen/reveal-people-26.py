# Bank session 19 Oct 2026: more Picture Reveal faces -> bank/reveal-people-26.json
# (Wikipedia title, accepted answers, difficulty). Checked against every answer in the live bank. Guessable names only: faces from
# the period and crime drama races written today (Downton, Sherlock, Happy Valley, Poldark, Luther, Bodyguard, All Creatures).
# Stock with PEOPLE=bank/reveal-people-26.json node tools/reveal-stock.mjs, then contact-sheet them (wrong person, tiny face, small image -> RETIRED below).
import json, os
P = [
 ("Dan Stevens", ["Dan Stevens", "Stevens"], "hard"), ("Mark Gatiss", ["Mark Gatiss", "Gatiss"], "medium"),
 ("James Norton (actor)", ["James Norton", "Norton"], "medium"), ("Aidan Turner", ["Aidan Turner", "Turner"], "medium"),
 ("Eleanor Tomlinson", ["Eleanor Tomlinson", "Tomlinson"], "hard"), ("Ruth Wilson", ["Ruth Wilson", "Wilson"], "hard"),
 ("Richard Madden", ["Richard Madden", "Madden"], "medium"), ("Amanda Redman", ["Amanda Redman", "Redman"], "medium"),
 ("Christopher Timothy", ["Christopher Timothy", "Timothy"], "hard"), ("Robert Hardy", ["Robert Hardy", "Hardy"], "hard"),
 ("Peter Davison", ["Peter Davison", "Davison"], "medium"), ("Samuel West", ["Samuel West", "Sam West", "West"], "hard"),
 ("Julian Fellowes", ["Julian Fellowes", "Fellowes"], "hard"), ("Helen McCrory", ["Helen McCrory", "McCrory"], "medium"),
 ("Jim Carter (actor)", ["Jim Carter", "Carter"], "hard"), ("Siobhan Finneran", ["Siobhan Finneran", "Finneran"], "hard"),
]
# After stocking: no usable Wikipedia picture for Robert Hardy. Retired from the contact sheet: Christopher Timothy (distant
# full-length shot), Aidan Turner (small image) and Dan Stevens (sunglasses).
NO_PICTURE = {"Robert Hardy"}
RETIRED = {"Christopher Timothy", "Aidan Turner", "Dan Stevens"}
P = [p for p in P if p[0] not in NO_PICTURE | RETIRED]
here = os.path.dirname(os.path.abspath(__file__))
json.dump([{"title": t, "answers": list(dict.fromkeys(a)), "difficulty": d} for t, a, d in P], open(os.path.join(here, '..', 'reveal-people-26.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(P), 'people written')
