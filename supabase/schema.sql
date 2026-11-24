-- SILENT SIX — Supabase schema v1
-- Supabase 대시보드 > SQL Editor 에 전체를 붙여 넣고 Run. 여러 번 실행해도 안전하다.
-- 원칙: 클라이언트는 테이블에 직접 쓰지 못한다. 모든 쓰기는 아래 s6_* 함수로만 한다.

create table if not exists public.profiles(
  id uuid primary key references auth.users(id) on delete cascade,
  name text not null default '',
  pt integer not null default 0 check (pt >= 0),
  is_admin boolean not null default false,
  imported boolean not null default false,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
create table if not exists public.clears(
  user_id uuid not null references auth.users(id) on delete cascade,
  mission text not null,
  diff smallint not null check (diff between 0 and 3),
  best_time integer not null,
  best_score integer not null,
  updated_at timestamptz not null default now(),
  primary key(user_id, mission, diff)
);
create index if not exists clears_rank on public.clears(mission, diff, best_score desc);
create table if not exists public.badges(
  user_id uuid not null references auth.users(id) on delete cascade,
  mission text not null,
  bits smallint not null default 0 check (bits between 0 and 7),
  primary key(user_id, mission)
);
alter table public.badges add column if not exists hbest smallint not null default 0 check (hbest between 0 and 3); -- HARD 이상 '한 판'에서 딴 배지의 최고 개수(클리어 이미지 단계)
create table if not exists public.unlocks(
  user_id uuid not null references auth.users(id) on delete cascade,
  item text not null,
  created_at timestamptz not null default now(),
  primary key(user_id, item)
);
create table if not exists public.ledger(
  id bigserial primary key,
  user_id uuid not null references auth.users(id) on delete cascade,
  delta integer not null,
  reason text not null,
  ref text,
  created_at timestamptz not null default now()
);
create index if not exists ledger_user on public.ledger(user_id, created_at desc);
create table if not exists public.app_config(
  id smallint primary key check (id = 1),
  data jsonb not null default '{}'::jsonb,
  updated_at timestamptz not null default now(),
  updated_by uuid
);
insert into public.app_config(id) values (1) on conflict do nothing;

alter table public.profiles enable row level security;
alter table public.clears enable row level security;
alter table public.badges enable row level security;
alter table public.unlocks enable row level security;
alter table public.ledger enable row level security;
alter table public.app_config enable row level security;

drop policy if exists own_profiles on public.profiles;
create policy own_profiles on public.profiles for select to authenticated using (id = (select auth.uid()));
drop policy if exists own_clears on public.clears;
create policy own_clears on public.clears for select to authenticated using (user_id = (select auth.uid()));
drop policy if exists own_badges on public.badges;
create policy own_badges on public.badges for select to authenticated using (user_id = (select auth.uid()));
drop policy if exists own_unlocks on public.unlocks;
create policy own_unlocks on public.unlocks for select to authenticated using (user_id = (select auth.uid()));
drop policy if exists own_ledger on public.ledger;
create policy own_ledger on public.ledger for select to authenticated using (user_id = (select auth.uid()));
drop policy if exists read_config on public.app_config;
create policy read_config on public.app_config for select to anon, authenticated using (true);

revoke insert, update, delete, truncate on public.profiles, public.clears, public.badges, public.unlocks, public.ledger, public.app_config from anon, authenticated;

-- 내부 도우미 ---------------------------------------------------------------
create or replace function public.s6_uid() returns uuid language plpgsql stable set search_path = public as $$
declare u uuid := auth.uid();
begin
  if u is null then raise exception 'login required' using errcode = '28000'; end if;
  return u;
end $$;

create or replace function public.s6_mission_ok(m text) returns boolean language sql immutable set search_path = public as $$
  select m ~ '^(S1-(0[1-9]|1[0-2])|P-(raven|viper|glitch|brick|mirage|doc)-[1-3]|W-[1-5]|C-(raven|viper|glitch|brick|mirage|doc))$'
$$;

create or replace function public.s6_gcost(k integer) returns integer language sql immutable set search_path = public as $$
  select case when k in (1) then 25 when k in (2,3) then 15 when k between 4 and 7 then 10 else null end
$$;

create or replace function public.s6_ensure(u uuid) returns void language sql security definer set search_path = public as $$
  insert into profiles(id) values (u) on conflict do nothing
$$;

-- 내 상태 전체 ---------------------------------------------------------------
create or replace function public.s6_state() returns jsonb language plpgsql security definer set search_path = public as $$
declare u uuid := s6_uid();
begin
  perform s6_ensure(u);
  return jsonb_build_object(
    'profile', (select jsonb_build_object('name', name, 'pt', pt, 'admin', is_admin, 'imported', imported) from profiles where id = u),
    'clears', coalesce((select jsonb_agg(jsonb_build_object('m', mission, 'd', diff, 't', best_time, 's', best_score)) from clears where user_id = u), '[]'::jsonb),
    'badges', coalesce((select jsonb_object_agg(mission, bits) from badges where user_id = u), '{}'::jsonb),
    'hbest', coalesce((select jsonb_object_agg(mission, hbest) from badges where user_id = u and hbest > 0), '{}'::jsonb),
    'unlocks', coalesce((select jsonb_agg(item) from unlocks where user_id = u), '[]'::jsonb)
  );
end $$;

-- 미션 클리어 기록. 점수 한도와 간격을 서버에서 확인하고 포인트를 적립한다.
create or replace function public.s6_clear(p_mission text, p_diff integer, p_time integer, p_score integer, p_bits integer, p_kv text default null)
returns jsonb language plpgsql security definer set search_path = public as $$
declare u uuid := s6_uid(); gain integer; last_at timestamptz; cap integer; prev integer;
begin
  perform s6_ensure(u);
  if not s6_mission_ok(p_mission) or p_diff not between 0 and 3 then raise exception 'bad mission'; end if;
  cap := round(11000 * (array[0.6,0.8,1.0,1.5])[p_diff + 1]);
  if p_score < 0 or p_score > cap or p_time < 8 or p_time > 86400 or p_bits not between 0 and 7 then raise exception 'bad result'; end if;
  select max(created_at) into last_at from ledger where user_id = u and reason = 'clear';
  if last_at is not null and now() - last_at < interval '8 seconds' then raise exception 'too fast'; end if;

  select best_score into prev from clears where user_id = u and mission = p_mission and diff = p_diff;
  insert into clears(user_id, mission, diff, best_time, best_score) values (u, p_mission, p_diff, p_time, p_score)
  on conflict (user_id, mission, diff) do update
    set best_time = least(clears.best_time, excluded.best_time),
        best_score = greatest(clears.best_score, excluded.best_score),
        updated_at = now();
  insert into badges(user_id, mission, bits, hbest) values (u, p_mission, p_bits, case when p_diff >= 2 then (p_bits & 1) + ((p_bits >> 1) & 1) + ((p_bits >> 2) & 1) else 0 end)
  on conflict (user_id, mission) do update set bits = badges.bits | excluded.bits, hbest = greatest(badges.hbest, excluded.hbest);
  if p_kv is not null and p_kv ~ '^g:(raven|viper|glitch|brick|mirage|doc):[1-7]$' then
    insert into unlocks(user_id, item) values (u, p_kv) on conflict do nothing;
  end if;
  -- 같은 미션 · 난이도 재클리어는 30%. 그 난이도 최고 점수를 넘기면 전액.
  gain := round(p_score / 100.0);
  if prev is not null and p_score <= prev then gain := round(gain * 0.3); end if;
  update profiles set pt = pt + gain, updated_at = now() where id = u;
  insert into ledger(user_id, delta, reason, ref) values (u, gain, 'clear', p_mission || ':' || p_diff);
  return s6_state();
end $$;

-- 갤러리 해금. 값은 서버가 정한다. p_k = 0 이면 그 요원 전체(최대 15P).
create or replace function public.s6_buy(p_agent text, p_k integer) returns jsonb language plpgsql security definer set search_path = public as $$
declare u uuid := s6_uid(); cost integer := 0; k integer; bal integer;
begin
  perform s6_ensure(u);
  if p_agent !~ '^(raven|viper|glitch|brick|mirage|doc)$' or p_k not between 0 and 7 then raise exception 'bad item'; end if;
  if p_k = 0 then
    for k in 1..7 loop
      if not exists (select 1 from unlocks where user_id = u and item = 'g:' || p_agent || ':' || k) then cost := cost + s6_gcost(k); end if;
    end loop;
    cost := least(cost, 75);
  else
    if exists (select 1 from unlocks where user_id = u and item = 'g:' || p_agent || ':' || p_k) then return s6_state(); end if;
    cost := s6_gcost(p_k);
  end if;
  select pt into bal from profiles where id = u for update;
  if bal < cost then raise exception 'not enough points'; end if;
  if cost > 0 then
    update profiles set pt = pt - cost, updated_at = now() where id = u;
    insert into ledger(user_id, delta, reason, ref) values (u, -cost, 'gallery', p_agent || ':' || p_k);
  end if;
  if p_k = 0 then
    insert into unlocks(user_id, item) select u, 'g:' || p_agent || ':' || g from generate_series(1, 7) g on conflict do nothing;
  else
    insert into unlocks(user_id, item) values (u, 'g:' || p_agent || ':' || p_k) on conflict do nothing;
  end if;
  return s6_state();
end $$;

-- 리워드 컷 소장(포인트 구매). kind 'n' = 로맨틱 "그날 밤" 2~6번 컷(1번은 기본 제공), kind 'c' = 코스튬 1번~마지막 컷(0번은 기본 제공, 고자극 추가 컷 포함). 남은 컷 전부는 컷당 30P.
-- p_k = 0 이면 남은 컷 전부(상한가 적용). 권한: n 은 TAKE 1·2·3 모두 HARD 이상, c 는 해당 코스튬 미션 클리어.
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

-- 개인 미션 3장을 끝낸 요원의 "그날 밤" 그림
create or replace function public.s6_end(p_agent text) returns jsonb language plpgsql security definer set search_path = public as $$
declare u uuid := s6_uid();
begin
  if not exists (select 1 from clears where user_id = u and mission = 'P-' || p_agent || '-3') then raise exception 'not cleared'; end if;
  insert into unlocks(user_id, item) values (u, 'end:' || p_agent) on conflict do nothing;
  return s6_state();
end $$;

create or replace function public.s6_name(p_name text) returns jsonb language plpgsql security definer set search_path = public as $$
declare u uuid := s6_uid();
begin
  perform s6_ensure(u);
  update profiles set name = left(regexp_replace(btrim(coalesce(p_name, '')), '[<>&"'']', '', 'g'), 12), updated_at = now() where id = u;
  return s6_state();
end $$;

-- 로그인 전 기기에 쌓인 기록을 계정으로 한 번만 옮긴다.
create or replace function public.s6_import(p jsonb) returns jsonb language plpgsql security definer set search_path = public as $$
declare u uuid := s6_uid(); r jsonb; done boolean; total integer := 0; grant_pt integer; it text; cap integer;
begin
  perform s6_ensure(u);
  select imported into done from profiles where id = u for update;
  if done then return s6_state(); end if;
  for r in select * from jsonb_array_elements(coalesce(p->'clears', '[]'::jsonb)) limit 200 loop
    if s6_mission_ok(r->>'m') and (r->>'d')::int between 0 and 3 then
      cap := round(11000 * (array[0.6,0.8,1.0,1.5])[(r->>'d')::int + 1]);
      if (r->>'s')::int between 0 and cap and (r->>'t')::int between 8 and 86400 then
        insert into clears(user_id, mission, diff, best_time, best_score) values (u, r->>'m', (r->>'d')::int, (r->>'t')::int, (r->>'s')::int)
        on conflict (user_id, mission, diff) do update set best_time = least(clears.best_time, excluded.best_time), best_score = greatest(clears.best_score, excluded.best_score);
        total := total + (r->>'s')::int;
      end if;
    end if;
  end loop;
  for r in select jsonb_build_object('m', key, 'b', value) from jsonb_each(coalesce(p->'badges', '{}'::jsonb)) limit 100 loop
    if s6_mission_ok(r->>'m') and (r->>'b')::int between 0 and 7 and exists (select 1 from clears where user_id = u and mission = r->>'m') then
      insert into badges(user_id, mission, bits) values (u, r->>'m', (r->>'b')::int)
      on conflict (user_id, mission) do update set bits = badges.bits | excluded.bits;
    end if;
  end loop;
  for r in select jsonb_build_object('m', key, 'b', value) from jsonb_each(coalesce(p->'hbest', '{}'::jsonb)) limit 100 loop
    if s6_mission_ok(r->>'m') and (r->>'b')::int between 0 and 3 and exists (select 1 from clears where user_id = u and mission = r->>'m' and diff >= 2) then
      update badges set hbest = greatest(hbest, least((r->>'b')::int, (bits & 1) + ((bits >> 1) & 1) + ((bits >> 2) & 1))) where user_id = u and mission = r->>'m';
    end if;
  end loop;
  for it in select jsonb_array_elements_text(coalesce(p->'unlocks', '[]'::jsonb)) limit 100 loop
    if it ~ '^g:(raven|viper|glitch|brick|mirage|doc):[1-7]$'
       or (it ~ '^n:(raven|viper|glitch|brick|mirage|doc):[2-6]$' and (select count(distinct mission) = 3 from clears where user_id = u and diff >= 2 and mission like 'P-' || split_part(it, ':', 2) || '-%'))
       or (it ~ '^end:(raven|viper|glitch|brick|mirage|doc)$' and exists (select 1 from clears where user_id = u and mission = 'P-' || split_part(it, ':', 2) || '-3')) then
      insert into unlocks(user_id, item) values (u, it) on conflict do nothing;
    end if;
  end loop;
  -- 포인트는 옮긴 기록으로 설명되는 만큼만 인정한다(최고 점수 합의 3배분, 최대 3000P).
  grant_pt := least(greatest(coalesce((p->>'pt')::int, 0), 0), round(total / 100.0 * 3)::int, 3000);
  update profiles set pt = pt + grant_pt, imported = true, name = case when name = '' then left(regexp_replace(btrim(coalesce(p->>'name', '')), '[<>&"'']', '', 'g'), 12) else name end, updated_at = now() where id = u;
  if grant_pt > 0 then insert into ledger(user_id, delta, reason, ref) values (u, grant_pt, 'import', null); end if;
  return s6_state();
end $$;

-- 내 기록 지우기
create or replace function public.s6_reset() returns jsonb language plpgsql security definer set search_path = public as $$
declare u uuid := s6_uid(); bal integer;
begin
  perform s6_ensure(u);
  delete from clears where user_id = u; delete from badges where user_id = u; delete from unlocks where user_id = u;
  select pt into bal from profiles where id = u for update;
  update profiles set pt = 0, updated_at = now() where id = u;
  insert into ledger(user_id, delta, reason) values (u, -bal, 'reset');
  return s6_state();
end $$;

-- 랭킹. p_mission 이 null 이면 스토리 미션 통합(미션별 최고 점수의 합).
create or replace function public.s6_rank(p_mission text default null, p_diff integer default null, p_limit integer default 50)
returns table(rank bigint, name text, score bigint, best_time integer, me boolean)
language sql stable security definer set search_path = public as $$
  with b as (
    select user_id, mission, max(best_score) as s, min(best_time) as t from clears
    where (p_diff is null or diff = p_diff) and (case when p_mission is null then mission like 'S1-%' else mission = p_mission end)
    group by user_id, mission
  ), a as (
    select user_id, sum(s)::bigint as score, case when p_mission is null then null else min(t) end as t from b group by user_id
  ), r as (
    select row_number() over (order by a.score desc, a.t asc nulls last, a.user_id) as rank, a.user_id, a.score, a.t from a
  )
  select r.rank, case when coalesce(p.name, '') = '' then 'HANDLER' else p.name end, r.score, r.t, coalesce(r.user_id = auth.uid(), false)
  from r left join profiles p on p.id = r.user_id
  where r.rank <= least(greatest(p_limit, 1), 100) or r.user_id = auth.uid()
  order by r.rank
$$;

-- 관리자: 공개 설정 저장
create or replace function public.s6_cfg_set(p jsonb) returns jsonb language plpgsql security definer set search_path = public as $$
declare u uuid := s6_uid();
begin
  if not exists (select 1 from profiles where id = u and is_admin) then raise exception 'admin only' using errcode = '42501'; end if;
  if pg_column_size(p) > 65536 then raise exception 'too large'; end if;
  update app_config set data = p, updated_at = now(), updated_by = u where id = 1;
  return p;
end $$;

revoke all on function public.s6_uid(), public.s6_mission_ok(text), public.s6_gcost(integer), public.s6_ensure(uuid), public.s6_state(),
  public.s6_clear(text,integer,integer,integer,integer,text), public.s6_buy(text,integer), public.s6_buy_cut(text,text,integer), public.s6_end(text), public.s6_name(text),
  public.s6_import(jsonb), public.s6_reset(), public.s6_rank(text,integer,integer), public.s6_cfg_set(jsonb) from public, anon, authenticated;
grant execute on function public.s6_state(),
  public.s6_clear(text,integer,integer,integer,integer,text), public.s6_buy(text,integer), public.s6_buy_cut(text,text,integer), public.s6_end(text), public.s6_name(text),
  public.s6_import(jsonb), public.s6_reset(), public.s6_cfg_set(jsonb) to authenticated;
grant execute on function public.s6_rank(text,integer,integer) to anon, authenticated;

-- 관리자 지정(첫 구글 로그인 뒤, 본인 이메일로 바꿔 한 번 실행):
-- update public.profiles set is_admin = true where id = (select id from auth.users where email = '본인 구글 이메일');
