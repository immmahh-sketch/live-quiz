# Bank session 19 Oct 2026: 1 sitcom race -> bank/race-270.json (As Time Goes By). A Waiting for God race was drafted but had too few solid rows.
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

race("As Time Goes By - name it", "Television", "medium", ["As Time Goes By", "sitcoms", "BBC"], [
 ("The actress who plays Jean", "Judi Dench", ["Judi Love", "Julie Walters", "Joan Collins"]),
 ("The actor who plays Lionel", "Geoffrey Palmer", ["Geoffrey Whitehead", "Geoffrey Boycott", "Geoffrey Rush"]),
 ("Jean's surname", "Pargetter", ["Partridge", "Pargeter-Smith", "Pagett"]),
 ("Lionel's surname", "Hardcastle", ["Hardwick", "Hartley", "Hargreaves"]),
 ("Where Lionel was posted when they lost touch", "Korea", ["Malaya", "Egypt", "Cyprus"]),
 ("Years until they met again", "38", ["18", "28", "48"]),
 ("Jean's business", "A secretarial agency", ["A florist", "A bookshop", "A tea room"]),
 ("Lionel's book", "My Life in Kenya", ["My Life in Africa", "My Kenyan Years", "Out of Kenya"]),
 ("Jean's daughter", "Judy", ["Julie", "Jenny", "Jane"]),
 ("Lionel's lively father", "Rocky", ["Rocco", "Ricky", "Reggie"]),
 ("The writer", "Bob Larbey", ["Bob Monkhouse", "Bob Mortimer", "Bob Holness"]),
 ("His earlier co-written sitcom", "The Good Life", ["Porridge", "Rising Damp", "Steptoe and Son"]),
 ("The film the theme song comes from", "Casablanca", ["Brief Encounter", "Gone with the Wind", "Some Like It Hot"]),
 ("The channel", "BBC One", ["ITV", "BBC Two", "Channel 4"]),
 ("The year it began", "1992", ["1988", "1996", "2000"]),
 ("The year it finally ended", "2005", ["2001", "2008", "2011"]),
 ("Series made", "9", ["5", "7", "11"]),
 ("The star's Bond role", "M", ["Q", "Moneypenny", "Blofeld"]),
 ("Her Oscar-winning film", "Shakespeare in Love", ["Mrs Brown", "Iris", "Philomena"]),
 ("Her earlier sitcom with her husband Michael Williams", "A Fine Romance", ["Just Good Friends", "Ever Decreasing Circles", "Solo"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-270.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
