# Bank session 10 Oct 2026: 2 more general races -> bank/race-119.json (retro sweets, nuts and seeds). 20 rows each, target 10; wrong options are
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

race("which classic sweet is this?", "Food and drink", "easy", ["sweets", "nostalgia"], [
 ("A liquorice stick dipped into sherbet in a paper tube", "Sherbet Fountain", ["Dip Dab", "Refreshers", "Fizzers"]),
 ("Black aniseed chews, four for a penny", "Black Jacks", ["Mojos", "Chewits", "Midget Gems"]),
 ("Raspberry-and-pineapple chews", "Fruit Salads", ["Refreshers", "Mojos", "Chewits"]),
 ("Rice-paper discs filled with sherbet", "Flying Saucers", ["Refreshers", "Fizzers", "Dip Dab"]),
 ("Purple, perfumed, flower-flavoured tablets", "Parma Violets", ["Refreshers", "Fizzers", "Midget Gems"]),
 ("Fizzy tablets with messages like 'Be Mine'", "Love Hearts", ["Refreshers", "Fizzers", "Dip Dab"]),
 ("A raspberry-and-milk lolly", "Drumstick", ["Chupa Chups", "Dip Dab", "Fab"]),
 ("A huge hard ball that changes colour as you suck it", "Gobstopper", ["Chupa Chups", "Bonbons", "Mint imperials"]),
 ("Boiled sweets that smell like nail varnish", "Pear drops", ["Barley sugar", "Mint imperials", "Bonbons"]),
 ("Tiny red-brown balls with a seed in the middle", "Aniseed balls", ["Bonbons", "Mint imperials", "Midget Gems"]),
 ("Pink and white foam sweets shaped like a sea creature", "Foam shrimps", ["Flumps", "Fried eggs", "Milk teeth"]),
 ("A fizzy chewy bar with a cartoon alien on the wrapper", "Wham bar", ["Fab", "Refreshers", "Chewits"]),
 ("Little jelly people", "Jelly babies", ["Jelly beans", "Midget Gems", "Wine gums"]),
 ("Tiny pastel fondants and jellies", "Dolly mixtures", ["Midget Gems", "Jelly tots", "Wine gums"]),
 ("Round liquorice discs stamped with a castle, from Yorkshire", "Pontefract cakes", ["Liquorice Allsorts", "Mojos", "Midget Gems"]),
 ("A powder that crackles and pops on your tongue", "Space Dust", ["Fizzers", "Dip Dab", "Refreshers"]),
 ("Lemon boiled sweets with a fizzy powder inside", "Sherbet lemons", ["Barley sugar", "Bonbons", "Mint imperials"]),
 ("Fizzy cola cubes dusted in sugar", "Cola cubes", ["Bonbons", "Barley sugar", "Mint imperials"]),
 ("Two-tone pink and yellow boiled sweets", "Rhubarb and custards", ["Barley sugar", "Bonbons", "Mint imperials"]),
 ("Chewy butter toffee from Scotland in tartan wrappers", "Highland toffee", ["Fudge", "Bonbons", "Chewits"])])

race("which nut or seed is this?", "Food and drink", "medium", ["nuts", "seeds", "food"], [
 ("Ground up to make marzipan", "Almond", ["Candlenut", "Shea nut", "Pili nut"]),
 ("Grows hanging below a fruit called an 'apple'", "Cashew", ["Shea nut", "Betel nut", "Candlenut"]),
 ("Green nut in a shell that splits open, turned into green ice cream", "Pistachio", ["Ginkgo nut", "Pili nut", "Candlenut"]),
 ("Big three-sided nut always left at the bottom of the Christmas tin", "Brazil nut", ["Pili nut", "Candlenut", "Shea nut"]),
 ("Round Australian nut with the hardest shell of all", "Macadamia", ["Candlenut", "Bunya nut", "Pili nut"]),
 ("Looks like a tiny brain", "Walnut", ["Pili nut", "Candlenut", "Ginkgo nut"]),
 ("The nut in Nutella and Ferrero Rocher", "Hazelnut", ["Pili nut", "Candlenut", "Ginkgo nut"]),
 ("Not a nut at all but a legume that grows underground", "Peanut", ["Lotus seed", "Ginkgo nut", "Betel nut"]),
 ("Star of a sticky American pie", "Pecan", ["Candlenut", "Pili nut", "Bunya nut"]),
 ("Roasted on an open fire at Christmas", "Chestnut", ["Ginkgo nut", "Pili nut", "Bunya nut"]),
 ("Hairy brown shell with milk inside", "Coconut", ["Pili nut", "Bunya nut", "Shea nut"]),
 ("Small cream seed from cones, blended into pesto", "Pine nut", ["Lotus seed", "Ginkgo nut", "Hemp seed"]),
 ("The fruit of the oak tree", "Acorn", ["Beechnut", "Ginkgo nut", "Bunya nut"]),
 ("Shiny brown seed of the horse chestnut, used in playground fights", "Conker", ["Beechnut", "Ginkgo nut", "Candlenut"]),
 ("Gave its name to a famous fizzy drink", "Kola nut", ["Betel nut", "Shea nut", "Candlenut"]),
 ("A little tuber blended into Spanish horchata", "Tiger nut", ["Lotus seed", "Betel nut", "Ginkgo nut"]),
 ("Crunchy white discs in Chinese stir-fries", "Water chestnut", ["Lotus seed", "Ginkgo nut", "Bamboo shoot"]),
 ("Ground into tahini", "Sesame seed", ["Poppy seed", "Linseed", "Hemp seed"]),
 ("Striped seed from a tall yellow flower", "Sunflower seed", ["Linseed", "Hemp seed", "Poppy seed"]),
 ("Green seed scooped out at Halloween", "Pumpkin seed", ["Linseed", "Hemp seed", "Poppy seed"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-119.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
