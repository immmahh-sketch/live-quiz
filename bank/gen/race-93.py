# Bank session 10 Oct 2026: 2 more general races -> bank/race-93.json. 20 rows each, target 10; wrong options are
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

race("which famous 'Fox'?", "General knowledge", "medium", ["foxes", "wordplay"], [
 ("The actor who played DS Hathaway in Lewis", "Laurence Fox", ["Kevin Whately", "John Thaw", "Shaun Evans"]), ("Marty McFly in Back to the Future", "Michael J. Fox", ["Matthew Broderick", "Christopher Lloyd", "Rob Lowe"]),
 ("The 1980s pin-up who sang 'Touch Me'", "Samantha Fox", ["Sabrina", "Kim Wilde", "Sinitta"]), ("The actress who starred in the first two Transformers films", "Megan Fox", ["Rosie Huntington-Whiteley", "Margot Robbie", "Mila Kunis"]),
 ("The actress who plays pathologist Nikki Alexander in Silent Witness", "Emilia Fox", ["Amanda Burton", "Liz Carr", "Sophie Okonedo"]), ("The poisonous purple flower that gave medicine digitalis", "Foxglove", ["Bluebell", "Lupin", "Hollyhock"]),
 ("The smooth, gliding ballroom dance on Strictly", "Foxtrot", ["Quickstep", "Waltz", "Tango"]), ("Mozilla's web browser", "Firefox", ["Chrome", "Safari", "Opera"]),
 ("Rupert Murdoch's American news channel", "Fox News", ["CNN", "MSNBC", "CBS News"]), ("The film studio with the searchlights and fanfare", "20th Century Fox", ["Paramount", "Universal", "MGM"]),
 ("Jimi Hendrix's 1967 song", "Foxy Lady", ["Hey Joe", "The Wind Cries Mary", "Fire"]), ("The mints sold by Peppy the polar bear", "Fox's Glacier Mints", ["Polo", "Trebor Extra Strong Mints", "Murray Mints"]),
 ("The X-Files agent who wants to believe", "Fox Mulder", ["Dana Scully", "Walter Skinner", "Cigarette Smoking Man"]), ("The Victorian photography pioneer of Lacock Abbey", "Fox Talbot", ["Louis Daguerre", "Julia Margaret Cameron", "Eadweard Muybridge"]),
 ("Ylvis's 2013 viral hit", "What Does the Fox Say?", ["Gangnam Style", "Harlem Shake", "The Ketchup Song"]), ("The smallest fox of all, with huge ears, from the Sahara", "Fennec fox", ["Arctic fox", "Red fox", "Swift fox"]),
 ("Disney's 1981 film about a hunting dog's friendship with a fox cub", "The Fox and the Hound", ["The Aristocats", "The Rescuers", "Oliver & Company"]), ("A soldier's dug-in shelter", "Foxhole", ["Trench", "Bunker", "Pillbox"]),
 ("The Whig politician who was Pitt the Younger's great rival", "Charles James Fox", ["Edmund Burke", "Lord North", "Spencer Perceval"]), ("The actor who played the Jackal in 1973's The Day of the Jackal", "Edward Fox", ["James Fox", "Michael Caine", "Oliver Reed"])])

race("which famous 'Tiger'?", "General knowledge", "medium", ["tigers", "wordplay"], [
 ("The golfer with 15 major titles", "Tiger Woods", ["Phil Mickelson", "Jack Nicklaus", "Rory McIlroy"]), ("Netflix's 2020 series about Joe Exotic", "Tiger King", ["Making a Murderer", "The Tinder Swindler", "Wild Wild Country"]),
 ("The de Havilland biplane that trained wartime pilots", "Tiger Moth", ["Sopwith Camel", "Gipsy Moth", "Spitfire"]), ("Ireland's boom economy of the 1990s and 2000s", "Celtic Tiger", ["Asian Tiger", "Emerald Boom", "Shamrock Surge"]),
 ("Cardiff's old docklands, home of Shirley Bassey", "Tiger Bay", ["Splott", "Grangetown", "Penarth"]), ("Mud's 1974 number one", "Tiger Feet", ["Lonely This Christmas", "Dyna-mite", "Blockbuster"]),
 ("The spotted orange lily", "Tiger lily", ["Arum lily", "Water lily", "Easter lily"]), ("The big striped prawn", "Tiger prawn", ["King prawn", "Langoustine", "Crayfish"]),
 ("The loaf with the crackly, mottled top", "Tiger bread", ["Bloomer", "Cob", "Farmhouse"]), ("The Frosties mascot who says they're 'Grrreat!'", "Tony the Tiger", ["Coco the Monkey", "Cornelius the Rooster", "Sugar Bear"]),
 ("Ang Lee's 2000 martial arts film", "Crouching Tiger, Hidden Dragon", ["Hero", "House of Flying Daggers", "Kung Fu Hustle"]), ("Judith Kerr's picture book about an unexpected visitor", "The Tiger Who Came to Tea", ["Mog the Forgetful Cat", "When Hitler Stole Pink Rabbit", "The Gruffalo"]),
 ("Hull City's nickname", "The Tigers", ["The Blades", "The Owls", "The Terriers"]), ("Leicester's rugby union club", "Leicester Tigers", ["Northampton Saints", "Bath", "Gloucester"]),
 ("Germany's feared heavy tank of the Second World War", "Tiger", ["Panther", "Sherman", "Leopard"]), ("The striped shark that will eat almost anything", "Tiger shark", ["Great white", "Hammerhead", "Bull shark"]),
 ("William Blake's poem: 'burning bright, in the forests of the night'", "The Tyger", ["The Lamb", "Jerusalem", "London"]), ("The horse that won the Grand National in 2018 and 2019", "Tiger Roll", ["Red Rum", "Many Clouds", "Minella Times"]),
 ("The ointment from Asia sold in a little jar", "Tiger Balm", ["Vicks VapoRub", "Deep Heat", "Olbas Oil"]), ("Winnie-the-Pooh's bouncy friend", "Tigger", ["Eeyore", "Roo", "Piglet"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-93.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
