# Bank session 11 Oct 2026: 5 more Only One prompts (finals line-ups, the Chasers, TV cook duos, Euro semi-finalists) appended to bank/unique-prompts.json.
# Each is a closed list with every correct answer (other accepted forms after a slash), so a fair answer is never knocked out.
import json, os
NEW = [
 ("Name one of the Lionesses who started the Euro 2022 final", ["Mary Earps/Earps", "Lucy Bronze/Bronze", "Millie Bright/Bright", "Leah Williamson/Williamson", "Rachel Daly/Daly", "Keira Walsh/Walsh", "Georgia Stanway/Stanway", "Fran Kirby/Kirby", "Beth Mead/Mead", "Lauren Hemp/Hemp", "Ellen White/White"]),
 ("Name one of the Chasers on the UK Chase, up to 2025, by name or nickname", ["Mark Labbett/The Beast", "Anne Hegerty/The Governess", "Shaun Wallace/The Dark Destroyer", "Paul Sinha/The Sinnerman", "Jenny Ryan/The Vixen", "Darragh Ennis/The Menace"]),
 ("Name one of England's starting XV in the 2003 Rugby World Cup final", ["Josh Lewsey/Lewsey", "Jason Robinson/Robinson", "Will Greenwood/Greenwood", "Mike Tindall/Tindall", "Ben Cohen/Cohen", "Jonny Wilkinson/Wilkinson", "Matt Dawson/Dawson", "Trevor Woodman/Woodman", "Steve Thompson/Thompson", "Phil Vickery/Vickery", "Martin Johnson/Johnson", "Ben Kay/Kay", "Richard Hill/Hill", "Neil Back/Back", "Lawrence Dallaglio/Dallaglio"]),
 ("Name one of the Hairy Bikers or one of the Two Fat Ladies", ["Si King/Simon King", "Dave Myers", "Jennifer Paterson", "Clarissa Dickson Wright"]),
 ("Name a country that reached the semi-finals of the men's Euro 2024 or the women's Euro 2025", ["Spain", "France", "England", "Netherlands/Holland", "Germany", "Italy"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
