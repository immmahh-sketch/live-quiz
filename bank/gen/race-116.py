# Bank session 10 Oct 2026: 2 more general races -> bank/race-116.json (cheers in other languages, actors with two famous roles). 20 rows each, target 10; wrong options are
# the same kind of thing, never another row's right answer, and never also right for that row.
import json, os
R = []
def race(title, cat, diff, tags, rows):
    rights = {r[1] for r in rows}
    assert len(rows) == 20, (title, len(rows))
    assert len(rights) == 20, (title, 'duplicate right answers')
    bad = [(q, w) for q, right, wrong in rows for w in wrong if w in rights]
    assert not bad, (title, 'recycled', bad)
    for q, right, wrong in rows:
        assert len(wrong) == 3 and len(set(wrong)) == 3 and right not in wrong, (title, q)
    R.append({"type": "race", "text": "The Race: " + title, "target": 10, "category": cat, "tags": tags, "difficulty": diff,
              "bank": [{"q": q, "right": right, "wrong": wrong} for q, right, wrong in rows]})

race("which language says 'Cheers!' like this?", "Words and language", "medium", ["languages", "drinks", "toasts"], [
 ("Prost!", "German", ["Danish", "Swedish", "Romanian"]),
 ("¡Salud!", "Spanish", ["Catalan", "Romanian", "Basque"]),
 ("Santé!", "French", ["Romanian", "Catalan", "Breton"]),
 ("Cin cin!", "Italian", ["Romanian", "Catalan", "Maltese"]),
 ("Kanpai!", "Japanese", ["Thai", "Vietnamese", "Malay"]),
 ("Na zdrowie!", "Polish", ["Russian", "Ukrainian", "Bulgarian"]),
 ("Sláinte!", "Irish", ["Cornish", "Breton", "Basque"]),
 ("Iechyd da!", "Welsh", ["Cornish", "Breton", "Manx"]),
 ("Proost!", "Dutch", ["Danish", "Swedish", "Norwegian"]),
 ("Saúde!", "Portuguese", ["Catalan", "Romanian", "Basque"]),
 ("Gānbēi!", "Mandarin", ["Thai", "Vietnamese", "Malay"]),
 ("Geonbae!", "Korean", ["Thai", "Vietnamese", "Malay"]),
 ("Şerefe!", "Turkish", ["Arabic", "Persian", "Hindi"]),
 ("Yamas!", "Greek", ["Bulgarian", "Albanian", "Romanian"]),
 ("Egészségedre!", "Hungarian", ["Estonian", "Romanian", "Croatian"]),
 ("Na zdraví!", "Czech", ["Russian", "Bulgarian", "Ukrainian"]),
 ("Kippis!", "Finnish", ["Estonian", "Latvian", "Lithuanian"]),
 ("L'chaim!", "Hebrew", ["Arabic", "Persian", "Maltese"]),
 ("Gesondheid!", "Afrikaans", ["Zulu", "Swahili", "Xhosa"]),
 ("Mabuhay!", "Tagalog", ["Malay", "Indonesian", "Thai"])])

race("which actor played both of these?", "Film", "medium", ["actors", "films", "roles"], [
 ("Han Solo and Indiana Jones", "Harrison Ford", ["Mark Hamill", "Kurt Russell", "Tom Selleck"]),
 ("Wolverine and P. T. Barnum", "Hugh Jackman", ["Russell Crowe", "Ryan Reynolds", "Chris Hemsworth"]),
 ("Gandalf and Magneto", "Ian McKellen", ["Michael Gambon", "Christopher Lee", "Michael Fassbender"]),
 ("Hannibal Lecter and Odin", "Anthony Hopkins", ["Mads Mikkelsen", "Brian Cox", "Christopher Plummer"]),
 ("Mr Darcy and King George VI", "Colin Firth", ["Hugh Grant", "Matthew Macfadyen", "Kenneth Branagh"]),
 ("Batman and Beetlejuice", "Michael Keaton", ["George Clooney", "Val Kilmer", "Christian Bale"]),
 ("Captain Jack Sparrow and Willy Wonka", "Johnny Depp", ["Gene Wilder", "Orlando Bloom", "Timothée Chalamet"]),
 ("Professor X and Captain Jean-Luc Picard", "Patrick Stewart", ["James McAvoy", "William Shatner", "Jonathan Frakes"]),
 ("M and Queen Victoria", "Judi Dench", ["Helen Mirren", "Maggie Smith", "Emily Blunt"]),
 ("Gollum and Caesar the ape", "Andy Serkis", ["Elijah Wood", "Ian Holm", "Tom Felton"]),
 ("Iron Man and Sherlock Holmes", "Robert Downey Jr.", ["Jude Law", "Chris Evans", "Mark Ruffalo"]),
 ("Doctor Strange and the TV Sherlock", "Benedict Cumberbatch", ["Tom Hiddleston", "Andrew Scott", "Eddie Redmayne"]),
 ("Mrs Doubtfire and Popeye", "Robin Williams", ["Steve Martin", "Jim Carrey", "Dustin Hoffman"]),
 ("Forrest Gump and the voice of Woody", "Tom Hanks", ["Tim Allen", "Kevin Costner", "Bill Murray"]),
 ("The Terminator and Mr Freeze", "Arnold Schwarzenegger", ["Dolph Lundgren", "Jean-Claude Van Damme", "Dwayne Johnson"]),
 ("Rocky and Rambo", "Sylvester Stallone", ["Dolph Lundgren", "Jean-Claude Van Damme", "Bruce Willis"]),
 ("Mad Max and William Wallace", "Mel Gibson", ["Tom Hardy", "Liam Neeson", "Russell Crowe"]),
 ("Neo and John Wick", "Keanu Reeves", ["Laurence Fishburne", "Hugo Weaving", "Tom Cruise"]),
 ("Bilbo Baggins and Dr Watson", "Martin Freeman", ["Ian Holm", "Jude Law", "Elijah Wood"]),
 ("Elizabeth I and Galadriel", "Cate Blanchett", ["Liv Tyler", "Helen Mirren", "Margot Robbie"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-116.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
