# Bank session 18 Oct 2026: 2 general races -> bank/race-226.json (Thunderbirds and Gerry Anderson, Blue Peter).
# Whose-autobiography and double-act races were drafted first but both already existed (memoirs, famous pairs).
# The "what's this X word?" shape is saturated (beekeeping, pottery, newspapers and canals all had races), so these use new shapes.
# Checked against every race in stock with lqsql/audit/race-overlap.py before importing.
# raceOk: 20 rows, 20 different right answers, no right answer among another row's options, no wrong option on 3+ rows.
import json, os
from collections import Counter
R = []
def race(title, cat, diff, tags, rows):
    rights = {r[1] for r in rows}
    assert len(rows) == 20, (title, len(rows))
    assert len(rights) == 20, (title, 'duplicate right answers')
    bad = [(q, w) for q, right, wrong in rows for w in wrong if w in rights]
    assert not bad, (title, 'recycled', bad)
    for q, right, wrong in rows:
        assert len(wrong) == 3 and len(set(wrong)) == 3 and right not in wrong, (title, q)
    over = [w for w, n in Counter(w for _, _, wrong in rows for w in wrong).items() if n > 2]
    assert not over, (title, 'wrong option on 3+ rows', over)
    R.append({"type": "race", "text": "The Race: " + title, "target": 10, "category": cat, "tags": tags, "difficulty": diff,
              "bank": [{"q": q, "right": right, "wrong": wrong} for q, right, wrong in rows]})

race("Thunderbirds and Gerry Anderson, name it", "Television", "medium", ["Thunderbirds", "Gerry Anderson", "puppets", "children's TV"], [
 ("The father who runs International Rescue", "Jeff Tracy", ["Jack Tracy", "Jim Tracy", "Jed Tracy"]),
 ("The son who flies Thunderbird 1", "Scott", ["Steve", "Stuart", "Simon"]),
 ("The son who flies the big green Thunderbird 2", "Virgil", ["Vernon", "Victor", "Vincent"]),
 ("The organisation the Tracys secretly run", "International Rescue", ["Global Rescue", "World Patrol", "Thunder Squad"]),
 ("Their secret Pacific base", "Tracy Island", ["Thunder Island", "Rescue Island", "Paradise Island"]),
 ("The London agent with the pink Rolls-Royce", "Lady Penelope", ["Lady Jane", "Lady Pamela", "Lady Victoria"]),
 ("Her chauffeur, a reformed safecracker", "Parker", ["Barker", "Jenkins", "Hudson"]),
 ("The number plate on her Rolls-Royce", "FAB 1", ["PEN 1", "LDY 1", "IR 1"]),
 ("The shy genius who designs all the machines", "Brains", ["Boffin", "Gizmo", "Professor"]),
 ("The master criminal who spies on them", "The Hood", ["The Mole", "The Mask", "The Shadow"]),
 ("Their word for 'message understood'", "FAB", ["Roger", "Wilco", "Ten-four"]),
 ("The Thunderbird that launches from under the swimming pool", "Thunderbird 1", ["Thunderbird 2", "Thunderbird 3", "Thunderbird 4"]),
 ("The name for the puppet technique the shows used", "Supermarionation", ["Animatronics", "Claymation", "Stop-motion"]),
 ("The man who created them all", "Gerry Anderson", ["Oliver Postgate", "Brian Cosgrove", "Ivor Wood"]),
 ("His underwater show, starring Troy Tempest", "Stingray", ["Seaview", "Sealab", "Aquanaut"]),
 ("The silent mermaid in that show", "Marina", ["Ariel", "Coral", "Pearl"]),
 ("The indestructible hero who fights the Mysterons", "Captain Scarlet", ["Captain Blue", "Captain Black", "Captain Ochre"]),
 ("The boy who could take on any expert's brain patterns", "Joe 90", ["Max 90", "Sam 2000", "Tom Thumb"]),
 ("Steve Zodiac's spaceship", "Fireball XL5", ["Starfire XL7", "Rocket XR1", "Comet X9"]),
 ("The 1980s show with Zelda and the Zeroids", "Terrahawks", ["Space Precinct", "UFO", "Space: 1999"])])

race("Blue Peter, name it", "Television", "medium", ["Blue Peter", "children's TV", "BBC", "nostalgia"], [
 ("The ship on the Blue Peter logo", "Galleon", ["Lifeboat", "Clipper", "Trawler"]),
 ("What viewers win for writing in or taking part", "Badge", ["Medal", "Rosette", "Certificate"]),
 ("The presenter who climbed Nelson's Column", "John Noakes", ["Peter Purves", "Simon Groom", "Mark Curry"]),
 ("The elephant who caused chaos in the studio in 1969", "Lulu", ["Jumbo", "Nellie", "Dumbo"]),
 ("John Noakes's border collie", "Shep", ["Rex", "Bruno", "Patch"]),
 ("The show's very first dog, in 1962", "Petra", ["Lassie", "Sandy", "Bess"]),
 ("The golden retriever of the 1980s and 90s", "Goldie", ["Honey", "Sandy", "Amber"]),
 ("The Siamese cat of the 1960s and 70s", "Jason", ["Jasper", "Jethro", "Jinx"]),
 ("The tortoise who lived on the show for over 20 years", "George", ["Tommy", "Toby", "Terence"]),
 ("The famous craft material, never called by its brand name", "Sticky-backed plastic", ["Sellotape", "Blu Tack", "Crepe paper"]),
 ("What the presenters say as they bring out a finished model", "Here's one I made earlier", ["Here's one we did yesterday", "Look what I've got", "Ta-da!"]),
 ("The gardener who designed the Blue Peter garden", "Percy Thrower", ["Alan Titchmarsh", "Geoff Hamilton", "Bill Sowerbutts"]),
 ("The theme tune, a sea shanty", "Barnacle Bill", ["Sailor's Hornpipe", "Drunken Sailor", "Rule Britannia"]),
 ("The year it began", "1958", ["1955", "1962", "1965"]),
 ("The channel it moved to in 2012", "CBBC", ["ITV", "BBC Two", "CITV"]),
 ("Where it moved to from London in 2011", "MediaCityUK", ["Television Centre", "Elstree", "Pebble Mill"]),
 ("What was buried in the garden in 1971 and dug up in 2000", "Time capsule", ["Treasure chest", "Statue", "Old badges"]),
 ("The presenter of 1962 to 1972 who later hosted Radio 4's PM", "Valerie Singleton", ["Anthea Turner", "Janet Ellis", "Sarah Greene"]),
 ("The longest-serving female presenter, 1997 to 2008", "Konnie Huq", ["Katy Hill", "Zoe Salmon", "Liz Barker"]),
 ("What a 'blue peter' flag means at sea", "A ship is about to sail", ["Man overboard", "A pilot is needed", "Quarantine"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-226.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
