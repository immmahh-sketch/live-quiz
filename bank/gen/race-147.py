# Bank session 10 Oct 2026: 3 more general races -> bank/race-147.json (fishing words, furniture words, poker words). 20 rows each, target 10; wrong options are
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

race("what's this fishing word?", "Sport", "medium", ["fishing", "angling", "words"], [
 ("The long, flexible pole you fish with", "Rod", ["Harpoon", "Trident", "Gaff"]),
 ("The winding drum that holds the line", "Reel", ["Swivel", "Lobster pot", "Buoy"]),
 ("The sharp, curved bit the fish bites on", "Hook", ["Swivel", "Harpoon", "Trident"]),
 ("Food put on the hook to tempt the fish", "Bait", ["Ballast", "Swivel", "Tippet"]),
 ("Bobs on the water and dips when a fish bites", "Float", ["Swivel", "Weir", "Sluice"]),
 ("A small lead weight that takes the line down", "Sinker", ["Swivel", "Tippet", "Buoy"]),
 ("A shiny fake fish or spoon that attracts a bite", "Lure", ["Swivel", "Tippet", "Creel"]),
 ("Wriggly bait bought by the pint", "Maggots", ["Lugworms", "Mealworms", "Waxworms"]),
 ("A long net in the water that holds your catch until you weigh it", "Keepnet", ["Lobster pot", "Trawl", "Weir"]),
 ("Scoops up a fish as you reel it to the bank", "Landing net", ["Trawl", "Lobster pot", "Creel"]),
 ("Casting a feathery imitation insect for trout and salmon", "Fly fishing", ["Trawling", "Spearfishing", "Netting"]),
 ("Someone who fishes with a rod and line", "Angler", ["Trawlerman", "Fishmonger", "Harpooner"]),
 ("Putting the fish straight back after landing it", "Catch and release", ["Trawling", "Netting", "Spearfishing"]),
 ("Where the hooks, floats and weights are kept", "Tackle box", ["Creel", "Lobster pot", "Buoy"]),
 ("Flicking the line out over the water", "Cast", ["Trawl", "Dredge", "Troll"]),
 ("Waterproof trousers and boots in one, for standing in the river", "Waders", ["Oilskins", "Gaiters", "Sou'wester"]),
 ("A Scottish guide who helps on a fishing or stalking trip", "Ghillie", ["Trawlerman", "Fishmonger", "Harpooner"]),
 ("The thin nylon thread wound on the reel", "Line", ["Swivel", "Rowlock", "Buoy"]),
 ("Thrown into the water to draw fish to your spot", "Groundbait", ["Ballast", "Swivel", "Tippet"]),
 ("Beeps when a carp takes the bait", "Bite alarm", ["Buoy", "Swivel", "Rowlock"])])

race("what's this furniture word?", "Everyday life", "medium", ["furniture", "home", "words"], [
 ("A sofa-like chair long enough to stretch your legs out on", "Chaise longue", ["Settle", "Love seat", "Pew"]),
 ("A padded box seat with storage inside the lid", "Ottoman", ["Settle", "Pew", "Kneeler"]),
 ("A buttoned leather sofa with arms as high as its back", "Chesterfield", ["Settle", "Love seat", "Pew"]),
 ("A Japanese-style mattress on a low frame that folds up into a sofa", "Futon", ["Trundle bed", "Cot", "Cradle"]),
 ("Curved runners underneath let you sway back and forth", "Rocking chair", ["Wingback", "Settle", "Pew"]),
 ("An armchair whose back tips and whose footrest pops up", "Recliner", ["Wingback", "Settle", "Pew"]),
 ("A floppy sack of polystyrene balls you sink into", "Bean bag", ["Kneeler", "Settle", "Pew"]),
 ("A low padded cushion seat, often round", "Pouffe", ["Kneeler", "Settle", "Pew"]),
 ("A sideboard topped with shelves for showing off plates", "Welsh dresser", ["Commode", "Lowboy", "Escritoire"]),
 ("A low cabinet of drawers for clothes", "Chest of drawers", ["Whatnot", "Étagère", "Dumbwaiter"]),
 ("A tall cupboard with a rail for hanging clothes", "Wardrobe", ["Whatnot", "Étagère", "Commode"]),
 ("A tall chest of drawers, often one stacked on top of another", "Tallboy", ["Lowboy", "Whatnot", "Étagère"]),
 ("A writing desk with a sloping lid that folds down", "Bureau", ["Whatnot", "Commode", "Lowboy"]),
 ("A bed with a tall post at each corner holding up curtains", "Four-poster", ["Trundle bed", "Cot", "Cradle"]),
 ("Two beds stacked one above the other", "Bunk beds", ["Trundle bed", "Cot", "Cradle"]),
 ("A settee that unfolds into somewhere to sleep", "Sofa bed", ["Trundle bed", "Cot", "Cradle"]),
 ("A tall pole with hooks, by the front door", "Hat stand", ["Whatnot", "Étagère", "Dumbwaiter"]),
 ("A heated cart on wheels that keeps dinner warm at the table", "Hostess trolley", ["Dumbwaiter", "Lazy Susan", "Whatnot"]),
 ("Three little tables that tuck under one another", "Nest of tables", ["Whatnot", "Étagère", "Lazy Susan"]),
 ("A tall pendulum clock that stands in the hall", "Grandfather clock", ["Carriage clock", "Cuckoo clock", "Mantel clock"])])

race("what's this poker word?", "Games and toys", "medium", ["poker", "card games", "words"], [
 ("Betting big on a weak hand to scare others off", "Bluff", ["Slow play", "Limp", "Straddle"]),
 ("Five cards all of the same suit", "Flush", ["Rainbow", "Gutshot", "Kicker"]),
 ("Five cards in a run, like 5-6-7-8-9", "Straight", ["Rainbow", "Kicker", "Gutshot"]),
 ("Three of a kind plus a pair", "Full house", ["Kicker", "Rainbow", "Bad beat"]),
 ("Ace, king, queen, jack and ten of one suit, the best hand of all", "Royal flush", ["Bad beat", "Rainbow", "Kicker"]),
 ("A small forced bet everyone puts in before the deal", "Ante", ["Rake", "Bounty", "Straddle"]),
 ("The two forced bets from the players to the dealer's left", "Blinds", ["Rake", "Bounty", "Kicker"]),
 ("The first three shared cards, dealt face up together", "Flop", ["Turn", "Burn card", "Hole cards"]),
 ("The fifth and final shared card", "River", ["Turn", "Burn card", "Hole cards"]),
 ("Pushing every chip you have into the pot", "All in", ["Limp", "Slow play", "Straddle"]),
 ("Throwing your cards away and dropping out of the hand", "Fold", ["Limp", "Straddle", "Showdown"]),
 ("Upping the bet that's already been made", "Raise", ["Limp", "Showdown", "Rake"]),
 ("Passing without betting when no one else has bet yet", "Check", ["Straddle", "Rake", "Bounty"]),
 ("All the chips in the middle, waiting to be won", "Pot", ["Rake", "Bounty", "Satellite"]),
 ("The plastic discs used as money at the table", "Chips", ["Burn cards", "Hole cards", "Kickers"]),
 ("A blank expression that gives nothing away", "Poker face", ["Bad beat", "Rainbow", "Showdown"]),
 ("Two cards of the same value", "Pair", ["Kicker", "Rainbow", "Gutshot"]),
 ("Three cards of the same value", "Three of a kind", ["Kicker", "Rainbow", "Gutshot"]),
 ("All four cards of one value, like four kings", "Four of a kind", ["Kicker", "Rainbow", "Bad beat"]),
 ("A nervous habit that gives away what you're holding", "Tell", ["Bad beat", "Rainbow", "Kicker"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-147.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
