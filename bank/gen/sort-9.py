# Bank session 10 Oct 2026: 13 more Categorise questions -> bank/sort-6.json. Two groups, four items each. Each pair of
# categories was checked against every Categorise question already in the live bank.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Numbers", ["calendar", "leap years", "wow"], "hard", "Leap year or not?", "Leap year", "Not a leap year", ["2000", "1996", "2024", "2400"], ["1900", "2100", "2023", "1800"])
s("Words and language", ["Shakespeare", "Bible", "quotes"], "medium", "From Shakespeare or from the Bible?", "Shakespeare", "The Bible", ["To thine own self be true", "The course of true love never did run smooth", "Neither a borrower nor a lender be", "All the world's a stage"], ["Let there be light", "The love of money is the root of all evil", "An eye for an eye", "Am I my brother's keeper?"])
s("Art", ["Turner", "Constable", "painting"], "hard", "Painted by Turner or by Constable?", "Turner", "Constable", ["The Fighting Temeraire", "Rain, Steam and Speed", "The Slave Ship", "Snow Storm: Hannibal Crossing the Alps"], ["The Hay Wain", "Flatford Mill", "Salisbury Cathedral from the Meadows", "The Cornfield"])
s("Film", ["Kubrick", "Tarantino", "directors"], "medium", "Directed by Stanley Kubrick or by Quentin Tarantino?", "Kubrick", "Tarantino", ["The Shining", "A Clockwork Orange", "Full Metal Jacket", "Spartacus"], ["Pulp Fiction", "Reservoir Dogs", "Jackie Brown", "Django Unchained"])
s("Film", ["Nolan", "Spielberg", "directors"], "medium", "Directed by Christopher Nolan or by Steven Spielberg?", "Nolan", "Spielberg", ["Inception", "Interstellar", "Memento", "Dunkirk"], ["War Horse", "Lincoln", "Munich", "The Terminal"])
s("James Bond", ["Daniel Craig", "Pierce Brosnan"], "easy", "A Daniel Craig Bond film or a Pierce Brosnan one?", "Daniel Craig", "Pierce Brosnan", ["Casino Royale", "Skyfall", "Spectre", "Quantum of Solace"], ["GoldenEye", "Tomorrow Never Dies", "The World Is Not Enough", "Die Another Day"])
s("Books", ["Harry Potter", "Lord of the Rings"], "easy", "Harry Potter character or Lord of the Rings character?", "Harry Potter", "Lord of the Rings", ["Dobby", "Hagrid", "Sirius Black", "Luna Lovegood"], ["Gimli", "Legolas", "Samwise Gamgee", "Boromir"])
s("Art", ["Rembrandt", "Vermeer", "Dutch art"], "hard", "Painted by Rembrandt or by Vermeer?", "Rembrandt", "Vermeer", ["The Night Watch", "The Anatomy Lesson of Dr Tulp", "The Jewish Bride", "Self-Portrait with Two Circles"], ["Girl with a Pearl Earring", "The Milkmaid", "View of Delft", "The Art of Painting"])
s("Books", ["poetry", "Wordsworth", "Keats"], "hard", "A poem by Wordsworth or by Keats?", "Wordsworth", "Keats", ["The Prelude", "Tintern Abbey", "Upon Westminster Bridge", "I Wandered Lonely as a Cloud"], ["Ode to a Nightingale", "To Autumn", "Ode on a Grecian Urn", "La Belle Dame sans Merci"])
s("Music", ["opera", "Verdi", "Puccini"], "medium", "An opera by Verdi or by Puccini?", "Verdi", "Puccini", ["Aida", "La Traviata", "Rigoletto", "Otello"], ["Madama Butterfly", "La Bohème", "Tosca", "Turandot"])
s("Music", ["Liverpool", "Manchester", "bands"], "medium", "A band from Liverpool or from Manchester?", "Liverpool", "Manchester", ["The Beatles", "Echo & the Bunnymen", "Frankie Goes to Hollywood", "The La's"], ["Oasis", "The Smiths", "Joy Division", "The Stone Roses"])
s("Science", ["weather", "clouds"], "hard", "A low cloud or a high cloud?", "Low", "High", ["Stratus", "Stratocumulus", "Nimbostratus", "Cumulus"], ["Cirrus", "Cirrostratus", "Cirrocumulus", "Contrails"])
s("Olympics", ["Winter Olympics"], "easy", "Winter Olympic sport on ice or on snow?", "Ice", "Snow", ["Curling", "Bobsleigh", "Speed skating", "Ice hockey"], ["Biathlon", "Ski jumping", "Slalom", "Snowboard cross"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-6.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
