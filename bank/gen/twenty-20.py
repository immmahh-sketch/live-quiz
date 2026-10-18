# Bank session 18 Oct 2026: more 20 Questions objects (the thinnest kind, 118 unused) -> bank/twenty-20.json.
# Only the Yes questions are listed; anything arguable (is a bucket a garden thing? is a bath heavier than a person?) is left No.
# At most one Yes per group (use / room / material). Check with: node tools/twenty-check.mjs bank/twenty-20.json
import json, os
B = []
def t(what, answers, diff, yes):
    yes = yes.split()
    assert len(set(yes)) == len(yes), answers
    B.append({"type": "twenty", "answers": answers, "what": what, "yes": yes, "difficulty": diff, "category": "20 Questions", "tags": ["20 Questions", what]})

t("object", ["Teapot"], "easy", "o_eat o_home o_kitchen o_hold o_old")
t("object", ["Bucket"], "easy", "o_clean o_home o_plastic o_hold o_old")
t("object", ["Chopsticks"], "easy", "o_eat o_wood o_hold o_old")
t("object", ["Postbox", "Post box", "Pillar box"], "medium", "o_comm o_metal o_heavy o_old")
t("object", ["Fire extinguisher"], "medium", "o_metal o_hold o_office")
t("object", ["Smoke alarm", "Smoke detector"], "medium", "o_electric o_home o_sound o_plastic o_round")
t("object", ["Rocking chair"], "medium", "o_furniture o_wood o_old")
t("object", ["Rowing boat", "Rowboat"], "easy", "o_vehicle o_boat o_wood o_heavy o_old")
t("object", ["Fountain pen"], "medium", "o_write o_metal o_hold o_pocket o_old")
t("object", ["Ice skates"], "easy", "o_sport o_metal o_sharp o_old")
t("object", ["Barbecue", "BBQ"], "easy", "o_cook o_garden o_metal")
t("object", ["Wind chime", "Wind chimes"], "medium", "o_garden o_sound o_metal o_moving")
# Acoustic guitar, trombone and whisk came out identical to the violin, trumpet and saucepan; bath was already in. All dropped.

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'twenty-20.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), '20 Questions answers written')
