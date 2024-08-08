-- Creates a stored procedure to compute and store the average score
-- of students

DELIMITER |

CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
	DECLARE Average FLOAT;
	SELECT AVG(score) INTO Average FROM corrections WHERE corrections.user_id = user_id;
	UPDATE users SET average_score = Average WHERE id = user_id;
END |

DELIMITER ;
