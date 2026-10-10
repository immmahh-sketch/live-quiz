# Bank session 10 Oct 2026: 2 more general races -> bank/race-124.json (card games, hairstyles). 20 rows each, target 10; wrong options are
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


race("which card game is this?", "Games and toys", "medium", ["card games", "games"], [
 ("Shout its name when two matching cards land on top of each other", "Snap", ["Spit", "Slapjack", "Pairs"]),
 ("A game for one, building down in alternating colours; Americans call it Solitaire", "Patience", ["Spit", "Racing Demon", "Cassino"]),
 ("Bet on your hand, where a royal flush beats everything", "Poker", ["Brag", "Faro", "Écarté"]),
 ("Two partnerships bid for tricks, and one hand is laid face up as 'dummy'", "Bridge", ["Euchre", "Spades", "Bezique"]),
 ("Collect sets and runs, then lay them down to go out", "Rummy", ["Cassino", "Bezique", "Piquet"]),
 ("Get as close to 21 as you can without going bust, against the dealer", "Blackjack", ["Faro", "Brag", "Écarté"]),
 ("Scored with pegs on a wooden board: 'fifteen two, fifteen four...'", "Cribbage", ["Bezique", "Piquet", "Skat"]),
 ("A trick-taking game for two pairs with no bidding, the ancestor of bridge", "Whist", ["Euchre", "Spades", "Skat"]),
 ("Ask another player 'Have you got any sevens?' and hope they don't send you off to the pile", "Go Fish", ["Pairs", "Spit", "Slapjack"]),
 ("Pass cards round and don't get stuck with the unmatched queen at the end", "Old Maid", ["Slapjack", "Pairs", "Spit"]),
 ("Collect all four members of families like Mr Bun the Baker", "Happy Families", ["Pairs", "Slapjack", "Spit"]),
 ("Compare stats like speed or height to win your opponent's card", "Top Trumps", ["Pairs", "Slapjack", "Cassino"]),
 ("A pub game with lives: swap with your neighbour to avoid holding the lowest card", "Chase the Ace", ["Spit", "Brag", "Switch"]),
 ("Avoid winning any heart in a trick, and above all the queen of spades", "Hearts", ["Spades", "Euchre", "Skat"]),
 ("A rummy-style game from Uruguay, played with two packs and jokers, chasing sets of seven", "Canasta", ["Bezique", "Piquet", "Cassino"]),
 ("Bet on 'player' or 'banker' in the casino game James Bond plays in 'Dr. No'", "Baccarat", ["Faro", "Écarté", "Brag"]),
 ("Build out from the four sevens, up and down in each suit", "Sevens", ["Switch", "Cassino", "Spit"]),
 ("Lay cards face down, say what they are, and hope nobody calls you a liar", "Cheat", ["Brag", "Switch", "Spit"]),
 ("Match the suit or number of the top card; an eight lets you change the suit", "Crazy Eights", ["Spit", "Cassino", "Slapjack"]),
 ("Turn cards over in turn; a court card or ace makes your opponent pay up to four cards", "Beggar My Neighbour", ["Slapjack", "Spit", "Pairs"])])

race("what's this hairstyle?", "Fashion", "medium", ["hair", "hairstyles", "fashion"], [
 ("Business at the front, party at the back", "Mullet", ["Shag", "Rat tail", "Feathered"]),
 ("A towering 1960s 'do' piled high on the head, as worn by Amy Winehouse", "Beehive", ["Victory rolls", "Topknot", "Marcel wave"]),
 ("Head shaved on both sides, leaving a tall strip down the middle: a punk favourite", "Mohican", ["Liberty spikes", "Fade", "Skinhead"]),
 ("Hair swept up and back at the front, as worn by Morrissey and Tintin", "Quiff", ["Fade", "Caesar cut", "Spiky"]),
 ("A straight cut level with the jaw, all the way round", "Bob", ["Wedge", "Shag", "Eton crop"]),
 ("A very short, cropped women's style made famous by Twiggy", "Pixie cut", ["Wedge", "Shag", "Lob"]),
 ("Naturally curly hair grown out into a big round halo", "Afro", ["Jheri curl", "Box braids", "Bantu knots"]),
 ("Hair matted into rope-like strands, as worn by Bob Marley", "Dreadlocks", ["Box braids", "Bantu knots", "Jheri curl"]),
 ("Hair braided close to the scalp in neat straight lines", "Cornrows", ["Box braids", "Fishtail plait", "French plait"]),
 ("Very short all over, a little longer on top: the classic military trim", "Crew cut", ["Caesar cut", "Fade", "Skinhead"]),
 ("Looks like someone put a pudding basin on your head and cut round it", "Bowl cut", ["Caesar cut", "Eton crop", "Wedge"]),
 ("A layered, bouncy cut named after a 'Friends' character", "The Rachel", ["Shag", "Feathered", "Lob"]),
 ("Shaved short at the sides and back with long hair on top: the 'Peaky Blinders' look", "Undercut", ["Spiky", "Caesar cut", "Skinhead"]),
 ("Long hair from one side swept across to hide a bald patch", "Comb-over", ["Tonsure", "Topknot", "Rat tail"]),
 ("A 1990s boys' cut, parted in the middle and hanging either side of the face", "Curtains", ["Fringe", "Feathered", "Shag"]),
 ("Short at the sides and dead flat across the top, as on Dolph Lundgren in 'Rocky IV'", "Flat top", ["Caesar cut", "Fade", "Spiky"]),
 ("Teased and backcombed into a big rounded puff, a 1960s favourite of Dusty Springfield", "Bouffant", ["Victory rolls", "Marcel wave", "Finger waves"]),
 ("A smooth knot or coil of hair pinned at the nape of the neck", "Chignon", ["Topknot", "Ponytail", "French plait"]),
 ("Chemically set curls, a huge 1980s craze among footballers", "Perm", ["Marcel wave", "Finger waves", "Feathered"]),
 ("Two ponytails, one on either side of the head", "Bunches", ["Topknot", "Fishtail plait", "Ponytail"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-124.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
