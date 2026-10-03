-- Taskmaster photos: a private bucket. Phones upload through quiz-api (task_photo); the host reads them back as
-- signed links (task_photos). Nothing here is public.
insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values ('quiz-tasks', 'quiz-tasks', false, 1500000, array['image/jpeg'])
on conflict (id) do nothing;
