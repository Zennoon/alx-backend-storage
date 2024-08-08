-- Creates a view for the students table that lists all students
-- with a score under 80 and no last_meeting or more than a month
-- passed since last meeting

CREATE VIEW need_meeting AS
SELECT name FROM students WHERE (score < 80) AND (last_meeting IS NULL OR CURDATE() - last_meeting > 100);
