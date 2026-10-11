-- Run in a NEW Supabase project, never in the Xyool production project.
BEGIN;
CREATE TABLE public.couple_members(
 user_id uuid PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
 role text UNIQUE NOT NULL CHECK(role IN ('person_one','person_two')),
 added_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE public.couple_room(
 id smallint PRIMARY KEY CHECK(id=1),
 salt text NOT NULL,
 verifier_iv text,
 verifier_ciphertext text,
 CONSTRAINT verifier_pair CHECK ((verifier_iv IS NULL) = (verifier_ciphertext IS NULL))
);
INSERT INTO public.couple_room(id,salt) VALUES(1,encode(gen_random_uuid()::text::bytea,'base64'));
CREATE TABLE public.couple_messages(
 id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
 sender_id uuid NOT NULL REFERENCES auth.users(id),
 iv text NOT NULL CHECK(length(iv) BETWEEN 16 AND 64),
 ciphertext text NOT NULL CHECK(length(ciphertext) BETWEEN 16 AND 12000),
 created_at timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX couple_messages_latest_idx ON public.couple_messages(created_at DESC);
ALTER TABLE public.couple_members ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.couple_room ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.couple_messages ENABLE ROW LEVEL SECURITY;
CREATE POLICY "member sees own membership" ON public.couple_members
 FOR SELECT TO authenticated USING(user_id=(SELECT auth.uid()));
CREATE POLICY "member sees room" ON public.couple_room
 FOR SELECT TO authenticated USING(id=1 AND EXISTS(
 SELECT 1 FROM public.couple_members m WHERE m.user_id=(SELECT auth.uid())));
CREATE POLICY "member sees messages" ON public.couple_messages
 FOR SELECT TO authenticated USING(EXISTS(
 SELECT 1 FROM public.couple_members m WHERE m.user_id=(SELECT auth.uid())));
CREATE POLICY "member sends own messages" ON public.couple_messages
 FOR INSERT TO authenticated WITH CHECK(
 sender_id=(SELECT auth.uid()) AND EXISTS(
 SELECT 1 FROM public.couple_members m WHERE m.user_id=(SELECT auth.uid())));
CREATE POLICY "member sets verifier once" ON public.couple_room
 FOR UPDATE TO authenticated USING(id=1 AND verifier_ciphertext IS NULL AND EXISTS(
 SELECT 1 FROM public.couple_members m WHERE m.user_id=(SELECT auth.uid())))
 WITH CHECK(id=1 AND verifier_iv IS NOT NULL AND verifier_ciphertext IS NOT NULL AND EXISTS(
 SELECT 1 FROM public.couple_members m WHERE m.user_id=(SELECT auth.uid())));
REVOKE ALL ON public.couple_members,public.couple_room,public.couple_messages FROM anon,authenticated;
GRANT SELECT ON public.couple_members,public.couple_room TO authenticated;
GRANT SELECT,INSERT ON public.couple_messages TO authenticated;
GRANT UPDATE(verifier_iv,verifier_ciphertext) ON public.couple_room TO authenticated;
DO $$
BEGIN
 IF NOT EXISTS(
 SELECT 1 FROM pg_publication_tables WHERE pubname='supabase_realtime'
 AND schemaname='public' AND tablename='couple_messages')
 THEN ALTER PUBLICATION supabase_realtime ADD TABLE public.couple_messages;
 END IF;
END $$;
COMMIT;
-- AFTER inviting/creating and verifying TWO users in Authentication > Users,
-- execute BOTH enrollment statements below separately, replacing the email placeholders:
-- INSERT INTO public.couple_members(user_id,role)
-- SELECT id,'person_one' FROM auth.users WHERE lower(email)=lower('EMAIL_ONE');
-- INSERT INTO public.couple_members(user_id,role)
-- SELECT id,'person_two' FROM auth.users WHERE lower(email)=lower('EMAIL_TWO');
-- Check: SELECT * FROM public.couple_members; must contain EXACTLY two rows.
