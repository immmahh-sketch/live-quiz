# Bank session 10 Oct 2026: 3 more general races -> bank/race-140.json (police words, TV words, newspaper words). 20 rows each, target 10; wrong options are
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

race("what's this police word?", "Everyday life", "medium", ["police", "crime", "words"], [
 ("Slang for a police officer, named after Sir Robert Peel", "Bobby", ["Screw", "Squaddie", "Traffic warden"]),
 ("The short wooden club an old-fashioned bobby carried", "Truncheon", ["Taser", "Cordon", "Bodycam"]),
 ("Locked round a suspect's wrists", "Handcuffs", ["Tag", "Cordon", "Bodycam"]),
 ("Being held at the police station", "Custody", ["Probation", "Stop and search", "Duty solicitor"]),
 ("'You do not have to say anything, but it may harm your defence...'", "Caution", ["Kettle", "Stop and search", "Duty solicitor"]),
 ("The ID a plain-clothes officer flashes to prove who they are", "Warrant card", ["Bodycam", "Tag", "Hi-vis"]),
 ("Old nickname for a small blue-and-white police car", "Panda car", ["Black Maria", "Jam sandwich", "Hi-vis"]),
 ("The patch a constable patrols on foot", "Beat", ["Cordon", "Kettle", "Tag"]),
 ("The plain-clothes detectives' department", "CID", ["Interpol", "Scotland Yard", "Traffic division"]),
 ("The officer behind the front counter at the station", "Desk sergeant", ["Duty solicitor", "Traffic warden", "Screw"]),
 ("A row of people for a witness to pick out the suspect", "Identity parade", ["Stop and search", "Kettle", "Cordon"]),
 ("The photo taken of a suspect after an arrest", "Mugshot", ["Bodycam", "Speed camera", "Hi-vis"]),
 ("Secretly watching a place for hours, waiting for something to happen", "Stake-out", ["Kettle", "Stop and search", "Cordon"]),
 ("Slang for an informer who tells the police", "Grass", ["Screw", "Rozzer", "Squaddie"]),
 ("The wailing noise as a police car rushes to a 999 call", "Siren", ["Blue light", "Hi-vis", "Speed camera"]),
 ("The Met's armed-robbery unit, nicknamed 'the Sweeney'", "Flying Squad", ["Interpol", "Traffic division", "Special Branch"]),
 ("A volunteer officer with the same powers as a regular one", "Special constable", ["Traffic warden", "Screw", "Duty solicitor"]),
 ("You blow into it to check you haven't been drinking", "Breathalyser", ["Speed camera", "Tag", "Bodycam"]),
 ("Dusted for at a crime scene and matched to a suspect", "Fingerprints", ["Hi-vis", "Tag", "Cordon"]),
 ("A specially trained animal that searches bags for drugs", "Sniffer dog", ["Police horse", "Guide dog", "Mascot"])])

race("what's this TV word?", "TV", "easy", ["television", "words"], [
 ("An episode that ends on a knife-edge, leaving you desperate for the next", "Cliffhanger", ["Montage", "Outtake", "Voiceover"]),
 ("A new show built around a character from an older one", "Spin-off", ["Simulcast", "Syndication", "Montage"]),
 ("The trial first episode made to test a new series", "Pilot", ["Promo", "Trailer", "Outtake"]),
 ("An old episode shown again", "Repeat", ["Simulcast", "Outtake", "Promo"]),
 ("A whole series released together to watch in one go", "Box set", ["Simulcast", "Syndication", "Promo"]),
 ("Recorded giggles added to a sitcom", "Laughter track", ["Voiceover", "Sting", "Ident"]),
 ("9pm, after which more grown-up programmes may be shown", "Watershed", ["Primetime", "Daytime", "Ident"]),
 ("The pause for commercials on ITV", "Ad break", ["Ident", "Sting", "Montage"]),
 ("A one-off festive episode, often watched after the turkey", "Christmas special", ["Simulcast", "Outtake", "Montage"]),
 ("The very last episode of a series", "Finale", ["Promo", "Outtake", "Teaser"]),
 ("A story set before the original, like 'House of the Dragon'", "Prequel", ["Sequel", "Crossover", "Simulcast"]),
 ("A new version of an old show or film", "Remake", ["Sequel", "Crossover", "Montage"]),
 ("A brief surprise appearance by a famous face", "Cameo", ["Voiceover", "Outtake", "Ident"]),
 ("Watching episode after episode in one sitting", "Binge-watch", ["Simulcast", "Channel-hop", "Syndication"]),
 ("The person in overall charge of making a TV series", "Showrunner", ["Continuity announcer", "Floor manager", "Clapper loader"]),
 ("The names and theme tune at the start of a show", "Opening credits", ["Ident", "Sting", "Outtake"]),
 ("A comedy series built round the same characters and setting", "Sitcom", ["Simulcast", "Montage", "Docudrama"]),
 ("A never-ending drama about one street or village, on several nights a week", "Soap opera", ["Docudrama", "Mockumentary", "Miniseries"]),
 ("Watching a programme later on iPlayer or ITVX", "Catch-up", ["Simulcast", "Syndication", "Ident"]),
 ("The picture of a girl and a clown shown when nothing else was on", "Test card", ["Ident", "Sting", "Autocue"])])

race("what's this newspaper word?", "Everyday life", "medium", ["newspapers", "journalism", "words"], [
 ("A smaller-format paper known for punchy headlines and gossip", "Tabloid", ["Masthead", "Classifieds", "Advertorial"]),
 ("A big-format 'serious' newspaper", "Broadsheet", ["Masthead", "Freesheet", "Classifieds"]),
 ("The boss who decides what goes in the paper", "Editor", ["Stringer", "Proofreader", "Copy boy"]),
 ("Writes a regular opinion piece under their own name", "Columnist", ["Stringer", "Proofreader", "Copy boy"]),
 ("A big story one paper gets before all the others", "Scoop", ["Puff piece", "Advertorial", "Embargo"]),
 ("Where the biggest story of the day goes", "Front page", ["Back page", "Classifieds", "Centre spread"]),
 ("A write-up of someone's life after they've died", "Obituary", ["Puff piece", "Advertorial", "Classifieds"]),
 ("Answers readers' letters about their problems", "Agony aunt", ["Stringer", "Proofreader", "Copy boy"]),
 ("A grid of clues to solve, cryptic or quick", "Crossword", ["Classifieds", "Masthead", "Advertorial"]),
 ("What the stars say for your sign this week", "Horoscope", ["Classifieds", "Masthead", "Advertorial"]),
 ("Photographers who chase celebrities for pictures", "Paparazzi", ["Stringers", "Proofreaders", "Copy boys"]),
 ("The line naming who wrote a story", "Byline", ["Masthead", "Dateline", "Lede"]),
 ("The paper's own opinion on the news of the day", "Editorial", ["Advertorial", "Puff piece", "Classifieds"]),
 ("An extra magazine tucked inside at the weekend", "Supplement", ["Classifieds", "Masthead", "Centre spread"]),
 ("How many copies a paper sells", "Circulation", ["Embargo", "Masthead", "Dateline"]),
 ("Secret information passed to a journalist", "Leak", ["Embargo", "Proof", "Puff piece"]),
 ("The big bold words at the top of a story", "Headline", ["Dateline", "Lede", "Masthead"]),
 ("A statement a company sends out, hoping to get coverage", "Press release", ["Embargo", "Puff piece", "Advertorial"]),
 ("A journalist covering one subject or country, like politics or Washington", "Correspondent", ["Proofreader", "Copy boy", "Typesetter"]),
 ("What an editor does to a story they decide not to run", "Spike", ["Embargo", "Proof", "Splash"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-140.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
