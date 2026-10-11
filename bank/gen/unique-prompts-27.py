# Bank session 11 Oct 2026: 7 more Only One prompts (famous families, double acts and superhero teams) appended to bank/unique-prompts.json.
# Each is a closed list with every correct answer (other accepted forms after a slash), so a fair answer is never knocked out.
import json, os
NEW = [
 ("Name one of the nine Osmond brothers and sisters", ["Virl", "Tom", "Alan", "Wayne", "Merrill", "Jay", "Donny", "Marie", "Jimmy/Little Jimmy"]),
 ("Name one of the nine children of Joseph and Rose Kennedy", ["Joseph Jr/Joe", "John/JFK/Jack", "Rosemary", "Kathleen/Kick", "Eunice", "Patricia/Pat", "Robert/Bobby/RFK", "Jean", "Edward/Ted/Teddy"]),
 ("Name one of Queen Victoria's nine children", ["Victoria/Vicky", "Albert Edward/Edward VII/Edward/Bertie", "Alice", "Alfred", "Helena", "Louise", "Arthur", "Leopold", "Beatrice"]),
 ("Name one of the Walton children or one of the Brady Bunch kids", ["John-Boy/John", "Jason", "Mary Ellen", "Erin", "Ben", "Jim-Bob", "Elizabeth", "Greg", "Peter", "Bobby", "Marcia", "Jan", "Cindy"]),
 ("Name one half of the Two Ronnies, Morecambe and Wise, French and Saunders, or Laurel and Hardy", ["Ronnie Barker/Barker", "Ronnie Corbett/Corbett", "Eric Morecambe/Morecambe", "Ernie Wise/Wise", "Dawn French/French", "Jennifer Saunders/Saunders", "Stan Laurel/Laurel", "Oliver Hardy/Hardy"]),
 ("Name one of the original X-Men from the 1963 comic, or their leader", ["Cyclops", "Marvel Girl/Jean Grey", "Beast", "Angel", "Iceman", "Professor X/Charles Xavier"]),
 ("Name one of the seven founding members of DC's Justice League", ["Superman", "Batman", "Wonder Woman", "The Flash/Flash", "Green Lantern", "Aquaman", "Martian Manhunter"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
