# Bank session 10 Oct 2026: 14 more Categorise questions -> bank/sort-11.json. Two groups, three or four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Books", ["Agatha Christie", "Poirot", "Miss Marple"], "medium", "A Poirot mystery or a Miss Marple mystery?", "Poirot", "Miss Marple", ["Murder on the Orient Express", "Death on the Nile", "The ABC Murders", "The Murder of Roger Ackroyd"], ["The Murder at the Vicarage", "A Murder Is Announced", "The Body in the Library", "4.50 from Paddington"])
s("Music", ["Oscars", "Eurovision"], "medium", "An Oscar-winning film song or a Eurovision winner?", "Oscar winner", "Eurovision winner", ["Let It Go", "Skyfall", "My Heart Will Go On", "Shallow"], ["Waterloo", "Euphoria", "Love Shine a Light", "Puppet on a String"])
s("TV", ["cartoons", "dogs", "cats"], "easy", "A cartoon dog or a cartoon cat?", "Dog", "Cat", ["Scooby-Doo", "Snoopy", "Gromit", "Pluto"], ["Garfield", "Tom", "Sylvester", "Top Cat"])
s("TV", ["The Muppets", "Fraggle Rock"], "medium", "A Muppet or a Fraggle?", "Muppet", "Fraggle", ["Kermit", "Miss Piggy", "Fozzie", "Gonzo"], ["Gobo", "Red", "Mokey", "Wembley"])
s("History", ["Romans", "ancient Greece"], "easy", "A Roman emperor or a Greek philosopher?", "Roman emperor", "Greek philosopher", ["Nero", "Caligula", "Hadrian", "Augustus"], ["Plato", "Socrates", "Aristotle", "Pythagoras"])
s("UK geography", ["Lake District", "Peak District"], "medium", "A town in the Lake District or the Peak District?", "Lake District", "Peak District", ["Keswick", "Ambleside", "Windermere", "Coniston"], ["Bakewell", "Buxton", "Castleton", "Matlock"])
s("Animals", ["baby animals", "collective nouns"], "medium", "A name for a baby animal or for a group of animals?", "Baby animal", "Group", ["Cub", "Kid", "Joey", "Kit"], ["Pride", "Murder", "Gaggle", "Parliament"])
s("Music", ["The Beatles", "Oasis"], "easy", "A Beatles song or an Oasis song?", "The Beatles", "Oasis", ["Yesterday", "Let It Be", "Hey Jude", "Help!"], ["Wonderwall", "Live Forever", "Supersonic", "Whatever"])
s("TV", ["Strictly Come Dancing", "dance"], "medium", "A Latin dance or a ballroom dance, on Strictly?", "Latin", "Ballroom", ["Cha-cha-cha", "Rumba", "Samba", "Paso doble"], ["Waltz", "Foxtrot", "Quickstep", "Tango"])
s("Food and drink", ["whisky", "Scotland", "Ireland"], "medium", "A Scotch whisky or an Irish whiskey?", "Scotch", "Irish", ["Glenfiddich", "Laphroaig", "The Macallan", "Talisker"], ["Jameson", "Bushmills", "Tullamore D.E.W.", "Redbreast"])
s("World geography", ["capital cities", "Africa", "South America"], "hard", "A capital in Africa or in South America?", "Africa", "South America", ["Nairobi", "Accra", "Dakar", "Lusaka"], ["Caracas", "Asunción", "Montevideo", "La Paz"])
s("TV", ["James Bond", "Doctor Who", "actors"], "easy", "Has played James Bond or the Doctor?", "James Bond", "The Doctor", ["Roger Moore", "Timothy Dalton", "Pierce Brosnan", "Daniel Craig"], ["Tom Baker", "Matt Smith", "Peter Capaldi", "David Tennant"])
s("Sport", ["tennis", "Spain", "Switzerland"], "medium", "A tennis star from Spain or from Switzerland?", "Spain", "Switzerland", ["Rafael Nadal", "Carlos Alcaraz", "Juan Carlos Ferrero", "Garbiñe Muguruza"], ["Roger Federer", "Stan Wawrinka", "Martina Hingis", "Belinda Bencic"])
s("World geography", ["capital cities", "Nordic countries", "Baltic states"], "medium", "A Nordic capital or a Baltic states capital?", "Nordic", "Baltic", ["Oslo", "Stockholm", "Copenhagen", "Reykjavik"], ["Tallinn", "Riga", "Vilnius"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-11.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
