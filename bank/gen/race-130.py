# Bank session 10 Oct 2026: 2 more general races -> bank/race-130.json (chess words, theatre words). 20 rows each, target 10; wrong options are
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


race("what's this chess word?", "Games and toys", "medium", ["chess", "games"], [
 ("The king is under attack and can't escape: game over", "Checkmate", ["Perpetual check", "Swindle", "Bughouse"]),
 ("The player to move has no legal move but isn't in check, so it's a draw", "Stalemate", ["Perpetual check", "Zwischenzug", "Fianchetto"]),
 ("King and rook move in one go, tucking the king away safely", "Castling", ["Fianchetto", "Outpost", "Battery"]),
 ("A pawn captures another that has just jumped two squares past it", "En passant", ["Zwischenzug", "Fianchetto", "Outpost"]),
 ("One piece attacks two enemy pieces at once", "Fork", ["Battery", "Outpost", "Zwischenzug"]),
 ("A piece can't move without exposing a more valuable piece behind it", "Pin", ["Battery", "Outpost", "Tempo"]),
 ("A valuable piece is attacked and, when it moves, a lesser one behind it is taken", "Skewer", ["Battery", "Outpost", "Tempo"]),
 ("Giving up a pawn early on to get ahead in development", "Gambit", ["Fianchetto", "Outpost", "Swindle"]),
 ("A pawn reaches the far side of the board and becomes a queen", "Promotion", ["Fianchetto", "Outpost", "Battery"]),
 ("Every move you could make will worsen your position, but you have to move", "Zugzwang", ["Zwischenzug", "Fianchetto", "Tempo"]),
 ("The piece shaped like a castle tower", "Rook", ["King", "Chancellor", "Archbishop"]),
 ("The only piece that can jump over others, moving in an L-shape", "Knight", ["King", "Chancellor", "Amazon"]),
 ("Moves any distance diagonally and stays on one colour all game", "Bishop", ["King", "Archbishop", "Chancellor"]),
 ("Moves forward one square at a time, but captures diagonally", "Pawn", ["King", "Amazon", "Chancellor"]),
 ("The most powerful piece, moving any distance in any straight line", "Queen", ["King", "Archbishop", "Chancellor"]),
 ("The top title a chess player can earn, kept for life", "Grandmaster", ["Arbiter", "Patzer", "Simul"]),
 ("Your king is under attack and you must deal with it at once", "Check", ["Swindle", "Blunder", "Tempo"]),
 ("Give up the game before checkmate, often by tipping over your king", "Resign", ["Swindle", "Blunder", "Simul"]),
 ("A fast game with just a few minutes each on the clock", "Blitz", ["Simul", "Patzer", "Arbiter"]),
 ("A four-move checkmate that catches out beginners, with queen and bishop", "Scholar's Mate", ["Fool's Mate", "Ruy Lopez", "Caro-Kann"])])

race("what's this theatre word?", "Theatre", "medium", ["theatre", "words"], [
 ("The hidden areas at the sides of the stage where actors wait", "Wings", ["Flats", "Fly tower", "Trap room"]),
 ("A row of lamps along the front edge of the stage floor", "Footlights", ["Followspot", "Cyclorama", "Gauze"]),
 ("The frame around the front of the stage, like a picture frame", "Proscenium arch", ["Cyclorama", "Fly tower", "Orchestra pit"]),
 ("The seats on the ground floor, nearest the stage", "Stalls", ["Mezzanine", "Foyer", "Gallery"]),
 ("The first balcony of seats above the stalls", "Dress circle", ["Foyer", "Gallery", "Auditorium"]),
 ("The highest, cheapest seats, right up near the ceiling", "The gods", ["Mezzanine", "Foyer", "Orchestra pit"]),
 ("An actor who learns a part in case the star can't go on", "Understudy", ["Walk-on", "Chorus", "Extra"]),
 ("An afternoon performance", "Matinée", ["Previews", "Read-through", "Tech run"]),
 ("An extra number performed because the audience calls for more", "Encore", ["Aside", "Cue", "Walk-on"]),
 ("When the cast come back on stage at the end to take their bows", "Curtain call", ["Get-in", "Blocking", "Walk-on"]),
 ("Making up lines on the spot when you've forgotten them", "Ad lib", ["Blocking", "Cue", "Aside"]),
 ("What you say to wish an actor good luck", "Break a leg", ["Fit-up", "Get-in", "Walk-on"]),
 ("The lounge where performers relax before and after going on", "Green room", ["Trap room", "Foyer", "Dock"]),
 ("The back of the stage, furthest from the audience", "Upstage", ["Apron", "Orchestra pit", "Fly tower"]),
 ("The break halfway through, when you dash for an ice cream", "Interval", ["Previews", "Tech run", "Read-through"]),
 ("The final run-through in full costume before opening night", "Dress rehearsal", ["Read-through", "Tech run", "Previews"]),
 ("A speech where a character alone on stage speaks their thoughts aloud", "Soliloquy", ["Aside", "Chorus", "Cue"]),
 ("Getting the giggles on stage and breaking character", "Corpsing", ["Blocking", "Cue", "Fit-up"]),
 ("Where you buy or collect your tickets", "Box office", ["Foyer", "Dock", "Fly tower"]),
 ("The person offstage who whispers a line when an actor forgets it", "Prompter", ["Dresser", "Call boy", "Chaperone"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-130.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
