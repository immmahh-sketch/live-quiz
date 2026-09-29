-- Every hosted quiz (not bank rows), for the play-at-home clash checks.
select id, title, questions from quiz_quizzes where settings->>'bank' is null;
