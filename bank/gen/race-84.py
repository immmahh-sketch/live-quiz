# Bank session 10 Oct 2026: 2 more general races -> bank/race-84.json. 20 rows each, target 10; wrong options are
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

race("which famous 'Day'?", "General knowledge", "medium", ["days", "wordplay"], [
 ("The Allied landings in Normandy, 6 June 1944", "D-Day", ["VJ Day", "Dunkirk", "Pearl Harbor"]), ("8 May 1945, when the war in Europe ended", "VE Day", ["VJ Day", "Remembrance Day", "Liberation Day"]),
 ("Bill Murray's 1993 film about living the same day over and over", "Groundhog Day", ["Edge of Tomorrow", "Palm Springs", "Scrooged"]), ("Will Smith's 1996 alien invasion blockbuster", "Independence Day", ["Men in Black", "War of the Worlds", "Armageddon"]),
 ("Shrove Tuesday's other name", "Pancake Day", ["Ash Wednesday", "Plough Monday", "Maundy Thursday"]), ("America's holiday on the first Monday in September", "Labor Day", ["Memorial Day", "Thanksgiving", "Columbus Day"]),
 ("Mexico's festival of sugar skulls in early November", "Day of the Dead", ["All Saints' Day", "Cinco de Mayo", "Halloween"]), ("The Beatles' 1965 double A-side with 'We Can Work It Out'", "Day Tripper", ["Paperback Writer", "Ticket to Ride", "Help!"]),
 ("Frederick Forsyth's thriller about a plot to shoot de Gaulle", "The Day of the Jackal", ["The Odessa File", "The Dogs of War", "The Fourth Protocol"]), ("John Wyndham's novel about killer plants", "The Day of the Triffids", ["The Midwich Cuckoos", "The Kraken Wakes", "The Chrysalids"]),
 ("The last track on Sgt. Pepper", "A Day in the Life", ["Lucy in the Sky with Diamonds", "Penny Lane", "With a Little Help from My Friends"]), ("The 1970s American sitcom with the Fonz", "Happy Days", ["Laverne & Shirley", "Mork & Mindy", "The Wonder Years"]),
 ("Terminator 2's subtitle", "Judgment Day", ["Rise of the Machines", "Salvation", "Dark Fate"]), ("The Thursday of Royal Ascot, famous for its hats", "Ladies' Day", ["Derby Day", "Grand National Day", "Gentlemen's Day"]),
 ("Comic Relief's big night of telly", "Red Nose Day", ["Children in Need", "Sport Relief", "Telethon"]), ("The first of May, with maypoles and morris dancers", "May Day", ["Whit Monday", "Lammas Day", "Midsummer Day"]),
 ("The singer of 'Que Sera, Sera'", "Doris Day", ["Julie Andrews", "Debbie Reynolds", "Rosemary Clooney"]), ("The only man to win three Best Actor Oscars", "Daniel Day-Lewis", ["Jack Nicholson", "Sean Penn", "Tom Hanks"]),
 ("25 April, when Australians and New Zealanders remember Gallipoli", "Anzac Day", ["Australia Day", "Waitangi Day", "Remembrance Day"]), ("11 November 1918, when the First World War ended", "Armistice Day", ["VJ Day", "Victory Day", "Trafalgar Day"])])

race("which famous 'Paper'?", "General knowledge", "medium", ["paper", "wordplay"], [
 ("Something that looks threatening but has no real power", "Paper tiger", ["Damp squib", "Lame duck", "Straw man"]), ("A trail of documents that shows what happened", "Paper trail", ["Audit", "Smoking gun", "Breadcrumbs"]),
 ("What you paste onto walls to decorate them", "Wallpaper", ["Lining paper", "Plaster", "Emulsion"]), ("Rough paper for smoothing wood", "Sandpaper", ["Emery board", "Wire wool", "File"]),
 ("Thin see-through paper for copying a drawing", "Tracing paper", ["Carbon paper", "Blotting paper", "Cartridge paper"]), ("The paper you line a cake tin with", "Greaseproof paper", ["Kitchen roll", "Tin foil", "Cling film"]),
 ("The edible paper under macaroons and Vietnamese rolls", "Rice paper", ["Filo pastry", "Marzipan", "Sugar paste"]), ("Crinkly coloured paper for party streamers", "Crêpe paper", ["Tissue paper", "Cellophane", "Doilies"]),
 ("The government's firm plans for a new law", "White paper", ["Blue book", "Red box", "Hansard"]), ("The government's consultation document, before firm plans", "Green paper", ["Blue book", "Hansard", "Manifesto"]),
 ("The daily agenda of business in the House of Commons", "Order paper", ["Hansard", "Whip", "Red box"]), ("The 1970s band behind 'Billy Don't Be a Hero'", "Paper Lace", ["Mud", "Sweet", "Showaddywaddy"]),
 ("M.I.A.'s 2008 hit with the gunshots and cash-register sounds", "Paper Planes", ["Boyz", "Bad Girls", "Galang"]), ("John Green's novel about Q and Margo", "Paper Towns", ["The Fault in Our Stars", "Looking for Alaska", "Turtles All the Way Down"]),
 ("Marie Osmond's 1973 hit", "Paper Roses", ["Puppy Love", "Long Haired Lover from Liverpool", "Crazy Horses"]), ("A teenager's job delivering newspapers", "Paper round", ["Milk round", "Odd jobs", "Saturday job"]),
 ("The 1973 film about first-year students at Harvard Law School", "The Paper Chase", ["Legally Blonde", "A Few Good Men", "The Firm"]), ("Torn paper and glue moulded into shapes", "Papier-mâché", ["Decoupage", "Collage", "Quilling"]),
 ("A heavy ornament that stops papers blowing away", "Paperweight", ["Bookend", "Doorstop", "Paperclip"]), ("In the hand game, what wraps rock", "Paper", ["Scissors", "Stone", "Lizard"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-84.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
