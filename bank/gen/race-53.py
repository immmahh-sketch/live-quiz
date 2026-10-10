# Bank session 10 Oct 2026: 3 more general races -> bank/race-53.json. 20 rows each, target 10; wrong options are
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

race("what's this Greek letter called?", "Words and language", "medium", ["Greek alphabet", "letters"], [
 ("α", "Alpha", ["Omicron", "Aleph", "Iota"]), ("β", "Beta", ["Kappa", "Beth", "Upsilon"]), ("γ", "Gamma", ["Upsilon", "Gimel", "Kappa"]),
 ("δ", "Delta", ["Omicron", "Iota", "Kappa"]), ("ε", "Epsilon", ["Iota", "Omicron", "Upsilon"]), ("ζ", "Zeta", ["Kappa", "Upsilon", "Iota"]),
 ("η", "Eta", ["Upsilon", "Kappa", "Omicron"]), ("θ", "Theta", ["Omicron", "Kappa", "Iota"]), ("λ", "Lambda", ["Kappa", "Upsilon", "Yod"]),
 ("μ", "Mu", ["Upsilon", "Kappa", "Omicron"]), ("ν", "Nu", ["Upsilon", "Kappa", "Iota"]), ("ξ", "Xi", ["Kappa", "Iota", "Omicron"]),
 ("π", "Pi", ["Iota", "Kappa", "Upsilon"]), ("ρ", "Rho", ["Omicron", "Iota", "Kappa"]), ("σ", "Sigma", ["Omicron", "Kappa", "Upsilon"]),
 ("τ", "Tau", ["Iota", "Kappa", "Upsilon"]), ("φ", "Phi", ["Omicron", "Upsilon", "Kappa"]), ("χ", "Chi", ["Kappa", "Upsilon", "Iota"]),
 ("ψ", "Psi", ["Upsilon", "Kappa", "Iota"]), ("ω", "Omega", ["Omicron", "Upsilon", "Kappa"])])

race("which part of the body does this specialist look after?", "Science and nature", "medium", ["medicine", "specialists"], [
 ("Cardiologist", "Heart", ["Spleen", "Pancreas", "Spine"]), ("Dermatologist", "Skin", ["Muscles", "Tendons", "Spine"]),
 ("Ophthalmologist", "Eyes", ["Spleen", "Thyroid", "Tonsils"]), ("Neurologist", "Nerves and brain", ["Pancreas", "Spleen", "Tendons"]),
 ("Nephrologist", "Kidneys", ["Spleen", "Pancreas", "Gallbladder"]), ("Hepatologist", "Liver", ["Spleen", "Pancreas", "Appendix"]),
 ("Podiatrist", "Feet", ["Hands", "Knees", "Spine"]), ("Gastroenterologist", "Stomach and gut", ["Spleen", "Thyroid", "Tonsils"]),
 ("Pulmonologist", "Lungs", ["Spleen", "Pancreas", "Thyroid"]), ("Urologist", "Bladder", ["Spleen", "Pancreas", "Gallbladder"]),
 ("Rheumatologist", "Joints", ["Spleen", "Pancreas", "Tonsils"]), ("Haematologist", "Blood", ["Tonsils", "Appendix", "Tendons"]),
 ("Otologist", "Ears", ["Tonsils", "Spine", "Knees"]), ("Rhinologist", "Nose", ["Tonsils", "Knees", "Spine"]),
 ("Laryngologist", "Voice box", ["Knees", "Spleen", "Appendix"]), ("Endocrinologist", "Hormone glands", ["Tendons", "Knees", "Appendix"]),
 ("Trichologist", "Hair", ["Nails", "Tendons", "Knees"]), ("Dentist", "Teeth", ["Tonsils", "Tendons", "Knees"]),
 ("Psychiatrist", "The mind", ["Spine", "Tendons", "Knees"]), ("Orthopaedic surgeon", "Bones", ["Tonsils", "Spleen", "Appendix"])])

race("which country did this royal house or dynasty rule?", "History", "hard", ["royal houses", "dynasties"], [
 ("The House of Windsor", "the United Kingdom", ["Ireland", "Denmark", "Norway"]), ("The Grimaldis", "Monaco", ["Andorra", "Liechtenstein", "San Marino"]),
 ("The House of Orange-Nassau", "the Netherlands", ["Belgium", "Denmark", "Norway"]), ("The House of Bernadotte", "Sweden", ["Denmark", "Finland", "Iceland"]),
 ("The Chakri dynasty", "Thailand", ["Cambodia", "Laos", "Myanmar"]), ("The Alaouite dynasty", "Morocco", ["Algeria", "Tunisia", "Egypt"]),
 ("The Hashemites", "Jordan", ["Kuwait", "Oman", "Bahrain"]), ("The House of Thani", "Qatar", ["Kuwait", "Bahrain", "Oman"]),
 ("The Wangchuck dynasty", "Bhutan", ["Nepal", "Sikkim", "Myanmar"]), ("The Romanovs", "Russia", ["Denmark", "Bulgaria", "Greece"]),
 ("The Habsburgs, from Vienna", "Austria", ["Denmark", "Norway", "Greece"]), ("The Hohenzollerns, as Kaisers", "Germany", ["Denmark", "Norway", "Belgium"]),
 ("The Bourbons, before 1792", "France", ["Belgium", "Norway", "Greece"]), ("The House of Savoy, as kings from 1861", "Italy", ["Denmark", "Norway", "Greece"]),
 ("The Pahlavi dynasty", "Iran", ["Iraq", "Afghanistan", "Egypt"]), ("The Qing dynasty", "China", ["Japan", "Korea", "Vietnam"]),
 ("The Ottomans", "Turkey", ["Afghanistan", "Oman", "Kuwait"]), ("The Mughals", "India", ["Nepal", "Sri Lanka", "Myanmar"]),
 ("The House of Braganza", "Portugal", ["Spain", "Greece", "Belgium"]), ("The Jagiellonians, from Kraków", "Poland", ["Denmark", "Norway", "Greece"])])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(here, '..', 'race-53.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'races written')
