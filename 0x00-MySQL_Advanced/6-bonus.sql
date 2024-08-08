-- Creates a new stored procedure that adds a new correction to a student
-- for a new or existing project (the procedure creates the project if
-- not found)

DELIMITER |

CREATE PROCEDURE AddBonus(user_id INT, project_name VARCHAR(255) , score INT)
BEGIN
	DECLARE ProjectExists INT;
	DECLARE ProjectId INT;
	SET ProjectExists = 0;
	SELECT COUNT(*) INTO ProjectExists FROM projects WHERE name = project_name;
	IF (ProjectExists = 0) THEN
	  INSERT INTO projects (name) VALUES (project_name);
	END IF;
	SELECT id INTO ProjectId FROM projects WHERE name = project_name;
	INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, ProjectId, score);
END |
DELIMITER ;
