-- A game that can be played more than once (settings.warmup.replay) keeps each phone's best go and counts the goes.
alter table quiz_warmup_plays add column if not exists goes integer not null default 1;
