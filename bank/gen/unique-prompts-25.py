# Bank session 11 Oct 2026: 11 more Only One prompts (album lists and children's TV) appended to bank/unique-prompts.json.
# Each is a closed list with every correct answer (other accepted forms after a slash), so a fair answer is never knocked out.
import json, os
NEW = [
 ("Name a studio album by Beyoncé (solo)", ["Dangerously in Love", "B'Day", "I Am... Sasha Fierce", "4", "Beyoncé", "Lemonade", "Renaissance", "Cowboy Carter"]),
 ("Name a studio album by Little Mix", ["DNA", "Salute", "Get Weird", "Glory Days", "LM5", "Confetti"]),
 ("Name a studio album by One Direction", ["Up All Night", "Take Me Home", "Midnight Memories", "Four", "Made in the A.M."]),
 ("Name a studio album by the Killers", ["Hot Fuss", "Sam's Town", "Day & Age", "Battle Born", "Wonderful Wonderful", "Imploding the Mirage", "Pressure Machine"]),
 ("Name a studio album by Muse", ["Showbiz", "Origin of Symmetry", "Absolution", "Black Holes and Revelations", "The Resistance", "The 2nd Law", "Drones", "Simulation Theory", "Will of the People"]),
 ("Name a studio album by Eminem", ["Infinite", "The Slim Shady LP", "The Marshall Mathers LP", "The Eminem Show", "Encore", "Relapse", "Recovery", "The Marshall Mathers LP 2", "Revival", "Kamikaze", "Music to Be Murdered By", "The Death of Slim Shady"]),
 ("Name a studio album by Billie Eilish or by Harry Styles", ["When We All Fall Asleep, Where Do We Go?", "Happier Than Ever", "Hit Me Hard and Soft", "Harry Styles", "Fine Line", "Harry's House"]),
 ("Name a studio album by Kaiser Chiefs", ["Employment", "Yours Truly, Angry Mob", "Off with Their Heads", "The Future Is Medieval", "Education, Education, Education & War", "Stay Together", "Duck", "Kaiser Chiefs' Easy Eighth Album"]),
 ("Name a member of the Paw Patrol, pups and their leader", ["Ryder", "Chase", "Marshall", "Skye", "Rocky", "Rubble", "Zuma", "Everest", "Tracker", "Rex", "Liberty"]),
 ("Name one of the Trumpton firemen", ["Pugh", "Barney McGrew", "Cuthbert", "Dibble", "Grubb", "Captain Flack"]),
 ("Name one of the original Mighty Morphin Power Rangers, or their colour", ["Jason/Red Ranger/Red", "Zack/Black Ranger/Black", "Billy/Blue Ranger/Blue", "Trini/Yellow Ranger/Yellow", "Kimberly/Pink Ranger/Pink", "Tommy/Green Ranger/Green/White Ranger/White"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
