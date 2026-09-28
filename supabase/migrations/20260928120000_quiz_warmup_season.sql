-- Warm-up seasons: a warm-up runs until a set time (settings.warmup.until), and its scores belong to that run.
-- Setting a new end date for a later quiz starts a fresh scoreboard, so every phone can play again.
alter table quiz_warmup_plays add column if not exists season text not null default '';
alter table quiz_warmup_plays drop constraint if exists quiz_warmup_plays_code_pid_key;
create unique index if not exists quiz_warmup_plays_one_go on quiz_warmup_plays (code, season, pid);
