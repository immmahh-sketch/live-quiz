# Bank session 18 Oct 2026: more Picture Reveal faces -> bank/reveal-people-16.json
# (Wikipedia title, accepted answers, difficulty). Checked against every answer in the live bank (1,159). Guessable names only,
# mostly stars of the shows written up as races today. Stock with PEOPLE=bank/reveal-people-16.json node tools/reveal-stock.mjs,
# then contact-sheet them (wrong person, tiny face, small image -> RETIRED below).
import json, os
P = [
 ("Patricia Routledge", ["Patricia Routledge", "Routledge"], "medium"), ("Prunella Scales", ["Prunella Scales", "Scales"], "medium"),
 ("Andrew Sachs", ["Andrew Sachs", "Sachs"], "medium"), ("Richard Briers", ["Richard Briers", "Briers"], "medium"),
 ("Gorden Kaye", ["Gorden Kaye", "Gordon Kaye", "Kaye"], "medium"), ("Ruth Madoc", ["Ruth Madoc", "Madoc"], "hard"),
 ("Ulrika Jonsson", ["Ulrika Jonsson", "Ulrika"], "easy"), ("John Fashanu", ["John Fashanu", "Fashanu", "Fash"], "medium"),
 ("Konnie Huq", ["Konnie Huq", "Huq"], "medium"), ("John Noakes", ["John Noakes", "Noakes"], "hard"),
 ("Todd Carty", ["Todd Carty", "Carty"], "medium"), ("Kathy Staff", ["Kathy Staff", "Nora Batty"], "medium"),
 ("Kelly Macdonald", ["Kelly Macdonald", "Kelly MacDonald"], "medium"), ("Thandiwe Newton", ["Thandiwe Newton", "Thandie Newton", "Newton"], "medium"),
 ("Richard Curtis", ["Richard Curtis", "Curtis"], "hard"), ("Ed Gamble", ["Ed Gamble", "Gamble"], "medium"),
 ("Dara Ó Briain", ["Dara Ó Briain", "Dara O Briain", "Dara O'Briain", "Dara"], "easy"), ("Liza Tarbuck", ["Liza Tarbuck", "Tarbuck"], "medium"),
 ("Peter Sallis", ["Peter Sallis", "Sallis"], "hard"), ("Valerie Singleton", ["Valerie Singleton", "Singleton"], "hard"),
]
# After stocking: no usable Wikipedia picture for Ruth Madoc, Ulrika Jonsson, John Noakes, Liza Tarbuck or Valerie Singleton.
# Retired from the contact sheet: full-length or distant shots with a tiny face (John Fashanu, Kathy Staff, Andrew Sachs, Peter Sallis).
NO_PICTURE = {"Ruth Madoc", "Ulrika Jonsson", "John Noakes", "Liza Tarbuck", "Valerie Singleton"}
RETIRED = {"John Fashanu", "Kathy Staff", "Andrew Sachs", "Peter Sallis"}
P = [p for p in P if p[0] not in NO_PICTURE | RETIRED]
here = os.path.dirname(os.path.abspath(__file__))
json.dump([{"title": t, "answers": list(dict.fromkeys(a)), "difficulty": d} for t, a, d in P], open(os.path.join(here, '..', 'reveal-people-16.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(P), 'people written')
