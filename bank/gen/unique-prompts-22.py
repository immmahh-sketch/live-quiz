# Bank session 11 Oct 2026: 21 more Only One prompts (British and American sitcoms and dramas, two band discographies) appended to bank/unique-prompts.json.
# Each is a closed list with every correct answer (other accepted forms after a slash), so a fair answer is never knocked out.
import json, os
NEW = [
 ("Name a character from Derry Girls", ["Erin Quinn/Erin", "Orla McCool/Orla", "Clare Devlin/Clare", "Michelle Mallon/Michelle", "James Maguire/James", "Mary Quinn/Mary", "Gerry Quinn/Gerry", "Sarah McCool/Sarah", "Granda Joe/Joe", "Sister Michael", "Uncle Colm/Colm", "Father Peter", "Jenny Joyce", "Aisling", "Anna Quinn", "Dee Devlin"]),
 ("Name a member of the Goodman family in Friday Night Dinner, or their neighbour", ["Martin Goodman/Martin", "Jackie Goodman/Jackie", "Adam Goodman/Adam", "Jonny Goodman/Jonny", "Grandma/Nelly", "Jim Bell/Jim", "Wilson"]),
 ("Name a member of the Brockman family in Outnumbered", ["Pete", "Sue", "Jake", "Ben", "Karen", "Grandad", "Angela"]),
 ("Name a character from Detectorists", ["Andy Stone/Andy", "Lance Stater/Lance", "Becky", "Sophie", "Maggie", "Terry", "Sheila", "Russell", "Hugh", "Varde", "Louise", "Kate", "Toni", "Simon", "Garfunkel", "Peter"]),
 ("Name a character from Mrs Brown's Boys", ["Agnes Brown/Mrs Brown/Agnes", "Cathy", "Dermot", "Buster", "Rory", "Dino", "Mark", "Betty", "Maria", "Winnie", "Grandad", "Sharon", "Father Damien"]),
 ("Name a character from Birds of a Feather", ["Sharon", "Tracey", "Dorien", "Garth", "Darryl/Daryl", "Chris", "Marcus", "Travis"]),
 ("Name a character, human or animal, from The Good Life", ["Tom Good/Tom", "Barbara Good/Barbara", "Margo Leadbetter/Margo", "Jerry Leadbetter/Jerry", "Geraldine", "Pinky", "Perky", "Lenin", "Sir"]),
 ("Name a character from Rising Damp, cat included", ["Rigsby", "Alan", "Philip", "Miss Jones/Ruth Jones/Ruth", "Vienna", "Brenda"]),
 ("Name a character from Hi-de-Hi!", ["Gladys Pugh/Gladys", "Jeffrey Fairbrother", "Ted Bovis/Ted", "Spike", "Peggy", "Mr Partridge", "Fred Quilley", "Sylvia", "Barry Stuart-Hargreaves/Barry", "Yvonne Stuart-Hargreaves/Yvonne", "Clive Dempster", "Joe Maplin"]),
 ("Name a character from Are You Being Served?", ["Mrs Slocombe", "Mr Humphries", "Captain Peacock", "Mr Lucas", "Miss Brahms", "Mr Rumbold", "Mr Grainger", "Young Mr Grace", "Mr Harman", "Mr Mash", "Mr Goldberg", "Mr Spooner", "Mr Tebbs"]),
 ("Name a character from Downton Abbey", ["Robert Crawley/Lord Grantham", "Cora", "Lady Mary/Mary", "Lady Edith/Edith", "Lady Sybil/Sybil", "Violet/Dowager Countess", "Matthew Crawley/Matthew", "Isobel Crawley/Isobel", "Tom Branson/Branson", "Carson", "Mrs Hughes", "Bates", "Anna", "Thomas Barrow/Barrow", "Mrs Patmore", "Daisy", "O'Brien", "Molesley", "William", "Rose", "Henry Talbot", "Bertie Pelham", "Andy", "Baxter"]),
 ("Name a character from Breaking Bad", ["Walter White/Walt/Heisenberg", "Jesse Pinkman/Jesse", "Skyler White/Skyler", "Hank Schrader/Hank", "Marie Schrader/Marie", "Walter White Jr./Flynn", "Saul Goodman/Saul", "Gus Fring/Gus", "Mike Ehrmantraut/Mike", "Todd", "Jane Margolis/Jane", "Tuco Salamanca/Tuco", "Hector Salamanca/Hector", "Gale Boetticher/Gale", "Lydia", "Badger", "Skinny Pete", "Steven Gomez/Gomez", "Jack Welker/Uncle Jack", "Holly", "Huell", "Krazy-8", "Combo", "Andrea", "Brock", "Ted Beneke"]),
 ("Name a member of the Gallagher family in Shameless", ["Frank", "Fiona", "Lip", "Ian", "Carl", "Debbie", "Liam", "Monica"]),
 ("Name a character from The Fresh Prince of Bel-Air", ["Will", "Carlton", "Uncle Phil/Philip", "Aunt Viv/Vivian", "Hilary", "Ashley", "Nicky", "Geoffrey", "Jazz"]),
 ("Name a character from Frasier, dog included", ["Frasier Crane/Frasier", "Niles", "Martin", "Daphne", "Roz", "Eddie", "Lilith", "Maris", "Bulldog", "Gil", "Noel", "Kenny", "Frederick"]),
 ("Name a character from Cheers", ["Sam Malone/Sam", "Diane Chambers/Diane", "Carla", "Norm", "Cliff", "Coach", "Woody", "Rebecca Howe/Rebecca", "Frasier Crane/Frasier", "Lilith"]),
 ("Name a character from Seinfeld", ["Jerry", "George", "Elaine", "Kramer", "Newman", "Frank Costanza", "Estelle Costanza", "Uncle Leo", "Puddy", "Peterman", "Steinbrenner", "Morty Seinfeld", "Helen Seinfeld", "Susan"]),
 ("Name a character from The Big Bang Theory", ["Sheldon", "Leonard", "Penny", "Howard", "Raj", "Bernadette", "Amy", "Stuart", "Mrs Wolowitz", "Leslie Winkle", "Barry Kripke", "Emily", "Wil Wheaton", "Mary Cooper", "Beverly Hofstadter"]),
 ("Name a character from The Sopranos", ["Tony Soprano/Tony", "Carmela", "Meadow", "A.J./Anthony Jr.", "Livia", "Uncle Junior/Junior", "Christopher Moltisanti/Christopher", "Paulie Walnuts/Paulie", "Silvio Dante/Silvio", "Big Pussy/Pussy", "Dr Melfi/Melfi", "Adriana", "Janice", "Bobby Bacala/Bobby", "Furio", "Richie Aprile", "Ralph Cifaretto/Ralphie", "Johnny Sack", "Phil Leotardo", "Vito"]),
 ("Name a studio album by Blur", ["Leisure", "Modern Life Is Rubbish", "Parklife", "The Great Escape", "Blur", "13", "Think Tank", "The Magic Whip", "The Ballad of Darren"]),
 ("Name a studio album by Radiohead", ["Pablo Honey", "The Bends", "OK Computer", "Kid A", "Amnesiac", "Hail to the Thief", "In Rainbows", "The King of Limbs", "A Moon Shaped Pool"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
