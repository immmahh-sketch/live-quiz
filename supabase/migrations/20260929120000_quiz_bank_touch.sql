-- Every change to a bank row stamps updated_at, so the quiz-api function can keep the bank in memory and fetch only
-- what has changed since it last looked (reading whole types on every call blew the Free plan's egress, Sept 2026).
create or replace function quiz_bank_touch() returns trigger language plpgsql as $$
begin
  new.updated_at := now();
  return new;
end $$;
drop trigger if exists quiz_bank_touch on quiz_bank;
create trigger quiz_bank_touch before update on quiz_bank for each row execute function quiz_bank_touch();
create index if not exists quiz_bank_type_updated on quiz_bank (type, updated_at);
