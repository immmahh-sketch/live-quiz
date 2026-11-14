-- ---------------------------------------------------------------------
-- The Box Clever game pool (tvbox/games): which games have been used, on any device
--
-- Box2p (the Fire TV) and the phone app both play the same 50 games, each once. A device claims a game when it starts it and marks it
-- played when it ends, so a game played on the Fire Stick is never offered in the car, and two devices never start the same game.
-- No names or scores are kept: only the game id, a device id, and when. RLS on, no public policies: quiz-api is the only reader and
-- writer (pool_state, pool_claim, pool_done, pool_reset).
-- ---------------------------------------------------------------------

create table if not exists quiz_box_pool (
  pool        text not null,                       -- 'BOX2P'
  game        text not null,                       -- 'g07'
  dev         text not null default '',            -- the device that claimed it
  state       text not null default 'claimed' check (state in ('claimed', 'played')),
  claimed_at  timestamptz not null default now(),
  played_at   timestamptz,
  primary key (pool, game)
);
alter table quiz_box_pool enable row level security;
