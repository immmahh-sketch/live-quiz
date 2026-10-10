# Bank session 10 Oct 2026: 4 more general races -> bank/race-28.json. 20 rows each, target 10; wrong options are
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

race("which body part is this slang for?", "Words and language", "easy", ["slang", "the body"], [
 ("Noggin", "Head", ["Knees", "Shoulders", "Chest"]), ("Conk", "Nose", ["Chin", "Cheeks", "Forehead"]), ("Gob", "Mouth", ["Chin", "Cheeks", "Throat"]),
 ("Lugholes", "Ears", ["Nostrils", "Cheeks", "Eyebrows"]), ("Peepers", "Eyes", ["Eyebrows", "Lips", "Cheeks"]), ("Gnashers", "Teeth", ["Lips", "Tongue", "Gums"]),
 ("Plates (of meat)", "Feet", ["Knees", "Ankles", "Shins"]), ("Mitts", "Hands", ["Wrists", "Thumbs", "Knees"]), ("Ticker", "Heart", ["Lungs", "Liver", "Kidneys"]),
 ("Pins", "Legs", ["Arms", "Wrists", "Ankles"]), ("Barnet (Fair)", "Hair", ["Beard", "Eyebrows", "Scalp"]), ("Boat (race)", "Face", ["Back", "Chest", "Knees"]),
 ("Bread basket", "Stomach", ["Chest", "Lungs", "Back"]), ("Digits", "Fingers", ["Wrists", "Ankles", "Kidneys"]), ("Derrière", "Bottom", ["Back", "Hips", "Thighs"]),
 ("Grey matter", "Brain", ["Lungs", "Liver", "Spine"]), ("Guns", "Biceps", ["Thighs", "Calves", "Shoulders"]), ("Scruff", "Back of the neck", ["Throat", "Chin", "Shoulders"]),
 ("Tootsies", "Toes", ["Ankles", "Knees", "Shins"]), ("Funny bone", "Elbow", ["Knee", "Wrist", "Ankle"])])

race("who composed the music for this film?", "Film", "hard", ["film music", "composers"], [
 ("Star Wars", "John Williams", ["Jerry Goldsmith", "Basil Poledouris", "Max Steiner"]), ("The Lord of the Rings", "Howard Shore", ["Patrick Doyle", "Harry Gregson-Williams", "John Powell"]),
 ("Gladiator", "Hans Zimmer", ["Harry Gregson-Williams", "John Powell", "Ramin Djawadi"]), ("Titanic", "James Horner", ["Thomas Newman", "Alexandre Desplat", "Craig Armstrong"]),
 ("The Good, the Bad and the Ugly", "Ennio Morricone", ["Nino Rota", "Jerry Goldsmith", "Max Steiner"]), ("Psycho", "Bernard Herrmann", ["Max Steiner", "Jerry Goldsmith", "Nino Rota"]),
 ("Chariots of Fire", "Vangelis", ["Jean-Michel Jarre", "Mike Oldfield", "Rick Wakeman"]), ("The Pink Panther", "Henry Mancini", ["Burt Bacharach", "Nelson Riddle", "Quincy Jones"]),
 ("Lawrence of Arabia", "Maurice Jarre", ["Miklós Rózsa", "Max Steiner", "Dimitri Tiomkin"]), ("Oppenheimer", "Ludwig Göransson", ["Mica Levi", "Jóhann Jóhannsson", "Justin Hurwitz"]),
 ("Back to the Future", "Alan Silvestri", ["Jerry Goldsmith", "James Newton Howard", "Basil Poledouris"]), ("Batman (1989)", "Danny Elfman", ["James Newton Howard", "Jerry Goldsmith", "Christopher Young"]),
 ("The Piano", "Michael Nyman", ["Philip Glass", "Gabriel Yared", "Rachel Portman"]), ("Amélie", "Yann Tiersen", ["Gabriel Yared", "Alexandre Desplat", "Philip Glass"]),
 ("Out of Africa", "John Barry", ["Ron Goodwin", "George Fenton", "David Arnold"]), ("Rocky", "Bill Conti", ["Ron Goodwin", "Jerry Goldsmith", "James Newton Howard"]),
 ("Spirited Away", "Joe Hisaishi", ["Ryuichi Sakamoto", "Yoko Kanno", "Toru Takemitsu"]), ("Up", "Michael Giacchino", ["Thomas Newman", "Randy Newman", "Mark Mothersbaugh"]),
 ("Joker", "Hildur Guðnadóttir", ["Mica Levi", "Jóhann Jóhannsson", "Justin Hurwitz"]), ("The Great Escape", "Elmer Bernstein", ["Ron Goodwin", "Malcolm Arnold", "Dimitri Tiomkin"])])

race("who's the real writer behind this pen name?", "Books", "hard", ["pen names", "authors"], [
 ("George Orwell", "Eric Blair", ["Aldous Huxley", "H. G. Wells", "Evelyn Waugh"]), ("Mark Twain", "Samuel Clemens", ["Bret Harte", "Jack London", "Herman Melville"]),
 ("George Eliot", "Mary Ann Evans", ["Elizabeth Gaskell", "Mary Shelley", "Fanny Burney"]), ("Lewis Carroll", "Charles Dodgson", ["Edward Lear", "Charles Kingsley", "Kenneth Grahame"]),
 ("Dr. Seuss", "Theodor Geisel", ["Maurice Sendak", "Shel Silverstein", "Roald Dahl"]), ("Voltaire", "François-Marie Arouet", ["Jean-Jacques Rousseau", "Denis Diderot", "Blaise Pascal"]),
 ("Currer Bell", "Charlotte Brontë", ["Branwell Brontë", "Elizabeth Gaskell", "Jane Austen"]), ("Ellis Bell", "Emily Brontë", ["Branwell Brontë", "Elizabeth Gaskell", "Mary Shelley"]),
 ("Acton Bell", "Anne Brontë", ["Branwell Brontë", "Mary Shelley", "Fanny Burney"]), ("Boz", "Charles Dickens", ["Wilkie Collins", "William Thackeray", "Anthony Trollope"]),
 ("O. Henry", "William Sydney Porter", ["Jack London", "Bret Harte", "Ambrose Bierce"]), ("Saki", "Hector Hugh Munro", ["P. G. Wodehouse", "E. F. Benson", "Jerome K. Jerome"]),
 ("Stendhal", "Marie-Henri Beyle", ["Gustave Flaubert", "Honoré de Balzac", "Victor Hugo"]), ("Molière", "Jean-Baptiste Poquelin", ["Jean Racine", "Pierre Corneille", "Jean de La Fontaine"]),
 ("John le Carré", "David Cornwell", ["Len Deighton", "Ian Fleming", "Frederick Forsyth"]), ("Richard Bachman", "Stephen King", ["Dean Koontz", "Peter Straub", "Clive Barker"]),
 ("Barbara Vine", "Ruth Rendell", ["P. D. James", "Minette Walters", "Val McDermid"]), ("Mary Westmacott", "Agatha Christie", ["Dorothy L. Sayers", "Ngaio Marsh", "Margery Allingham"]),
 ("Lemony Snicket", "Daniel Handler", ["Neil Gaiman", "Philip Pullman", "Roald Dahl"]), ("Ellis Peters", "Edith Pargeter", ["Dorothy L. Sayers", "Margery Allingham", "Ngaio Marsh"])])

race("whose parliament is this?", "Politics", "hard", ["parliaments", "countries"], [
 ("The Knesset", "Israel", ["Lebanon", "Jordan", "Cyprus"]), ("The Bundestag", "Germany", ["Austria", "Switzerland", "the Netherlands"]),
 ("The State Duma", "Russia", ["Ukraine", "Belarus", "Kazakhstan"]), ("The Dáil", "Ireland", ["Greenland", "the Faroe Islands", "Portugal"]),
 ("The Storting", "Norway", ["the Faroe Islands", "Greenland", "the Netherlands"]), ("The Riksdag", "Sweden", ["the Faroe Islands", "Greenland", "the Netherlands"]),
 ("The Folketing", "Denmark", ["the Faroe Islands", "Greenland", "the Netherlands"]), ("The Althing", "Iceland", ["the Faroe Islands", "Greenland", "Jersey"]),
 ("The Sejm", "Poland", ["Czechia", "Slovakia", "Ukraine"]), ("The Cortes Generales", "Spain", ["Portugal", "Italy", "Andorra"]),
 ("The National Diet", "Japan", ["South Korea", "China", "Taiwan"]), ("The Senedd", "Wales", ["Jersey", "Guernsey", "the Faroe Islands"]),
 ("Tynwald", "the Isle of Man", ["Jersey", "Guernsey", "the Faroe Islands"]), ("Holyrood", "Scotland", ["Jersey", "Guernsey", "England"]),
 ("Stormont", "Northern Ireland", ["Jersey", "Guernsey", "England"]), ("The Eduskunta", "Finland", ["Hungary", "Belarus", "Ukraine"]),
 ("The Saeima", "Latvia", ["Belarus", "Ukraine", "Hungary"]), ("The Seimas", "Lithuania", ["Belarus", "Ukraine", "Slovakia"]),
 ("The Riigikogu", "Estonia", ["Belarus", "Hungary", "Ukraine"]), ("The Lok Sabha", "India", ["Pakistan", "Bangladesh", "Sri Lanka"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-28.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
