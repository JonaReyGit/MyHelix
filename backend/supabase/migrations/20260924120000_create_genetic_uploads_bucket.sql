-- Private bucket for raw DNA exports. Files are namespaced by user id: <user_id>/<timestamp>_<filename>
insert into storage.buckets (id, name, public)
values ('genetic-uploads', 'genetic-uploads', false)
on conflict (id) do nothing;

create policy "Users can upload to their own folder"
  on storage.objects for insert
  with check (
    bucket_id = 'genetic-uploads'
    and (storage.foldername(name))[1] = auth.uid()::text
  );

create policy "Users can read their own uploads"
  on storage.objects for select
  using (
    bucket_id = 'genetic-uploads'
    and (storage.foldername(name))[1] = auth.uid()::text
  );

create policy "Users can delete their own uploads"
  on storage.objects for delete
  using (
    bucket_id = 'genetic-uploads'
    and (storage.foldername(name))[1] = auth.uid()::text
  );
