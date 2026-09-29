# Play at home

Four quiz shows to play on a phone, on your own or with friends round the table. There's no host screen: everything happens on the phones. Live at `letsquiz.uk/home`.

| Page | Game | Players |
|---|---|---|
| `millionaire.html` | Who Wants to Be a Millionaire? | 1 |
| `chase.html` | The Chase | 1–4 against a bot Chaser, or one of you is the Chaser |
| `weakest.html` | The Weakest Link | a team of 6–9: you and bots, or friends' phones plus bots |
| `club.html` | The 1% Club | 100: you, friends and bots |

## How it fits together

- **`assets/home.js` (`HQ`)** holds the shared pieces:
  - the sets and each phone's progress;
  - typed-answer matching (`HQ.isRight`);
  - sounds made in the browser, bots, QR codes and screen wake lock;
  - `HQ.session`, which runs a game on one phone (the lead) and mirrors it to the others.
- **Multi-phone games:** the lead phone runs the engine and broadcasts a view on the Supabase Realtime channel `home-<CODE>`. The other phones send their moves back. Nothing is stored on the server.
- **Saving a game:** the lead phone saves its game every couple of seconds (`lq_home_live_<game>`), so a reload can carry on. A joining phone that reloads rejoins with the same player id.
- **Styles:** `assets/home.css` holds the shared look. Each game page has its own theme in its `<style>` block.

## Never the same question twice

- **Sets:** every game is played from a numbered set, `home/sets/<game>-NN.json`. `home/sets/index.json` says how many sets each game has.
- **Progress:** a phone remembers which sets it has played (`localStorage.lq_home`) and always starts the lowest one it hasn't.
- **When a set counts as played:** as soon as its first question is shown, so quitting halfway can't bring the same questions back.
- **With friends:** the lead picks the lowest set that none of the phones in the room has played. When everything has been played, the game says so and replays the set this phone played longest ago.

## Kept apart from hosted quizzes

1. **Taken out of the bank.** Every question in a set comes from the bank and is taken out of its stock: `used = true`, and `q.used = { home: '<game>-NN' }`. The builder, `gameDeal` and `bank_restock` never pick or return these questions.
2. **Checked against hosted quizzes when the set is built.** `tools/home-check.mjs` compares the sets with every hosted quiz, including game rows and the deleted-quiz backup, and with each other.
3. **Checked again when a quiz is confirmed.** `assets/home-guard.js` (`LQH`) runs when a quiz is confirmed in `build.html`. It swaps out of the hosted quiz, and out of its warm-up, anything that repeats a home game. This catches questions the AI writer comes up with that happen to match a home game.

"The same question" means any of these:
- the same answer to a question about the same thing;
- near-identical wording;
- one fact asked both ways round ("What is the capital of Kenya?" and "Nairobi is the capital of which country?").

The rule lives in `tools/home-lib.mjs` `clash()`, with a copy in `home-guard.js`.

## Making more sets

Everything runs from the repo, with a working folder (here `../lqsql/home`) for exports and reviews.

1. **Export the bank.** Export the candidate pool and the hosted quizzes with `npx.cmd supabase db query --linked --project-ref safcrtrfdzsnftghibot -o json`:
   - `tools/home-pool.sql` gives `pool.json`;
   - `tools/home-history.sql` gives `history.json`.

   Put the deleted-quiz backup in as `backup-quizzes.json`.
2. **Pick candidates.** Run `node tools/home-cands.mjs <dir>`. It picks about 25% more than needed, spread across categories, and skips anything already in a set or a hosted quiz. `WANT` sets how many of each kind. The output is:
   - `cands-mc4.json` (Millionaire);
   - `cands-mc3.json` (Chase head-to-head);
   - `cands-typed.json` (Chase and Weakest Link quick-fire);
   - `cands-club.json` (1% Club).
3. **Review.** The typed and three-option candidates were split into chunks and read in full against the quiz standards. Each chunk has a `review/result-N.jsonl` with, for each question:
   - keep or drop;
   - an honest difficulty for this format;
   - extra accepted answers;
   - the two wrong options to keep;
   - an optional safe rewording.

   Millionaire and the 1% Club ladder were read by hand:
   - dropped Millionaire candidates go in `mc4-drop.json`;
   - the ladder goes in `club-pick.json`, with one list per rung in set order. It also holds extra answers (`addAnswers`; `~word` means that word anywhere in the answer), corrected explanations (`fixWhy`) and any duplicates to retire (`retire`).

   The bank's own 1% Club percentages were often far out, so every rung was rated again by hand.
4. **Build and check.**
   1. Run `node tools/home-build.mjs <dir> <first> <count>` (for example `11 10` for sets 11–20). It writes the sets and `<dir>/reserve.sql`.
   2. Run `node tools/home-check.mjs <dir>`. It must say **All clear**.
5. **Take them out of stock.** Run `reserve.sql` with `supabase db query`.
6. **Commit and push.**

### What's in each set

- **Millionaire:** 15 four-option questions on a ladder, like the show. Every question is rated 1–10 by hand and the rungs run 1 1 2 2 3 3 4 4 5 5 6 7 7 8 9: two nursery questions (the bank's "too easy" pile, which hosted quizzes never use), then a steady climb to a £1,000,000 question most people have to guess. Built by `tools/home-mil-ladder.mjs` from `home/build/millionaire-ratings-01-10.json`; it reserves the new questions and hands back what the sets no longer use.
- **The Chase:** 125 typed quick-fire questions (30 easy, 70 medium, 25 hard) and 48 three-option head-to-head questions. They are dealt as one stream through the whole game, so a set is sized for four contestants.
- **The Weakest Link:** 160 typed questions (68 easy, 76 medium, 16 hard).
- **The 1% Club:** 11 questions, one each at 90, 80, 70, 60, 50, 40, 30, 20, 10, 5 and 1%.

Every set is:
- mixed in category;
- free of repeated answers;
- free of any question that names another's answer.

## Game rules as built

### Millionaire

- **Money and safe havens:** £100 to £1,000,000, with safe havens at £1,000 and £32,000. You can walk away with what you've won at any point. There's no clock.
- **Phone a Friend:** the friend's final pick is right 70% of the time. They sound surest when right, but can be confidently wrong.
- **Ask the Audience:** 40% of the time the audience strongly backs the right answer, 20% narrowly right, 20% strongly wrong and 20% narrowly wrong.

### The Chase

- **Cash Builder:** 60 seconds of typed answers.
- **Offers:** a higher offer (start 2 steps from the Chaser), what you built (3 steps) or a lower offer (4 steps). The board has 8 rows, and home is row 8.
- **Head-to-head:** three-option questions with 20 seconds each.
- **Final Chase:**
  - Two minutes. Anyone in the team can answer, and the first right answer counts.
  - The head start is one step for each player who got home.
  - If nobody got home, everyone plays for £4,000 with no head start.
- **The bot Chaser:** gets 70–95% right. Its pace per question is set by the team size, because typing is slower than talking: 6.8–8.6 seconds for one player, faster for more. When it gets one wrong, the team gets a pushback chance.
- **"I was right":** after Cash Builder and the Final Chase, the player can claim a typed answer the matcher missed. It's an honour system.

### The Weakest Link

- **Money chain:** £20 up to £1,000, with at most £1,000 banked per round.
- **Round clock:** (30 + 15 × players) seconds.
- **Bots:** each bot has its own skill, speed and appetite for banking. At the vote, bots mostly go for the weakest by the numbers, sometimes the strongest for tactics, and sometimes hold a grudge.
- **Ties:** the strongest link has the casting vote.
- **The last two:** they play a trebled final round, then a head-to-head of five questions each, with sudden death if needed.
- **Everyone real voted off:** the rest is played out by the numbers.

### The 1% Club

- **The pot:** everyone out adds £1,000.
- **Pass:** one pass each, on any question except the 1% question.
- **Before the 1% question:** you can walk away with £1,000, or play for a share of the pot.
- **Bots:** their chance of a right answer comes from a per-rung base rate plus their own skill. On average about 64 are left after 50% and about 29 after 20%. About 2 join the 1% Club, and in 9% of games nobody does.
