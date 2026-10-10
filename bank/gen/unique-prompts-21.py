# Bank session 10 Oct 2026: 20 more Only One prompts (British sitcom and drama characters, landlocked countries) appended to bank/unique-prompts.json.
# Each is a closed list with every correct answer (other accepted forms after a slash), so a fair answer is never knocked out.
import json, os
NEW = [
 ("Name a character from the Wallace and Gromit films", ["Wallace", "Gromit", "Feathers McGraw", "Shaun", "Preston", "Wendolene", "Lady Tottington/Lady Campanula Tottington", "Victor Quartermaine", "Hutch", "Piella Bakewell", "Fluffles", "Norbot"]),
 ("Name one of the main crew of Red Dwarf", ["Dave Lister/Lister", "Arnold Rimmer/Rimmer", "Cat", "Kryten", "Holly", "Kristine Kochanski/Kochanski"]),
 ("Name one of the four students in The Young Ones", ["Rik", "Vyvyan", "Neil", "Mike"]),
 ("Name a character from Porridge", ["Norman Stanley Fletcher/Fletcher/Fletch", "Lennie Godber/Godber", "Mr Mackay/Mackay", "Mr Barrowclough/Barrowclough", "Lukewarm", "Harry Grout/Grouty", "Blanco", "McLaren", "Warren", "Ives"]),
 ("Name a landlocked country in Europe", ["Austria", "Switzerland", "Liechtenstein", "Czech Republic/Czechia", "Slovakia", "Hungary", "Serbia", "North Macedonia", "Kosovo", "Moldova", "Belarus", "Andorra", "San Marino", "Vatican City", "Luxembourg"]),
 ("Name a landlocked country in Africa", ["Mali", "Niger", "Chad", "Burkina Faso", "Central African Republic", "South Sudan", "Ethiopia", "Uganda", "Rwanda", "Burundi", "Zambia", "Zimbabwe", "Malawi", "Botswana", "Lesotho", "Eswatini/Swaziland"]),
 ("Name a character from The Inbetweeners", ["Will McKenzie/Will", "Simon Cooper/Simon", "Jay Cartwright/Jay", "Neil Sutherland/Neil", "Mr Gilbert", "Carli D'Amato/Carli", "Charlotte Hinchcliffe/Charlotte", "Polly McKenzie", "Pamela Cooper", "Alan Cooper", "Terry Cartwright"]),
 ("Name a character from Peep Show", ["Mark Corrigan/Mark", "Jeremy Usborne/Jez/Jeremy", "Sophie Chapman/Sophie", "Super Hans", "Alan Johnson/Johnson", "Dobby", "Toni", "Big Suze/Suze", "Jeff Heaney/Jeff", "Nancy", "Gerard"]),
 ("Name a character from Father Ted", ["Father Ted Crilly/Ted", "Father Dougal McGuire/Dougal", "Father Jack Hackett/Jack", "Mrs Doyle", "Bishop Len Brennan/Bishop Brennan", "Father Dick Byrne", "Father Noel Furlong", "Tom", "Pat Mustard", "Henry Sellers", "Father Larry Duff", "Father Stone"]),
 ("Name one of the main characters in Men Behaving Badly", ["Gary", "Tony", "Dorothy", "Deborah", "George", "Anthea", "Les"]),
 ("Name a character from Absolutely Fabulous", ["Edina/Eddy/Edina Monsoon", "Patsy/Patsy Stone", "Saffron/Saffy", "Bubble", "Mother", "Marshall", "Bo"]),
 ("Name a character from Keeping Up Appearances", ["Hyacinth Bucket/Hyacinth", "Richard", "Onslow", "Daisy", "Rose", "Violet", "Emmet", "Elizabeth", "Daddy", "Sheridan", "The Vicar"]),
 ("Name a character from Open All Hours", ["Arkwright", "Granville", "Nurse Gladys Emmanuel/Gladys", "Mrs Featherstone", "Mavis"]),
 ("Name a character from Last of the Summer Wine", ["Compo", "Clegg", "Foggy", "Blamire", "Nora Batty", "Ivy", "Wally Batty", "Howard", "Pearl", "Marina", "Truly", "Seymour", "Smiler", "Barry", "Glenda", "Edie", "Wesley"]),
 ("Name a character from Line of Duty", ["Ted Hastings", "Steve Arnott", "Kate Fleming", "Tony Gates", "Lindsay Denton", "Roz Huntley", "Ian Buckells", "Jo Davidson", "Matthew 'Dot' Cottan/Dot Cottan", "John Corbett", "Gill Biggeloe", "Patricia Carmichael", "Danny Waldron", "Ryan Pilkington"]),
 ("Name a character from Happy Valley", ["Catherine Cawood/Catherine", "Tommy Lee Royce", "Ryan Cawood/Ryan", "Clare Cartwright/Clare", "Kevin Weatherill", "Ann Gallagher", "Daniel Cawood", "Alison Garrs", "Faisal Bhatti", "Joanna Hepworth", "Ashley Cowgill", "Neville Buckley", "John Wadsworth"]),
 ("Name a character from The Thick of It", ["Malcolm Tucker", "Hugh Abbot", "Ollie Reeder", "Glenn Cullen", "Terri Coverley", "Nicola Murray", "Jamie McDonald", "Peter Mannion", "Stewart Pearson", "Phil Smith", "Emma Messinger", "Ben Swain"]),
 ("Name one of the 'Magnificent Seven' builders in Auf Wiedersehen, Pet", ["Dennis", "Neville", "Oz", "Barry", "Bomber", "Moxey", "Wayne"]),
 ("Name a character from the ITV drama Vera", ["Vera Stanhope/Vera", "Joe Ashworth", "Aiden Healy", "Kenny Lockhart", "Billy Cartwright", "Malcolm Donahue", "Jac Williams", "Bethany Whelan", "Holly Lawson", "Mark Edwards"]),
 ("Name a member of the Boswell family in Bread", ["Nellie Boswell/Nellie/Ma", "Joey", "Adrian", "Jack", "Aveline", "Billy", "Grandad", "Freddie"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
