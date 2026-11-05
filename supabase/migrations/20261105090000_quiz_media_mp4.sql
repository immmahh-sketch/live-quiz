-- A short muted clip can fill a Picture Reveal (it loops under the tiles).
update storage.buckets
   set allowed_mime_types = array['image/jpeg', 'image/png', 'image/webp', 'image/gif', 'audio/mpeg', 'video/mp4']
 where id = 'quiz-media';
