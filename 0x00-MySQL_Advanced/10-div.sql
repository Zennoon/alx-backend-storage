-- Creates a  function that divides its arguments, and returns quotient
-- The function returns 0 if the second argument is 0

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
RETURN IF(b = 0, 0, a / b);

