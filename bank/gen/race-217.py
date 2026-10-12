# Bank session 12 Oct 2026: 1 more general race -> bank/race-217.json (old money words). Checked against the money word, slang
# and banknote races; 240 pence to the pound left out as the 1970s moments race has it.
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

race("what's this old money word?", "History", "medium", ["pre-decimal", "money", "coins", "words"], [
 ("Slang for a sixpence", "Tanner", ["Quid", "Score", "Pony"]),
 ("Slang for a shilling", "Bob", ["Quid", "Score", "Pony"]),
 ("A quarter of a penny, the smallest coin", "Farthing", ["Mite", "Cent", "Pip"]),
 ("Half a penny, as people said it out loud", "Ha'penny", ["Tuppence", "Thruppence", "Penny-ha'penny"]),
 ("The chunky coin with twelve sides", "Threepenny bit", ["Sixpence", "Shilling", "Fifty pence"]),
 ("The two-shilling coin", "Florin", ["Ducat", "Doubloon", "Thaler"]),
 ("Two shillings and sixpence", "Half a crown", ["Half a guinea", "Half a sovereign", "Half a florin"]),
 ("Five shillings, now a coin for royal occasions", "Crown", ["Mark", "Noble", "Angel"]),
 ("Twenty-one shillings, still used for racehorse prices", "Guinea", ["Pound", "Mark", "Ducat"]),
 ("A gold coin worth a pound", "Sovereign", ["Doubloon", "Krugerrand", "Napoleon"]),
 ("An old silver coin worth fourpence", "Groat", ["Mite", "Stiver", "Pip"]),
 ("The brown paper note worth 50p after decimalisation", "Ten-bob note", ["Fiver", "Crown note", "Guinea note"]),
 ("The green paper note scrapped in 1988", "Pound note", ["Fiver", "Guinea note", "Crown note"]),
 ("What 15 February 1971 is remembered as", "Decimal Day", ["Budget Day", "Boxing Day", "Quarter Day"]),
 ("Pounds, shillings and pence, for short", "£sd", ["VAT", "PAYE", "GDP"]),
 ("The letter that stood for a penny, from the Latin denarius", "d", ["p", "c", "s"]),
 ("The bird on the back of the old farthing", "Wren", ["Robin", "Sparrow", "Puffin"]),
 ("How many pennies made a shilling", "Twelve", ["Ten", "Six", "Sixteen"]),
 ("How many shillings made a pound", "Twenty", ["Ten", "Sixteen", "Twenty-four"]),
 ("What the new decimal pennies were first called", "New pence", ["Royal pence", "Modern pence", "Metric pence"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-217.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
