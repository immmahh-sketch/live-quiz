-- The full record of a finished game: every question, every player's answer, whether it
-- was right and what it scored. The portal's Reports view reads it; the scoreboard in
-- `players` stays as the quick summary the games list uses.
alter table quiz_games add column if not exists report jsonb;
