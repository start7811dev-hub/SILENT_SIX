create or replace function public.s6_mission_ok(m text) returns boolean language sql immutable set search_path = public as $$
  select m ~ '^(S1-(0[1-9]|1[0-2])|P-(raven|viper|glitch|brick|mirage|doc)-[1-3]|W-[1-5]|C-(raven|viper|glitch|brick|mirage|doc))$'
$$;

create or replace function public.s6_buy_cut(p_kind text, p_agent text, p_k integer) returns jsonb language plpgsql security definer set search_path = public as $$
declare u uuid := s6_uid(); unit integer; cap integer; lo integer; hi integer; cost integer := 0; k integer; bal integer; ok boolean;
begin
  perform s6_ensure(u);
  if p_agent !~ '^(raven|viper|glitch|brick|mirage|doc)$' then raise exception 'bad item'; end if;
  if p_kind = 'n' then unit := 30; cap := 120; lo := 2; hi := 6;
    select count(distinct mission) = 3 into ok from clears where user_id = u and diff >= 2 and mission in ('P-' || p_agent || '-1', 'P-' || p_agent || '-2', 'P-' || p_agent || '-3');
  elsif p_kind = 'c' then unit := 50; lo := 1;
    hi := case p_agent when 'raven' then 10 when 'viper' then 8 when 'glitch' then 11 when 'brick' then 10 when 'mirage' then 12 else 11 end;
    cap := 100000;
    select exists (select 1 from clears where user_id = u and mission = 'C-' || p_agent) into ok;
  else raise exception 'bad item'; end if;
  if not coalesce(ok, false) then raise exception 'not eligible'; end if;
  if p_k <> 0 and p_k not between lo and hi then raise exception 'bad item'; end if;
  if p_k = 0 then
    for k in lo..hi loop
      if not exists (select 1 from unlocks where user_id = u and item = p_kind || ':' || p_agent || ':' || k) then cost := cost + case when p_kind = 'c' then 30 else unit end; end if;
    end loop;
    cost := least(cost, cap);
  else
    if exists (select 1 from unlocks where user_id = u and item = p_kind || ':' || p_agent || ':' || p_k) then return s6_state(); end if;
    cost := unit;
  end if;
  select pt into bal from profiles where id = u for update;
  if bal < cost then raise exception 'not enough points'; end if;
  if cost > 0 then
    update profiles set pt = pt - cost, updated_at = now() where id = u;
    insert into ledger(user_id, delta, reason, ref) values (u, -cost, 'cut', p_kind || ':' || p_agent || ':' || p_k);
  end if;
  if p_k = 0 then
    insert into unlocks(user_id, item) select u, p_kind || ':' || p_agent || ':' || g from generate_series(lo, hi) g on conflict do nothing;
  else
    insert into unlocks(user_id, item) values (u, p_kind || ':' || p_agent || ':' || p_k) on conflict do nothing;
  end if;
  return s6_state();
end $$;