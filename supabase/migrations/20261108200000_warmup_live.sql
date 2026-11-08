-- ---------------------------------------------------------------------
-- Warm-up games that have been started
--
-- A warm-up only wrote a row (quiz_warmup_plays) when a go finished, so the host could not see someone who
-- started and gave up, or who was playing right now. A phone now pings quiz-api (warmup_start) when a go begins
-- and every ~20 seconds while it runs; the row is removed when the score is saved. One row per device per season.
--
-- Only the host sees this (the builder's scoreboard, behind the host password). RLS on, no public policies: the
-- edge function is the only reader and writer, and no player-facing action returns it. Bots are never written.
-- ---------------------------------------------------------------------

create table if not exists quiz_warmup_live (
  code        text not null,
  season      text not null default '',
  pid         text not null,                 -- the device's player id
  quiz_id     uuid references quiz_quizzes(id) on delete set null,
  game_code   text not null default '',
  name        text not null default '',
  emoji       text not null default '',
  started_at  timestamptz not null default now(),   -- when this go began
  seen_at     timestamptz not null default now(),   -- the last ping from the phone
  progress    text not null default '',      -- "📦 14 of 25 boxes", "Question 6 of 20"
  step        integer not null default 0,
  total       integer not null default 0,
  primary key (code, season, pid)
);
alter table quiz_warmup_live enable row level security;
create index if not exists quiz_warmup_live_seen on quiz_warmup_live (seen_at desc);
