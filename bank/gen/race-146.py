# Bank session 10 Oct 2026: 3 more general races -> bank/race-146.json (Halloween words, science lab kit, circus words). 20 rows each, target 10; wrong options are
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

race("what's this Halloween word?", "Halloween", "easy", ["Halloween", "spooky", "words"], [
 ("A hollowed-out pumpkin with a carved face and a candle inside", "Jack-o'-lantern", ["Will-o'-the-wisp", "Crystal ball", "Scarecrow"]),
 ("What children say at your door on 31 October", "Trick or treat", ["Penny for the guy", "Wassail", "Knock down ginger"]),
 ("What a witch flies on", "Broomstick", ["Wand", "Pendulum", "Crystal ball"]),
 ("A witch's big black pot for brewing potions", "Cauldron", ["Pendulum", "Crystal ball", "Wand"]),
 ("Said to be bad luck if it crosses your path", "Black cat", ["Toad", "Owl", "Newt"]),
 ("A monster that robs graves to feed on the dead", "Ghoul", ["Poltergeist", "Wraith", "Imp"]),
 ("An Irish spirit whose wail warns of a death", "Banshee", ["Kelpie", "Changeling", "Poltergeist"]),
 ("Turns into a wolf at the full moon", "Werewolf", ["Wendigo", "Golem", "Gorgon"]),
 ("Drinks blood and hates garlic", "Vampire", ["Wendigo", "Golem", "Gorgon"]),
 ("The walking dead, hungry for brains", "Zombie", ["Golem", "Gorgon", "Harpy"]),
 ("An ancient Egyptian body wrapped in bandages", "Mummy", ["Golem", "Gorgon", "Harpy"]),
 ("All bones and no flesh", "Skeleton", ["Spectre", "Wraith", "Imp"]),
 ("Dusty threads hanging in every corner of a haunted house", "Cobweb", ["Scarecrow", "Gargoyle", "Pendulum"]),
 ("Hangs upside down and flies out at night", "Bat", ["Raven", "Owl", "Toad"]),
 ("Trying to catch fruit floating in water using only your teeth", "Apple bobbing", ["Snapdragon", "Conkers", "Egg rolling"]),
 ("The Scottish name for going door to door in costume", "Guising", ["Wassailing", "Mumming", "First-footing"]),
 ("The old Celtic festival Halloween grew out of", "Samhain", ["Beltane", "Imbolc", "Lughnasadh"]),
 ("The old name for Halloween, the night before All Saints' Day", "All Hallows' Eve", ["Walpurgis Night", "Twelfth Night", "Bonfire Night"]),
 ("Mexico's festival of skulls and marigolds for loved ones who have died", "Day of the Dead", ["Walpurgis Night", "Holi", "Diwali"]),
 ("A board of letters that a glass slides across to spell out messages from spirits", "Ouija board", ["Tarot", "Crystal ball", "Pendulum"])])

race("what's this bit of science lab kit?", "Science", "medium", ["science", "school", "laboratory"], [
 ("A gas flame on a tube, with an air hole to make it roar blue", "Bunsen burner", ["Condenser", "Centrifuge", "Desiccator"]),
 ("A thin glass tube with a rounded bottom", "Test tube", ["Condenser", "Watch glass", "Volumetric flask"]),
 ("Sucks up and lets out tiny measured amounts of liquid", "Pipette", ["Condenser", "Centrifuge", "Balance"]),
 ("A glass cup with a lip for pouring", "Beaker", ["Volumetric flask", "Watch glass", "Round-bottomed flask"]),
 ("A flask with a wide flat base and a narrow neck, good for swirling", "Conical flask", ["Round-bottomed flask", "Volumetric flask", "Watch glass"]),
 ("A shallow round dish for growing bacteria", "Petri dish", ["Watch glass", "Mortar and pestle", "Desiccator"]),
 ("Magnifies cells too small to see", "Microscope", ["Centrifuge", "Desiccator", "Balance"]),
 ("Protect your eyes from splashes", "Goggles", ["Gloves", "Apron", "Clamp"]),
 ("A three-legged stand to rest things on over the flame", "Tripod", ["Clamp", "Retort stand", "Boss"]),
 ("Wire mesh laid on the tripod to spread out the heat", "Gauze", ["Filter paper", "Splint", "Watch glass"]),
 ("Turns red in acid and blue in alkali", "Litmus paper", ["Filter paper", "Splint", "Agar"]),
 ("A cone for pouring liquid into a narrow neck", "Funnel", ["Condenser", "Clamp", "Splint"]),
 ("A tall, narrow jug with a scale up the side for measuring liquid", "Measuring cylinder", ["Condenser", "Watch glass", "Desiccator"]),
 ("A little flat scoop for moving powders", "Spatula", ["Splint", "Clamp", "Boss"]),
 ("Grip hot things so you don't burn your fingers", "Tongs", ["Splint", "Boss", "Watch glass"]),
 ("A small heat-proof pot for heating solids to very high temperatures", "Crucible", ["Mortar and pestle", "Watch glass", "Desiccator"]),
 ("A shallow dish for heating a solution until only crystals are left", "Evaporating basin", ["Mortar and pestle", "Desiccator", "Centrifuge"]),
 ("A long tube with a tap at the bottom, used in titrations", "Burette", ["Condenser", "Centrifuge", "Balance"]),
 ("A glass-fronted cabinet that sucks away nasty gases", "Fume cupboard", ["Desiccator", "Centrifuge", "Incubator"]),
 ("A white overcoat that keeps chemicals off your clothes", "Lab coat", ["Hairnet", "Gloves", "Face mask"])])

race("what's this circus word?", "Everyday life", "easy", ["circus", "words"], [
 ("Top hat and tails, introducing every act", "Ringmaster", ["Ventriloquist", "Puppeteer", "Hypnotist"]),
 ("The huge striped tent", "Big top", ["Bandstand", "Pavilion", "Gazebo"]),
 ("A swinging bar high above the ring", "Trapeze", ["Springboard", "Seesaw", "Pommel horse"]),
 ("A wire you walk along, high in the air", "Tightrope", ["Bunting", "Zip wire", "Climbing rope"]),
 ("Keeps several balls in the air at once", "Juggler", ["Ventriloquist", "Escapologist", "Hypnotist"]),
 ("Red nose, baggy trousers and enormous shoes", "Clown", ["Mime", "Ventriloquist", "Escapologist"]),
 ("A bike with just one wheel", "Unicycle", ["Penny-farthing", "Tandem", "Recumbent"]),
 ("Long poles that make you walk tall", "Stilts", ["Pogo stick", "Space hopper", "Skateboard"]),
 ("Fired across the tent into a net", "Human cannonball", ["Stuntman", "Escapologist", "Ventriloquist"]),
 ("Faces big cats with a whip and a chair", "Lion tamer", ["Escapologist", "Puppeteer", "Hypnotist"]),
 ("Tumbles, flips and builds human pyramids", "Acrobat", ["Ventriloquist", "Puppeteer", "Hypnotist"]),
 ("Bends their body into impossible shapes", "Contortionist", ["Escapologist", "Ventriloquist", "Hypnotist"]),
 ("Puts flaming torches in their mouth", "Fire-eater", ["Escapologist", "Puppeteer", "Ventriloquist"]),
 ("Slides a long blade down their throat", "Sword swallower", ["Escapologist", "Puppeteer", "Hypnotist"]),
 ("Lifts enormous weights, often sporting a curly moustache", "Strongman", ["Escapologist", "Ventriloquist", "Puppeteer"]),
 ("Stretched below the high-wire act in case anyone falls", "Safety net", ["Bunting", "Sawdust", "Spotlight"]),
 ("Hurls blades at a spinning board with an assistant strapped to it", "Knife thrower", ["Escapologist", "Hypnotist", "Puppeteer"]),
 ("The round space in the middle where the acts perform", "Ring", ["Wings", "Pit", "Gallery"]),
 ("The thick make-up clowns wear", "Greasepaint", ["Sawdust", "Spotlight", "Drumroll"]),
 ("Splatted into a clown's face", "Custard pie", ["Trifle", "Jelly", "Blancmange"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-146.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
