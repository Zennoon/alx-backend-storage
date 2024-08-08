-- Creates trigger to reset the valid_email column when a row's email
-- is updated

DELIMITER |

CREATE TRIGGER rest_valid_email BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
IF NEW.email != OLD.email THEN
SET NEW.valid_email = 0;
END IF;
END |

DELIMITER ;
