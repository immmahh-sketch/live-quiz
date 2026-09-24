# Bank-writing sessions

The host wants the question bank filled by hand in this tool (no API spend), 50 questions per
plain type per topic, one or two topics per session, sessions five minutes apart, forever.

Each session:

1. `node tools/bank-next.mjs` says which topic is next and what it still needs
   (50 multiple choice, 50 typed, 50 true/false, 5 put-in-order, 5 categorise per topic).
2. Write that many into `bank/topics/<slug>.json` (or `<slug>__2.json`, `__3`… to top up an
   existing file). Items are the writer's JSON shape plus `"type"`:
   - `{"type":"choice","text":"…","options":["RIGHT ANSWER FIRST","…","…","…"]}`
   - `{"type":"text","text":"…","answers":["canonical","also accepted"]}`
   - `{"type":"tf","text":"…","answer":true}`
   - `{"type":"order","text":"…","items":["first","second","third","fourth"],"hint":"…"}`
   - `{"type":"sort","text":"…","categories":["A","B"],"items":[{"text":"…","category":"A"}]}`
   Quality bar: facts you are sure of, UK spelling, no "Trick:" or "no:" corrections in the
   text, no duplicates of what is already in the file, a spread of easy to hard. Pub-quiz
   quality: nothing nursery-level, nothing only a specialist could know.
3. Import: `LQ_PASSWORD=Buzzer-Round-1465 TOPICS=<slug> node tools/import-bank.mjs topics`
   (run from the repo root; duplicates are skipped, so re-running is safe).
4. Commit and push the new file.
5. Schedule the next session five minutes later with the same instructions.

`node tools/bank-next.mjs --list` shows every topic's counts.
