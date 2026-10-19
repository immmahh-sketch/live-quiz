# Bank session 19 Oct 2026: more 20 Questions people -> bank/twenty-29.json (stars of today's period and crime drama races).
# Only the Yes questions are listed; anything arguable is left No (Tom Hardy's Venom as Marvel, Maggie Smith's Ilford as London,
# whether Hugh Bonneville, Tom Hardy or Benedict Cumberbatch were famous before 2010).
# Check with: node tools/twenty-check.mjs bank/twenty-29.json
import json, os
B = []
def t(what, answers, diff, yes):
    yes = yes.split()
    assert len(set(yes)) == len(yes), answers
    B.append({"type": "twenty", "answers": answers, "what": what, "yes": yes, "difficulty": diff, "category": "20 Questions", "tags": ["20 Questions", what]})

t("person", ["Idris Elba"], "easy", "p_man p_alive p_over50 p_british p_english p_london p_actor p_hollywood p_superhero p_marvel p_action p_b2010")
t("person", ["Benedict Cumberbatch"], "easy", "p_man p_alive p_over50 p_british p_english p_london p_actor p_hollywood p_superhero p_marvel p_voice p_stage")
t("person", ["Martin Freeman"], "medium", "p_man p_alive p_over50 p_british p_english p_actor p_sitcom p_funny p_hollywood p_marvel p_b2010")
t("person", ["Cillian Murphy"], "medium", "p_man p_alive p_over50 p_irish p_actor p_hollywood p_oscar p_b2010")
t("person", ["Tom Hardy"], "medium", "p_man p_alive p_british p_english p_london p_actor p_hollywood p_action")
t("person", ["Maggie Smith"], "easy", "p_woman p_over50 p_over70 p_british p_english p_actor p_hollywood p_oscar p_potter p_knighted p_stage p_period p_b1970 p_b1980 p_b1990 p_b2000 p_b2010")
t("person", ["Hugh Bonneville"], "hard", "p_man p_alive p_over50 p_british p_english p_london p_actor p_period")
t("person", ["Sarah Lancashire"], "medium", "p_woman p_alive p_over50 p_british p_english p_north p_actor p_soap p_corrie p_b2000 p_b2010")
t("person", ["Richard Madden"], "medium", "p_man p_alive p_british p_scottish p_actor p_hollywood p_marvel p_superhero")
t("person", ["Keeley Hawes"], "hard", "p_woman p_alive p_over50 p_british p_english p_london p_actor p_b2010")
t("person", ["Jodie Whittaker"], "medium", "p_woman p_alive p_british p_english p_north p_actor p_whoactor")
t("person", ["Andrew Scott"], "medium", "p_man p_alive p_over50 p_irish p_actor p_hollywood p_bond p_stage")
t("person", ["Suranne Jones"], "medium", "p_woman p_alive p_british p_english p_north p_actor p_soap p_corrie p_whoactor p_b2010")
t("person", ["Jodie Comer"], "medium", "p_woman p_alive p_british p_english p_north p_actor p_hollywood")
t("person", ["Phoebe Waller-Bridge"], "medium", "p_woman p_alive p_british p_english p_london p_actor p_sitcom p_funny p_writer p_plays p_hollywood p_starwars")
t("person", ["Daniel Craig"], "easy", "p_man p_alive p_over50 p_british p_english p_north p_actor p_hollywood p_bond p_action p_b2000 p_b2010")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(B, open(os.path.join(here, '..', 'twenty-29.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), '20 Questions answers written')
