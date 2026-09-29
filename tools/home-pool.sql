-- Unused, unflagged, picture-free choice, typed and 1% Club questions: the candidates for the play-at-home games.
-- Run with: npx.cmd supabase db query --linked --project-ref safcrtrfdzsnftghibot -f tools/home-pool.sql -o json > <dir>/pool.json
select id, type, difficulty, q from quiz_bank
where type in ('choice','text','club') and not used and q->'used' is null
 and coalesce(q->>'tooEasy','false')='false' and coalesce(q->>'giveaway','false')='false'
 and coalesce(q->>'doubt','false')='false' and coalesce(q->>'recycled','false')='false'
 and coalesce(q->>'local','false')='false' and coalesce(q->'media'->>'kind','none')='none'
order by id;
