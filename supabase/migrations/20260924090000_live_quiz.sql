-- ---------------------------------------------------------------------
-- Live Quiz
--
-- Two tables and one public bucket. The live game itself never touches
-- the database: it runs over Supabase Realtime (broadcast + presence)
-- between the host's screen and the players' phones. The database only
-- holds what needs to outlive a session — the quizzes the host builds,
-- the pictures in them, and a record of who won.
--
-- RLS is on with no public policies, the same as every other app in this
-- project. The publishable key in the browser can read none of it;
-- everything goes through the quiz-api edge function on the service role.
-- ---------------------------------------------------------------------

create table if not exists quiz_quizzes (
  id          uuid primary key default gen_random_uuid(),
  title       text not null default 'Untitled quiz',
  settings    jsonb not null default '{}'::jsonb,   -- points, default time, etc.
  questions   jsonb not null default '[]'::jsonb,   -- the slides, in order
  created_at  timestamptz not null default now(),
  updated_at  timestamptz not null default now()
);
alter table quiz_quizzes enable row level security;

-- Written once at the end of a game so there is a record of the result.
create table if not exists quiz_games (
  id          uuid primary key default gen_random_uuid(),
  code        text not null,
  quiz_id     uuid references quiz_quizzes(id) on delete set null,
  title       text,
  players     jsonb not null default '[]'::jsonb,   -- [{name, score, rank, correct}]
  questions   integer not null default 0,
  started_at  timestamptz,
  ended_at    timestamptz not null default now()
);
alter table quiz_games enable row level security;

-- Pictures for questions. Public so the host screen and every phone can
-- load them with a plain <img>; uploads only ever come through the edge
-- function, which is the only thing holding a key that can write.
insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values ('quiz-media', 'quiz-media', true, 8388608,
        array['image/jpeg', 'image/png', 'image/webp', 'image/gif'])
on conflict (id) do update
  set public = excluded.public,
      file_size_limit = excluded.file_size_limit,
      allowed_mime_types = excluded.allowed_mime_types;
