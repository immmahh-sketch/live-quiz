# Bank session 19 Oct 2026: 2 sitcom races -> bank/race-257.json (The Thick of It; Detectorists).
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

race("The Thick of It - name it", "Television", "medium", ["The Thick of It", "sitcoms", "BBC", "politics"], [
 ("The foul-mouthed spin doctor", "Malcolm Tucker", ["Malcolm Turner", "Malcolm Tyler", "Malcolm Taylor"]),
 ("The actor who played him", "Peter Capaldi", ["Peter Davison", "Peter Kay", "Peter Purves"]),
 ("The role that actor took next on the BBC", "The Doctor", ["Sherlock Holmes", "Inspector Morse", "Poldark"]),
 ("What the spin doctor is famous for", "Inventive swearing", ["Singing", "Sarcastic poems", "Long silences"]),
 ("His scary Scottish sidekick", "Jamie McDonald", ["Jamie Murray", "Jamie Oliver", "Jamie Carragher"]),
 ("The first minister", "Hugh Abbot", ["Hugh Dennis", "Hugh Bonneville", "Hugh Laurie"]),
 ("The actor who played him", "Chris Langham", ["Chris Barrie", "Chris Lowe", "Chris Morris"]),
 ("The minister who followed", "Nicola Murray", ["Nicola Walker", "Nicola Adams", "Nicola Roberts"]),
 ("The actress who played her", "Rebecca Front", ["Rebecca Adlington", "Rebecca Hall", "Rebecca Ferguson"]),
 ("The actor who played Ollie Reeder", "Chris Addison", ["Chris Evans", "Chris Packham", "Chris Martin"]),
 ("The department", "Social Affairs and Citizenship", ["Administrative Affairs", "Culture, Media and Sport", "Work and Pensions"]),
 ("The word it gave the dictionary", "Omnishambles", ["Shambolic", "Brexit", "Spin"]),
 ("The channel it began on", "BBC Four", ["BBC Three", "Channel 4", "Sky Atlantic"]),
 ("The year it began", "2005", ["2001", "2008", "2012"]),
 ("Its creator", "Armando Iannucci", ["Ricky Gervais", "Chris Morris", "Graham Linehan"]),
 ("The film spin-off", "In the Loop", ["Out of the Loop", "The Loop", "Spin City"]),
 ("The creator's American political comedy", "Veep", ["The West Wing", "House of Cards", "Succession"]),
 ("The character he co-created with Steve Coogan", "Alan Partridge", ["David Brent", "Gareth Keenan", "Mark Corrigan"]),
 ("His film about a Soviet leader", "The Death of Stalin", ["The Iron Lady", "Darkest Hour", "The Lives of Others"]),
 ("The spin doctor's job title", "Director of Communications", ["Press Secretary", "Chief Whip", "Cabinet Secretary"])])

race("Detectorists - name it", "Television", "medium", ["Detectorists", "sitcoms", "BBC"], [
 ("Their hobby", "Metal detecting", ["Birdwatching", "Trainspotting", "Fishing"]),
 ("The actor who plays Andy", "Mackenzie Crook", ["Martin Freeman", "Stephen Merchant", "Ralph Ineson"]),
 ("The career Andy trains for", "Archaeology", ["Teaching", "Nursing", "Law"]),
 ("The actor who plays Lance", "Toby Jones", ["Tom Jones", "Toby Stephens", "Rupert Jones"]),
 ("Lance's beloved car", "A Triumph TR7", ["An MG Midget", "A Ford Capri", "A Reliant Scimitar"]),
 ("Their club", "Danebury", ["Dunwich", "Danbury", "Dartley"]),
 ("Andy's partner", "Becky", ["Sophie", "Lucy", "Kate"]),
 ("The Avengers star who played Becky's mum", "Diana Rigg", ["Diana Dors", "Diana Quick", "Diana Ross"]),
 ("The rival pair they call", "Simon and Garfunkel", ["Hall and Oates", "Peters and Lee", "Chas and Dave"]),
 ("The treasure they dream of", "Saxon gold", ["Roman coins", "Viking silver", "Pirate treasure"]),
 ("The theme singer", "Johnny Flynn", ["Johnny Marr", "Johnny Vegas", "Johnny Borrell"]),
 ("The county it was filmed in", "Suffolk", ["Norfolk", "Kent", "Dorset"]),
 ("The channel", "BBC Four", ["Channel 4", "ITV", "Sky Arts"]),
 ("The year it began", "2014", ["2010", "2017", "2020"]),
 ("Series made", "3", ["2", "4", "5"]),
 ("The year of the special that ended it", "2022", ["2019", "2021", "2024"]),
 ("The award it won in 2015", "BAFTA", ["Emmy", "Golden Globe", "Oscar"]),
 ("Andy's actor's role in The Office", "Gareth Keenan", ["Tim Canterbury", "Keith Bishop", "Chris Finch"]),
 ("His pirate with a wooden eye", "Ragetti", ["Pintel", "Gibbs", "Cotton"]),
 ("The Harry Potter elf Lance's actor voiced", "Dobby", ["Kreacher", "Winky", "Hokey"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-257.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
