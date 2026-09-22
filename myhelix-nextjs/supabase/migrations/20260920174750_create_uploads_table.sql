create table uploads(
  id uuid primary key default gen_random_uuid(),
  user_id uuid references auth.users(id) not null,
  file_name varchar not null,
  storage_path varchar not null,
  genome_build varchar not null default 'unknown' check (genome_build in ('hg-19', 'hg-38', 'unknown')),
  status varchar not null default 'pending' check (status in ('pending', 'processing', 'complete', 'failed')),
  uploaded_at timestamptz not null default now()
);

alter table uploads enable row level security;

create policy "Users can view their own uploads"
  on uploads for select
  using (auth.uid() = user_id);

create policy "Users can insert their own uploads"
  on uploads for insert
  with check (auth.uid() = user_id);