# Bank session 18 Oct 2026: more 20 Questions animals (the thinnest kind in the files, 124) -> bank/twenty-22.json.
# Only the Yes questions are listed; anything arguable (does an anteater eat meat? is a ferret smaller than a cat?) is left No.
# Dropped: donkey, jaguar, turkey and ant (already in), wombat (same answers as the koala).
# At most one Yes per group (sort of animal / which mammal). Check with: node tools/twenty-check.mjs bank/twenty-22.json
import json, os
B = []
def t(what, answers, diff, yes):
    yes = yes.split()
    assert len(set(yes)) == len(yes), answers
    B.append({"type": "twenty", "answers": answers, "what": what, "yes": yes, "difficulty": diff, "category": "20 Questions", "tags": ["20 Questions", what]})

t("animal", ["Cat", "House cat"], "easy", "a_mammal a_pet a_fourlegs a_meat a_tail a_catfam")
t("animal", ["Tasmanian devil"], "hard", "a_mammal a_zoo a_fourlegs a_meat a_nocturnal a_endangered a_australia a_marsupial")
t("animal", ["Anteater", "Giant anteater"], "medium", "a_mammal a_zoo a_fourlegs a_tail a_americas")
t("animal", ["Goose"], "easy", "a_bird a_farm a_wildbritain a_fly a_water a_plants a_eggs a_eat a_swims a_herd")
t("animal", ["Ferret"], "medium", "a_mammal a_pet a_fourlegs a_meat a_tail")
t("animal", ["Kiwi"], "medium", "a_bird a_flightless a_nocturnal a_eggs")
t("animal", ["Sparrow", "House sparrow"], "easy", "a_bird a_wildbritain a_small a_fly a_plants a_eggs a_garden")
t("animal", ["Spider", "House spider"], "easy", "a_insect a_eightlegs a_wildbritain a_small a_meat a_eggs")
t("animal", ["Grasshopper"], "easy", "a_insect a_wildbritain a_small a_plants a_eggs")
t("animal", ["Starfish"], "medium", "a_water a_sea a_wildbritain a_meat")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'twenty-22.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), '20 Questions answers written')
