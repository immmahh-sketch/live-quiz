# Bank session 19 Oct 2026: 8 more Answer Smash questions written by hand -> bank/smash-3.json. Picture answers are faces stocked as
# Picture Reveals earlier today (so their Wikipedia photos are known to be good); the clue answer starts with the last letters of the
# name (at least two letters overlap, the server's rule). Checked against every picture and clue answer in the live bank; clue
# answers already used (Tissue, Tongue, Sonic, Songbird, Mansion, Terrier, Sonogram, Terminal) were swapped for fresh ones. Helen McCrory + Orchestra was dropped: the names have to overlap
# letter for letter at the join (McCRORY ends 'ory', Orchestra starts 'orc'), which they don't.
import json, os, re
OUT = []
def sm(picture, clue_answer, text, diff="medium", cat="Wordplay"):
    name = re.sub(r' \(.*\)$', '', picture)
    la = re.sub(r'[^a-z0-9]', '', name.lower()); lb = re.sub(r'[^a-z0-9]', '', clue_answer.lower())
    n = next((k for k in range(min(len(la), len(lb)) - 1, 0, -1) if la[-k:] == lb[:k]), 0)
    assert n >= 2, (picture, clue_answer)
    OUT.append({"type": "smash", "text": text, "picture": picture, "pictureAnswer": name, "clueAnswer": clue_answer, "category": cat, "tags": ["Answer Smash"], "difficulty": diff})

sm("Mark Gatiss", "Issue", "A magazine's weekly edition, or a problem")
sm("James Norton (actor)", "Tonight", "This evening")
sm("Ruth Wilson", "Songwriter", "Someone who composes the words and tunes of hits")
sm("Richard Madden", "Denim", "Blue jeans cloth", "easy")
sm("Amanda Redman", "Manager", "Someone who runs a team or a football club", "easy")
sm("Samuel West", "Estate", "A large country property", "easy")
sm("Jim Carter (actor)", "Terrific", "Really great, or really scary")
sm("Siobhan Finneran", "Ranger", "Park warden, or the Lone one")

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'smash-3.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'smash questions written')

# After import: Ruth Wilson and Jim Carter had no picture the Answer Smash importer would accept, and James Norton was skipped as a
# repeat, so 5 of the 8 are live (Gatiss, Madden, Redman, West, Finneran).
