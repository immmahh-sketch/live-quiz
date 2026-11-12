# Christmas Day (built 12 Nov 2026)

The Christmas night played as one Christmas Day, 7am to midnight. Everyone builds a Christmas dinner while the elf, a family of characters and a
few surprises get in the way. Works for individuals and for teams (a team is one player with several phones, so it has one dish, one character).

## The rules (as the host set them)

- **The plate:** nine items, each tied to a question category, plus the tomato ketchup. Get a question right and its item goes on your dish.
  Item / category: 🦃 Turkey / Christmas · 🥔 Roast potatoes / TV & Film · 🌭 Pigs in blankets / Music · 🍞 Stuffing / History · 🥕 Carrots & parsnips / Geography ·
  🥦 Brussels sprouts / Food & Drink · 🥣 Gravy / Celebrities · 🍒 Cranberry sauce / Sport · 🥧 Yorkshire pudding / Science. (The builder lets you change each category.)
- **Rarity:** common dishes (turkey, potatoes, pigs) are collected by every right answer; uncommon ones (stuffing, veg, sprouts) only by the quickest 60% of
  right answers who lack it; rare ones (gravy, cranberry, Yorkshire) only by the quickest 35% (at least one). Rare items also come up in fewer questions
  and ask harder ones (round difficulty easy / medium / hard).
- **The ketchup:** only for a player with all nine items, and only by getting a 1% Club style question right (type `club`, tagged `xi: 'ketchup'`). Three of them
  are asked (after courses 2, 3 and 4), the hardest last. A player who misses one tries again at the next.
- **The end:** every item missing (ketchup counts, 10 in all) costs 2,000; a full dish pays 5,000 (instead of any deduction).
- **Steals:** every 5th item question the quickest right answer who has not had a pinch lately gets a PINCH: 30 s to pick any item they lack from any dish.
  The ELF visits six times: everyone's phone shows him popping up; the first to tap him picks two dishes to swap one item each way (nobody taps: he picks).
  Uncle Keith (twice) takes an item from the fullest unshielded dish and slips it to an emptier one. The board-game row swaps the top two scores. A doorbell
  (twice) doubles the next question. A power cut (once) blacks out four plain questions in a row: the host screen goes dark, and on phones the screen goes black with the question hidden and a torch beam lighting only the answers (the host reads each question out). Answering, or a waiting screen, brings the phone lights back.
- **The family:** everyone is dealt a character, the least-used first. Quirk (always on) and power (once, between questions):
  👵 Nan: first theft or swap against her fails / Handbag Surprise: any missing common item ·
  👴 Grandad: +300 for each rare item / Wake Up: next item question double points and a guaranteed item ·
  🧒 Teenager: elf-proof / Hide in Your Room: untouchable for six item questions ·
  🐕 Dog: thefts are anonymous / Snatch the Sausage: steal any item now ·
  🧠 Know-It-All Cousin: +100 for a wrong item answer / Insurance: next item question wrong still collects ·
  🥂 Auntie Maureen: sees the first elf 3 s early (first visit only) / Spill the Gravy: a player cannot collect on their next item question ·
  🧔 Uncle Keith: steals ignore shields and Nan / Dodgy Deal: random item from the fullest dish ·
  👩 Mum: a missing item costs her 1,500 / Swap Seats: swap a random item each with a chosen player.

## Making and hosting a night

- Portal quiz list: **🎄 Make a Christmas Day night**. Choose each item's category and how many questions carry it (defaults 13/11/11/8/8/8/6/5/5 = 75), the number of
  ketchup questions, question style, break, party games, and whether to finish with Double Points Answer Smash and The Final Chase. Questions come from the bank
  (`bankonly`, no AI), are mixed so no item comes up twice running, and are laid out as four courses (🧦 Stockings and presents, 🍳 Cooking the dinner,
  🍽 The big dinner, 📺 Telly and the board games) with games, ketchup questions and a half-time break between. About 90 items.
- By hand: Settings > tick **🎄 Christmas Day** (`settings.xmas = { on: true }`), then pick an item on each question (🎄 field in the item form: `q.xi`).
  Only plain questions collect items; the group games (Wipeout, Race, Chase...) do not.
- Host as normal (no extra buttons). Surprise screens (pinch, elf, Keith, argument, dinner table, the end) come up between questions and Next carries on;
  a pinch or elf waiting for a phone can be skipped with Next ("Pick for them" / "Let the elf choose"). In Test by myself the bots play their powers and tap the elf.
- Phones: a family card the first time, a 🍽 button (dish, what is left, power), a chip with the item up for grabs on each question, pop-ups when an item arrives or is stolen.

## Code

- `assets/xmas-data.js` items, rarity, family, clock scenes, the nine ketchup puzzles (all loaded by host, phones, portal).
- `assets/xmas.js` host engine (`G.xm`), hooks in `party.js` (`partyGameStart / StartQuestion / AfterGrade / State`) and `host.html` (`nextFrom`, `primaryAction`,
  `renderPhase`, `scheduleAuto`, `goBack`, `skipItem`, `finish`, `render`, and the `xm` channel event).
- `assets/xmas-phone.js` phones (hook: `partyPhoneAfter`; `xmno` refusals in `play.js`), `assets/xmas.css` both.
- `assets/night-tools.js` `xmasNight()` / `xmLayout()` (builder) and `xmHtml/xmBind` (item picker). `index.html`: button, Settings tick.
- No server change, nothing to deploy beyond pushing the repo.

## Tests (lqsql\review\trtest)

`xm_run.mjs` (builder, mock bank), `xm_host.mjs` / `xm_host_shots.mjs` (whole night with 8 bots and 2 players, screenshots), `xm_powers.mjs` (28 checks of steals, shields,
swaps, every power, the end, Keith, the argument), `xm_phone.mjs` / `xm_phone2.mjs` (phone screens from captured states), `xm_live.mjs` (host and a phone page over the real channel:
join, family card, pinch pick, elf tap, swap, refused power). All pass with no page errors. **Not done:** real phones, the builder against the real bank, a real night.

## Not built (offered earlier)

Secret Santa, Twelve Days of Christmas, the cracker-pull duel, the leftovers round, a true sound-only power cut. The ketchup `pct` values are my estimates of how few people solve each puzzle.
