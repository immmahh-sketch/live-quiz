# Bank session 19 Oct 2026: 2 Categorise questions -> bank/sort-83.json. Each pair of categories was probed against every
# Categorise question in the live bank first (no Downton or Peaky Blinders sorts). The two use different Downton characters, so they
# can share a night. A sea v freshwater fish sort was drafted and dropped: already in.
import json, os
OUT = []
def s(cat, tags, diff, text, a, b, A, B):
    assert len(A) >= 3 and len(B) >= 3 and len(A) + len(B) <= 8 and len(set(A + B)) == len(A + B), text
    OUT.append({"type": "sort", "text": text, "categories": [a, b], "items": [{"text": t, "category": a} for t in A] + [{"text": t, "category": b} for t in B],
                "category": cat, "tags": tags, "difficulty": diff})

s("Television", ["Downton Abbey", "Peaky Blinders"], "easy", "A character from Downton Abbey or from Peaky Blinders?", "Downton Abbey", "Peaky Blinders",
  ["Mr Carson", "Mrs Patmore", "Lady Mary", "Mr Bates"], ["Tommy Shelby", "Polly Gray", "Alfie Solomons", "Arthur Shelby"])
s("Television", ["Downton Abbey", "ITV"], "medium", "At Downton Abbey: one of the family upstairs, or a servant downstairs?", "Upstairs", "Downstairs",
  ["Lord Grantham", "Lady Edith", "Cora", "Violet"], ["Mrs Hughes", "Anna", "Daisy", "Thomas Barrow"])

here = os.path.dirname(os.path.abspath(__file__))
json.dump(OUT, open(os.path.join(here, '..', 'sort-83.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(OUT), 'sort questions written')
