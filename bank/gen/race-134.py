# Bank session 10 Oct 2026: 2 more general races -> bank/race-134.json (cooking words, soups). 20 rows each, target 10; wrong options are
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


race("what's this cooking word?", "Food and drink", "medium", ["cooking", "kitchen", "words"], [
 ("Cook gently in barely simmering liquid, like an egg in water", "Poach", ["Render", "Temper", "Clarify"]),
 ("Brown meat, then cook it slowly in a little liquid in a covered pot", "Braise", ["Render", "Dredge", "Bard"]),
 ("Plunge vegetables into boiling water briefly, then straight into ice water", "Blanch", ["Temper", "Clarify", "Dredge"]),
 ("Fry quickly in a little fat, tossing the pan", "Sauté", ["Render", "Dredge", "Emulsify"]),
 ("Pour on brandy and set it alight", "Flambé", ["Temper", "Clarify", "Render"]),
 ("Spoon the cooking juices over meat while it roasts", "Baste", ["Bard", "Lard", "Dredge"]),
 ("Cut vegetables into thin matchsticks", "Julienne", ["Brunoise", "Chiffonade", "Mirepoix"]),
 ("Soak meat in a flavoured liquid before cooking it", "Marinate", ["Macerate", "Dredge", "Lard"]),
 ("Pour wine or stock into a hot pan to lift the browned bits off the bottom", "Deglaze", ["Clarify", "Emulsify", "Temper"]),
 ("Seal food in a bag and cook it in a precisely heated water bath", "Sous vide", ["En papillote", "Tempura", "Dredge"]),
 ("Toss small pieces over a very high heat in a wok", "Stir-fry", ["Tempura", "Dredge", "Render"]),
 ("Cook food in the vapour from boiling water", "Steam", ["Tempura", "Render", "Dredge"]),
 ("Cure or flavour food over smouldering wood chips", "Smoke", ["Render", "Clarify", "Temper"]),
 ("Cook duck legs slowly, submerged in their own fat", "Confit", ["Render", "Bard", "Lard"]),
 ("Preserve vegetables in vinegar", "Pickle", ["Macerate", "Clarify", "Emulsify"]),
 ("Boil a sauce down so it thickens and its flavour gets stronger", "Reduce", ["Clarify", "Emulsify", "Temper"]),
 ("Brown the outside of meat quickly over a very high heat", "Sear", ["Render", "Dredge", "Bard"]),
 ("Tie up a chicken with string so it keeps its shape while roasting", "Truss", ["Spatchcock", "Bard", "Lard"]),
 ("Cut the bones out of a fish", "Fillet", ["Spatchcock", "Score", "Dredge"]),
 ("Soak a turkey in salty water before roasting to keep it juicy", "Brine", ["Macerate", "Dredge", "Lard"])])

race("which soup is this?", "Food and drink", "medium", ["soup", "food", "world food"], [
 ("A cold Spanish tomato soup", "Gazpacho", ["Caldo verde", "Fabada", "Sopa de ajo"]),
 ("A thick Italian vegetable soup, often with pasta or rice", "Minestrone", ["Stracciatella", "Consommé", "Bouillon"]),
 ("A deep red Eastern European soup made with beetroot", "Borscht", ["Shchi", "Solyanka", "Goulash"]),
 ("A fish soup from Marseille, served with garlicky rouille", "Bouillabaisse", ["Velouté", "Consommé", "Cawl"]),
 ("A cold, creamy leek and potato soup", "Vichyssoise", ["Velouté", "Consommé", "Stracciatella"]),
 ("Slow-cooked onions in beef broth, topped with bread and melted cheese", "French onion", ["Velouté", "Consommé", "Shchi"]),
 ("A Scottish soup of chicken and leeks, sometimes with prunes", "Cock-a-leekie", ["Partan bree", "Cawl", "Shchi"]),
 ("A creamy Scottish soup of smoked haddock, potato and onion", "Cullen skink", ["Partan bree", "Cawl", "Solyanka"]),
 ("A spicy Anglo-Indian soup whose name means 'pepper water'", "Mulligatawny", ["Laksa", "Callaloo", "Pozole"]),
 ("A hearty soup of mutton, barley and root vegetables", "Scotch broth", ["Partan bree", "Shchi", "Solyanka"]),
 ("A Japanese soup of fermented soybean paste, tofu and seaweed", "Miso", ["Laksa", "Bird's nest soup", "Pozole"]),
 ("A Vietnamese beef broth with rice noodles and fresh herbs", "Pho", ["Laksa", "Pozole", "Callaloo"]),
 ("A hot and sour Thai soup, often with prawns and lemongrass", "Tom yum", ["Callaloo", "Bird's nest soup", "Pozole"]),
 ("A thick Louisiana stew-soup with okra, sausage and seafood", "Gumbo", ["Pozole", "Fabada", "Solyanka"]),
 ("A thick, creamy New England soup of shellfish and potatoes", "Clam chowder", ["Partan bree", "Velouté", "Waterzooi"]),
 ("A smooth, rich French shellfish soup", "Lobster bisque", ["Velouté", "Consommé", "Partan bree"]),
 ("Japanese wheat noodles in a rich broth, often with a soft-boiled egg", "Ramen", ["Laksa", "Pozole", "Bird's nest soup"]),
 ("A thick green soup of split peas and a ham hock, once called a 'London particular'", "Pea and ham", ["Cawl", "Shchi", "Partan bree"]),
 ("A Greek chicken soup thickened with egg and lemon", "Avgolemono", ["Stracciatella", "Consommé", "Solyanka"]),
 ("A clear Chinese broth with filled dumplings", "Wonton soup", ["Bird's nest soup", "Laksa", "Pozole"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-134.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
