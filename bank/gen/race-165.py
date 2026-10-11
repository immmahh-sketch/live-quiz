# Bank session 11 Oct 2026: 3 more general races -> bank/race-165.json (woodwork, surfing and zoo words). 20 rows each, target 10; wrong options are
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

race("what's this woodwork word?", "Everyday life", "medium", ["woodwork", "carpentry", "words"], [
 ("A toothed blade for cutting wood", "Saw", ["Trowel", "Spanner", "Pliers"]),
 ("A flat blade tapped with a mallet to carve out wood", "Chisel", ["Trowel", "Spanner", "Wrench"]),
 ("Shaves thin curls off a wooden surface", "Plane", ["Trowel", "Pliers", "Wrench"]),
 ("A wooden hammer", "Mallet", ["Spanner", "Pliers", "Trowel"]),
 ("The pattern of lines running through the wood", "Grain", ["Weave", "Nap", "Seam"]),
 ("A dark, round mark where a branch once grew", "Knot", ["Blot", "Smudge", "Dent"]),
 ("A gritty sheet for smoothing", "Sandpaper", ["Wallpaper", "Tracing paper", "Greaseproof paper"]),
 ("An interlocking joint shaped like a bird's tail", "Dovetail", ["Butt joint", "Lap joint", "Biscuit joint"]),
 ("A joint where a tongue of wood fits into a slot", "Mortise and tenon", ["Butt joint", "Lap joint", "Biscuit joint"]),
 ("A joint cut at 45 degrees, like the corner of a picture frame", "Mitre", ["Butt joint", "Lap joint", "Biscuit joint"]),
 ("The powder left after cutting", "Sawdust", ["Stardust", "Talc", "Pumice"]),
 ("The bench clamp that holds the wood tight", "Vice", ["Anvil", "Easel", "Trestle"]),
 ("The machine that spins wood so you can turn bowls and table legs", "Lathe", ["Kiln", "Loom", "Forge"]),
 ("Board made of thin layers glued crossways", "Plywood", ["Chipboard", "Hardboard", "Veneer"]),
 ("Board made of pressed wood fibres, by its initials", "MDF", ["PVC", "DPC", "LED"]),
 ("White wood glue, by its initials", "PVA", ["PVC", "DPC", "LED"]),
 ("The strong hardwood of Tudor beams and wine barrels", "Oak", ["Pine", "Spruce", "Larch"]),
 ("The super-light wood used for model aeroplanes", "Balsa", ["Teak", "Mahogany", "Ebony"]),
 ("A woodworker who builds things on site", "Carpenter", ["Cooper", "Wheelwright", "Fletcher"]),
 ("Widening a screw hole so the head sits flush", "Countersink", ["Counterweight", "Counterfeit", "Countertop"])])

race("what's this surfing word?", "Sport", "medium", ["surfing", "beach", "words"], [
 ("A spectacular fall off the board", "Wipeout", ["Knockout", "Walkout", "Blackout"]),
 ("The hollow tube inside a breaking wave", "Barrel", ["Bucket", "Funnel", "Trough"]),
 ("Standing with all ten toes over the front of the board", "Hang ten", ["Count to ten", "High ten", "Top ten"]),
 ("The cord tying the board to your ankle", "Leash", ["Lasso", "Halter", "Reins"]),
 ("Rubbed on the deck for grip", "Wax", ["Polish", "Varnish", "Talc"]),
 ("The small blade under the tail that steers", "Fin", ["Rudder", "Keel", "Paddle"]),
 ("A board over nine feet long, for gentle waves", "Longboard", ["Skateboard", "Snowboard", "Kickboard"]),
 ("A short foam board ridden lying down", "Bodyboard", ["Skateboard", "Snowboard", "Kickboard"]),
 ("Rolling waves arriving from a distant storm", "Swell", ["Ripple", "Eddy", "Puddle"]),
 ("A strong channel of water dragging swimmers out to sea", "Rip current", ["Gulf Stream", "Jet stream", "Trade wind"]),
 ("Swimming your board out through the breaking waves", "Paddle out", ["Bail out", "Drop out", "Check out"]),
 ("Stealing a wave someone else is already riding", "Drop in", ["Drop off", "Drop kick", "Drop out"]),
 ("Riding with your right foot forward", "Goofy", ["Regular", "Natural", "Normal"]),
 ("Slang for a young surfer", "Grom", ["Dude", "Bro", "Rookie"]),
 ("Cornwall's surf capital, home of Fistral Beach", "Newquay", ["Padstow", "Falmouth", "Penzance"]),
 ("The Portuguese town with the biggest waves ever surfed", "Nazaré", ["Biarritz", "Malibu", "Bondi"]),
 ("Where modern surfing was born", "Hawaii", ["California", "Australia", "Portugal"]),
 ("The hand sign with the thumb and little finger out", "Shaka", ["Thumbs up", "V sign", "Peace sign"]),
 ("Slang for a clueless beginner who gets in the way", "Kook", ["Chump", "Muppet", "Plonker"]),
 ("Where surfers sit waiting for a wave", "Line-up", ["Queue", "Rank", "Huddle"])])

race("what's this zoo word?", "Animals", "easy", ["zoos", "animals", "words"], [
 ("The person who looks after the animals", "Zookeeper", ["Gamekeeper", "Shepherd", "Groom"]),
 ("An animal's fenced home at the zoo", "Enclosure", ["Kennel", "Stable", "Hutch"]),
 ("A building full of fish tanks", "Aquarium", ["Planetarium", "Conservatory", "Arboretum"]),
 ("A huge cage for birds", "Aviary", ["Apiary", "Dovecote", "Hatchery"]),
 ("Where the snakes and lizards are kept", "Reptile house", ["Bird hide", "Glasshouse", "Bat cave"]),
 ("Where children can stroke the goats and rabbits", "Petting zoo", ["Circus", "Kennels", "Pound"]),
 ("Drive round in your car while the animals roam", "Safari park", ["Theme park", "Car park", "Business park"]),
 ("When crowds gather to watch the penguins get their fish", "Feeding time", ["Closing time", "Opening time", "Tea time"]),
 ("A plan to help rare animals have young", "Breeding programme", ["Training course", "Exercise class", "Diet plan"]),
 ("At risk of dying out", "Endangered", ["Extinct", "Domesticated", "Invasive"]),
 ("An animal that eats only plants", "Herbivore", ["Insectivore", "Scavenger", "Predator"]),
 ("An animal that eats only meat", "Carnivore", ["Insectivore", "Scavenger", "Grazer"]),
 ("An animal that eats both plants and meat", "Omnivore", ["Insectivore", "Grazer", "Predator"]),
 ("The world's oldest scientific zoo, in Regent's Park", "London Zoo", ["Whipsnade", "Edinburgh Zoo", "Bristol Zoo"]),
 ("The UK's most visited zoo, in Cheshire", "Chester Zoo", ["Whipsnade", "Twycross", "Edinburgh Zoo"]),
 ("Edinburgh Zoo's black-and-white pair, Tian Tian and Yang Guang", "Giant pandas", ["Red pandas", "Sun bears", "Koalas"]),
 ("The biggest of the apes", "Gorilla", ["Orangutan", "Chimpanzee", "Baboon"]),
 ("When staff tell visitors about the animals", "Keeper talk", ["Pep talk", "Small talk", "Pillow talk"]),
 ("A dark building for animals that come out at night", "Nocturnal house", ["Night shelter", "Darkroom", "Lighthouse"]),
 ("Protecting animals and their habitats", "Conservation", ["Conversation", "Conservatory", "Constellation"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-165.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
