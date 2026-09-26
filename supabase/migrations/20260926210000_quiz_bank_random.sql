-- A few random questions of one bank type, for the public demo. Read-only: it never stamps an
-- item as used, so trying the demo never takes a question out of stock. Rejected items are left out.
create or replace function quiz_bank_random(t text, n int)
returns setof jsonb
language sql
stable
as $$
  select q from quiz_bank
  where type = t and coalesce(q->'used'->>'rejected', 'false') <> 'true'
  order by random()
  limit least(greatest(n, 0), 10);
$$;
revoke all on function quiz_bank_random(text, int) from public, anon, authenticated;
grant execute on function quiz_bank_random(text, int) to service_role;
