# Bank session 12 Oct 2026: 1 more general race -> bank/race-221.json (curling words). Checked against the bowls, ice hockey,
# ice skating and Olympic sport races: end, rink, skip, lead and draw left out, as the bowls race has them.
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

race("what's this curling word?", "Sport", "medium", ["curling", "Winter Olympics", "Scotland", "words"], [
 ("The heavy polished rock slid down the ice", "Stone", ["Puck", "Bowl", "Disc"]),
 ("What players sweep the ice with", "Broom", ["Mop", "Rake", "Paddle"]),
 ("The target of rings at the far end", "House", ["Bullseye", "Pocket", "Goal"]),
 ("The very centre of the target", "Button", ["Jack", "Pin", "Spot"]),
 ("The line a stone has to cross to stay in play", "Hog line", ["Baseline", "Offside line", "Free-throw line"]),
 ("The foothold players push off from", "Hack", ["Block", "Tee", "Crease"]),
 ("The last stone of an end, a big advantage", "Hammer", ["Anvil", "Sledge", "Mallet"]),
 ("The strip of ice a game is played on", "Sheet", ["Lane", "Pitch", "Track"]),
 ("Tiny water droplets sprayed on the ice so the stones curl", "Pebble", ["Frost", "Glaze", "Gravel"]),
 ("Brushing the ice so a stone goes further and straighter", "Sweeping", ["Mopping", "Polishing", "Buffing"]),
 ("A shot that knocks an opponent's stone out of play", "Takeout", ["Strike", "Slam dunk", "Smash"]),
 ("A stone left short to protect another", "Guard", ["Shield", "Blocker", "Goalkeeper"]),
 ("The Scottish island whose granite makes the best stones", "Ailsa Craig", ["Arran", "Bass Rock", "Iona"]),
 ("An old word for a curling tournament", "Bonspiel", ["Bonfire", "Ceilidh", "Shindig"]),
 ("The skip who led Team GB's women to Olympic gold in 2002", "Rhona Martin", ["Lizzy Yarnold", "Amy Williams", "Jayne Torvill"]),
 ("The Scottish skip who won Olympic gold in 2022", "Eve Muirhead", ["Laura Muir", "Katarina Johnson-Thompson", "Lizzy Yarnold"]),
 ("The skip's deputy, who holds the broom when the skip throws", "Vice", ["Mate", "Deputy", "Sub"]),
 ("The rock curling stones are made from", "Granite", ["Marble", "Slate", "Basalt"]),
 ("Where curling began, on frozen lochs", "Scotland", ["Canada", "Norway", "Switzerland"]),
 ("What the skip shouts when they want hard sweeping", "Hurry hard", ["Go go go", "Push it", "Faster faster"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-221.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
