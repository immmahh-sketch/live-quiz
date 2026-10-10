# Bank session 10 Oct 2026: 3 more general races -> bank/race-139.json (baby words, computer keys, tea). 20 rows each, target 10; wrong options are
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


race("what's this baby word?", "Everyday life", "easy", ["babies", "parenting", "words"], [
 ("What a baby wears to catch the wee and poo", "Nappy", ["Romper suit", "Layette", "Bouncer"]),
 ("A rubber teat for a baby to suck on; Americans call it a pacifier", "Dummy", ["Sippy cup", "Night light", "Mobile"]),
 ("A stretchy all-in-one suit with feet", "Babygro", ["Layette", "Mobile", "Bouncer"]),
 ("A small carry-cot of woven wicker for a newborn", "Moses basket", ["Bouncer", "Walker", "Jumperoo"]),
 ("A big hooded carriage for a baby to lie flat in", "Pram", ["Bouncer", "Walker", "Jumperoo"]),
 ("A baby's bed with bars round the sides", "Cot", ["Bouncer", "Walker", "Stair gate"]),
 ("Tied round a baby's neck to catch the mess at mealtimes", "Bib", ["Layette", "Mobile", "Night light"]),
 ("Something cool and chewy for sore gums", "Teething ring", ["Sippy cup", "Night light", "Mobile"]),
 ("A thin cotton cloth kept handy for mopping up sick", "Muslin", ["Layette", "Mobile", "Romper suit"]),
 ("Wrapping a newborn up snugly in a blanket", "Swaddling", ["Tummy time", "Layette", "Stair gate"]),
 ("Long bouts of crying, often in the evening, with no obvious cause", "Colic", ["Cradle cap", "Milk spots", "Tummy time"]),
 ("Moving a baby on to solid food", "Weaning", ["Tummy time", "Cradle cap", "Formula"]),
 ("Patting a baby's back to bring up wind after a feed", "Burping", ["Tummy time", "Gripe water", "Cradle cap"]),
 ("Lets you listen in on a sleeping baby from another room", "Baby monitor", ["Night light", "Mobile", "Stair gate"]),
 ("A little fenced area where a baby can play safely", "Playpen", ["Stair gate", "Bouncer", "Walker"]),
 ("Keeps a baby safe on a journey, strapped into the back seat", "Car seat", ["Bouncer", "Walker", "Jumperoo"]),
 ("A hard, dry biscuit for babies to gnaw on", "Rusk", ["Formula", "Gripe water", "Sippy cup"]),
 ("Carries the nappies, wipes and spare clothes on a day out", "Changing bag", ["Layette", "Night light", "Mobile"]),
 ("Carries a baby strapped against your chest", "Sling", ["Bouncer", "Walker", "Jumperoo"]),
 ("A church ceremony to name a baby and welcome them in", "Christening", ["Tummy time", "Layette", "Baby shower"])])

race("which computer key is this?", "Computers and the internet", "medium", ["computers", "keyboards"], [
 ("The top-left key that cancels or closes things", "Escape", ["Scroll Lock", "Pause/Break", "SysRq"]),
 ("Jumps you to the next box on a form", "Tab", ["Fn", "Alt Gr", "Scroll Lock"]),
 ("Makes everything you type come out in capitals", "Caps Lock", ["Scroll Lock", "Fn", "Alt Gr"]),
 ("Hold it down for a single capital letter", "Shift", ["Fn", "Alt Gr", "Scroll Lock"]),
 ("Hold it with C to copy and V to paste on a PC", "Control", ["Fn", "Alt Gr", "Menu key"]),
 ("The longest key, right at the bottom", "Space bar", ["Fn", "Menu key", "Scroll Lock"]),
 ("Rubs out the letter to the left of the cursor", "Backspace", ["Pause/Break", "SysRq", "Clear"]),
 ("Rubs out the letter to the right of the cursor", "Delete", ["Pause/Break", "SysRq", "Scroll Lock"]),
 ("Sends a message or starts a new line; also called Return", "Enter", ["Fn", "Menu key", "Pause/Break"]),
 ("Jumps to the start of the line", "Home", ["Pause/Break", "Scroll Lock", "SysRq"]),
 ("Jumps to the end of the line", "End", ["Pause/Break", "Scroll Lock", "SysRq"]),
 ("Scrolls a whole screen further down", "Page Down", ["Pause/Break", "Fn", "Menu key"]),
 ("Switches between typing over letters and pushing them along", "Insert", ["Pause/Break", "SysRq", "Clear"]),
 ("Takes a picture of everything on the screen", "Print Screen", ["Pause/Break", "Scroll Lock", "Fn"]),
 ("The function key that usually opens Help", "F1", ["F12", "F5", "F11"]),
 ("Turns the number pad on the right on and off", "Num Lock", ["Scroll Lock", "Fn", "Alt Gr"]),
 ("Opens the Start menu on a PC", "Windows key", ["Menu key", "Fn", "Alt Gr"]),
 ("Four keys that move the cursor up, down, left and right", "Arrow keys", ["Function keys", "Media keys", "Modifier keys"]),
 ("The Mac key marked ⌘, used for copy and paste", "Command", ["Option", "Fn", "Alt Gr"]),
 ("Held with F4 to close a window on a PC", "Alt", ["Fn", "Alt Gr", "Menu key"])])

race("what's this tea word?", "Food and drink", "medium", ["tea", "drinks"], [
 ("Strong, with milk and two sugars, the way a tradesman likes it", "Builder's tea", ["Pu-erh", "Yerba mate", "Kombucha"]),
 ("Black tea flavoured with oil of bergamot", "Earl Grey", ["Keemun", "Ceylon", "Pu-erh"]),
 ("A light black tea from the foothills of the Himalayas, the 'champagne of teas'", "Darjeeling", ["Keemun", "Ceylon", "Pu-erh"]),
 ("A strong, malty black tea from north-east India", "Assam", ["Keemun", "Ceylon", "Pu-erh"]),
 ("A Chinese black tea dried over pine fires, so it tastes smoky", "Lapsang souchong", ["Keemun", "Gunpowder", "Pu-erh"]),
 ("Indian tea brewed with milk and spices like cardamom and cinnamon", "Chai", ["Yerba mate", "Kombucha", "Hibiscus"]),
 ("Bright green powdered tea whisked into hot water, from Japan", "Matcha", ["Gunpowder", "Pu-erh", "Yerba mate"]),
 ("A caffeine-free red 'bush tea' from South Africa", "Rooibos", ["Hibiscus", "Yerba mate", "Nettle"]),
 ("A calming herbal tea made from daisy-like flowers, drunk at bedtime", "Camomile", ["Nettle", "Hibiscus", "Lemon and ginger"]),
 ("A fresh-tasting herbal tea said to settle the stomach", "Peppermint", ["Nettle", "Hibiscus", "Kombucha"]),
 ("A Chinese tea halfway between green and black", "Oolong", ["Keemun", "Pu-erh", "Gunpowder"]),
 ("A strong morning blend, often of Assam, Ceylon and Kenyan teas", "English Breakfast", ["Pu-erh", "Gunpowder", "Yerba mate"]),
 ("Sandwiches, scones and cakes on a tiered stand, said to be the Duchess of Bedford's idea", "Afternoon tea", ["Kombucha", "Tea caddy", "Samovar"]),
 ("A pot of tea with scones, jam and clotted cream", "Cream tea", ["Tea caddy", "Samovar", "Kombucha"]),
 ("A knitted cover that keeps the teapot warm", "Tea cosy", ["Tea caddy", "Samovar", "Saucer"]),
 ("A little mesh ball or basket for brewing loose leaves", "Infuser", ["Tea caddy", "Samovar", "Saucer"]),
 ("Invented by accident when Americans dunked little silk pouches of samples", "Tea bag", ["Tea caddy", "Samovar", "Saucer"]),
 ("Telling fortunes from the leaves left in the bottom of a cup", "Tasseography", ["Kombucha", "Samovar", "Pu-erh"]),
 ("Dip a biscuit into your tea", "Dunk", ["Stir", "Steep", "Sip"]),
 ("Unoxidised tea, drunk without milk, much loved in China and Japan", "Green tea", ["Pu-erh", "Keemun", "Yerba mate"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-139.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
