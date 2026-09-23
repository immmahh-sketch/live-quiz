# Live Quiz

A Kahoot-style live quiz for video calls. You build quizzes in a desktop portal, share your
screen on the call, and everyone plays on their phone by scanning the QR code. Scores reward
speed as well as accuracy.

- **Host portal** (`index.html`) — sign in, build quizzes in rounds, set time limits per
  question type, write rounds with AI from a brief, host a game.
- **Host screen** (`host.html`) — the slideshow you share: lobby with QR code, questions,
  timer, answer reveal, scoreboard, podium.
- **Player app** (`play.html`) — what everyone opens on their phone.

Plain static HTML, no build step. Hosted on GitHub Pages; backend on Supabase
(Realtime for the live game, one edge function for storage and AI).

Full scope and design decisions: [docs/SCOPE.md](docs/SCOPE.md).

## Question types

| Type | Players do | Scored |
|---|---|---|
| Multiple choice | Tap one of up to four coloured answers | Right or wrong |
| Type the answer | Type it in | Exact/near match instantly; anything else judged by AI (misspellings, other wordings) |
| Put in order | Arrange items with arrows | All-or-nothing, or partial credit per correct position (toggle) |
| Drop the pin | Tap a spot on a picture | Full points inside the bullseye, falling to zero at the outer radius; closest player is flagged |
| Match up | Pair each word with a picture or word | All-or-nothing, or partial credit per correct pair (toggle) |
| True or false | Tap true or false | Right or wrong |
| Categorise | Put each answer into one of 2–4 categories | All-or-nothing, or partial credit per correct placement (toggle) |
| The Race | Played on the phones: a bank of quick multiple-choice questions, answer or skip, first to the target (default 10 right) wins | Winner takes the prize (default 5000), nobody else scores; you're out once you can't reach the target; on the time limit the clear leader wins |
| Wipeout | Take turns picking right answers from a scattered board of up to 20 (some wrong) | Each right pick scores (default 200) and vanishes; a wrong pick costs the picker (default 500) and ends the question; running out of your 5-second turn drops you out of that question |

Any question can carry a **picture** or a **YouTube video**. The video plays on the host
screen (with sound, if you share system audio on the call) while players answer.

**Points:** a right answer scores from the quiz's top figure (default 1000) at the instant the
question starts, falling in a straight line to the floor figure (default 500) at the buzzer.
Wrong answers score nothing. Both figures and the default time limit are in Quiz settings.

## Running a game

1. Open the portal, sign in with the host password, build or pick a quiz, press **Host live**.
2. Share the host tab on the call. Players scan the QR code (or go to the short link and
   type the six-character code), enter a name and pick an emoji.
3. Press **Start**. Each question: 3-second lead-in, the question with timer, then the
   reveal, then the scoreboard. **Space** advances. A question ends early once everyone has
   answered.
4. After the last question: podium and confetti. The result is saved and shows under
   *Recent games* in the portal.

If the host tab is refreshed mid-game it offers to carry on where it left off. Players who
refresh rejoin as themselves.

**Try it without signing in:** `host.html?quiz=demo` loads a built-in sample quiz with one
question of every type.

**Test mode:** press **Add test bots** in the lobby (or open the host screen with `&bots=3`
on the URL) to add three simulated players. They answer every question type after a
realistic pause with mixed accuracy, take their Wipeout turns and run the race, through
the same code a real phone's answer goes through. Join from your own phone alongside them
to see the whole thing from both sides.

## AI

- **Answer judging** — typed answers that don't match an accepted answer closely enough are
  sent to Claude in one batch at the end of the question. It accepts misspellings,
  abbreviations and alternative names, and rejects hedges and different things. If the AI is
  unavailable the game falls back to a closest-match rule and carries on.
- **Quiz writer** — *Write one with AI* / *Add with AI* in the portal. Give it a topic, how
  many, difficulty and which types; it searches the web to check facts and cover recent
  events, and finds pictures from Wikipedia (copied into our own storage). Drop-the-pin
  questions get a blank map of the right country or continent. Read the questions through
  before hosting.
- **Fact-checker** — *Check all*, or the tick on a round. A separate pass with web search
  marks each question ✓ / ? / ✗ with a note and a suggested answer. Editing a checked
  question marks the check as stale.

Both need the `ANTHROPIC_API_KEY` secret on the Supabase project. Without it, judging falls
back to closest-match and the writer is disabled (the portal says so).

## Deploying

### Front end

Push to `main`. GitHub Pages serves the repo root.

### Backend (Supabase project `safcrtrfdzsnftghibot`)

The Supabase CLI is linked in `C:\Users\GM\Documents\Till App`, which holds the full
migration history, so database changes are pushed from there.

```bash
# 1. Copy the migration and the function into the linked folder
cp supabase/migrations/20260924090000_live_quiz.sql "C:/Users/GM/Documents/Till App/supabase/migrations/"
mkdir -p "C:/Users/GM/Documents/Till App/supabase/functions/quiz-api"
cp supabase/functions/quiz-api/index.ts "C:/Users/GM/Documents/Till App/supabase/functions/quiz-api/"
```

```bash
# 2. From the Till App folder: secrets, tables and bucket, then the function
cd "C:/Users/GM/Documents/Till App"
npx.cmd supabase secrets set QUIZ_HOST_PASSWORD="<the host password>"
npx.cmd supabase secrets set ANTHROPIC_API_KEY="<your Anthropic key>"
npx.cmd supabase db push --yes
npx.cmd supabase functions deploy quiz-api --no-verify-jwt
```

The migration creates `quiz_quizzes`, `quiz_games` and the public `quiz-media` bucket, all
with RLS on and no public policies — the browser holds only the publishable key and
everything goes through `quiz-api` on the service role, gated by `QUIZ_HOST_PASSWORD`.

To change the host password later, set the secret again; the portal will ask for the new one.

## Files

```
index.html                       host portal: sign-in, quiz list, builder, AI writer
host.html                        live game screen
play.html                        player app
assets/common.js                 config, API helper, question types, scoring, helpers
assets/style.css                 all three pages
assets/demo-quiz.js              the built-in sample quiz
supabase/functions/quiz-api/     the edge function (copy into Till App to deploy)
supabase/migrations/             the schema (copy into Till App to deploy)
docs/SCOPE.md                    what was built and why
```
