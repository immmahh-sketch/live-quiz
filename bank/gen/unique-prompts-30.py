# Bank session 12 Oct 2026: 3 more Only One prompts (Geordie Shore's first cast, the forts on Hadrian's Wall, Sunderland's home
# grounds) appended to bank/unique-prompts.json. Each is a closed list with every correct answer (other accepted forms after a
# slash), so a fair answer is never knocked out. Checked against all 680 prompts already in the pool.
import json, os
NEW = [
 ("Name a cast member from the first series of Geordie Shore (2011)", ["Charlotte Crosby/Charlotte", "Vicky Pattison/Vicky", "Gaz Beadle/Gary Beadle/Gaz", "Holly Hagan/Holly", "Sophie Kasaei/Sophie", "Jay Gardner/Jay", "James Tindale/James", "Greg Lake/Greg"]),
 ("Name a Roman fort on the line of Hadrian's Wall itself (not Vindolanda or South Shields)", ["Segedunum/Wallsend", "Pons Aelius/Newcastle", "Condercum/Benwell", "Vindobala/Rudchester", "Onnum/Halton Chesters", "Cilurnum/Chesters", "Brocolitia/Carrawburgh", "Vercovicium/Housesteads", "Aesica/Great Chesters", "Banna/Birdoswald", "Camboglanna/Castlesteads", "Uxelodunum/Stanwix", "Aballava/Burgh by Sands", "Coggabata/Drumburgh", "Maia/Bowness-on-Solway/Bowness"]),
 ("Name a ground where Sunderland AFC have played their home games", ["Blue House Field", "Groves Field", "Horatio Street", "Abbs Field", "Newcastle Road", "Roker Park/Roker", "Stadium of Light/The Stadium of Light/SoL"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
