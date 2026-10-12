# Bank session 12 Oct 2026 (second pass): 4 more Only One prompts (Scouts and Girlguiding sections, the monks' daily services, the
# Warsaw Pact, NATO's founders) appended to bank/unique-prompts.json. Each is a closed list with every correct answer (other accepted
# forms after a slash), so a fair answer is never knocked out. Checked against all 683 prompts already in the pool.
import json, os
NEW = [
 ("Name a section of the Scouts or of Girlguiding in the UK, from youngest to oldest", ["Squirrels", "Beavers", "Cubs/Cub Scouts", "Scouts", "Explorers/Explorer Scouts", "Network/Scout Network", "Rainbows", "Brownies", "Guides/Girl Guides", "Rangers"]),
 ("Name one of the services monks sing through the day (the canonical hours)", ["Matins/Vigils", "Lauds", "Prime", "Terce", "Sext", "None", "Vespers", "Compline"]),
 ("Name a country that was a member of the Warsaw Pact", ["Soviet Union/USSR/Russia", "Poland", "East Germany/GDR", "Czechoslovakia", "Hungary", "Romania", "Bulgaria", "Albania"]),
 ("Name one of the twelve countries that founded NATO in 1949", ["United States/USA/America", "Canada", "United Kingdom/UK/Britain", "France", "Belgium", "Netherlands/Holland", "Luxembourg", "Norway", "Denmark", "Iceland", "Italy", "Portugal"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
