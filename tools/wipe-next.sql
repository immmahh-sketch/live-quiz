-- The next Wipeout boards to repair: fewest right answers first, skipping retired (rejected) ones.
-- Run from C:\Users\GM\Documents\Till App:
--   npx.cmd supabase db query --linked --project-ref safcrtrfdzsnftghibot -f C:/Users/GM/Documents/live-quiz/tools/wipe-next.sql -o csv
select id, q->>'text' as board, category,
  jsonb_array_length(coalesce(q->'right','[]'::jsonb)) as r, jsonb_array_length(coalesce(q->'wrong','[]'::jsonb)) as w,
  (select string_agg(x->>'text', ' | ') from jsonb_array_elements(q->'right') x) as right_answers,
  (select string_agg(x->>'text', ' | ') from jsonb_array_elements(q->'wrong') x) as wrong_answers
from quiz_bank
where type = 'wipeout' and coalesce(q->'used'->>'rejected', 'false') <> 'true'
  and (jsonb_array_length(coalesce(q->'right','[]'::jsonb)) < 12 or jsonb_array_length(coalesce(q->'wrong','[]'::jsonb)) < 5)
order by r, w, id
limit 25;
