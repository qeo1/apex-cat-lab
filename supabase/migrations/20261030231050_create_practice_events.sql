create table public.practice_events (
  event_id uuid not null,
  user_id uuid not null references auth.users (id) on delete cascade,
  question_key text not null,
  section text not null check (section in ('VARC', 'DILR', 'QUANT', 'UNKNOWN')),
  is_correct boolean not null,
  occurred_at timestamptz not null default now(),
  primary key (user_id, event_id)
);

create index practice_events_user_occurred_idx
  on public.practice_events (user_id, occurred_at desc);

alter table public.practice_events enable row level security;

create policy "Users can read their own practice events"
  on public.practice_events for select
  to authenticated
  using ((select auth.uid()) = user_id);

create policy "Users can add their own practice events"
  on public.practice_events for insert
  to authenticated
  with check ((select auth.uid()) = user_id);

create policy "Users can reconcile their own practice events"
  on public.practice_events for update
  to authenticated
  using ((select auth.uid()) = user_id)
  with check ((select auth.uid()) = user_id);

revoke all on public.practice_events from anon, public;
grant usage on schema public to authenticated;
grant select, insert, update on public.practice_events to authenticated;

