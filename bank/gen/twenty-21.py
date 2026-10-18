# Bank session 18 Oct 2026: more 20 Questions brands (the thinnest kind, 119 unused) -> bank/twenty-21.json.
# Only the Yes questions are listed; anything arguable (is Currys a tech company? is the Toblerone bear a logo animal?) is left No.
# One Yes at most in the origin group. The brand questions are coarse: Domino's, Currys, Superdrug, Mini, Virgin Atlantic,
# Caffè Nero and Bassett's came out identical to Subway, Holland & Barrett, Specsavers, Land Rover, Jet2, Pret and Tunnock's,
# and Iceland and Irn-Bru were already in, so all nine were dropped. Check with: node tools/twenty-check.mjs bank/twenty-21.json
import json, os
B = []
def t(what, answers, diff, yes):
    yes = yes.split()
    assert len(set(yes)) == len(yes), answers
    B.append({"type": "twenty", "answers": answers, "what": what, "yes": yes, "difficulty": diff, "category": "20 Questions", "tags": ["20 Questions", what]})

t("brand", ["Toblerone"], "medium", "b_food b_sweets b_old")
t("brand", ["Co-op", "The Co-op", "Coop"], "easy", "b_shop b_supermarket b_uk b_old b_highstreet")
t("brand", ["Air France"], "medium", "b_airline b_french")
t("brand", ["Lloyds Bank", "Lloyds"], "medium", "b_bank b_uk b_old b_logo b_highstreet")
t("brand", ["Santander"], "medium", "b_bank b_red b_highstreet")
t("brand", ["Ralph Lauren", "Polo Ralph Lauren"], "medium", "b_clothes b_american b_logo b_person b_luxury")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'twenty-21.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), '20 Questions answers written')
