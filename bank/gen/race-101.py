# Bank session 10 Oct 2026: 2 more general races -> bank/race-101.json (cakes and biscuits, dances). 20 rows each, target 10; wrong options are
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

race("which cake or biscuit is this?", "Food and drink", "easy", ["cakes", "biscuits", "baking"], [
 ("Pink and yellow chequered sponge wrapped in marzipan", "Battenberg", ["Madeira cake", "Angel cake", "Genoa cake"]),
 ("Two sponges sandwiched with jam, named after a queen", "Victoria sponge", ["Madeira cake", "Genoa cake", "Angel cake"]),
 ("Almond tart with jam, iced and topped with a cherry, from Derbyshire", "Bakewell tart", ["Treacle tart", "Custard tart", "Manchester tart"]),
 ("Flaky pastry round packed with currants, from near Manchester", "Eccles cake", ["Chorley cake", "Banbury cake", "Welsh cake"]),
 ("Orange jelly on sponge under chocolate, legally a cake", "Jaffa Cake", ["Wagon Wheel", "Penguin", "Club"]),
 ("Oblong chocolate biscuits sandwiching chocolate cream", "Bourbon", ["Party Ring", "Malted milk", "Fig roll"]),
 ("The 'squashed fly' biscuit, full of currants", "Garibaldi", ["Fig roll", "Malted milk", "Lincoln"]),
 ("Two shortbreads with a jam heart showing through", "Jammie Dodger", ["Viennese whirl", "Party Ring", "Lincoln"]),
 ("Oaty biscuit: 'one nibble and you're nobbled'", "Hobnob", ["Flapjack", "Ginger nut", "Lincoln"]),
 ("Semi-sweet wholemeal biscuit, often coated in chocolate", "Digestive", ["Rich Tea", "Malted milk", "Ginger nut"]),
 ("Sticky Yorkshire gingerbread with oatmeal and treacle, eaten on Bonfire Night", "Parkin", ["Flapjack", "Lardy cake", "Gingerbread"]),
 ("Thin sponge rolled into a spiral round jam", "Swiss roll", ["Jam roly-poly", "Arctic roll", "Yule log"]),
 ("Fruit cake topped with rings of whole almonds", "Dundee cake", ["Madeira cake", "Christmas cake", "Lardy cake"]),
 ("Easter fruit cake with eleven marzipan balls on top", "Simnel cake", ["Christmas cake", "Genoa cake", "Madeira cake"]),
 ("Sticky square spiral bun with currants, named after a part of London", "Chelsea bun", ["Bath bun", "Belgian bun", "Hot cross bun"]),
 ("Banana, toffee and cream on a biscuit base, invented in Sussex", "Banoffee pie", ["Key lime pie", "Cheesecake", "Mississippi mud pie"]),
 ("Marshmallow dome in chocolate on a biscuit, made in Scotland", "Tunnock's teacake", ["Wagon Wheel", "Snowball", "Penguin"]),
 ("Vanilla cream between two patterned biscuits", "Custard cream", ["Malted milk", "Lincoln", "Party Ring"]),
 ("Scottish butter biscuit, often cut into fingers or petticoat tails", "Shortbread", ["Oatcake", "Flapjack", "Ginger nut"]),
 ("Chewy dark loaf you slice and butter, made famous by Soreen", "Malt loaf", ["Tea loaf", "Banana bread", "Lardy cake"])])

race("which dance is this?", "Music", "easy", ["dancing", "Strictly"], [
 ("Ballroom dance named after the music-hall star Harry Fox", "Foxtrot", ["Viennese waltz", "Tango", "Mambo"]),
 ("1920s flapper dance named after a South Carolina city", "Charleston", ["Shimmy", "Black Bottom", "Mambo"]),
 ("Dramatic ballroom dance acting out a bullfight", "Paso doble", ["Tango", "Samba", "Mambo"]),
 ("Cuban 'dance of love', the slowest Latin dance on Strictly", "Rumba", ["Samba", "Salsa", "Bossa nova"]),
 ("Latin dance named after the shuffling sound of its steps", "Cha-cha-cha", ["Mambo", "Samba", "Bossa nova"]),
 ("Fast ballroom dance full of hops and runs, done in hold", "Quickstep", ["Viennese waltz", "Polka", "Tango"]),
 ("Rock 'n' roll Latin dance with lots of kicks and flicks", "Jive", ["Shimmy", "Bop", "Hustle"]),
 ("1996 line dance with hands on hips, head and bum", "Macarena", ["The Ketchup Song", "Saturday Night", "Mambo No. 5"]),
 ("A long party line, each holding the hips of the person in front", "Conga", ["Hustle", "Mambo", "Shimmy"]),
 ("How low can you go? Bending back under a pole", "Limbo", ["Shimmy", "Bop", "Worm"]),
 ("Michael Jackson's backwards glide", "Moonwalk", ["Running man", "Robot", "Worm"]),
 ("The 1989 'forbidden dance' hit by Kaoma", "Lambada", ["Bossa nova", "Mambo", "Salsa"]),
 ("Chubby Checker's 1960 craze: swivel your hips like drying off with a towel", "The Twist", ["Mashed Potato", "Hustle", "Shimmy"]),
 ("Madonna's 1990 dance of striking magazine-cover poses", "Vogue", ["Robot", "Dab", "Running man"]),
 ("Swinging your arms behind and in front of your hips, made famous by Fortnite", "The Floss", ["Dab", "Running man", "Worm"]),
 ("'You put your left leg in, your left leg out'", "Hokey cokey", ["Bunny hop", "Locomotion", "Hustle"]),
 ("Swing dance born in 1920s Harlem, named after Charles Lindbergh's flight", "Lindy hop", ["Shimmy", "Black Bottom", "Bop"]),
 ("Psy's horse-riding dance from 2012", "Gangnam Style", ["Dab", "Running man", "Robot"]),
 ("Arms spelling out four letters, from the Village People", "YMCA", ["Locomotion", "Bunny hop", "Hustle"]),
 ("'It's just a jump to the left, and then a step to the right'", "Time Warp", ["Locomotion", "Bunny hop", "Hustle"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-101.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
