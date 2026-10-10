# Bank session 10 Oct 2026: 3 more general races -> bank/race-149.json (phone words, cleaning words, railway words). 20 rows each, target 10; wrong options are
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

race("what's this phone word?", "Computers and the internet", "easy", ["phones", "mobiles", "words"], [
 ("The tune your mobile plays when someone calls", "Ringtone", ["Dial tone", "Hold music", "Engaged tone"]),
 ("Where callers leave a message when you don't pick up", "Voicemail", ["Telex", "Telegram", "Fax"]),
 ("A short written message sent from one phone to another", "Text message", ["Fax", "Telex", "Morse code"]),
 ("The tiny chip that links your phone to your network", "SIM card", ["Fax", "Dial tone", "Extension"]),
 ("Switches off calls and data so you can use the phone on a flight", "Airplane mode", ["Party line", "Hold music", "Extension"]),
 ("Lets everyone in the room hear the call", "Speakerphone", ["Party line", "Extension", "Answerphone"]),
 ("The list of names and numbers saved in your phone", "Contacts", ["Switchboard", "Operator", "Directory enquiries"]),
 ("Changes 'teh' to 'the', and sometimes something far worse", "Autocorrect", ["Morse code", "Telex", "Dial tone"]),
 ("A display you tap and swipe with your finger", "Touchscreen", ["Rotary dial", "Pager", "Telex"]),
 ("A mobile that folds shut, like a clam", "Flip phone", ["Walkie-talkie", "Pager", "Payphone"]),
 ("A code or fingerprint you need to get into the phone", "Screen lock", ["Extension", "Dial tone", "Hold music"]),
 ("A pole to hold your phone further out than your arm can reach", "Selfie stick", ["Walkie-talkie", "Pager", "Aerial"]),
 ("Using your phone abroad on a foreign network", "Roaming", ["Reverse charges", "Party line", "Directory enquiries"]),
 ("Topping up credit instead of having a contract", "Pay as you go", ["Reverse charges", "Party line", "Hold music"]),
 ("Talking without holding the phone, as when you're driving", "Hands-free", ["Party line", "Extension", "Hold music"]),
 ("Seeing each other's faces on screen while you talk", "Video call", ["Party line", "Telex", "Telegram"]),
 ("Guesses the next word before you've typed it", "Predictive text", ["Morse code", "Telex", "Shorthand"]),
 ("A call you didn't answer in time", "Missed call", ["Reverse charges", "Dial tone", "Engaged tone"]),
 ("One conversation shared between lots of friends", "Group chat", ["Party line", "Switchboard", "Telex"]),
 ("The bars at the top of the screen show how strong this is", "Signal", ["Dial tone", "Hold music", "Extension"])])

race("what's this cleaning word?", "Everyday life", "easy", ["cleaning", "home", "words"], [
 ("A soft cloth for wiping the shelves", "Duster", ["Sandpaper", "Emery board", "Spatula"]),
 ("The British name for a vacuum cleaner, after an American brand", "Hoover", ["Kenwood", "Teasmade", "Breville"]),
 ("A stick with a shaggy head for washing the floor", "Mop", ["Whisk", "Ladle", "Trowel"]),
 ("A rubber blade for wiping water off windows", "Squeegee", ["Spatula", "Trowel", "Paintbrush"]),
 ("A fluffy stick for flicking dust off high places", "Feather duster", ["Paintbrush", "Whisk", "Ladle"]),
 ("Sweep the crumbs up with this pair", "Dustpan and brush", ["Pestle and mortar", "Salt and pepper", "Knife and fork"]),
 ("A strong chemical that kills germs and whitens", "Bleach", ["Turpentine", "Talc", "Hairspray"]),
 ("Rubbed on furniture or shoes to make them shine", "Polish", ["Turpentine", "Talc", "Hairspray"]),
 ("Clears the chalky crust from kettles and taps", "Limescale remover", ["Turpentine", "Talc", "Hairspray"]),
 ("A rough pad for scrubbing burnt pans", "Scourer", ["Emery board", "Sandpaper", "Grater"]),
 ("Yellow rubber gloves for the washing-up", "Marigolds", ["Oven gloves", "Mittens", "Gauntlets"]),
 ("A soft leather cloth for drying the car", "Chamois", ["Emery board", "Sandpaper", "Paintbrush"]),
 ("Blasts hot vapour at grubby carpets and grout", "Steam cleaner", ["Kenwood", "Teasmade", "Breville"]),
 ("A top-to-bottom clean of the whole house, traditionally as the weather warms up", "Spring clean", ["Car boot sale", "Bring and buy", "Jumble sale"]),
 ("Squeezed into the sink to wash the dishes", "Washing-up liquid", ["Turpentine", "Talc", "Hairspray"]),
 ("Goes in the washing machine to make clothes soft", "Fabric conditioner", ["Turpentine", "Talc", "Hairspray"]),
 ("A sticky roller for picking fluff off clothes", "Lint roller", ["Rolling pin", "Paint roller", "Grater"]),
 ("A black plastic sack for rubbish", "Bin bag", ["Carrier bag", "Bag for life", "Freezer bag"]),
 ("A wicker paddle for whacking the dust out of rugs on the line", "Carpet beater", ["Rolling pin", "Ladle", "Fly swatter"]),
 ("A rubber cup on a stick for clearing a blocked loo", "Plunger", ["Ladle", "Whisk", "Trowel"])])

race("what's this railway word?", "Travel", "medium", ["trains", "railways", "words"], [
 ("Where you stand to wait for the train", "Platform", ["Quay", "Berth", "Kerb"]),
 ("The big springy stops at the very end of the line", "Buffers", ["Kerb", "Bollard", "Speed bump"]),
 ("A trackside cabin where the signals and points are worked", "Signal box", ["Control tower", "Toll booth", "Sentry box"]),
 ("Where a road crosses the railway, with barriers that come down", "Level crossing", ["Roundabout", "Box junction", "Slip road"]),
 ("One of the wooden or concrete beams the rails sit on", "Sleeper", ["Kerb", "Joist", "Girder"]),
 ("Moving rails that switch a train from one track to another", "Points", ["Roundabout", "Slip road", "Filter lane"]),
 ("The member of staff who checks the doors and blows the whistle", "Guard", ["Steward", "Purser", "Porter"]),
 ("The list of when every train arrives and leaves", "Timetable", ["Manifest", "Logbook", "Ledger"]),
 ("Pay once for a whole year of commuting", "Season ticket", ["Boarding pass", "Passport", "Visa"]),
 ("Cheaper travel outside the busy rush hours", "Off-peak", ["Red-eye", "Standby", "Happy hour"]),
 ("A ticket there and back again", "Return", ["Single", "Standby", "Boarding pass"]),
 ("One of the coaches that make up the train", "Carriage", ["Cabin", "Deck", "Hold"]),
 ("Where you buy a tea and a sandwich on board", "Buffet car", ["Galley", "Mess", "Canteen"]),
 ("Where phone calls and loud music are frowned on", "Quiet coach", ["Departure lounge", "Hold", "Galley"]),
 ("Gets you a third off fares if you're young, older or travelling as a family", "Railcard", ["Boarding pass", "Passport", "Loyalty card"]),
 ("Gates that open when you feed in your ticket", "Ticket barrier", ["Security scanner", "Toll booth", "Revolving door"]),
 ("Lets you cross over the tracks to the other platform", "Footbridge", ["Gangway", "Jetty", "Pier"]),
 ("Where two or more lines meet", "Junction", ["Terminus", "Quay", "Lay-by"]),
 ("A short side track where trains are parked", "Siding", ["Lay-by", "Hard shoulder", "Berth"]),
 ("A long bridge of arches carrying the railway over a valley", "Viaduct", ["Aqueduct", "Causeway", "Pier"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-149.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
