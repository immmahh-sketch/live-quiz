# Bank session 10 Oct 2026: 14 more Categorise questions -> bank/sort-7.json. Two groups, four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Film", ["Tim Burton", "Wes Anderson", "directors"], "medium", "Directed by Tim Burton or by Wes Anderson?", "Tim Burton", "Wes Anderson", ["Edward Scissorhands", "Beetlejuice", "Corpse Bride", "Sleepy Hollow"], ["The Grand Budapest Hotel", "Fantastic Mr Fox", "Moonrise Kingdom", "The Royal Tenenbaums"])
s("Books", ["George Orwell", "Aldous Huxley"], "hard", "Written by George Orwell or by Aldous Huxley?", "George Orwell", "Aldous Huxley", ["Animal Farm", "Nineteen Eighty-Four", "Down and Out in Paris and London", "Homage to Catalonia"], ["Brave New World", "The Doors of Perception", "Island", "Point Counter Point"])
s("Music", ["Coldplay", "Keane"], "medium", "A Coldplay song or a Keane song?", "Coldplay", "Keane", ["Yellow", "The Scientist", "Clocks", "Fix You"], ["Somewhere Only We Know", "Everybody's Changing", "This Is the Last Time", "Bedshaped"])
s("Music", ["Arctic Monkeys", "Kaiser Chiefs", "indie"], "medium", "An Arctic Monkeys song or a Kaiser Chiefs song?", "Arctic Monkeys", "Kaiser Chiefs", ["I Bet You Look Good on the Dancefloor", "Fluorescent Adolescent", "Do I Wanna Know?", "505"], ["I Predict a Riot", "Ruby", "Oh My God", "Everyday I Love You Less and Less"])
s("Music", ["Ed Sheeran", "Lewis Capaldi"], "easy", "An Ed Sheeran song or a Lewis Capaldi song?", "Ed Sheeran", "Lewis Capaldi", ["Shape of You", "Perfect", "Castle on the Hill", "Bad Habits"], ["Someone You Loved", "Before You Go", "Hold Me While You Wait", "Bruises"])
s("History", ["castles", "Wales", "England"], "medium", "A castle in Wales or in England?", "Wales", "England", ["Cardiff Castle", "Caerphilly Castle", "Pembroke Castle", "Chepstow Castle"], ["Bamburgh Castle", "Warwick Castle", "Alnwick Castle", "Leeds Castle"])
s("UK geography", ["Scotland", "islands", "Hebrides"], "hard", "An island in the Inner Hebrides or the Outer Hebrides?", "Inner Hebrides", "Outer Hebrides", ["Skye", "Mull", "Islay", "Jura"], ["Lewis", "Harris", "Barra", "South Uist"])
s("Food and drink", ["cocktails", "vodka", "tequila"], "medium", "A cocktail made with vodka or with tequila?", "Vodka", "Tequila", ["Cosmopolitan", "Moscow Mule", "Bloody Mary", "White Russian"], ["Margarita", "Tequila Sunrise", "Paloma", "El Diablo"])
s("Food and drink", ["Mexican food", "Indian food"], "easy", "A Mexican dish or an Indian dish?", "Mexican", "Indian", ["Enchilada", "Quesadilla", "Burrito", "Guacamole"], ["Biryani", "Pakora", "Samosa", "Dhal"])
s("Science", ["Nobel Prize"], "medium", "A Nobel Prize category or not?", "Nobel Prize", "No Nobel Prize", ["Physics", "Chemistry", "Literature", "Peace"], ["Mathematics", "Music", "Architecture", "Engineering"])
s("Science", ["space", "moons", "Jupiter", "Saturn"], "hard", "A moon of Jupiter or a moon of Saturn?", "Jupiter", "Saturn", ["Io", "Europa", "Ganymede", "Callisto"], ["Titan", "Enceladus", "Mimas", "Rhea"])
s("Books", ["spy novels", "Ian Fleming", "John le Carré"], "medium", "Written by Ian Fleming or by John le Carré?", "Ian Fleming", "John le Carré", ["Goldfinger", "Casino Royale", "Dr. No", "Moonraker"], ["Tinker Tailor Soldier Spy", "The Spy Who Came in from the Cold", "The Little Drummer Girl", "The Night Manager"])
s("Music", ["Whitney Houston", "Mariah Carey"], "easy", "A Whitney Houston hit or a Mariah Carey hit?", "Whitney Houston", "Mariah Carey", ["I Wanna Dance with Somebody", "I Will Always Love You", "Greatest Love of All", "One Moment in Time"], ["Hero", "Fantasy", "We Belong Together", "Vision of Love"])
s("UK geography", ["national parks", "Peak District", "North York Moors"], "hard", "In the Peak District or the North York Moors?", "Peak District", "North York Moors", ["Kinder Scout", "Mam Tor", "Bakewell", "Castleton"], ["Goathland", "Helmsley", "Hutton-le-Hole", "Robin Hood's Bay"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-7.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
