# Bank session 11 Oct 2026: 3 more general races -> bank/race-170.json (ice hockey, Strictly and coronation words). 20 rows each, target 10; wrong options are
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

race("what's this ice hockey word?", "Sport", "medium", ["ice hockey", "NHL", "words"], [
 ("The hard rubber disc", "Puck", ["Quoit", "Counter", "Coaster"]),
 ("The ice surface", "Rink", ["Pitch", "Court", "Green"]),
 ("Dropping the puck between two players to restart", "Face-off", ["Bully-off", "Tip-off", "Jump ball"]),
 ("Playing with an extra skater while an opponent sits out", "Power play", ["Power cut", "Power nap", "Powerhouse"]),
 ("The nickname for the penalty box", "Sin bin", ["Dugout", "Bullpen", "Pavilion"]),
 ("The machine that resurfaces the ice", "Zamboni", ["Lamborghini", "Zeppelin", "Zambezi"]),
 ("Three goals by one player, so fans throw their caps on the ice", "Hat-trick", ["Hole in one", "Maximum", "Triple crown"]),
 ("Shooting the puck the length of the ice, stopping play", "Icing", ["Frosting", "Glazing", "Freezing"]),
 ("Barging an opponent into the boards", "Body check", ["Spot check", "Rain check", "Double check"]),
 ("The walls around the rink", "Boards", ["Ropes", "Nets", "Cushions"]),
 ("The padded player guarding the net", "Goaltender", ["Wicketkeeper", "Catcher", "Sweeper"]),
 ("The NHL's famous trophy", "Stanley Cup", ["Ryder Cup", "Davis Cup", "Webb Ellis Cup"]),
 ("North America's top league, by its initials", "NHL", ["NFL", "NBA", "MLB"]),
 ("'The Great One', the record goalscorer", "Wayne Gretzky", ["Bobby Orr", "Mario Lemieux", "Sidney Crosby"]),
 ("The country where the modern game was born", "Canada", ["USA", "Sweden", "Russia"]),
 ("Extra time played after a draw", "Overtime", ["Injury time", "Extra innings", "Super over"]),
 ("A wind-up shot hit as hard as possible", "Slapshot", ["Wrist shot", "Drop shot", "Lob"]),
 ("The tough guy whose job is to fight", "Enforcer", ["Bouncer", "Minder", "Prop"]),
 ("Each of the three 20-minute sections of a game", "Period", ["Quarter", "Half", "Innings"]),
 ("Footwear with blades", "Skates", ["Spikes", "Cleats", "Studs"])])

race("what's this Strictly word?", "TV", "easy", ["Strictly Come Dancing", "dance", "TV"], [
 ("The trophy the winners lift", "Glitterball", ["Golden Boot", "Silver Plate", "Crystal Maze"]),
 ("The bottom two dance again to stay in", "Dance-off", ["Face-off", "Run-off", "Bake-off"]),
 ("The top score on a judge's paddle", "Ten", ["Five", "Twelve", "Twenty"]),
 ("Craig Revel Horwood's drawn-out word of praise", "Fab-u-lous", ["Marvellous", "Spectacular", "Gorgeous"]),
 ("The score Len Goodman loved to shout", "Seven", ["Eight", "Nine", "Six"]),
 ("Bruce Forsyth's sign-off", "Keep dancing", ["Keep smiling", "Keep calm", "Keep going"]),
 ("The seaside town whose Tower Ballroom hosts a special show", "Blackpool", ["Brighton", "Scarborough", "Bournemouth"]),
 ("The dramatic dance about a bullfighter and his cape", "Paso doble", ["Tango", "Rumba", "Samba"]),
 ("The 1920s flapper dance with swivelling heels", "Charleston", ["Jive", "Quickstep", "Twist"]),
 ("Sparkly discs sewn all over the costumes", "Sequins", ["Buttons", "Rivets", "Sprinkles"]),
 ("The bronzed fake colour every celeb gets", "Spray tan", ["Sunburn", "Tan line", "Freckles"]),
 ("The professional dancer partnering a celebrity", "Pro", ["Rookie", "Amateur", "Stand-in"]),
 ("The week where pairs pick any style they like", "Couple's choice", ["Wild card", "Lucky dip", "Free kick"]),
 ("The host who started in 2004 alongside Bruce Forsyth", "Tess Daly", ["Claudia Winkleman", "Zoe Ball", "Holly Willoughby"]),
 ("The weekday spin-off show on BBC Two", "It Takes Two", ["Strictly Kids", "Dancing on Ice", "Step Up"]),
 ("Head judge from 2017, the 'Queen of Latin'", "Shirley Ballas", ["Arlene Phillips", "Darcey Bussell", "Motsi Mabuse"]),
 ("The waltz, foxtrot and quickstep family of dances", "Ballroom", ["Latin", "Street", "Contemporary"]),
 ("The final's no-rules routine, full of lifts", "Showdance", ["Showboat", "Showtime", "Showreel"]),
 ("The ranking after the judges' scores", "Leaderboard", ["Dashboard", "Clipboard", "Billboard"]),
 ("The first deaf contestant, who won in 2021", "Rose Ayling-Ellis", ["Giovanni Pernice", "Joe McFadden", "Bill Bailey"])])

race("what's this coronation word?", "The Royal Family", "medium", ["coronations", "royals", "words"], [
 ("Where coronations take place", "Westminster Abbey", ["St Paul's Cathedral", "Windsor Castle", "Buckingham Palace"]),
 ("Places the crown on the monarch's head", "Archbishop of Canterbury", ["Archbishop of York", "Lord Chancellor", "Dean of Westminster"]),
 ("The solid-gold crown used at the moment of crowning", "St Edward's Crown", ["Imperial State Crown", "Tiara", "Coronet"]),
 ("The 700-year-old wooden throne", "Coronation Chair", ["Cathedra", "Sedan chair", "Woolsack"]),
 ("The Scottish stone that sits beneath that chair", "Stone of Scone", ["Blarney Stone", "Rosetta Stone", "Bluestone"]),
 ("The sacred moment with holy oil, hidden behind a screen", "Anointing", ["Knighting", "Christening", "Unveiling"]),
 ("A golden globe topped with a cross", "Orb", ["Mace", "Chalice", "Thurible"]),
 ("The rod held in the right hand, set with the Cullinan diamond", "Sceptre", ["Mace", "Crozier", "Wand"]),
 ("The eagle-shaped flask holding the holy oil", "Ampulla", ["Amphora", "Decanter", "Goblet"]),
 ("The royal treasures kept at the Tower of London", "Crown Jewels", ["Royal Collection", "Family silver", "Treasure trove"]),
 ("The Yeoman Warders who guard them", "Beefeaters", ["Grenadiers", "Gurkhas", "Gamekeepers"]),
 ("The anthem sung at the end", "God Save the King", ["Land of Hope and Glory", "Jerusalem", "Rule, Britannia!"]),
 ("The Handel anthem sung at every coronation since 1727", "Zadok the Priest", ["Messiah", "Water Music", "Ode to Joy"]),
 ("The gilded carriage used since 1762", "Gold State Coach", ["Diamond Jubilee Coach", "Cinderella's coach", "Stagecoach"]),
 ("Where the royals wave from at Buckingham Palace", "Balcony", ["Rooftop", "Bandstand", "Gatehouse"]),
 ("RAF planes roaring over the Mall", "Flypast", ["Fly-tipping", "Flyover", "Flypaper"]),
 ("The year Elizabeth II was crowned", "1953", ["1952", "1947", "1960"]),
 ("When Charles III was crowned", "May 2023", ["June 2023", "September 2022", "April 2024"]),
 ("The white fur with black tail-spots on the robes", "Ermine", ["Mink", "Sable", "Chinchilla"]),
 ("The pledge of loyalty spoken by Prince William", "Homage", ["Toast", "Ovation", "Salute"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-170.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
