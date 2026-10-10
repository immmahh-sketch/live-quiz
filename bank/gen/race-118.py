# Bank session 10 Oct 2026: 2 more general races -> bank/race-118.json (colours, what organs do). 20 rows each, target 10; wrong options are
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

race("what colour is it?", "General knowledge", "easy", ["colours", "everyday"], [
 ("The snooker ball worth four points", "Brown", ["Tan", "Bronze", "Copper"]),
 ("The Tour de France leader's jersey", "Yellow", ["Saffron", "Lime", "Peach"]),
 ("A British postbox", "Red", ["Maroon", "Coral", "Rose"]),
 ("A traditional London taxi", "Black", ["Charcoal", "Olive", "Burgundy"]),
 ("The middle stripe of the Irish flag", "White", ["Ivory", "Cream", "Beige"]),
 ("The Smurfs", "Blue", ["Teal", "Lilac", "Mauve"]),
 ("The Incredible Hulk", "Green", ["Olive", "Teal", "Lime"]),
 ("A Cadbury Dairy Milk wrapper", "Purple", ["Lilac", "Mauve", "Lavender"]),
 ("A Tiffany & Co. gift box", "Turquoise", ["Teal", "Lime", "Sky blue"]),
 ("A first-place Olympic medal", "Gold", ["Bronze", "Copper", "Platinum"]),
 ("A second-place Olympic medal", "Silver", ["Bronze", "Platinum", "Copper"]),
 ("An easyJet plane's tail", "Orange", ["Peach", "Coral", "Saffron"]),
 ("The colour between blue and violet in the rainbow", "Indigo", ["Teal", "Mauve", "Lilac"]),
 ("The last colour of the rainbow", "Violet", ["Lilac", "Mauve", "Lavender"]),
 ("An African elephant", "Grey", ["Charcoal", "Tan", "Taupe"]),
 ("Barbie's signature colour", "Pink", ["Coral", "Peach", "Rose"]),
 ("The dark blue named after Royal Navy uniforms", "Navy", ["Teal", "Charcoal", "Sky blue"]),
 ("The M in CMYK printer ink", "Magenta", ["Maroon", "Mauve", "Crimson"]),
 ("The British Army's sandy desert kit", "Khaki", ["Olive", "Tan", "Beige"]),
 ("The middle traffic light", "Amber", ["Saffron", "Peach", "Coral"])])

race("which part of the body does this job?", "The human body", "medium", ["human body", "organs"], [
 ("Filters the blood and makes urine", "Kidneys", ["Pancreas", "Ureter", "Adrenal glands"]),
 ("Pumps blood round the body", "Heart", ["Thymus", "Bone marrow", "Lymph nodes"]),
 ("Stores bile until it's needed", "Gall bladder", ["Pancreas", "Duodenum", "Thymus"]),
 ("The body's largest organ", "Skin", ["Bone marrow", "Thymus", "Pancreas"]),
 ("Cleans toxins out of the blood and makes bile", "Liver", ["Pancreas", "Duodenum", "Thymus"]),
 ("Where most of the goodness in food is absorbed", "Small intestine", ["Rectum", "Pancreas", "Ureter"]),
 ("Takes water back out of waste before it leaves", "Large intestine", ["Rectum", "Ureter", "Duodenum"]),
 ("Swaps oxygen for carbon dioxide", "Lungs", ["Bronchi", "Sinuses", "Thymus"]),
 ("Runs everything, with around 86 billion nerve cells", "Brain", ["Spinal cord", "Pituitary gland", "Thymus"]),
 ("Clears out old red blood cells and helps fight infection", "Spleen", ["Thymus", "Lymph nodes", "Bone marrow"]),
 ("Stores urine", "Bladder", ["Ureter", "Urethra", "Prostate"]),
 ("Carries food from the mouth to the stomach", "Oesophagus", ["Epiglottis", "Uvula", "Duodenum"]),
 ("The voice box", "Larynx", ["Epiglottis", "Uvula", "Sinuses"]),
 ("The windpipe", "Trachea", ["Bronchi", "Epiglottis", "Sinuses"]),
 ("Helps you keep your balance", "Inner ear", ["Eardrum", "Sinuses", "Adenoids"]),
 ("Churns food in acid", "Stomach", ["Duodenum", "Pancreas", "Rectum"]),
 ("A small pouch off the gut that can burst and need taking out", "Appendix", ["Adenoids", "Thymus", "Duodenum"]),
 ("The sheet of muscle under the lungs that powers breathing", "Diaphragm", ["Epiglottis", "Bronchi", "Sinuses"]),
 ("The light-sensitive layer at the back of the eye", "Retina", ["Cornea", "Iris", "Lens"]),
 ("Lumps at the back of the throat that can get infected and be taken out", "Tonsils", ["Adenoids", "Uvula", "Epiglottis"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-118.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
