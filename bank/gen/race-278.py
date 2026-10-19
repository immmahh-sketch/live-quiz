# Bank session 19 Oct 2026: 2 races -> bank/race-278.json (Bergerac; Lovejoy).
# Neither show had a race in the live bank. Checked against every live race with lqsql/audit/race-overlap-live.py before importing.
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

race("Bergerac - name it", "Television", "medium", ["Bergerac", "detectives", "BBC"], [
 ("The actor who played him", "John Nettles", ["John Thaw", "Dennis Waterman", "Martin Shaw"]),
 ("Bergerac's first name", "Jim", ["Tom", "Frank", "Mike"]),
 ("The island", "Jersey", ["Guernsey", "Isle of Man", "Isle of Wight"]),
 ("Its capital, where he worked", "St Helier", ["St Peter Port", "Douglas", "Newport"]),
 ("The police unit he worked for", "Bureau des Étrangers", ["Special Branch", "CID", "Flying Squad"]),
 ("What that unit dealt with", "Crimes involving visitors to the island", ["Only drug smuggling", "Only tax fraud", "Traffic offences"]),
 ("His classic car", "Triumph Roadster", ["Jaguar Mark 2", "MG Midget", "Austin-Healey"]),
 ("What he was recovering from", "Alcoholism", ["Gambling", "A bad back", "Debt"]),
 ("His ex-father-in-law", "Charlie Hungerford", ["Charlie Endell", "Arthur Daley", "Boycie"]),
 ("What Charlie was", "A wealthy wheeler-dealer", ["A judge", "A vicar", "A police chief"]),
 ("The actor who played Charlie", "Terence Alexander", ["Terence Stamp", "Terry-Thomas", "Leslie Phillips"]),
 ("The glamorous jewel thief", "Philippa Vale", ["Maddie Hayes", "Purdey", "Emma Peel"]),
 ("The actress who played her", "Liza Goddard", ["Felicity Kendal", "Joanna Lumley", "Diana Rigg"]),
 ("The channel", "BBC One", ["ITV", "BBC Two", "Channel 4"]),
 ("The year it began", "1981", ["1976", "1985", "1989"]),
 ("The year it ended", "1991", ["1987", "1994", "1997"]),
 ("Who created it", "Robert Banks Stewart", ["Lynda La Plante", "Anthony Horowitz", "Jimmy McGovern"]),
 ("The theme tune composer", "George Fenton", ["Ron Grainer", "Barrington Pheloung", "Ed Welch"]),
 ("The lead actor's later Midsomer Murders role", "Tom Barnaby", ["Ben Jones", "Jack Frost", "George Gently"]),
 ("The actor who played Bergerac in the 2025 reboot", "Damien Molony", ["Aidan Turner", "Richard Armitage", "Tom Hughes"])])

race("Lovejoy - name it", "Television", "medium", ["Lovejoy", "TV drama", "BBC"], [
 ("The actor who played him", "Ian McShane", ["Ian Ogilvy", "Ian Lavender", "Ian Hogg"]),
 ("His trade", "Antiques dealer", ["Car dealer", "Art forger", "Pawnbroker"]),
 ("His gift for spotting the real thing", "Being a divvy", ["Being a bloodhound", "Being a spotter", "Being a sniffer"]),
 ("The region it's set in", "East Anglia", ["The Cotswolds", "The Lake District", "Cornwall"]),
 ("The county where most of it was filmed", "Suffolk", ["Kent", "Devon", "Dorset"]),
 ("The author of the novels", "Jonathan Gash", ["Colin Dexter", "Peter Lovesey", "Reginald Hill"]),
 ("That author's real job", "Doctor", ["Lawyer", "Teacher", "Vicar"]),
 ("His old, hard-drinking sidekick", "Tinker", ["Boycie", "Trigger", "Rodney"]),
 ("The actor who played him", "Dudley Sutton", ["Dudley Moore", "Roger Lloyd-Pack", "John Challis"]),
 ("His young sidekick", "Eric Catchpole", ["Mickey Pearce", "Denzil", "Gary Sparrow"]),
 ("The aristocrat he was sweet on", "Lady Jane Felsham", ["Lady Penelope", "Lady Sybil", "Lady Marjorie"]),
 ("The actress who played her", "Phyllis Logan", ["Penelope Keith", "Felicity Kendal", "Joanna Lumley"]),
 ("The actress who played auctioneer Charlotte Cavendish", "Caroline Langrishe", ["Caroline Quentin", "Caroline Aherne", "Caroline Catz"]),
 ("His car", "A Morris Minor", ["A Reliant Robin", "A Ford Capri", "A Land Rover"]),
 ("The car's name", "Miriam", ["Doris", "Betsy", "Rosie"]),
 ("What he often did that most dramas don't", "Talk straight to the camera", ["Sing", "Narrate in rhyme", "Break into dance"]),
 ("The channel", "BBC One", ["ITV", "BBC Two", "Channel 4"]),
 ("The year it first aired", "1986", ["1979", "1983", "1990"]),
 ("The year it ended", "1994", ["1989", "1997", "2001"]),
 ("The star's foul-mouthed role in Deadwood", "Al Swearengen", ["Wild Bill Hickok", "Seth Bullock", "Calamity Jane"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-278.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
