# Bank session 19 Oct 2026: more 20 Questions places (the thinnest kind in the files, 129) -> bank/twenty-25.json.
# Only the Yes questions are listed; anything arguable (is Dartmoor a tourist attraction? is Blackpool's club famous?) is left No.
# At most one Yes per group (continent / kind of place). Check with: node tools/twenty-check.mjs bank/twenty-25.json
import json, os
B = []
def t(what, answers, diff, yes):
    yes = yes.split()
    assert len(set(yes)) == len(yes), answers
    B.append({"type": "twenty", "answers": answers, "what": what, "yes": yes, "difficulty": diff, "category": "20 Questions", "tags": ["20 Questions", what]})

t("place", ["Belfast"], "easy", "pl_uk pl_ni pl_city pl_capital pl_sea pl_river pl_tourist")
t("place", ["Swansea"], "easy", "pl_uk pl_wales pl_city pl_sea pl_river pl_club")
t("place", ["Blackpool"], "easy", "pl_uk pl_england pl_north pl_city pl_sea pl_tourist")
t("place", ["Barnard Castle"], "medium", "pl_uk pl_england pl_north pl_northeast pl_durham pl_city pl_river")
t("place", ["Saltburn-by-the-Sea", "Saltburn"], "medium", "pl_uk pl_england pl_north pl_northeast pl_city pl_sea")
t("place", ["Norway"], "easy", "pl_europe pl_country pl_bigpop pl_olympics pl_sea pl_snow pl_tourist pl_heritage")
t("place", ["Naples"], "medium", "pl_europe pl_italy pl_city pl_bigpop pl_club pl_sea pl_hot pl_tourist pl_heritage")
t("place", ["Munich"], "medium", "pl_europe pl_germany pl_city pl_bigpop pl_olympics pl_club pl_river pl_tourist")
t("place", ["Chicago"], "medium", "pl_americas pl_usa pl_city pl_bigpop pl_english pl_river pl_snow pl_tourist")
t("place", ["Kenya"], "medium", "pl_africa pl_country pl_bigpop pl_english pl_sea pl_hot pl_tourist pl_heritage")
t("place", ["The Alhambra", "Alhambra"], "hard", "pl_europe pl_spain pl_building pl_castle pl_old pl_hot pl_tourist pl_heritage")
t("place", ["Angkor Wat"], "hard", "pl_asia pl_building pl_religious pl_old pl_hot pl_tourist pl_heritage")
t("place", ["Dartmoor"], "medium", "pl_uk pl_england pl_natural pl_forest")
t("place", ["The Eden Project", "Eden Project"], "medium", "pl_uk pl_england pl_building pl_tourist")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'twenty-25.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), '20 Questions answers written')
