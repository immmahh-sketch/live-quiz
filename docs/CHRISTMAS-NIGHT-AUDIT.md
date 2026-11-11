# Christmas bank audit (11 Nov 2026)

Usable = not rejected and not flagged (tooEasy, giveaway, doubt, recycled). Totals across the four Christmas
categories (Christmas, Christmas films, Christmas songs, Christmas TV), from `quiz_bank`.

| Type | Usable | Note |
|---|---|---|
| choice | ~225 | plenty |
| text | ~170 | plenty |
| tf | ~170 | plenty |
| order | 25 | fine |
| sort | 27 | fine |
| highlow | 40 | fine |
| smash | 40 | fine |
| tune | 42 | fine |
| rhyme | ~34 | fine |
| match | 35 | fine |
| wheel | 20 | fine |
| club | 20 | fine |
| pin | 20 | fine |
| dingbat | 35 | fine |
| race | ~13 | only a few; one night needs 2 to 3 |
| cards | 10 | ok |
| nearest | 10 | Christmas category only; could use more |
| wipeout | 6 before, 11 after the 11 Nov top-up | WAS THE GAP; thin because many were retired as repeats |
| conundrum, reveal, survey, unique, twenty, catchphrase | 0 Christmas | not written yet |

## Done
- 11 Nov: `christmas__n1.json` (7 new Wipeout boards, one repeated an existing board and was replaced).
  After `wipe-dupes.sql` two more repeated existing boards (Christmas dinner, Christmas number ones) and were retired
  (`bank/wipe-topups/48-retire-christmas-repeats.json`). Net: 5 new Christmas boards.

## Still to do
1. More Christmas Wipeout boards (aim for 12+ usable), then more races (aim 6+), nearest (aim 25), cards.
2. Christmas conundrums: festive 9-letter words with ONE anagram (see live-quiz-conundrum memory; files `bank/conundrum*.json`).
3. Christmas reveal pictures, if the picture source allows.
4. Cracker jokes as `text` (answer = punchline), festive dingbats, pins (Bethlehem, Rovaniemi, Nuremberg, ...).
5. Then assemble the night (see CHRISTMAS-NIGHT.md).

## Session 2 (11 Nov, later)
- `christmas__n2.json`: 4 more Wipeout boards (Christmas films, Santa names around the world, nativity people; the pudding board repeated an existing one and was retired, `49-retire-pudding-repeat.json`). Christmas Wipeout now about 14 usable.
- `christmas__n3.json`: 12 cracker-joke multiple-choice questions (all easy, for a light round).
- Still to do: Christmas races (aim 6+), more `nearest`, conundrums, reveal pictures, pins, festive dingbats.
