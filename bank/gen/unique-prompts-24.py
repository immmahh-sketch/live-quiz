# Bank session 11 Oct 2026: 17 more Only One prompts (sketch shows, sitcoms and dramas) appended to bank/unique-prompts.json.
# Each is a closed list with every correct answer (other accepted forms after a slash), so a fair answer is never knocked out.
import json, os
NEW = [
 ("Name a character from The Fast Show", ["Swiss Toni", "Ted", "Ralph", "Rowley Birkin QC", "Ron Manager", "Jesse", "Arthur Atkinson", "Johnny Nice Painter", "Competitive Dad", "Unlucky Alf", "Ken", "Kenneth", "Bob Fleming", "Billy Bleach", "Dave Angel", "Colin Hunt", "Professor Denzil Dexter", "Tommy Cockles", "Brilliant Kid", "Chanel 9"]),
 ("Name a character from The League of Gentlemen", ["Tubbs/Tubbs Tattsyrup", "Edward/Edward Tattsyrup", "Papa Lazarou", "Pauline/Pauline Campbell-Jones", "Hilary Briss", "Herr Lipp", "Barbara Dixon/Babs", "Mr Chinnery", "Les McQueen", "Benjamin Denton/Benjamin", "Harvey Denton/Harvey", "Val Denton/Val", "Geoff Tipps/Geoff", "Mickey Michaels/Mickey", "Ross Gaines/Ross", "Judee Levinson", "Iris Krell", "Reverend Bernice Woodall/Bernice"]),
 ("Name a character from Bottom", ["Richie/Richard Richard", "Eddie/Eddie Hitler", "Spudgun", "Dave Hedgehog", "Dick Head"]),
 ("Name a character from Spaced, dog included", ["Tim/Tim Bisley", "Daisy/Daisy Steiner", "Mike/Mike Watt", "Brian/Brian Topp", "Marsha", "Twist", "Colin", "Tyres", "Duane Benzie"]),
 ("Name a character from Shetland", ["Jimmy Perez/Perez", "Tosh/Alison McIntosh", "Sandy Wilson/Sandy", "Rhona Kelly/Rhona", "Duncan Hunter/Duncan", "Cassie", "Billy McCabe", "Ruth Calder"]),
 ("Name a character from Broadchurch", ["Alec Hardy/Hardy", "Ellie Miller/Ellie", "Beth Latimer/Beth", "Mark Latimer/Mark", "Danny Latimer/Danny", "Chloe Latimer/Chloe", "Joe Miller", "Tom Miller", "Jocelyn Knight", "Sharon Bishop", "Olly Stevens", "Maggie Radcliffe", "Susan Wright", "Nige Carter/Nigel", "Paul Coates/Reverend Coates", "Trish Winterman", "Claire Ripley", "Lee Ashworth", "Jack Marshall"]),
 ("Name a character from Heartbeat", ["Nick Rowan", "Kate Rowan", "Claude Greengrass/Greengrass", "Oscar Blaketon/Blaketon", "Alf Ventress/Ventress", "Phil Bellamy/Bellamy", "Gina Ward/Gina", "Bernie Scripps/Bernie", "Mike Bradley", "Jackie Lambert", "Vernon Scripps", "David Stockwell", "Rosie Cartwright", "Jo Weston", "Peggy Armstrong"]),
 ("Name a character from Call the Midwife", ["Jenny Lee/Jenny", "Sister Julienne", "Sister Evangelina", "Sister Monica Joan", "Trixie Franklin/Trixie", "Chummy/Camilla Browne", "Cynthia", "Shelagh Turner/Sister Bernadette", "Dr Turner/Patrick Turner", "Fred Buckle/Fred", "Nurse Crane/Phyllis Crane", "Lucille", "Valerie", "Barbara", "Sister Hilda", "Sister Frances", "Violet Buckle/Violet", "Cyril", "Nancy", "Timothy Turner"]),
 ("Name a character from All Creatures Great and Small, Pekingese included", ["James Herriot/James", "Siegfried Farnon/Siegfried", "Tristan Farnon/Tristan", "Helen Alderson/Helen", "Mrs Hall", "Mrs Pumphrey", "Tricki Woo", "Calum Buchanan/Calum"]),
 ("Name a character from Father Brown", ["Father Brown", "Mrs McCarthy/Bridgette McCarthy", "Lady Felicia/Felicia", "Sid Carter/Sid", "Inspector Valentine", "Inspector Sullivan", "Inspector Mallory", "Bunty", "Flambeau", "Brenda Palmer"]),
 ("Name a character from Lost", ["Jack/Jack Shephard", "Kate/Kate Austen", "Sawyer/James Ford", "John Locke/Locke", "Hurley/Hugo Reyes", "Sayid", "Charlie/Charlie Pace", "Claire", "Jin", "Sun", "Michael", "Walt", "Shannon", "Boone", "Ben Linus/Ben", "Desmond", "Juliet", "Ana Lucia", "Mr Eko", "Richard Alpert", "Miles", "Daniel Faraday", "Charlotte", "Frank Lapidus", "Rose", "Bernard", "Vincent"]),
 ("Name a character from Arrested Development", ["Michael Bluth/Michael", "George Michael", "George Bluth Sr/George Sr", "Lucille Bluth/Lucille", "Gob", "Lindsay", "Tobias Fünke/Tobias", "Maeby", "Buster", "Lucille 2/Lucille Austero", "Barry Zuckerkorn/Barry", "Ann Veal/Ann", "Oscar"]),
 ("Name a character from Gilmore Girls", ["Lorelai", "Rory", "Emily", "Richard", "Luke", "Sookie", "Lane", "Paris", "Jess", "Dean", "Logan", "Kirk", "Taylor", "Michel", "Mrs Kim", "Jackson", "Christopher", "April"]),
 ("Name a character from Veep", ["Selina Meyer/Selina", "Gary/Gary Walsh", "Amy/Amy Brookheimer", "Dan/Dan Egan", "Mike/Mike McLintock", "Kent Davison/Kent", "Ben Cafferty/Ben", "Jonah Ryan/Jonah", "Sue", "Catherine Meyer/Catherine", "Richard Splett/Richard", "Tom James"]),
 ("Name a character from Taggart", ["Jim Taggart/Taggart", "Mike Jardine/Jardine", "Jackie Reid", "Matt Burke/Burke", "Stuart Fraser/Fraser", "Robbie Ross", "Peter Livingstone", "Jean Taggart"]),
 ("Name a character from Rab C. Nesbitt", ["Rab/Rab C. Nesbitt", "Mary/Mary Doll", "Jamesie Cotter/Jamesie", "Gash", "Burney", "Ella Cotter/Ella", "Dodie", "Andra"]),
 ("Name a character from Green Wing", ["Guy Secretan/Guy", "Martin Dear/Martin", "Caroline Todd/Caroline", "Mac", "Alan Statham/Statham", "Joanna Clore/Joanna", "Sue White", "Karen Ball/Karen", "Boyce", "Kim Alabaster/Kim", "Harriet Schulenburg/Harriet", "Naughty Rachel/Rachel", "Lyndon"]),
]
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'unique-prompts.json')
cur = json.load(open(path, encoding='utf-8'))
have = {x['p'].lower() for x in cur}
added = [{"p": p, "a": a} for p, a in NEW if p.lower() not in have]
json.dump(cur + added, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(added), 'prompts added; now', len(cur) + len(added))
