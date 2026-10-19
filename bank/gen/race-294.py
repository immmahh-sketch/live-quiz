# Bank session 19 Oct 2026: 2 races -> bank/race-294.json (Cracker; Alan Partridge).
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

race("Cracker - name it", "Television", "medium", ["Cracker", "TV drama", "ITV"], [
 ("The actor who played the criminal psychologist", "Robbie Coltrane", ["Robbie Williams", "Robbie Fowler", "Robson Green"]),
 ("His nickname", "Fitz", ["Fido", "Fitch", "Finn"]),
 ("His full name", "Dr Eddie Fitzgerald", ["Dr Ed Finnegan", "Dr Eric Fitzpatrick", "Dr Ernest Fitzroy"]),
 ("The writer who created it", "Jimmy McGovern", ["Jimmy Nail", "Jimmy Carr", "Jim Davidson"]),
 ("The city it's set in", "Manchester", ["Leeds", "Liverpool", "Newcastle"]),
 ("The ITV company that made it", "Granada", ["Thames", "Central", "Anglia"]),
 ("The channel", "ITV", ["BBC One", "Channel 4", "BBC Two"]),
 ("The year it began", "1993", ["1989", "1996", "1999"]),
 ("Fitz's vices", "Gambling, drink and cigarettes", ["Fast cars and golf", "Shopping and sleeping", "Chocolate and crosswords"]),
 ("His wife", "Judith", ["Julie", "Jean", "Janet"]),
 ("The actress who played her", "Barbara Flynn", ["Barbara Windsor", "Barbara Knox", "Barbara Dickson"]),
 ("The DS who works with him", "Jane Penhaligon", ["Jane Tennison", "Jane Marple", "Jane Eyre"]),
 ("The actress who played her", "Geraldine Somerville", ["Geraldine McEwan", "Geraldine James", "Geraldine Chaplin"]),
 ("The DS who is her rival", "Jimmy Beck", ["Jimmy Perez", "Jimmy Corkhill", "Jimmy Bullard"]),
 ("The detective who was killed", "Bilborough", ["Beckinsale", "Barnaby", "Bergerac"]),
 ("The actor who played him", "Christopher Eccleston", ["Christopher Timothy", "Christopher Biggins", "Christopher Ellison"]),
 ("The Doctor Who role Eccleston later played", "The Ninth Doctor", ["The Fourth Doctor", "The Tenth Doctor", "The Eleventh Doctor"]),
 ("The killer in 'To Be a Somebody'", "Albie Kinsella", ["Alfie Solomons", "Alec Hardy", "Alan Bradley"]),
 ("The actor who played him", "Robert Carlyle", ["Robert Lindsay", "Robert Powell", "Robert Webb"]),
 ("The US remake's lead", "Robert Pastorelli", ["Robert Redford", "Robert Mitchum", "Robert Vaughn"])])

race("Alan Partridge - name it", "Television", "medium", ["Alan Partridge", "sitcoms", "BBC"], [
 ("The comedian who plays Alan", "Steve Coogan", ["Steve Pemberton", "Steve Punt", "Steve Davis"]),
 ("The city he comes from", "Norwich", ["Ipswich", "Lincoln", "Cambridge"]),
 ("The radio station he works for", "North Norfolk Digital", ["Radio Norfolk", "Norwich FM", "Anglia Gold"]),
 ("The chat show that introduced him", "Knowing Me, Knowing You", ["The Alan Partridge Show", "Alan's Place", "Partridge Tonight"]),
 ("The sitcom that followed", "I'm Alan Partridge", ["Alan Partridge: Reborn", "Partridge Tonight", "Alan on Air"]),
 ("The year the sitcom began", "1997", ["1993", "2001", "2005"]),
 ("The hotel he lives in", "Linton Travel Tavern", ["Norwich Premier Inn", "Sleepy Hollow Lodge", "The Wherry Hotel"]),
 ("His catchphrase of delight", "Aha!", ["Ooh!", "Eureka!", "Oh my life!"]),
 ("What he shouts to celebrate", "Back of the net!", ["Top of the pops!", "Over the moon!", "Into the pocket!"]),
 ("His long-suffering PA", "Lynn", ["Linda", "Lorna", "Louise"]),
 ("The actress who plays her", "Felicity Montagu", ["Felicity Kendal", "Felicity Jones", "Felicity Huffman"]),
 ("His assistant who lives in a caravan", "Michael", ["Martin", "Mark", "Matthew"]),
 ("The rival DJ", "Dan Moody", ["Dan Snow", "Dan Walker", "Dan Brown"]),
 ("His favourite band", "ABBA", ["Queen", "Genesis", "Oasis"]),
 ("The band he thinks the Beatles could have been", "Wings", ["Take That", "The Kinks", "Status Quo"]),
 ("The 2013 film", "Alpha Papa", ["Omega Beta", "Gamma Ray", "Delta Foxtrot"]),
 ("The channel the first shows were on", "BBC Two", ["BBC One", "ITV", "Channel 4"]),
 ("The 2019 chat-show series", "This Time with Alan Partridge", ["Alan Tonight", "Partridge Live", "Alan Tomorrow"]),
 ("The online series where he sits in a studio", "Mid Morning Matters", ["Early Morning Matters", "Late Night Matters", "Afternoon Matters"]),
 ("The year Steve Coogan was born", "1965", ["1961", "1969", "1973"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-294.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
