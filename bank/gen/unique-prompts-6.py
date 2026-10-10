# Bank session 10 Oct 2026: 20 more Only One prompts appended to bank/unique-prompts.json. Each is a closed list with
# every correct answer (other accepted forms after a slash), so a fair answer is never knocked out.
import json, os
NEW = [
 ("Name a country that shares a land border with Spain or Italy", ["Portugal", "France", "Andorra", "Morocco", "United Kingdom/UK/Britain (Gibraltar)", "Switzerland", "Austria", "Slovenia", "San Marino", "Vatican City/Holy See/the Vatican"]),
 ("Name a country that shares a land border with India", ["Pakistan", "China", "Nepal", "Bhutan", "Bangladesh", "Myanmar/Burma", "Afghanistan"]),
 ("Name one of the New Seven Wonders of the World, voted for in 2007", ["Great Wall of China/Great Wall", "Petra", "Christ the Redeemer", "Machu Picchu", "Chichén Itzá/Chichen Itza", "Colosseum", "Taj Mahal", "Great Pyramid of Giza/Pyramids of Giza (honorary)"]),
 ("Name a member of the Fellowship of the Ring", ["Frodo/Frodo Baggins", "Sam/Samwise Gamgee", "Merry/Meriadoc Brandybuck", "Pippin/Peregrin Took", "Gandalf", "Aragorn/Strider", "Legolas", "Gimli", "Boromir"]),
 ("Name a Hunger Games book or film", ["The Hunger Games", "Catching Fire", "Mockingjay", "Mockingjay – Part 1", "Mockingjay – Part 2", "The Ballad of Songbirds and Snakes", "Sunrise on the Reaping"]),
 ("Name a piece of apparatus in Olympic artistic gymnastics, men's or women's", ["Floor", "Pommel horse", "Rings", "Vault", "Parallel bars", "Horizontal bar/High bar", "Uneven bars/Asymmetric bars", "Balance beam/Beam"]),
 ("Name one of the four ghosts in Pac-Man, or a Tetris piece by its letter", ["Blinky", "Pinky", "Inky", "Clyde", "I", "O", "T", "S", "Z", "J", "L"]),
 ("Name a man who won the Wimbledon singles title from 2000 to 2025", ["Pete Sampras/Sampras", "Goran Ivanišević/Ivanisevic", "Lleyton Hewitt/Hewitt", "Roger Federer/Federer", "Rafael Nadal/Nadal", "Novak Djokovic/Djokovic", "Andy Murray/Murray", "Carlos Alcaraz/Alcaraz", "Jannik Sinner/Sinner"]),
 ("Name a woman who won the Wimbledon singles title from 2010 to 2025", ["Serena Williams/Serena", "Petra Kvitová/Kvitova", "Marion Bartoli/Bartoli", "Garbiñe Muguruza/Muguruza", "Angelique Kerber/Kerber", "Simona Halep/Halep", "Ashleigh Barty/Barty", "Elena Rybakina/Rybakina", "Markéta Vondroušová/Vondrousova", "Barbora Krejčíková/Krejcikova", "Iga Świątek/Swiatek"]),
 ("Name a club that won the FA Cup from 2000 to 2025", ["Chelsea", "Liverpool", "Arsenal", "Manchester United/Man Utd", "Portsmouth", "Manchester City/Man City", "Wigan Athletic/Wigan", "Leicester City/Leicester", "Crystal Palace"]),
 ("Name a club that won the Champions League from 2000 to 2025", ["Real Madrid", "Bayern Munich/Bayern", "AC Milan/Milan", "Porto", "Liverpool", "Barcelona", "Manchester United/Man Utd", "Inter Milan/Inter", "Chelsea", "Manchester City/Man City", "Paris Saint-Germain/PSG"]),
 ("Name a member of Destiny's Child or the Sugababes, any line-up", ["Beyoncé/Beyonce", "Kelly Rowland", "Michelle Williams", "LaTavia Roberson", "LeToya Luckett", "Farrah Franklin", "Siobhán Donaghy/Siobhan Donaghy", "Mutya Buena", "Keisha Buchanan", "Heidi Range", "Amelle Berrabah", "Jade Ewen"]),
 ("Name an English county that borders Scotland or Wales", ["Cumbria", "Northumberland", "Cheshire", "Shropshire", "Herefordshire", "Gloucestershire"]),
 ("Name a country on the Arabian Peninsula", ["Saudi Arabia", "Yemen", "Oman", "United Arab Emirates/UAE", "Qatar", "Kuwait", "Bahrain"]),
 ("Name a country that shares a land border with Brazil", ["Argentina", "Uruguay", "Paraguay", "Bolivia", "Peru", "Colombia", "Venezuela", "Guyana", "Suriname", "France (French Guiana)"]),
 ("Name one of the ten plagues of Egypt", ["Water turned to blood/Blood", "Frogs", "Lice/Gnats", "Flies", "Death of livestock/Pestilence/Dead cattle", "Boils", "Hail", "Locusts", "Darkness", "Death of the firstborn"]),
 ("Name a rank of the British peerage, or its female equivalent", ["Duke", "Duchess", "Marquess/Marquis", "Marchioness", "Earl", "Countess", "Viscount", "Viscountess", "Baron", "Baroness"]),
 ("Name a club from the North East (Durham, Northumberland, Tyne and Wear or Teesside) that has played in the Football League", ["Newcastle United/Newcastle", "Sunderland", "Middlesbrough/Boro", "Hartlepool United/Hartlepool", "Darlington", "Gateshead", "South Shields", "Ashington", "Durham City", "Middlesbrough Ironopolis"]),
 ("Name a stage in a butterfly's life cycle, or a phase of the Moon", ["Egg", "Caterpillar/Larva", "Chrysalis/Pupa", "Butterfly/Adult", "New moon", "Waxing crescent", "First quarter", "Waxing gibbous", "Full moon", "Waning gibbous", "Last quarter/Third quarter", "Waning crescent"]),
 ("Name a member of Oasis or Blur, past or present", ["Liam Gallagher", "Noel Gallagher", "Paul Arthurs/Bonehead", "Paul McGuigan/Guigsy", "Tony McCarroll", "Alan White", "Gem Archer", "Andy Bell", "Zak Starkey", "Chris Sharrock", "Damon Albarn", "Graham Coxon", "Alex James", "Dave Rowntree"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
