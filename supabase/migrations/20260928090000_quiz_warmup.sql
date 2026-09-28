-- ---------------------------------------------------------------------
-- Warm-up games
--
-- A quiz can be opened as a warm-up (settings.warmup = { code, open }):
-- anyone with the code plays it on their own device against three bots,
-- with friends free to join. Each real player's score is written here
-- when their game ends, one row per device (the player id their phone
-- keeps), so a device plays once. Bots are never written.
--
-- RLS on, no public policies: only the quiz-api edge function reads and
-- writes it.
-- ---------------------------------------------------------------------

create table if not exists quiz_warmup_plays (
  id          uuid primary key default gen_random_uuid(),
  code        text not null,                 -- the warm-up code (settings.warmup.code)
  quiz_id     uuid references quiz_quizzes(id) on delete set null,
  game_code   text not null default '',      -- the six-letter code of that game
  pid         text not null,                 -- the device's player id
  name        text not null default '',
  emoji       text not null default '',
  score       integer not null default 0,
  rank        integer not null default 0,    -- place in that game, bots included
  players     integer not null default 1,    -- real players in that game
  bots        integer not null default 0,
  started_at  timestamptz,
  played_at   timestamptz not null default now(),
  unique (code, pid)
);
alter table quiz_warmup_plays enable row level security;
create index if not exists quiz_warmup_plays_board on quiz_warmup_plays (code, score desc);
