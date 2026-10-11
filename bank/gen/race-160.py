# Bank session 11 Oct 2026: 3 more general races -> bank/race-160.json (betting, radio and Viking words). 20 rows each, target 10; wrong options are
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

race("what's this betting word?", "Sport", "medium", ["betting", "horse racing", "words"], [
 ("The chances, like 5-1, that set your winnings", "Odds", ["Margins", "Ratios", "Rates"]),
 ("The money you put on the bet", "Stake", ["Payout", "Return", "Jackpot"]),
 ("The horse expected to win, with the shortest odds", "Favourite", ["Also-ran", "Non-starter", "Pacemaker"]),
 ("A long-odds runner nobody expects to win", "Outsider", ["Front-runner", "Pacemaker", "Non-starter"]),
 ("Odds of 1-1: you win as much as you staked", "Evens", ["Double", "Treble", "Forecast"]),
 ("When a runner's so likely to win you'd get back less than your stake in profit", "Odds-on", ["Double", "Treble", "Forecast"]),
 ("A bet split half on winning and half on finishing placed", "Each way", ["Double", "Treble", "Reverse forecast"]),
 ("One bet linking lots of selections that all have to win", "Accumulator", ["Patent", "Yankee", "Lucky 15"]),
 ("The person who takes your bet", "Bookie", ["Croupier", "Cashier", "Steward"]),
 ("Pool betting where all the stakes are shared among the winners", "Tote", ["Lottery", "Raffle", "Kitty"]),
 ("A bet with little chance but a big payout", "Long shot", ["Sure thing", "Dead cert", "Banker"]),
 ("Someone who hands out their selections", "Tipster", ["Steward", "Starter", "Clerk"]),
 ("Someone placing a bet", "Punter", ["Bidder", "Shopper", "Client"]),
 ("When the result has to be judged from a picture of the line", "Photo finish", ["Stewards' enquiry", "False start", "Walkover"]),
 ("Two runners crossing the line together, a tie", "Dead heat", ["Walkover", "False start", "Whitewash"]),
 ("A horse withdrawn before the race", "Non-runner", ["Faller", "Also-ran", "Pacemaker"]),
 ("The Aintree steeplechase that's Britain's biggest betting race", "Grand National", ["Derby", "Gold Cup", "St Leger"]),
 ("The weekly football coupon for predicting score draws", "Pools", ["Lotto", "Bingo", "Premium Bonds"]),
 ("Rub off the silver panel to see if you've won", "Scratchcard", ["Raffle ticket", "Bingo card", "Betting slip"]),
 ("The pub slot machine with spinning reels", "Fruit machine", ["Jukebox", "Pinball", "Cash machine"])])

race("what's this radio word?", "TV", "medium", ["radio", "BBC", "words"], [
 ("Plays the records and chats in between", "DJ", ["Roadie", "Usher", "Compère"]),
 ("A short, catchy tune that announces the station", "Jingle", ["Ringtone", "Anthem", "Lullaby"]),
 ("Listeners ring up to share their views live", "Phone-in", ["Sit-in", "Walk-in", "Drop-in"]),
 ("The number you tune to, like 97.6", "Frequency", ["Postcode", "Bandwidth", "Volume"]),
 ("The band most music stations broadcast on, in two letters", "FM", ["AM", "TV", "PA"]),
 ("Guests pick eight records to take to a remote island", "Desert Island Discs", ["Pick of the Pops", "In Our Time", "Gardeners' Question Time"]),
 ("The world's longest-running drama serial, set in Ambridge", "The Archers", ["Emmerdale", "Mrs Dale's Diary", "Coronation Street"]),
 ("Talk for sixty seconds without hesitation, repetition or deviation", "Just a Minute", ["The News Quiz", "The Unbelievable Truth", "Gardeners' Question Time"]),
 ("The comedy panel show with a game called Mornington Crescent", "I'm Sorry I Haven't a Clue", ["The News Quiz", "The Unbelievable Truth", "The Now Show"]),
 ("The late-night bulletin listing Dogger, Fisher and German Bight", "Shipping Forecast", ["Sailing By", "Farming Today", "The News"]),
 ("Six short beeps marking the hour", "The pips", ["The bongs", "The chimes", "The bleeps"]),
 ("Unlicensed stations broadcasting from ships in the 1960s", "Pirate radio", ["Hospital radio", "Community radio", "Talk radio"]),
 ("The most famous of those offshore pirate stations", "Radio Caroline", ["Radio Luxembourg", "Capital Radio", "Radio City"]),
 ("Radio 4's flagship morning news programme", "Today", ["PM", "The World at One", "Front Row"]),
 ("What the presenter speaks into", "Microphone", ["Megaphone", "Gramophone", "Headphones"]),
 ("Silence when nothing's being broadcast", "Dead air", ["Hot air", "Fresh air", "Thin air"]),
 ("What the red light in the studio means", "On air", ["Off air", "On hold", "On call"]),
 ("The old-fashioned word for a radio", "Wireless", ["Gramophone", "Telegraph", "Phonograph"]),
 ("The Italian who pioneered radio", "Marconi", ["Edison", "Baird", "Bell"]),
 ("A song a listener asks the DJ to play", "Request", ["Encore", "Medley", "Remix"])])

race("what's this Viking word?", "History", "medium", ["Vikings", "Norse", "words"], [
 ("The Vikings' long, narrow ship with oars and a square sail", "Longship", ["Galleon", "Trireme", "Junk"]),
 ("The holy island raided in 793, the start of the Viking Age in England", "Lindisfarne", ["Iona", "Skye", "Anglesey"]),
 ("The Viking name for York", "Jorvik", ["Eboracum", "Lundenwic", "Camulodunum"]),
 ("The part of England ruled under Viking law", "Danelaw", ["Wessex", "Cornwall", "Strathclyde"]),
 ("The great hall where warriors who die in battle feast", "Valhalla", ["Asgard", "Midgard", "Olympus"]),
 ("The one-eyed chief of the Norse gods", "Odin", ["Tyr", "Baldr", "Heimdall"]),
 ("The god of thunder", "Thor", ["Tyr", "Baldr", "Freyr"]),
 ("The shape-shifting trickster god", "Loki", ["Baldr", "Heimdall", "Freyr"]),
 ("Thor's hammer", "Mjölnir", ["Gungnir", "Excalibur", "Durendal"]),
 ("A Viking warrior who fought in a wild trance", "Berserker", ["Housecarl", "Thane", "Squire"]),
 ("A letter of the old Viking alphabet", "Rune", ["Hieroglyph", "Cuneiform", "Ogham"]),
 ("A long Old Norse story of heroes and families", "Saga", ["Sonnet", "Ballad", "Fable"]),
 ("The Viking who founded the first settlement in Greenland", "Erik the Red", ["Harald Hardrada", "Ivar the Boneless", "Sweyn Forkbeard"]),
 ("His son, who reached North America around the year 1000", "Leif Erikson", ["Harald Hardrada", "Ragnar Lothbrok", "Sweyn Forkbeard"]),
 ("The 1066 battle where King Harold beat Harald Hardrada", "Stamford Bridge", ["Hastings", "Fulford", "Maldon"]),
 ("The Viking king of England who supposedly ordered back the tide", "Cnut", ["Æthelred", "Edgar", "Athelstan"]),
 ("The Wessex king who burned the cakes while fighting the Danes", "Alfred the Great", ["Æthelred", "Edgar", "Athelstan"]),
 ("The Shetland fire festival where a Viking galley is burned", "Up Helly Aa", ["Hogmanay", "Beltane", "Burns Night"]),
 ("What Vikings almost certainly did NOT wear into battle", "Horned helmets", ["Chain mail", "Round shields", "Woollen cloaks"]),
 ("A Viking assembly where laws were made, and a word we still use for an object", "Thing", ["Moot", "Witan", "Senate"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-160.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
