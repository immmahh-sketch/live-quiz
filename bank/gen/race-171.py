# Bank session 11 Oct 2026: 3 more general races -> bank/race-171.json (rowing, fencing and lifeboat words). 20 rows each, target 10; wrong options are
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

race("what's this rowing word?", "Sport", "medium", ["rowing", "boats", "words"], [
 ("The long pole with a blade, pulled through the water", "Oar", ["Paddle", "Rudder", "Mast"]),
 ("The small person who steers and shouts the orders", "Cox", ["Coach", "Bosun", "Purser"]),
 ("The rower nearest the stern, who sets the rhythm", "Stroke", ["Purser", "Bosun", "Lookout"]),
 ("The rower nearest the front of the boat", "Bow", ["Purser", "Bosun", "Lookout"]),
 ("Rowing with an oar in each hand", "Sculls", ["Sweep", "Paddles", "Punts"]),
 ("The boat with eight rowers and a cox", "Eight", ["Four", "Pair", "Single"]),
 ("Oxford against Cambridge on the Thames every spring", "Boat Race", ["Henley Regatta", "Head of the River", "Doggett's Coat and Badge"]),
 ("Royal ___ Regatta, every summer on the Thames", "Henley", ["Hampton", "Marlow", "Windsor"]),
 ("The indoor rowing machine", "Erg", ["Treadmill", "Stepper", "Spinner"]),
 ("Getting your oar stuck in the water by mistake", "Catch a crab", ["Catch a cold", "Catch a wave", "Catch a tan"]),
 ("The five-time Olympic champion", "Steve Redgrave", ["Matthew Pinsent", "James Cracknell", "Andy Holmes"]),
 ("The fitting that holds the oar on the boat", "Rowlock", ["Padlock", "Deadlock", "Wedlock"]),
 ("The flat end of the oar", "Blade", ["Fin", "Rudder", "Keel"]),
 ("What the rower sits on, rolling back and forth", "Sliding seat", ["Swivel chair", "Bench", "Saddle"]),
 ("Tipping the boat right over", "Capsize", ["Scuttle", "Moor", "Dock"]),
 ("A series of boat races", "Regatta", ["Rally", "Grand Prix", "Derby"]),
 ("What an Oxford or Cambridge rower earns for racing", "Blue", ["Cap", "Badge", "Medal"]),
 ("A boat with no one steering", "Coxless", ["Captainless", "Crewless", "Oarless"]),
 ("Turning the blade flat between strokes", "Feathering", ["Featherbedding", "Tarring", "Fledging"]),
 ("Another name for an oarsman or oarswoman", "Rower", ["Rambler", "Rover", "Roamer"])])

race("what's this fencing word?", "Sport", "medium", ["fencing", "swords", "words"], [
 ("The light weapon where only the torso scores", "Foil", ["Rapier", "Cutlass", "Scimitar"]),
 ("The heaviest weapon, where the whole body is a target", "Épée", ["Rapier", "Cutlass", "Scimitar"]),
 ("The weapon that scores with cuts as well as thrusts", "Sabre", ["Rapier", "Cutlass", "Scimitar"]),
 ("'On guard!' – the call to get ready", "En garde", ["Bon voyage", "Voilà", "Au revoir"]),
 ("French for 'touched', said when you're hit", "Touché", ["Bon voyage", "Voilà", "Encore"]),
 ("A long attacking step forward", "Lunge", ["Squat", "Leapfrog", "Pirouette"]),
 ("Blocking your opponent's blade", "Parry", ["Tackle", "Volley", "Smash"]),
 ("A counter-attack straight after a parry", "Riposte", ["Rebuttal", "Reprise", "Encore"]),
 ("The long narrow strip you fence on", "Piste", ["Rink", "Mat", "Lane"]),
 ("The mesh face guard", "Mask", ["Visor", "Goggles", "Balaclava"]),
 ("The metallic jacket that registers hits", "Lamé", ["Lycra", "Tweed", "Velvet"]),
 ("A single fencing match", "Bout", ["Rally", "Frame", "Heat"]),
 ("Raising the sword to your opponent before you start", "Salute", ["Wave", "Curtsey", "High five"]),
 ("A running attack, French for 'arrow'", "Flèche", ["Flair", "Fleece", "Flash"]),
 ("The tip of the blade", "Point", ["Pommel", "Hilt", "Grip"]),
 ("The dish-shaped shield protecting the hand", "Guard", ["Gauntlet", "Cuff", "Bracer"]),
 ("A scoring hit", "Touch", ["Goal", "Try", "Run"]),
 ("Athos, Porthos and Aramis", "Musketeers", ["Highwaymen", "Buccaneers", "Cavaliers"]),
 ("The masked swordsman who carves a Z", "Zorro", ["Robin Hood", "The Saint", "The Phantom"]),
 ("'Hello. My name is...' – the swordsman in The Princess Bride", "Inigo Montoya", ["Westley", "Captain Hook", "Errol Flynn"])])

race("what's this lifeboat word?", "Everyday life", "medium", ["RNLI", "sea rescue", "words"], [
 ("The lifeboat charity, by its initials", "RNLI", ["RSPB", "RNIB", "RAC"]),
 ("The skipper of a lifeboat", "Coxswain", ["Purser", "Bosun", "Pilot"]),
 ("The distress call meaning a life is in danger", "Mayday", ["Pan-pan", "Sécurité", "Over and out"]),
 ("The inflatable vest that keeps you afloat", "Lifejacket", ["Straitjacket", "Dinner jacket", "Flak jacket"]),
 ("A bright red light fired into the sky to show you're in trouble", "Flare", ["Firework", "Lantern", "Torch"]),
 ("The lighthouse keeper's daughter famous for an 1838 rescue", "Grace Darling", ["Florence Nightingale", "Edith Cavell", "Mary Seacole"]),
 ("The service that coordinates sea rescues, reached on 999", "Coastguard", ["Border Force", "Lifeguard", "Harbour master"]),
 ("The tall tower with a flashing lamp to warn ships", "Lighthouse", ["Windmill", "Watchtower", "Water tower"]),
 ("Sending the lifeboat out to sea", "Launch", ["Lunch", "Lurch", "Lounge"]),
 ("The ramp the lifeboat slides down into the sea", "Slipway", ["Gangway", "Runway", "Causeway"]),
 ("What most lifeboat crew are, unpaid", "Volunteers", ["Conscripts", "Mercenaries", "Contractors"]),
 ("The device that buzzes to call the crew out", "Pager", ["Fax", "Telex", "Walkie-talkie"]),
 ("The dangerous chilling of the body in cold water", "Hypothermia", ["Hyperthermia", "Hydrophobia", "Vertigo"]),
 ("Getting cut off on the sand by the incoming ___", "Tide", ["Wind", "Fog", "Current"]),
 ("The small, fast inflatable for rescues close to shore", "Inshore lifeboat", ["All-weather lifeboat", "Dinghy", "Jet ski"]),
 ("A hidden ridge that ships run aground on", "Sandbank", ["Sandcastle", "Sandpit", "Sandbag"]),
 ("Stuck fast on the bottom", "Aground", ["Adrift", "Ashore", "Abroad"]),
 ("What's left after a ship breaks up", "Shipwreck", ["Shipshape", "Shipyard", "Shipment"]),
 ("The cry when someone falls into the sea", "Man overboard", ["All aboard", "Land ahoy", "Anchors aweigh"]),
 ("The coastguard's flying rescue craft", "Helicopter", ["Hovercraft", "Seaplane", "Airship"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-171.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
