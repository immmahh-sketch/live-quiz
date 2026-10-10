# Bank session 10 Oct 2026: more 20 Questions answers for animals and people (now the two thinnest kinds)
# -> bank/twenty-11.json. Only the Yes questions are listed; ambiguous facts are left No.
# Check with: node tools/twenty-check.mjs bank/twenty-11.json
import json, os
B = []
def t(what, answers, diff, yes):
    yes = yes.split()
    assert len(set(yes)) == len(yes), answers
    B.append({"type": "twenty", "answers": answers, "what": what, "yes": yes, "difficulty": diff, "category": "20 Questions", "tags": ["20 Questions", what]})

# ---- animals ----
t("animal", ["Hyena"], "medium", "a_mammal a_zoo a_fourlegs a_meat a_danger a_stripes a_herd a_africa a_nocturnal")
t("animal", ["Antelope"], "medium", "a_mammal a_zoo a_fourlegs a_plants a_horns a_herd a_africa a_fast a_hooves")
t("animal", ["Warthog"], "medium", "a_mammal a_zoo a_fourlegs a_horns a_africa a_hooves")
t("animal", ["Cougar", "Mountain lion"], "medium", "a_mammal a_zoo a_fourlegs a_meat a_danger a_tail a_americas a_catfam")
t("animal", ["Lynx"], "hard", "a_mammal a_zoo a_fourlegs a_meat a_catfam a_asia a_americas")
t("animal", ["Coyote"], "medium", "a_mammal a_fourlegs a_meat a_dogfam a_americas a_tail")
t("animal", ["Raccoon"], "medium", "a_mammal a_fourlegs a_nocturnal a_americas a_stripes a_zoo")
t("animal", ["Skunk"], "easy", "a_mammal a_fourlegs a_nocturnal a_americas a_blackwhite a_stripes a_tail")
t("animal", ["Armadillo"], "medium", "a_mammal a_fourlegs a_nocturnal a_americas a_zoo")
t("animal", ["Iguana"], "medium", "a_reptile a_fourlegs a_plants a_tail a_eggs a_americas a_zoo")
t("animal", ["Rattlesnake"], "medium", "a_reptile a_venom a_danger a_meat a_americas")
t("animal", ["Newt"], "medium", "a_amphibian a_small a_water a_wildbritain a_eggs a_tail a_fourlegs a_meat")
t("animal", ["Salamander"], "medium", "a_amphibian a_small a_tail a_eggs a_fourlegs a_water a_meat a_venom")
t("animal", ["Heron", "Grey heron"], "medium", "a_bird a_fly a_water a_meat a_wildbritain a_eggs")
t("animal", ["Seagull", "Gull"], "easy", "a_bird a_fly a_sea a_water a_wildbritain a_eggs a_meat a_herd")
t("animal", ["Albatross"], "medium", "a_bird a_fly a_sea a_water a_eggs a_meat a_endangered")
t("animal", ["Eel"], "medium", "a_fish a_water a_sea a_meat a_eat a_wildbritain")
t("animal", ["Cod"], "easy", "a_fish a_water a_sea a_eat a_wildbritain a_eggs")
t("animal", ["Termite"], "medium", "a_insect a_small a_herd a_eggs a_africa a_plants")
t("animal", ["Dragonfly"], "easy", "a_insect a_fly a_small a_water a_meat a_wildbritain a_eggs")

# ---- people ----
t("person", ["Paul Hollywood"], "easy", "p_man p_alive p_over50 p_british p_english p_north p_tv p_cook p_bakeoff")
t("person", ["Gareth Southgate"], "easy", "p_man p_alive p_over50 p_british p_english p_sport p_football p_country p_captain p_manager p_retired p_prem p_knighted p_b2000 p_b2010")
t("person", ["Bobby Robson", "Sir Bobby Robson"], "medium", "p_man p_over50 p_over70 p_british p_english p_northeast p_north p_sport p_football p_country p_manager p_retired p_knighted p_b1970 p_b1980 p_b1990 p_b2000 p_b2010")
t("person", ["Jack Charlton"], "medium", "p_man p_over50 p_over70 p_british p_english p_northeast p_north p_sport p_football p_country p_world p_manager p_retired p_leeds p_b1970 p_b1980 p_b1990 p_b2000 p_b2010")
t("person", ["Steve Cram"], "hard", "p_man p_alive p_over50 p_british p_english p_northeast p_north p_sport p_athletics p_country p_olympic p_world p_retired p_pundit p_b1990 p_b2000 p_b2010")
t("person", ["Sam Fender"], "easy", "p_man p_alive p_british p_english p_northeast p_north p_music p_solo p_songwriter p_instrument p_rock p_brit p_active")
t("person", ["Jimmy Nail"], "medium", "p_man p_alive p_over50 p_over70 p_british p_english p_northeast p_north p_actor p_music p_number1 p_solo p_acted p_b1990 p_b2000 p_b2010")
t("person", ["Jill Scott"], "medium", "p_woman p_alive p_british p_english p_northeast p_north p_sport p_football p_country p_retired p_tv p_jungle")
t("person", ["Lady Gaga"], "easy", "p_woman p_alive p_american p_music p_solo p_songwriter p_instrument p_pop p_acted p_grammy p_number1 p_actor p_oscar p_hollywood p_sang p_b2010")
t("person", ["Tom Hanks"], "easy", "p_man p_alive p_over50 p_american p_actor p_hollywood p_oscar p_voice p_b1990 p_b2000 p_b2010")
t("person", ["Judi Dench", "Dame Judi Dench"], "easy", "p_woman p_alive p_over50 p_over70 p_british p_english p_actor p_hollywood p_oscar p_bond p_stage p_sitcom p_period p_knighted p_b1970 p_b1980 p_b1990 p_b2000 p_b2010")
t("person", ["Frankie Dettori"], "medium", "p_man p_alive p_over50 p_sport p_retired p_tv p_jungle p_b2000 p_b2010")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'twenty-11.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), '20 Questions answers written')
