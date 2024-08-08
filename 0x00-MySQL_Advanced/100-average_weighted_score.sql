-- Created a stored procedure to compute and store the weighted average
-- of students

DELIMITER |

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
BEGIN
	DECLARE done INT DEFAULT FALSE;
	DECLARE Curr_P_id INT;
        DECLARE CurrScore FLOAT;
	DECLARE CurrWeight INT;
        DECLARE TotalScore FLOAT DEFAULT 0;
        DECLARE TotalWeight INT DEFAULT 0;
	DECLARE ScoreCursor CURSOR
	FOR
		SELECT project_id, score FROM corrections WHERE corrections.user_id = user_id;
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
	OPEN ScoreCursor;
	ScoreLoop: LOOP
		   FETCH ScoreCursor INTO Curr_P_id, CurrScore;
		   IF done THEN
	   	      LEAVE ScoreLoop;
		   END IF;
		   SELECT weight INTO CurrWeight FROM projects WHERE id = Curr_P_id;
		   SET TotalScore = TotalScore + (CurrScore * CurrWeight);
		   SET TotalWeight = TotalWeight + CurrWeight;
	END LOOP;
	CLOSE ScoreCursor;
	UPDATE users SET average_score = (TotalScore / TotalWeight) WHERE id = user_id;
END |

DELIMITER ;
