# Bank session 19 Oct 2026: 2 races -> bank/race-291.json (Gavin & Stacey; Cold Feet).
# Neither show had a 'name it' race in the live bank (Gavin & Stacey only had a race about its words). Checked against every live race
# with lqsql/audit/race-overlap-live.py before importing; three Gavin &
# Stacey rows (Billericay, Essex, Mick) were swapped after the check found five rights shared with the word race.
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

race("Gavin & Stacey - name it", "Television", "medium", ["Gavin & Stacey", "sitcoms", "BBC"], [
 ("The pair who wrote it", "James Corden and Ruth Jones", ["Ricky Gervais and Stephen Merchant", "Simon Pegg and Jessica Hynes", "Graham Linehan and Arthur Mathews"]),
 ("The coach firm Dave runs", "Dave Coaches", ["Dave's Taxis", "Coastal Coaches", "Barry Buses"]),
 ("Dawn and Pete's surname", "Sutcliffe", ["Smith", "Shipman", "Sanders"]),
 ("Stacey's home town", "Barry", ["Cardiff", "Newport", "Swansea"]),
 ("The actor who played Gavin", "Mathew Horne", ["Matt Lucas", "Matthew Perry", "Mathew Baynton"]),
 ("The actress who played Stacey", "Joanna Page", ["Joanna Lumley", "Joanna Scanlan", "Jo Brand"]),
 ("Gavin's mum", "Pam", ["Pat", "Peggy", "Paula"]),
 ("The actress who played her", "Alison Steadman", ["Alison Moyet", "Alison Hammond", "Alison Lapper"]),
 ("Her favourite exclamation", "Oh my life!", ["I don't believe it!", "Stupid boy!", "Am I bovvered?"]),
 ("The actor who played Gavin's dad", "Larry Lamb", ["Larry Grayson", "Larry Hagman", "Lenny Henry"]),
 ("The actor who played Uncle Bryn", "Rob Brydon", ["Rob Beckett", "Robson Green", "Rob Rinder"]),
 ("Nessa's catchphrase", "What's occurring?", ["Lovely jubbly", "Shut that door!", "Nice to see you!"]),
 ("Nessa's surname", "Jenkins", ["Jones", "Evans", "Davies"]),
 ("Smithy's first name", "Neil", ["Nick", "Nigel", "Norman"]),
 ("The channel it started on", "BBC Three", ["BBC Two", "Channel 4", "ITV2"]),
 ("The year it began", "2007", ["2003", "2010", "2013"]),
 ("The cliffhanger at the end of the 2019 special", "Nessa proposed to Smithy", ["Gavin left Stacey", "Bryn won the lottery", "Pam moved to Wales"]),
 ("The year of the final episode", "2024", ["2020", "2022", "2026"]),
 ("The day the specials go out", "Christmas Day", ["Boxing Day", "New Year's Eve", "Easter Sunday"]),
 ("The fishing trip mystery Bryn never explains", "What happened on the fishing trip", ["What happened at the wedding", "Where Dawn's ring went", "Who ate the turkey"])])

race("Cold Feet - name it", "Television", "medium", ["Cold Feet", "TV drama", "ITV"], [
 ("The city it's set in", "Manchester", ["Leeds", "Liverpool", "Birmingham"]),
 ("The channel", "ITV", ["BBC One", "Channel 4", "BBC Two"]),
 ("The year of the pilot", "1997", ["1993", "2001", "2005"]),
 ("The writer who created it", "Mike Bullen", ["Mike Leigh", "Mike Bartlett", "Mike Hodges"]),
 ("Couples at its heart", "3", ["2", "4", "5"]),
 ("The award the pilot won", "The Golden Rose of Montreux", ["An Emmy", "An Oscar", "A Grammy"]),
 ("The actor who played Adam", "James Nesbitt", ["James Norton", "James Bolam", "James Purefoy"]),
 ("Where he comes from", "Northern Ireland", ["Scotland", "Wales", "Cornwall"]),
 ("His dwarf in The Hobbit films", "Bofur", ["Bombur", "Bifur", "Balin"]),
 ("Adam's famous romantic stunt", "Standing naked with a rose", ["Hiring a skywriter", "Singing on a bus", "Proposing on a pier"]),
 ("The actress who played Rachel", "Helen Baxendale", ["Helen McCrory", "Helen Mirren", "Helen Flanagan"]),
 ("How Rachel left the show", "She died in a car crash", ["She moved to Australia", "She joined a convent", "She won the lottery"]),
 ("The year that happened", "2003", ["1999", "2006", "2009"]),
 ("Adam and Rachel's son", "Matthew", ["Michael", "Mark", "Martin"]),
 ("The actor who played Pete", "John Thomson", ["John Simm", "John Bishop", "John Hannah"]),
 ("The actress who played Jenny", "Fay Ripley", ["Fay Weldon", "Faye Dunaway", "Faye Tozer"]),
 ("The actor who played David", "Robert Bathurst", ["Robert Lindsay", "Robert Powell", "Robert Hardy"]),
 ("David's job", "Management consultant", ["Teacher", "Plumber", "Vet"]),
 ("The actress who played Karen", "Hermione Norris", ["Hermione Gingold", "Hermione Baddeley", "Harriet Walter"]),
 ("The year it came back after 13 years away", "2016", ["2011", "2019", "2022"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-291.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
