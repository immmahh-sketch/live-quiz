# Bank-writing sessions

The host wants the question bank filled by hand in this tool (no API spend), topic by topic,
sessions five minutes apart, until every topic in `bank/topics.json` is complete.

Per topic the targets are: 50 multiple choice, 50 typed, 50 true/false, 5 put-in-order,
5 categorise, 10 highbrow/lowbrow, 10 answer smash, 10 name that tune, 10 rhyme time, 5 wipeout boards,
3 races, 5 drop the pin (10 for Geography topics), 5 match, 5 wheel of fortune, 5 1% Club and 3 dingbats.
Signature topics (group "Signature": Alan Shearer, Roger) only need choice and text. Catchphrase is not written
per topic: its questions are clips from the host's YouTube channel.

Good mix per topic: every topic carries every writable type, so a themed quiz can have any round.
Spread the topic's sub-subjects across the types too. Wales music should turn up in choice, text, tf,
rhyme and wipeout as well as Name That Tune, and Wales history in pins, orders and races, not only in
multiple choice. Topics written before these types were added get a top-up file (`<slug>__N.json`)
with just the missing types; `bank-next.mjs` asks for those first, in topic order.

Each session:

1. `node tools/bank-next.mjs` says which topic is next and what it still needs.
2. Write that into `bank/topics/<slug>.json` (or `<slug>__2.json`, `__3`… to top up an
   existing topic). Items are the writer's raw JSON shape plus `"type"`:
   - `{"type":"choice","text":"…","options":["RIGHT ANSWER FIRST","…","…","…"]}`
   - `{"type":"text","text":"…","answers":["canonical","also accepted"]}`
   - `{"type":"tf","text":"…","answer":true}`
   - `{"type":"order","text":"…","items":["first","second","third","fourth"],"hint":"…"}`
   - `{"type":"sort","text":"…","categories":["A","B"],"items":[{"text":"…","category":"A"}]}`
   - `{"type":"highlow","text":"HARD academic clue","lowText":"EASY pop-culture clue, same answer","answers":["…"]}`
   - `{"type":"smash","text":"clue for the second answer","pictureAnswer":"Wikipedia article title with a photo, e.g. Brad Pitt","clueAnswer":"Pittsburgh"}`
     (the end of pictureAnswer must overlap the start of clueAnswer by 2+ letters, or the server drops it)
   - `{"type":"tune","track":"…","artist":"…","ask":"song"|"artist"|"film"|"lyric"}` (`film` needs `"film"`, `lyric` needs `"lyricLine"` and `"cueLine"`; the server drops tracks with no iTunes preview)
   - `{"type":"wipeout","text":"board title","right":["…"×3–15],"wrong":["…"×1–8]}`
   - `{"type":"race","text":"The Race: …","target":10,"bank":[{"q":"…","right":"…","wrong":["…","…","…"]}×8–12]}`
   - `{"type":"pin","text":"fact clue that never names the place","place":"Cardiff","region":"Wales","lat":51.48,"lon":-3.18,"sizeKm":10}`
     (region is the map: a country or continent's usual English name, "London" for Greater London, a UK county such as "Tyne and Wear", "Northumberland" or "Cornwall", or "World"; sizeKm is how big the place is, which sets how close a pin must be)
   - `{"type":"match","text":"Match each … to …","pairs":[{"left":"…","right":"…"}×4]}` (max 4 pairs; `"rightPicture":"Wikipedia title"` swaps the right side for a photo)
   - `{"type":"wheel","phrase":"UPPER CASE PHRASE"}` (a well-known phrase, title or name tied to the topic; the importer skips any that do not fit the board)
   - `{"type":"club","text":"a logic or observation puzzle","answers":["…"],"pct":90}` (pct: the share of people expected to get it, 90 easy down to 1; it must be a genuine puzzle, not a plain fact)
   - `{"type":"dingbat","answers":["…"],"elements":[{"t":"MAN","x":50,"y":30,"s":5}]}` (x/y 0–100, s size 1–6, optional rot, flip "h"/"v", style strike/underline/box/outline)
   Every item also carries `"difficulty": "easy" | "medium" | "hard"`. Aim for roughly a
   quarter easy, nearly half medium and the rest hard (the bank picks in that proportion for a
   mixed round). Easy: most of the room knows it. Medium: a good table gets it. Hard: one
   person in the room knows it, but they exist.
   Quality bar: facts you are sure of, UK spelling, no "Trick:" or "no:" corrections in the
   text, no duplicates of what is already in the file, a spread of easy to hard. Pub-quiz
   quality: nothing nursery-level, nothing only a specialist could know.
3. Import: `LQ_PASSWORD=Buzzer-Round-1465 TOPICS=<slug> node tools/import-bank.mjs topics`
   (run from the repo root; exact and near duplicates are skipped, so re-running is safe).
4. Commit and push the new file.
5. Schedule the next session five minutes later with the same instructions.

`node tools/bank-next.mjs --list` shows every topic's counts; `--all` lists every incomplete topic.

Drop-the-pin rule (all pin questions, bank and writer): the text never names the place. It asks a fact whose
answer is the place, so the player must know the fact and then find it on the map ("Which city hosted the
2016 Olympics?"). Line-up pins ask a fact about one of the people or things shown. bank/pin-clues.json holds
the clue for every place in the pin bank; tools/rewrite-pins.mjs applies it.
