# Bank session 10 Oct 2026: 2 more general races -> bank/race-136.json (wedding words, rugby words; none repeat the quickfire rugby race). 20 rows each, target 10; wrong options are
# the same kind of thing, never another row's right answer, and never also right for that row.
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


race("what's this wedding word?", "Everyday life", "easy", ["weddings", "words"], [
 ("Gives the funniest speech and looks after the rings", "Best man", ["Toastmaster", "Chaperone", "Vicar"]),
 ("One of the bride's attendants, often in matching dresses", "Bridesmaid", ["Chaperone", "Toastmaster", "Vicar"]),
 ("Shows the guests to their seats in church", "Usher", ["Toastmaster", "Chaperone", "Vicar"]),
 ("A young boy who attends the bride", "Page boy", ["Chaperone", "Toastmaster", "Vicar"]),
 ("A little girl who scatters petals down the aisle", "Flower girl", ["Chaperone", "Toastmaster", "Vicar"]),
 ("The chief bridesmaid, if she isn't married", "Maid of honour", ["Chaperone", "Toastmaster", "Vicar"]),
 ("Sheer fabric over the bride's face, lifted for the kiss", "Veil", ["Fascinator", "Tiara", "Train"]),
 ("The flowers the bride carries, then throws over her shoulder", "Bouquet", ["Buttonhole", "Corsage", "Fascinator"]),
 ("Little paper shapes or petals thrown over the couple outside", "Confetti", ["Charger plate", "Cake topper", "Order of service"]),
 ("The announcement read out in church on three Sundays before the wedding", "Banns", ["Order of service", "Prenup", "Trousseau"]),
 ("The official who conducts a civil ceremony", "Registrar", ["Toastmaster", "Chaperone", "Vicar"]),
 ("The main meal after the ceremony, whatever time of day it's served", "Wedding breakfast", ["Evening do", "Receiving line", "Honeymoon"]),
 ("Where the couple, their parents and the best man sit for the meal", "Top table", ["Receiving line", "Charger plate", "Cake topper"]),
 ("Little gifts left at each guest's place, often sugared almonds", "Favours", ["Charger plate", "Cake topper", "Buttonhole"]),
 ("The couple's first spin round the floor as newlyweds", "First dance", ["Receiving line", "Evening do", "Handfasting"]),
 ("The bride-to-be's big night out with her friends", "Hen do", ["Evening do", "Receiving line", "Vow renewal"]),
 ("The groom-to-be's big night out with his mates", "Stag do", ["Evening do", "Receiving line", "Vow renewal"]),
 ("A band worn round the bride's leg, sometimes tossed to the guests", "Garter", ["Tiara", "Train", "Fascinator"]),
 ("Running off to marry in secret", "Elopement", ["Handfasting", "Vow renewal", "Prenup"]),
 ("Something old, something new, ____, something blue", "Something borrowed", ["Something gold", "Something true", "Something given"])])

race("what's this rugby word?", "Sport", "medium", ["rugby", "words"], [
 ("Eight forwards from each side bind together and push to restart play", "Scrum", ["Pod", "Jackal", "Play the ball"]),
 ("Grounding the ball over the opponents' line for five points", "Try", ["Turnover", "Line break", "Bonus point"]),
 ("The kick at goal worth two points after a try", "Conversion", ["Grubber", "Box kick", "Bonus point"]),
 ("A kick through the posts in open play, bouncing the ball first, worth three points", "Drop goal", ["Grubber", "Box kick", "Golden point"]),
 ("Losing the ball forwards out of your hands", "Knock-on", ["Offload", "Dummy", "Turnover"]),
 ("Ten minutes off the pitch for a yellow card", "Sin bin", ["Blood bin", "Dead ball line", "Twenty-two"]),
 ("Players stay on their feet and drive over a ball lying on the ground", "Ruck", ["Pod", "Jackal", "Play the ball"]),
 ("The ball carrier is held up and team-mates bind on and drive forward, ball off the ground", "Maul", ["Pod", "Jackal", "Line break"]),
 ("A high kick ahead for the chasers to compete for, named after an Irish club", "Garryowen", ["Grubber", "Dummy", "Sidestep"]),
 ("The forward in the middle of the front row, who throws the ball in at the lineout", "Hooker", ["Flanker", "Number eight", "Lock"]),
 ("The number 10 who runs the back line and does most of the kicking", "Fly-half", ["Winger", "Full-back", "Centre"]),
 ("The number 9 who feeds the scrum and passes from the base", "Scrum-half", ["Winger", "Full-back", "Centre"]),
 ("One of the two big forwards either side of the hooker in the front row", "Prop", ["Flanker", "Number eight", "Lock"]),
 ("Won by a home nation that beats the other three in one Six Nations", "Triple Crown", ["Millennium Trophy", "Cook Cup", "Webb Ellis Cup"]),
 ("The 'prize' for finishing bottom of the Six Nations", "Wooden spoon", ["Millennium Trophy", "Cook Cup", "Bonus point"]),
 ("The trophy England and Scotland play for each year", "Calcutta Cup", ["Millennium Trophy", "Cook Cup", "Webb Ellis Cup"]),
 ("The challenge New Zealand perform before kick-off", "Haka", ["Siva Tau", "Cibi", "Sipi Tau"]),
 ("Awarded when foul play stops a try that would probably have been scored", "Penalty try", ["Bonus point", "Turnover", "Golden point"]),
 ("Throwing the ball towards the opponents' line, which isn't allowed", "Forward pass", ["Offload", "Dummy", "Sidestep"]),
 ("Catch a kick cleanly inside your own 22 and shout this to win a free kick", "Mark", ["Turnover", "Jackal", "Pod"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-136.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
