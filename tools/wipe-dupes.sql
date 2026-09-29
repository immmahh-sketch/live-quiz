-- Wipeout boards that repeat each other: pairs of unused boards where at least 60% of the smaller board's
-- right answers are also on the other. Run after adding boards; retire the weaker copy with tools/wipe-topup.mjs.
-- Run from C:\Users\GM\Documents\Till App:
--   npx.cmd supabase db query --linked --project-ref safcrtrfdzsnftghibot -f C:/Users/GM/Documents/live-quiz/tools/wipe-dupes.sql -o csv
with r as (
  select id, lower(regexp_replace(x->>'text','[^a-zA-Z0-9]','','g')) a
  from quiz_bank, jsonb_array_elements(q->'right') x where type='wipeout' and used=false),
c as (select id, count(distinct a) n from r group by id),
p as (select r1.id i1, r2.id i2, count(distinct r1.a) shared from r r1 join r r2 on r1.a=r2.a and r1.id<r2.id group by 1,2)
select p.i1, (select q->>'text' from quiz_bank where id=p.i1) t1, c1.n n1, p.i2, (select q->>'text' from quiz_bank where id=p.i2) t2, c2.n n2, shared,
  round(shared::numeric/least(c1.n,c2.n),2) frac
from p join c c1 on c1.id=p.i1 join c c2 on c2.id=p.i2
where shared::float/least(c1.n,c2.n) >= 0.6 order by frac desc, shared desc;
