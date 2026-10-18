# Bank session 18 Oct 2026: 4 more Only One prompts (UK nations' patron saints and plants, simple machines, the Big Four railway
# companies, the Platonic solids) appended to bank/unique-prompts.json. Each is a closed list with every correct answer (other
# accepted forms after a slash), so a fair answer is never knocked out. Probed against all 687 prompts already in the pool
# (Tracy family, Famous Five, Marx Brothers, Ghostbusters, NYC boroughs, the Classics and Python/Goodies were already there).
import json, os
NEW = [
 ("Name the patron saint, or the national flower or plant, of England, Scotland, Wales or Northern Ireland",
  ["St George/George", "St Andrew/Andrew", "St David/David/Dewi Sant", "St Patrick/Patrick", "Rose", "Thistle", "Daffodil", "Leek", "Shamrock", "Flax"]),
 ("Name one of the six classic simple machines", ["Lever", "Wheel and axle/Wheel", "Pulley", "Inclined plane/Ramp/Slope", "Wedge", "Screw"]),
 ("Name one of the 'Big Four' railway companies that ran Britain's trains from 1923 to 1947",
  ["LMS/London, Midland and Scottish/London Midland and Scottish", "LNER/London and North Eastern/London & North Eastern", "GWR/Great Western/Great Western Railway", "SR/Southern/Southern Railway"]),
 ("Name one of the five Platonic solids", ["Tetrahedron", "Cube/Hexahedron", "Octahedron", "Dodecahedron", "Icosahedron"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
