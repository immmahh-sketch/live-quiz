# Bank session 10 Oct 2026: 20 more Only One prompts (TV families, film series, bands, languages, shapes) appended to bank/unique-prompts.json.
# Each is a closed list with every correct answer (other accepted forms after a slash), so a fair answer is never knocked out.
import json, os
NEW = [
 ("Name a member of the Griffin family in Family Guy, including the dog", ["Peter", "Lois", "Meg", "Chris", "Stewie", "Brian"]),
 ("Name a Guardian of the Galaxy from the first film, or a member of the Fantastic Four", ["Star-Lord/Peter Quill", "Gamora", "Drax", "Rocket", "Groot", "Mister Fantastic/Reed Richards", "Invisible Woman/Sue Storm", "Human Torch/Johnny Storm", "The Thing/Ben Grimm"]),
 ("Name a member of The Corrs or of Hanson", ["Andrea Corr/Andrea", "Sharon Corr/Sharon", "Caroline Corr/Caroline", "Jim Corr/Jim", "Isaac Hanson/Isaac", "Taylor Hanson/Taylor", "Zac Hanson/Zac"]),
 ("Name one of the Shelby siblings in Peaky Blinders", ["Arthur", "Tommy/Thomas", "John", "Ada", "Finn"]),
 ("Name a member of the Roy family in Succession: the father or one of his four children", ["Logan", "Connor", "Kendall", "Roman", "Shiv/Siobhan"]),
 ("Name a Twilight book or film", ["Twilight", "New Moon", "Eclipse", "Breaking Dawn", "Breaking Dawn – Part 1", "Breaking Dawn – Part 2", "Midnight Sun"]),
 ("Name a Gallagher brother from Oasis, a Davies brother from the Kinks, or a Kemp brother from Spandau Ballet", ["Liam Gallagher/Liam", "Noel Gallagher/Noel", "Ray Davies/Ray", "Dave Davies/Dave", "Gary Kemp/Gary", "Martin Kemp/Martin"]),
 ("Name a queen who reigned in her own right in England or Britain", ["Mary I/Bloody Mary", "Elizabeth I", "Mary II", "Anne/Queen Anne", "Victoria/Queen Victoria", "Elizabeth II", "Lady Jane Grey/Jane", "Empress Matilda/Matilda"]),
 ("Name a US state whose name begins with New, North or South", ["New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "South Carolina", "South Dakota"]),
 ("Name a Wallace and Gromit film, long or short", ["A Grand Day Out", "The Wrong Trousers", "A Close Shave", "A Matter of Loaf and Death", "The Curse of the Were-Rabbit", "Vengeance Most Fowl"]),
 ("Name a member of the Supremes' original trio, or of the Ronettes", ["Diana Ross", "Mary Wilson", "Florence Ballard", "Ronnie Spector", "Estelle Bennett", "Nedra Talley"]),
 ("Name a member of the Munster family or the Jetson family, pets and robots included", ["Herman", "Lily", "Grandpa", "Eddie", "Marilyn", "George", "Jane", "Judy", "Elroy", "Astro", "Rosie"]),
 ("Name a day of the week in French or in Spanish", ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche", "Lunes", "Martes", "Miércoles/Miercoles", "Jueves", "Viernes", "Sábado/Sabado", "Domingo"]),
 ("Name a four-sided shape", ["Square", "Rectangle", "Rhombus/Diamond", "Parallelogram", "Trapezium/Trapezoid", "Kite"]),
 ("Name a month of the year in French", ["Janvier", "Février/Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août/Aout", "Septembre", "Octobre", "Novembre", "Décembre/Decembre"]),
 ("Name a number from one to ten in German", ["Eins", "Zwei", "Drei", "Vier", "Fünf/Funf/Fuenf", "Sechs", "Sieben", "Acht", "Neun", "Zehn"]),
 ("Name one of the Nolan sisters who sang in the Nolans", ["Anne", "Denise", "Maureen", "Linda", "Bernie", "Coleen"]),
 ("Name a member of Bananarama (any line-up) or of Shakespears Sister", ["Sara Dallin/Sara", "Keren Woodward/Keren", "Siobhan Fahey/Siobhan", "Jacquie O'Sullivan/Jacquie", "Marcella Detroit/Marcella"]),
 ("Name one of the Three Musketeers, d'Artagnan, or one of the Three Wise Men", ["Athos", "Porthos", "Aramis", "d'Artagnan/D'Artagnan", "Caspar/Gaspar/Casper", "Melchior", "Balthazar"]),
 ("Name one of the ghosts in Pac-Man, or one of the Mario brothers", ["Blinky", "Pinky", "Inky", "Clyde", "Mario", "Luigi"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
