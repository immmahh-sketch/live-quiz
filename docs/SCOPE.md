# Live Quiz — scope and design

*Written 23 September 2026, alongside the first build.*

## What it is

A live, Kahoot-style quiz played over a video call. One person hosts from a desktop browser
and shares their screen; everyone else plays on their phone. The host builds quizzes
beforehand in a portal, or has AI write them. A game is a live session that starts when the
host opens the lobby and ends with the podium.

## The three pages

**Portal — `index.html`.** Password sign-in. A list of quizzes with Host / Edit / Duplicate /
Delete, and *Recent games*. The builder: a question list on the left (reorder, duplicate,
delete), the selected question's form on the right. Each question has its text, the
type-specific answers, optional media (picture upload or link, or a YouTube link with a
start time), a time limit, and for order/match a partial-credit toggle. Quiz settings hold
the points curve and default time. Autosaves two seconds after a change; *Host live* saves
first and refuses to start while a question is unfinished (it selects the one that needs
attention and says why).

**Host screen — `host.html`.** Designed for screen sharing: big type, dark stage, one thing
at a time.

1. *Lobby* — QR code, six-character code, short link, players appearing as they join.
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
- builds drop-the-pin questions on a plain equirectangular world map (copied once from
  Wikimedia Commons) from the latitude and longitude Claude gives, with a bullseye sized to
  the place;
- drops anything malformed and reports what it left out.

The questions land in the builder unsaved-then-autosaved, selected, for the host to read
through. AI can be wrong; the portal says so.

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
