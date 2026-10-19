# Bank session 19 Oct 2026: 2 sitcom races -> bank/race-261.json (Rab C. Nesbitt; Benidorm).
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

race("Rab C. Nesbitt - name it", "Television", "medium", ["Rab C. Nesbitt", "sitcoms", "Scotland"], [
 ("The actor who plays Rab", "Gregor Fisher", ["Gregor Townsend", "Greg Hemphill", "Gregory Porter"]),
 ("What Rab always wears", "A string vest", ["A kilt", "A tracksuit", "A boiler suit"]),
 ("What he's often called", "A street philosopher", ["A local hero", "A gangster", "A bus driver"]),
 ("His wife", "Mary Doll", ["Mary Jane", "Molly Doll", "Maisie Doll"]),
 ("The actress who plays her", "Elaine C. Smith", ["Elaine Paige", "Elaine Stritch", "Elaine Lordan"]),
 ("Their two sons", "Gash and Burney", ["Gav and Barney", "Gus and Bernie", "Gaz and Benny"]),
 ("Rab's best pal", "Jamesie Cotter", ["Jimmy Cotter", "Jamesie Coulter", "Jamie Carter"]),
 ("The actor (not the footballer) who plays him", "Andy Gray", ["Andy Murray", "Andy Goldstein", "Andy Cameron"]),
 ("The part of Glasgow they live in", "Govan", ["Gorbals", "Easterhouse", "Partick"]),
 ("The city", "Glasgow", ["Edinburgh", "Dundee", "Aberdeen"]),
 ("The sketch show it grew out of", "Naked Video", ["Chewin' the Fat", "Absolutely", "Scotch and Wry"]),
 ("The writer", "Ian Pattison", ["Ian Hislop", "Ian La Frenais", "Ian Rankin"]),
 ("The channel", "BBC Two", ["BBC One", "STV", "Channel 4"]),
 ("The year it began", "1988", ["1984", "1992", "1996"]),
 ("The year the first run ended", "1999", ["1995", "2002", "2005"]),
 ("The year it came back", "2008", ["2004", "2011", "2014"]),
 ("The star's silent advert character", "The Baldy Man", ["The Bald Eagle", "The Hairless Man", "Mr Baldy"]),
 ("His role in Love Actually", "Billy Mack's manager", ["The Prime Minister's driver", "Colin's dad", "A wedding singer"]),
 ("Rab's headwear", "A bandage round his head", ["A flat cap", "A tartan bunnet", "A woolly hat"]),
 ("How Rab spends most of his time", "Out of work", ["In the shipyards", "Driving a taxi", "Running a pub"])])

race("Benidorm - name it", "Television", "medium", ["Benidorm", "sitcoms", "ITV"], [
 ("The hotel", "The Solana", ["The Sol Mar", "The Costa", "The Bella Vista"]),
 ("The holiday deal", "All-inclusive", ["Half board", "Self-catering", "Bed and breakfast"]),
 ("The Spanish coast it's on", "Costa Blanca", ["Costa del Sol", "Costa Brava", "Costa Dorada"]),
 ("The family at its heart", "The Garveys", ["The Royles", "The Boswells", "The Trotters"]),
 ("The actor who plays dad Mick", "Steve Pemberton", ["Steve Coogan", "Steve Speirs", "Steve Edge"]),
 ("That actor's comedy troupe", "The League of Gentlemen", ["Monty Python", "The Mighty Boosh", "The Fast Show"]),
 ("Mum", "Janice", ["Joan", "Julie", "Jackie"]),
 ("The gran on the mobility scooter", "Madge", ["Marge", "Maud", "Mabel"]),
 ("The actress who plays her", "Sheila Reid", ["Sheila Hancock", "Sheila Ferguson", "Sheila Steafel"]),
 ("The Garveys' teenage daughter", "Chantelle", ["Charlene", "Chanel", "Shannon"]),
 ("The swinging couple", "Donald and Jacqueline", ["Derek and Jean", "David and Joan", "Dennis and Jackie"]),
 ("The camp hairdresser", "Kenneth", ["Kevin", "Keith", "Kenny"]),
 ("The actor who plays him", "Tony Maudsley", ["Tony Slattery", "Tony Robinson", "Tony Hadley"]),
 ("The flirty Spanish barman", "Mateo", ["Manuel", "Miguel", "Marco"]),
 ("Johnny Vegas's character", "Martin Weedon", ["Martin Platt", "Martin Kemp", "Martin Brody"]),
 ("The actor who plays drag act Les/Lesley", "Tim Healy", ["Tim Vine", "Tim Spall", "Tim Brooke-Taylor"]),
 ("Its creator", "Derren Litten", ["Derren Brown", "Darren Day", "Darren Gough"]),
 ("The channel", "ITV", ["BBC One", "Channel 4", "Sky One"]),
 ("The year it began", "2007", ["2003", "2010", "2013"]),
 ("Series made", "10", ["8", "12", "14"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-261.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
