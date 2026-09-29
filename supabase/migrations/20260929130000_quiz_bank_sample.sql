-- A random sample of a type's unused questions, for picks where any question will do (a mixed round, a general
-- knowledge game): the quiz-api function reads this instead of the whole type, which kept the Free plan's egress
-- far over its limit (Sept 2026). At most 1,000 rows: PostgREST's cap on a response.
create or replace function quiz_bank_sample(t text, n int)
returns setof jsonb
language sql
volatile
as $$
  select q from quiz_bank where type = t and not used order by random() limit least(greatest(n, 0), 1000);
$$;
revoke all on function quiz_bank_sample(text, int) from public, anon, authenticated;
grant execute on function quiz_bank_sample(text, int) to service_role;
