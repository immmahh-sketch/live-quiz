# Bank session 10 Oct 2026: 2 more general races -> bank/race-126.json (parts of a car, internet words). 20 rows each, target 10; wrong options are
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


race("which part of a car is this?", "Cars and motoring", "medium", ["cars", "motoring"], [
 ("Holds the cogs that let you go from first gear to fifth", "Gearbox", ["Differential", "Crankshaft", "Drive shaft"]),
 ("The left-hand pedal you press to change gear", "Clutch", ["Brake pad", "Starter motor", "Differential"]),
 ("Carries burnt gases away from the engine and out at the back", "Exhaust", ["Fuel injector", "Sump", "Air filter"]),
 ("Keeps the engine cool by passing hot water through thin fins at the front", "Radiator", ["Thermostat", "Water pump", "Oil filter"]),
 ("Driven by the engine, it charges the battery while you drive", "Alternator", ["Starter motor", "Distributor", "Turbocharger"]),
 ("Makes the tiny flash that lights the petrol in each cylinder", "Spark plug", ["Fuel injector", "Piston", "Gasket"]),
 ("Pull it out and wipe it to check the oil level", "Dipstick", ["Fuel gauge", "Oil filter", "Sump"]),
 ("A lever you pull up to stop the parked car rolling away", "Handbrake", ["Gear stick", "Brake pad", "Tie rod"]),
 ("Cleans up the exhaust fumes, and is often stolen for its precious metals", "Catalytic converter", ["Turbocharger", "Oil filter", "Air filter"]),
 ("A rubber loop that drives the alternator; a pair of tights can stand in for it in an emergency", "Fan belt", ["Drive shaft", "Tie rod", "Gasket"]),
 ("The lid over the engine at the front; Americans call it the hood", "Bonnet", ["Tailgate", "Grille", "Wheel arch"]),
 ("Where the luggage goes; Americans call it the trunk", "Boot", ["Glovebox", "Footwell", "Sump"]),
 ("The dial that shows how fast you're going", "Speedometer", ["Odometer", "Fuel gauge", "Tachograph"]),
 ("The dial showing how fast the engine is turning, in thousands per minute", "Rev counter", ["Odometer", "Fuel gauge", "Tachograph"]),
 ("Sticks out from the side so you can see what's behind and beside you", "Wing mirror", ["Fog light", "Mud flap", "Wheel arch"]),
 ("A shiny cover over the middle of the wheel, easily lost on a kerb", "Hubcap", ["Wheel arch", "Mud flap", "Brake disc"]),
 ("Sweeps the rain off the glass in front of you", "Windscreen wiper", ["Sunroof", "Fog light", "Grille"]),
 ("Bursts out of the steering wheel in a crash", "Airbag", ["Crumple zone", "Roll cage", "Bumper"]),
 ("Part of the suspension that stops the car bouncing after a bump", "Shock absorber", ["Wishbone", "Anti-roll bar", "Tie rod"]),
 ("Blinks orange to show which way you're turning", "Indicator", ["Fog light", "Brake light", "Reversing light"])])

race("what's this internet word?", "Computers and the internet", "medium", ["internet", "social media", "words"], [
 ("Junk email you never asked for, named after a tinned meat", "Spam", ["Pop-up", "Bot", "Thread"]),
 ("A fake email pretending to be your bank, fishing for your password", "Phishing", ["Doxxing", "Lurking", "Torrent"]),
 ("A small file a website leaves on your computer to remember you", "Cookie", ["Pixel", "Widget", "Plug-in"]),
 ("A barrier that blocks unwanted traffic from reaching your computer", "Firewall", ["Router", "Encryption", "Server"]),
 ("The program you look at websites with, like Chrome or Safari", "Browser", ["Server", "Domain", "Router"]),
 ("Any software written to damage or spy on your computer", "Malware", ["Firmware", "Widget", "Plug-in"]),
 ("The # symbol used to tag a topic on social media", "Hashtag", ["Thread", "Feed", "Story"]),
 ("A little picture like a smiley face or a thumbs-up, sent in a message", "Emoji", ["Pixel", "Filter", "Widget"]),
 ("A funny picture or idea copied and passed around online, often with new captions", "Meme", ["Thread", "Story", "Screenshot"]),
 ("Someone who posts nasty things just to start arguments", "Troll", ["Lurker", "Newbie", "Bot"]),
 ("The little picture or character that stands for you online", "Avatar", ["Filter", "Pixel", "Widget"]),
 ("A test of wobbly letters or traffic lights to prove you're not a robot", "Captcha", ["Encryption", "Ping", "Pop-up"]),
 ("An audio show you download or stream, often a chat about one topic", "Podcast", ["Vlog", "Webinar", "Livestream"]),
 ("An online diary of written posts", "Blog", ["Thread", "Feed", "Wiki"]),
 ("A photo you take of yourself, often at arm's length", "Selfie", ["Screenshot", "Filter", "Story"]),
 ("Someone who uses a fake identity online to trick people into a relationship", "Catfish", ["Lurker", "Newbie", "Doxxer"]),
 ("A tempting headline written just to make you click: 'You won't believe what happened next'", "Clickbait", ["Pop-up", "Hyperlink", "Spoiler"]),
 ("Someone paid by brands to show products to their many followers", "Influencer", ["Lurker", "Newbie", "Moderator"]),
 ("What a video has 'gone' when millions share it within days", "Viral", ["Live", "Offline", "Encrypted"]),
 ("Suddenly cutting off all contact with someone, without a word", "Ghosting", ["Benching", "Breadcrumbing", "Orbiting"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-126.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
