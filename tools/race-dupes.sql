-- Races that repeat each other: pairs of unused races sharing 10 or more right answers, with a count of rows
-- whose clue also matches. Stored race rows are {text, options}; options[0] is the right answer.
-- Read the top pairs before retiring: the same answers asked in a different way (e.g. 'which band was this
-- singer in?' and 'which act had this hit?') can be a fair, separate race. Retire true repeats with
--   LQ_PASSWORD=… node tools/bank-retire.mjs race <id> …
-- Run from C:\Users\GM\Documents\Till App:
--   npx.cmd supabase db query --linked --project-ref safcrtrfdzsnftghibot -f C:/Users/GM/Documents/live-quiz/tools/race-dupes.sql -o csv
with r as (
  select id, lower(regexp_replace(x->'options'->>0,'[^a-zA-Z0-9]','','g')) a, lower(regexp_replace(x->>'text','[^a-zA-Z0-9]','','g')) p
  from quiz_bank, jsonb_array_elements(q->'bank') x where type='race' and used=false),
pa as (select r1.id i1, r2.id i2, count(distinct r1.a) sa from r r1 join r r2 on r1.a=r2.a and r1.id<r2.id group by 1,2 having count(distinct r1.a) >= 10),
pp as (select r1.id i1, r2.id i2, count(*) sp from r r1 join r r2 on r1.a=r2.a and r1.id<r2.id and (r1.p=r2.p or position(r1.p in r2.p)>0 or position(r2.p in r1.p)>0) group by 1,2)
select pa.i1, (select q->>'text' from quiz_bank where id=pa.i1) t1, pa.i2, (select q->>'text' from quiz_bank where id=pa.i2) t2, pa.sa same_answers, coalesce(pp.sp,0) same_clue_and_answer
from pa left join pp on pp.i1=pa.i1 and pp.i2=pa.i2 order by coalesce(pp.sp,0) desc, pa.sa desc;
