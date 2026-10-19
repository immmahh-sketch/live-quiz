# Bank session 19 Oct 2026: more Picture Reveal faces -> bank/reveal-people-24.json
# (Wikipedia title, accepted answers, difficulty). Checked against every answer in the live bank. Guessable names only: faces from
# the detective and drama races written today (Minder, Taggart, Bergerac, Lovejoy, Midsomer, antiques shows). Stock with
# PEOPLE=bank/reveal-people-24.json node tools/reveal-stock.mjs, then contact-sheet them (wrong person, tiny face, small image -> RETIRED below).
import json, os
P = [
 ("George Cole (actor)", ["George Cole", "Cole"], "medium"), ("Dennis Waterman", ["Dennis Waterman", "Waterman"], "medium"),
 ("Mark McManus", ["Mark McManus", "McManus"], "hard"), ("Blythe Duff", ["Blythe Duff", "Duff"], "hard"),
 ("Alex Norton", ["Alex Norton", "Norton"], "hard"), ("Neil Dudgeon", ["Neil Dudgeon", "Dudgeon"], "medium"),
 ("Ian McShane", ["Ian McShane", "McShane"], "medium"), ("Phyllis Logan", ["Phyllis Logan", "Logan"], "medium"),
 ("Caroline Langrishe", ["Caroline Langrishe", "Langrishe"], "hard"), ("John Nettles", ["John Nettles", "Nettles"], "medium"),
 ("Liza Goddard", ["Liza Goddard", "Goddard"], "hard"), ("Tim Wonnacott", ["Tim Wonnacott", "Wonnacott"], "medium"),
 ("David Dickinson", ["David Dickinson", "Dickinson"], "easy"), ("Patrick Malahide", ["Patrick Malahide", "Malahide"], "hard"),
 ("Douglas Henshall", ["Douglas Henshall", "Henshall"], "hard"), ("Martin Shaw", ["Martin Shaw", "Shaw"], "medium"),
 ("Dudley Sutton", ["Dudley Sutton", "Sutton"], "hard"),
]
# After stocking: no usable Wikipedia picture for George Cole, Mark McManus, Blythe Duff, Neil Dudgeon, Caroline Langrishe,
# Liza Goddard, Tim Wonnacott or Dudley Sutton. The contact sheet was clean: all nine stocked faces kept.
NO_PICTURE = {"George Cole (actor)", "Mark McManus", "Blythe Duff", "Neil Dudgeon", "Caroline Langrishe", "Liza Goddard", "Tim Wonnacott", "Dudley Sutton"}
RETIRED = set()
P = [p for p in P if p[0] not in NO_PICTURE | RETIRED]
here = os.path.dirname(os.path.abspath(__file__))
json.dump([{"title": t, "answers": list(dict.fromkeys(a)), "difficulty": d} for t, a, d in P], open(os.path.join(here, '..', 'reveal-people-24.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(P), 'people written')
