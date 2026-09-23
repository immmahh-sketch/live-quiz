# Live Quiz — scope and design

*Written 23 September 2026, alongside the first build.*

## What it is

A live, Kahoot-style quiz played over a video call. One person hosts from a desktop browser
and shares their screen; everyone else plays on their phone. The host builds quizzes
beforehand in a portal, or has AI write them. A game is a live session that starts when the
host opens the lobby and ends with the podium.

## The three pages

**Portal — `index.html`.** Password sign-in. A list of quizzes with Host / Edit / Duplicate /
Delete, and *Recent games*. The builder opens on the **rounds planner**: a card per round with
its title, what it is about (shown on the round card during the game), how many of each
question type it should have (the round's size is the sum) and a prompt for the AI, plus *Add a round*, *Write this round
with AI* and *Write every round with AI*, which write each type in the quantity asked,
skipping what the round already has. The question list on the left is grouped by round (reorder, duplicate and delete
questions; move a question to another round from its form), with the selected question's
form on the right. Each question has its text, the
type-specific answers, optional media (picture upload or link, or a YouTube link with a
start time), a time limit, and for order/match a partial-credit toggle. Quiz settings hold
the points curve and a **time limit per question type** (all typed-answer questions a minute,
say), with a switch to apply those to everything already in the quiz. New and AI-written
questions take their type's time; any question can still be changed on its own. Autosaves two seconds after a change; *Host live* saves
first and refuses to start while a question is unfinished (it selects the one that needs
attention and says why).

**Host screen — `host.html`.** Designed for screen sharing: big type, dark stage, one thing
at a time.

1. *Lobby* — QR code, six-character code, short link, players appearing as they join.
1a. *Round card* — when the quiz has more than one round, a title card before each round
   ("Round 2 of 3 — Sports, 8 questions"). Phones show the same.
2. *Lead-in* — three seconds showing the question number, type and text, so people can
   read before the clock starts. Any picture is pre-loaded here.
3. *Question* — question text, picture or video, the answers laid out to match the phones,
   a timer ring, and an answered counter. Ends at the buzzer, when every connected player
   has answered, or when the host stops the clock.
4. *Reveal* — the right answer and how people did: vote bars for multiple choice, everyone's
   typed answers marked right or wrong, the correct order, the correct pairs, or the map
   with every pin plus the target and a *Closest* badge.
5. *Scoreboard* — top eight with what they just gained.
6. *Podium* — after the last question, with confetti. The result is saved.

Space, Enter or → advances. The game state is kept in the browser so a refresh offers to
carry on.

**Player app — `play.html`.** Join with the code (pre-filled from the QR link) and a name.
Then it mirrors the host: waiting, get ready, the answer control for the question type, a
sent confirmation, the result with points and rank, and the final placing. Each phone has a
persistent player id so a refresh or a dropped connection rejoins as the same person with
the same score.

## Question types and scoring

Speed points for a right answer:

```
points = max − (max − min) × (time taken ÷ time limit)      default max 1000, min 500
```

| Type | Answer | Right when | Partial credit |
|---|---|---|---|
| Multiple choice | one of 2–4 options | it's the marked one | — |
| Type the answer | free text | exact or near match to an accepted answer, else AI says so | — |
| Put in order | the items arranged | every item in place | fraction of items in the right position (toggle) |
| Match up | word → picture/word pairs | every pair right | fraction of pairs right (toggle) |
| Drop the pin | a point on the picture | within the bullseye radius | linear fall-off to zero at the outer radius, always on |
| True or false | true or false | it matches | — |
| Categorise | each answer placed in a category | every answer in its category | fraction placed right (toggle) |
| Wipeout | turn-based picks from a board | see below | — |
| The Race | a bank of quick questions on the phone | first to the target | — |
| Answer Smash | free text | the smash (or both answers), AI-judged | — |
| Wheel of Fortune | free text | the phrase, AI-judged for typos | — |

**The Race** is played entirely on the phones while the host screen shows a track. The
question is a bank of quick multiple-choice questions (the builder fills it by hand or with
AI; the host needs more than the target to leave room for skips). Everyone gets the bank in
the same shuffled-answer order, taps an answer or skips, and moves straight on; every pick
goes to the host, which checks it and replies, so the phones never hold the answers. Each
player's emoji moves along their lane with their right answers. The first to the target
(default ten) wins the prize (default 5000) and the race ends; with more than three runners second place takes a prize (default 2000) and with more than five, third does too (default 500), each only when the place is clear-cut; whoever is alone at the bottom loses the forfeit (default 500). A player
is out the moment the questions left cannot get them to the target. If the time limit
(default two minutes) runs out first, the clear leader on right answers wins; a tie means
no winner. Players pick their emoji when they join, and it follows them onto the lobby,
the scoreboards and the podium.

**Drop the pin has two modes.** "Closest to a spot" is the map game above. "Anywhere on
the right thing" scores a hit or a miss against a box the host draws on the picture: full
speed points inside, nothing outside. The builder's collage tool tiles two to nine pictures
(uploaded, or fetched from Wikipedia by name) into one image and makes the answer's tile
the box, which is how "drop the pin on the amalgam carrier" gets built; the AI writer can
build these too by naming the things to picture. The pictures are composed on a canvas in
the browser and uploaded as one image.

**Answer Smash** follows House of Games: a picture and a clue whose answers overlap, and
the player types the two smashed together. The builder works out the overlap (the longest
run of letters that ends the first answer and starts the second) and shows it highlighted;
the host can type the smash by hand where the automatic one is wrong. Judged like a typed
answer, with the AI told the rules.

**Wheel of Fortune** puts a phrase on the show's board (four rows of 12, 14, 14 and 12
tiles, words never split, drawn in the app rather than fetched from a generator site, which
blocks automated use). Every few seconds the host turns a letter, everywhere it appears,
consonants first; players type the phrase whenever they think they have it, and points fall
with the clock. The host can turn a letter early with a button.

**Wipeout** is the one question that is not "everyone answers at once". Up to twenty
answers are scattered on the host screen, classically fifteen right and five wrong. Players
take turns in a shuffled order, each with the question's time limit per turn (default five
seconds). A right pick vanishes from the board and scores the pick points (default 200); a
wrong pick costs the picker the penalty (default 500) and ends the question for everyone;
running out of time drops that player out of the question without a penalty, so someone
away from their phone cannot stall the call. It also ends when every right answer has been
found or nobody is left. The phones show the board to everyone, live only for the player
whose turn it is. Scores accumulate during the question and are applied at the reveal, so a
player can finish the question with a negative total for it.

Drop the pin measures distance in fractions of the picture width, corrected for the
picture's aspect ratio. The builder shows both radii as rings on the picture. The closest
player is always flagged on the reveal, whatever they scored — the brief said the closest
gets the points, and the fall-off curve rewards exactly that while still letting a near miss
score something.

Video is not a separate type: any question can carry a YouTube video, which plays on the
host screen from the chosen start time when the question goes live. "Name the singer" is a
Type-the-answer question with a video.

## Typed answers and AI

The host never waits on the AI for the easy cases. When a text question ends:

1. Every answer is normalised (case, accents, punctuation, a leading "the") and compared with
   the accepted answers. Exact matches and near-misses (85% similar) are marked right
   locally.
2. Anything else goes to the edge function in one batch. Claude (`claude-opus-5`, low
   effort) is told it is a pub-quiz adjudicator: accept misspellings, abbreviations,
   alternative names and extra correct detail; reject hedges, different things and vague
   answers. It returns a verdict per player.
3. If the AI is unavailable, those answers are scored by a looser closest-match rule instead
   and the host sees a note. The game never stalls on the AI.

## AI quiz writer

From the portal: topic, count (1–40, written four at a time), difficulty, which types, whether to find pictures, and
whether to search the web. The edge function asks Claude for the questions in a fixed JSON
shape, with web search enabled to verify facts and cover recent events, then:

- fetches each requested picture from the English Wikipedia article's lead image and copies
  it into our storage bucket, so a game never depends on someone else's hosting;
- builds drop-the-pin questions on a blank map that fits the question: Claude names the
  region (the country for a city, the continent for a country, the world only when it has
  to) and the function fetches Wikipedia's label-free location map of it, with the map's
  own bounds or projection formula used to place the pin from the latitude and longitude,
  and a bullseye sized to the place in that map's scale. A place off the map's edge falls
  back to the world map. The same maps are a button away in the builder for hand-written
  pin questions;
- drops anything malformed and reports what it left out.

The questions land in the builder unsaved-then-autosaved, selected, for the host to read
through. AI can be wrong; the portal says so.

## Fact-checking

*Check all* in the toolbar, or the tick on a round, sends each finished question through a
separate pass: a different prompt that is told to trust nothing, to search the web for
anything it is not certain of, and to return a verdict per question. The list shows a
green tick (looks right), an amber question mark (worth a look: a second defensible
answer, a contested or dated fact, an option that is arguably right) or a red cross (the
marked answer is wrong), and the question's form shows the note and a suggested answer
where there is one. The verdict is tied to a hash of what was checked, so editing the
question turns it into "changed since it was checked" until it is run again. It runs four
questions per request, the same reason the writer batches. It makes an error much less
likely to reach the call; it does not make one impossible.

## Pictures

The writer names a Wikipedia article for each picture. Four sources are tried for a photo
of it, so the same subject does not always get the same picture: every photograph in the
article, the matching Wikimedia Commons category, a Commons search, and the article's lead
image. All but the lead image must name the subject in their file name and pass a filter
for logos, maps, diagrams, portraits and paintings, because article galleries drift (a
Labrador in the pug article). One is picked at random from what is left, skipping any
picture the quiz already uses, and copied into our bucket.

## Architecture

```
GitHub Pages (static)                     Supabase project safcrtrfdzsnftghibot
┌─────────────┐   Realtime broadcast     ┌─────────────────────────────────┐
│ host.html   │◄────────────────────────►│ Realtime channel quiz-<CODE>    │
│             │   + presence             │   (no database involved)        │
└─────────────┘                          └─────────────────────────────────┘
       ▲  ▲                              ┌─────────────────────────────────┐
       │  │  same channel                │ Edge function quiz-api          │
       │  ▼                              │  quizzes · uploads · AI judging │
┌─────────────┐                          │  AI writing · game results      │
│ play.html   │  (phones never call      └────────────┬────────────────────┘
└─────────────┘   the function)                       │ service role
                                          ┌───────────▼─────────────────────┐
┌─────────────┐   quiz-api (password)     │ quiz_quizzes · quiz_games       │
│ index.html  │──────────────────────────►│ bucket quiz-media (public read) │
└─────────────┘                           └─────────────────────────────────┘
```

**The live game is host-authoritative and runs entirely over Realtime.** The host's browser
holds the quiz, the clock and the scores. It broadcasts a `state` message on every change
and every two seconds as a heartbeat, so a phone that reconnects is back in step within two
seconds. Phones send `hello` on joining and `answer` when they answer; the host replies with
an `ack`, and a phone re-sends an unacknowledged answer until it gets one. The host times
every answer on its own clock from the moment it started the question, so phones can't
cheat by fiddling with theirs, and everyone shares the same network delay.

**Phones never see the right answers.** The host sends a player-view of each question with
opaque tokens in place of ids, shuffled for order and match questions, and maps them back
when scoring.

**Presence** tells the host who is connected right now, which is what "everyone has
answered" means; players who drop out don't hold up the question.

**Rounds live inside the quiz's settings blob**, not in a column of their own, so adding
them needed no migration. `LQ.normalizeQuiz` gives any older quiz a single round.

**The database only holds what outlives a session:** quizzes, pictures and final
scoreboards. RLS is on with no public policies, matching the rest of the project; the
publishable key in the browser can read nothing directly. Everything goes through the edge
function on the service role, gated by one host password kept as a Supabase secret.

**No build step, no framework.** Three HTML files, one stylesheet, one shared script,
supabase-js from a CDN. The same conventions as the other apps on this stack.

## Decisions worth knowing

- **Answers keep their builder order and colours on multiple choice.** The host lays them out
  by colour; shuffling would break "it's the blue one".
- **A question ends when everyone connected has answered**, not only at the buzzer. It keeps
  the pace up, as Kahoot does.
- **Partial credit is a per-question toggle, off by default.** All-or-nothing is the classic
  rule; partial suits longer order and match questions.
- **The password is a single shared host password**, like the other back-office pages on this
  stack, not per-user accounts. Players need nothing.
- **Pictures are copied into our bucket**, whether uploaded or found by AI, resized in the
  browser to at most 1600px before upload.
- **New repo rather than a folder in `bhb-till-portal`**, because the quiz isn't a venue
  system. It shares the Supabase project for convenience, with `quiz_` prefixes; moving it to
  its own project later is a config change in `assets/common.js` plus re-running the
  migration.

## Not built (deliberately, for now)

- Team play, or more than one host device.
- Player accounts, avatars or a history per player.
- A spectator view without answering.
- Importing questions from a spreadsheet.
- Image-only answer options for multiple choice.
- Drag-and-drop ordering on the phone (arrows are reliable on every phone; drag can come
  later).
- A short custom domain for the join link. The QR code carries the full URL so nobody has
  to type it.

## Limits

- Supabase Realtime on this plan allows a few hundred concurrent connections and a few
  hundred messages a second; the host sends one message every two seconds plus one per
  answer, so dozens of players are comfortable.
- One edge-function request has a time limit, and a big round with web search and pictures
  does not fit in it. The portal therefore asks for a round in batches of four, appending
  each batch to the quiz as it lands and telling later batches what has already been
  written so nothing repeats. Up to forty in one go.
- YouTube autoplay with sound relies on the host having clicked in the page first, which
  pressing Start guarantees.
