# Bank session 12 Oct 2026: 1 more general race -> bank/race-220.json (Brownies and Guides words). Checked against the Scouting
# and camping races: badge, promise, Guides and Brownies left out as answers, as the Scouting race has them.
# 20 rows each, target 10; wrong options are the same kind of thing, never another row's right answer, and never also right for that row.
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

race("what's this Brownies and Guides word?", "Everyday life", "medium", ["Brownies", "Girl Guides", "words"], [
 ("The leader of a Brownie pack", "Brown Owl", ["Akela", "Barn Owl", "Wise Owl"]),
 ("Brown Owl's assistant", "Tawny Owl", ["Little Owl", "Snowy Owl", "Eagle Owl"]),
 ("What Brownies traditionally gather round at the start of a meeting", "Toadstool", ["Totem pole", "Maypole", "Tree stump"]),
 ("A small group of Brownies within the pack", "Six", ["Patrol", "Den", "Lair"]),
 ("The Brownie in charge of a small group", "Sixer", ["Captain", "Monitor", "Prefect"]),
 ("One of the traditional Brownie groups, alongside Pixies and Elves", "Gnomes", ["Trolls", "Ogres", "Giants"]),
 ("The youngest section, for girls aged 4 to 7", "Rainbows", ["Beavers", "Squirrels", "Daisies"]),
 ("The oldest section, for 14 to 18-year-olds", "Rangers", ["Explorers", "Venturers", "Pioneers"]),
 ("The Brownie motto", "Lend a Hand", ["Be Prepared", "Do Your Best", "Look Wide"]),
 ("The three-leaf symbol of Guiding", "Trefoil", ["Fleur-de-lis", "Shamrock", "Thistle"]),
 ("The first World Chief Guide, wife of the Scouts' founder", "Olave Baden-Powell", ["Agnes Baden-Powell", "Lady Bracknell", "Florence Nightingale"]),
 ("22 February, when Guides everywhere think of each other", "Thinking Day", ["Founder's Day", "Remembrance Day", "Pancake Day"]),
 ("The Brownies' circle for talking and making plans", "Pow-wow", ["Huddle", "Natter", "Conflab"]),
 ("The band worn across the body to show off badges", "Sash", ["Lanyard", "Bandolier", "Garter"]),
 ("A Brownie trip away, sleeping indoors", "Pack holiday", ["Jamboree", "Expedition", "Field trip"]),
 ("What an adult Guide leader is called", "Guider", ["Scoutmaster", "Guidemaster", "Captain"]),
 ("The year Guiding began", "1910", ["1907", "1920", "1899"]),
 ("The 1909 rally where girls turned up demanding to be Scouts", "Crystal Palace", ["Hyde Park", "Brownsea Island", "Wembley"]),
 ("What the UK organisation has been called since 2002", "Girlguiding", ["The Guide Association", "Girl Scouts", "The Brownie Club"]),
 ("What American Girl Scouts famously sell", "Cookies", ["Lemonade", "Candles", "Raffle tickets"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-220.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
