-- Each warm-up go keeps what the player answered, question by question, so the host can look through it.
alter table quiz_warmup_plays add column if not exists answers jsonb;
