# Bank session 11 Oct 2026: 3 more general races -> bank/race-169.json (American football, gymnastics and barber's words). 20 rows each, target 10; wrong options are
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

race("what's this American football word?", "Sport", "medium", ["American football", "NFL", "words"], [
 ("Carrying the ball into the end zone for six points", "Touchdown", ["Try", "Home run", "Slam dunk"]),
 ("The area at each end where you score", "End zone", ["Penalty area", "In-goal", "Crease"]),
 ("The player who throws the passes", "Quarterback", ["Fly-half", "Point guard", "Pitcher"]),
 ("The NFL's championship game in February", "Super Bowl", ["World Series", "Stanley Cup", "Rose Bowl"]),
 ("Kicking the ball between the posts for three points", "Field goal", ["Drop goal", "Penalty", "Conversion"]),
 ("The team gathering to call the next play", "Huddle", ["Scrum", "Ruck", "Maul"]),
 ("Tackling the quarterback before he can throw", "Sack", ["Bag", "Bin", "Bundle"]),
 ("Dropping the ball while carrying it", "Fumble", ["Knock-on", "Butterfingers", "Juggle"]),
 ("Catching a pass meant for the other team", "Interception", ["Intervention", "Intersection", "Interruption"]),
 ("The nickname for the sport, from the lines on the field", "Gridiron", ["Griddle", "Gridlock", "Grid reference"]),
 ("A desperate long pass in the dying seconds", "Hail Mary", ["Ave Maria", "Our Father", "Amen"]),
 ("Pom-pom-waving dancers on the sidelines", "Cheerleaders", ["Ball boys", "Mascots", "Stewards"]),
 ("The league, by its initials", "NFL", ["NBA", "NHL", "MLB"]),
 ("The quarterback with a record seven Super Bowl wins", "Tom Brady", ["Peyton Manning", "Patrick Mahomes", "Joe Montana"]),
 ("The London stadium built with its own NFL pitch underneath", "Tottenham Hotspur Stadium", ["Emirates Stadium", "Stamford Bridge", "London Stadium"]),
 ("Kicking the ball away downfield on fourth down", "Punt", ["Bunt", "Pass", "Volley"]),
 ("The mid-game Super Bowl concert", "Halftime show", ["Interval act", "Tea break", "Seventh-inning stretch"]),
 ("The unit of distance on the field, 100 of them long", "Yard", ["Metre", "Foot", "Pace"]),
 ("Slang for the ball", "Pigskin", ["Cowhide", "Sheepskin", "Oxblood"]),
 ("What players wear over their faces", "Face mask", ["Visor", "Goggles", "Gumshield"])])

race("what's this gymnastics word?", "Sport", "medium", ["gymnastics", "Olympics", "words"], [
 ("The ten-centimetre-wide bar women balance on", "Beam", ["Plank", "Rail", "Joist"]),
 ("The leather apparatus with two handles that men swing over", "Pommel horse", ["Rocking horse", "Clothes horse", "Sawhorse"]),
 ("Sprinting, springing off a board and flipping over the table", "Vault", ["Hurdle", "Long jump", "Hop"]),
 ("Two hoops hanging from straps, for the strongest men", "Rings", ["Hoops", "Bangles", "Loops"]),
 ("The tumbling routine on a springy square mat", "Floor", ["Carpet", "Trampoline", "Stage"]),
 ("The women's apparatus with two bars at different heights", "Uneven bars", ["High bar", "Pull-up bar", "Wine bar"]),
 ("The men's apparatus with two bars side by side", "Parallel bars", ["High bar", "Crossbar", "Handlebars"]),
 ("Balancing upside down on your hands", "Handstand", ["Headstand", "Bandstand", "Grandstand"]),
 ("A sideways wheel, turning over hand to hand", "Cartwheel", ["Catherine wheel", "Waterwheel", "Big wheel"]),
 ("Flipping head over heels", "Somersault", ["Pirouette", "Plié", "Arabesque"]),
 ("Legs stretched flat in opposite directions", "Splits", ["Shards", "Halves", "Cracks"]),
 ("The American with the most world and Olympic medals of all", "Simone Biles", ["Olga Korbut", "Gabby Douglas", "Beth Tweddle"]),
 ("The first to score a perfect 10, in 1976", "Nadia Comăneci", ["Olga Korbut", "Beth Tweddle", "Mary Lou Retton"]),
 ("Britain's pommel horse Olympic champion in 2016 and 2021", "Max Whitlock", ["Louis Smith", "Nile Wilson", "Beth Tweddle"]),
 ("The stretchy one-piece suit", "Leotard", ["Tutu", "Kimono", "Sarong"]),
 ("The final move off the apparatus", "Dismount", ["Discount", "Dismantle", "Dislodge"]),
 ("Gymnastics with ribbons, hoops and clubs", "Rhythmic", ["Artistic", "Acrobatic", "Aerobic"]),
 ("The board you bounce off before the vault", "Springboard", ["Diving board", "Skateboard", "Surfboard"]),
 ("A gymnast's planned sequence of moves", "Routine", ["Rota", "Schedule", "Agenda"]),
 ("A run of flips and twists across the floor", "Tumble", ["Rumble", "Fumble", "Stumble"])])

race("what's this barber's word?", "Everyday life", "easy", ["barbers", "hair", "words"], [
 ("The buzzing electric tool for short hair", "Clippers", ["Pliers", "Tweezers", "Secateurs"]),
 ("The classic barber's cut", "Short back and sides", ["Mullet", "Mohican", "Beehive"]),
 ("Hair blended from very short to longer", "Fade", ["Fringe", "Quiff", "Perm"]),
 ("The long folding blade for a wet shave", "Cut-throat razor", ["Safety razor", "Penknife", "Scalpel"]),
 ("The soapy froth brushed on before a shave", "Lather", ["Mousse", "Gel", "Wax"]),
 ("The red-and-white striped sign outside the shop", "Barber's pole", ["Maypole", "Totem pole", "Barge pole"]),
 ("The shortest clipper guard setting", "Number one", ["Number ten", "Grade A", "Size zero"]),
 ("Hair growing down in front of the ears", "Sideburns", ["Eyebrows", "Earlobes", "Temples"]),
 ("Hair on the upper lip", "Moustache", ["Stubble", "Monobrow", "Fringe"]),
 ("A small beard on the chin only", "Goatee", ["Stubble", "Monobrow", "Fringe"]),
 ("A toothed strip for neatening hair", "Comb", ["Fork", "Rake", "Saw"]),
 ("The line where hair is combed in different directions", "Parting", ["Fringe", "Crown", "Nape"]),
 ("A steaming cloth laid on the face before a shave", "Hot towel", ["Tea towel", "Beach towel", "Bath towel"]),
 ("The stinging scented splash after shaving", "Aftershave", ["Mouthwash", "Conditioner", "Moisturiser"]),
 ("The hair cream: 'a little dab'll do ya'", "Brylcreem", ["Vaseline", "Nivea", "Germolene"]),
 ("The demon barber of Fleet Street", "Sweeney Todd", ["Jack the Ripper", "Dick Turpin", "Mack the Knife"]),
 ("A square-topped cut standing straight up", "Flat-top", ["Bob", "Bowl cut", "Pixie cut"]),
 ("What's swept off the floor afterwards", "Clippings", ["Shavings", "Crumbs", "Sawdust"]),
 ("Shaved short at the sides with longer hair on top", "Undercut", ["Bob", "Bowl cut", "Pixie cut"]),
 ("The trade named from the Latin 'barba', meaning beard", "Barber", ["Butcher", "Baker", "Barrister"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-169.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
