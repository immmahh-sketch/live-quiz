-- "Let them replay" can now allow a practice go that leaves the scoreboard alone: the row stays, flagged, and the
-- device may play once more; its first score stands (the save never overwrites it) and the flag clears.
alter table quiz_warmup_plays add column if not exists test_go boolean not null default false;
