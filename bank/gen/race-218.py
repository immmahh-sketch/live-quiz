# Bank session 12 Oct 2026: 1 more general race -> bank/race-218.json (Cold War words). Checked against the spy, space, 1960s,
# 1980s, army, election and home front races: no right answer repeats theirs.
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

race("what's this Cold War word?", "History", "medium", ["Cold War", "20th century", "words"], [
 ("Churchill's name for the line dividing Europe", "Iron Curtain", ["Bamboo Curtain", "Maginot Line", "Velvet Curtain"]),
 ("The barrier torn down in November 1989", "Berlin Wall", ["Great Wall", "Hadrian's Wall", "Atlantic Wall"]),
 ("The famous crossing point between East and West Berlin", "Checkpoint Charlie", ["Checkpoint Alpha", "Checkpoint Bravo", "Gate 19"]),
 ("The thirteen days in October 1962 when the world nearly went to nuclear war", "Cuban Missile Crisis", ["Suez Crisis", "Korean War", "Six-Day War"]),
 ("The failed 1961 invasion of Cuba, backed by the CIA", "Bay of Pigs", ["Gulf of Tonkin", "Pearl Harbor", "Port Stanley"]),
 ("Flying food and coal into West Berlin during the 1948 blockade", "Berlin Airlift", ["Dunkirk evacuation", "Kindertransport", "The Hump"]),
 ("The build-up of ever more nuclear weapons", "Arms race", ["Rat race", "Relay race", "Boat race"]),
 ("The rivalry to be first to the Moon", "Space race", ["Rat race", "Relay race", "Star Wars"]),
 ("The Western military alliance formed in 1949", "NATO", ["SEATO", "OPEC", "UNESCO"]),
 ("The Soviet bloc's military alliance", "Warsaw Pact", ["Molotov Pact", "Comecon", "Treaty of Rome"]),
 ("The easing of tension between the superpowers in the 1970s", "Détente", ["Entente", "Appeasement", "Blockade"]),
 ("Gorbachev's policy of openness", "Glasnost", ["Politburo", "Pravda", "Gulag"]),
 ("Gorbachev's policy of restructuring", "Perestroika", ["Politburo", "Pravda", "Gulag"]),
 ("America's 1950s hunt for communists", "McCarthyism", ["Reaganomics", "Watergate", "Thatcherism"]),
 ("The idea that if one country fell to communism, its neighbours would follow", "Domino theory", ["Chaos theory", "Game theory", "Big Bang theory"]),
 ("The 'MAD' idea that kept both sides from firing first", "Mutually assured destruction", ["Shock and awe", "Scorched earth", "Brinkmanship"]),
 ("How long Britons were told they'd have before a nuclear strike", "Four-minute warning", ["Two-minute silence", "Ten-second countdown", "One-hour notice"]),
 ("An underground bunker built to survive the bomb", "Fallout shelter", ["Anderson shelter", "Bus shelter", "Tax shelter"]),
 ("The direct line set up between the Kremlin and the White House in 1963", "Hotline", ["Landline", "Party line", "Helpline"]),
 ("The Polish trade union led by Lech Wałęsa", "Solidarity", ["Unity", "Liberty", "Fraternity"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-218.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
