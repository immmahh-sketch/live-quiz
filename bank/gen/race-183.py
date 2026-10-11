# Bank session 11 Oct 2026: 3 more general races -> bank/race-183.json (video game, Harry Potter and royal words). 20 rows each, target 10; wrong options are
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

race("what's this video game word?", "Games", "medium", ["video games", "gaming", "words"], [
 ("The big enemy at the end of a level", "Boss", ["Minion", "Mob", "Grunt"]),
 ("Where you restart after dying, partway through a level", "Checkpoint", ["Waypoint", "Hotspot", "Endpoint"]),
 ("The on-screen figure that represents you", "Avatar", ["Emoji", "Icon", "Cursor"]),
 ("A character the computer controls", "NPC", ["RPG", "MMO", "DLC"]),
 ("Players fighting each other rather than the computer", "PvP", ["Co-op", "Single-player", "Campaign"]),
 ("A shoot-'em-up seen through the hero's own eyes", "First-person shooter", ["Platformer", "Beat-'em-up", "Side-scroller"]),
 ("Coming back to life after being killed", "Respawn", ["Reload", "Rewind", "Refresh"]),
 ("A bug that makes the game behave strangely", "Glitch", ["Patch", "Mod", "Hack"]),
 ("Finishing a game as fast as humanly possible", "Speedrun", ["Sprint", "Dash", "Marathon"]),
 ("A beginner, in gamer slang", "Noob", ["Pro", "Grinder", "Camper"]),
 ("The delay you get on a slow connection", "Lag", ["Drag", "Stall", "Snag"]),
 ("A paid-for mystery crate of random items", "Loot box", ["Treasure chest", "Goody bag", "Lucky dip"]),
 ("An open game like Minecraft where you build freely", "Sandbox", ["Arcade", "Puzzler", "Racer"]),
 ("A hidden secret left in the game by its makers", "Easter egg", ["Golden ticket", "Time capsule", "Red herring"]),
 ("What you type in for infinite lives", "Cheat code", ["Pin code", "Postcode", "Area code"]),
 ("The stick you push to steer on old arcade machines", "Joystick", ["Gearstick", "Drumstick", "Lipstick"]),
 ("The box under the telly, like a PlayStation or Xbox", "Console", ["Router", "Modem", "Decoder"]),
 ("Gaining enough experience to get stronger", "Level up", ["Log in", "Top up", "Warm up"]),
 ("The words on screen when you've lost all your lives", "Game over", ["Time out", "Full time", "Checkmate"]),
 ("A temporary boost, like Mario's star", "Power-up", ["Pick-me-up", "Top-up", "Warm-up"])])

race("what's this Harry Potter word?", "Books", "medium", ["Harry Potter", "wizards", "words"], [
 ("A person with no magic at all", "Muggle", ["Mugwump", "Goblin", "Ghoul"]),
 ("Someone from a wizarding family born without magic", "Squib", ["Dud", "Hobbit", "Gremlin"]),
 ("The sport played on broomsticks at Hogwarts", "Quidditch", ["Gobstones", "Croquet", "Polo"]),
 ("The tiny winged golden ball worth 150 points", "Golden Snitch", ["Golden Egg", "Golden Fleece", "Philosopher's Stone"]),
 ("The red ball used to score goals", "Quaffle", ["Gobstone", "Remembrall", "Sneakoscope"]),
 ("The heavy balls that try to knock players off their brooms", "Bludgers", ["Bludgeons", "Bowlers", "Bouncers"]),
 ("An object hiding part of a dark wizard's soul", "Horcrux", ["Hallow", "Talisman", "Amulet"]),
 ("An everyday object that whisks you away when you touch it", "Portkey", ["Time-Turner", "Remembrall", "Sneakoscope"]),
 ("A stone basin for reliving memories", "Pensieve", ["Goblet of Fire", "Foe-glass", "Vanishing Cabinet"]),
 ("The mirror that shows your deepest desire", "Mirror of Erised", ["Two-way mirror", "Foe-glass", "Magic lantern"]),
 ("Thrown into a fireplace to travel through green flames", "Floo Powder", ["Pixie dust", "Sherbet Lemon", "Bubotuber pus"]),
 ("The potion that makes you look like someone else", "Polyjuice Potion", ["Amortentia", "Skele-Gro", "Wolfsbane"]),
 ("Liquid luck", "Felix Felicis", ["Amortentia", "Draught of Living Death", "Pepperup"]),
 ("The truth potion", "Veritaserum", ["Amortentia", "Skele-Gro", "Pepperup"]),
 ("The wizarding bank run by goblins", "Gringotts", ["Ollivanders", "Flourish and Blotts", "Honeydukes"]),
 ("The wizard prison guarded by Dementors", "Azkaban", ["Nurmengard", "Durmstrang", "Godric's Hollow"]),
 ("The wizarding world's daily newspaper", "Daily Prophet", ["The Quibbler", "Witch Weekly", "Evening Standard"]),
 ("Hooded guards who suck the happiness out of you", "Dementors", ["Inferi", "Boggarts", "Thestrals"]),
 ("The silvery guardian conjured to drive them off", "Patronus", ["Animagus", "Familiar", "Boggart"]),
 ("Decides which house each first-year joins", "Sorting Hat", ["Goblet of Fire", "Marauder's Map", "Remembrall"])])

race("what's this royal word?", "History", "medium", ["royal family", "monarchy", "words"], [
 ("The monarch's ceremonial chair", "Throne", ["Dais", "Pew", "Pulpit"]),
 ("The ceremony of crowning a new monarch", "Coronation", ["Inauguration", "Ordination", "Graduation"]),
 ("The person next in line", "Heir", ["Ward", "Squire", "Steward"]),
 ("Someone ruling for a monarch who is too young or too ill", "Regent", ["Viceroy", "Chancellor", "Steward"]),
 ("Giving up the throne by choice", "Abdication", ["Accession", "Succession", "Deposition"]),
 ("The flag flown when the monarch is in residence", "Royal Standard", ["Union Jack", "Red Ensign", "White Ensign"]),
 ("The crowns, orb and sceptres kept in the Tower of London", "Crown Jewels", ["Royal Collection", "Elgin Marbles", "Stone of Destiny"]),
 ("The ceremony where knighthoods and honours are handed out", "Investiture", ["Induction", "Ordination", "Graduation"]),
 ("The royal family's surname since 1917", "Windsor", ["Saxe-Coburg", "Hanover", "Stuart"]),
 ("The royal castle on Deeside in Scotland", "Balmoral", ["Holyrood", "Glamis", "Scone"]),
 ("The Norfolk estate where the royals spend Christmas", "Sandringham", ["Highgrove", "Osborne", "Frogmore"]),
 ("The palace with the balcony where the royals wave", "Buckingham Palace", ["Kensington Palace", "Hampton Court", "Blenheim Palace"]),
 ("The little bob a woman makes when meeting the King", "Curtsy", ["Salute", "Bow", "Wave"]),
 ("How you first address the King", "Your Majesty", ["Your Highness", "Your Grace", "Your Excellency"]),
 ("The heir is usually made Prince of where?", "Wales", ["York", "Kent", "Edinburgh"]),
 ("A noblewoman who attends the Queen", "Lady-in-waiting", ["Governess", "Matron", "Housekeeper"]),
 ("The June parade for the monarch's official birthday", "Trooping the Colour", ["Changing of the Guard", "Beating Retreat", "State Opening"]),
 ("A monarch's daughter", "Princess", ["Duchess", "Countess", "Marchioness"]),
 ("The title of a reigning king's wife", "Queen consort", ["Queen regnant", "Queen mother", "Dowager"]),
 ("A country with an elected head of state instead of a monarch", "Republic", ["Dominion", "Duchy", "Principality"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-183.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
