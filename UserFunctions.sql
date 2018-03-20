DROP FUNCTION IF EXISTS ValidateUser;

-- Validates a User with the given Username and Password, returns a boolean
DELIMITER //
CREATE FUNCTION ValidateUser(UserN VARCHAR(20), PASS VARCHAR(64))
	RETURNS BOOLEAN
 BEGIN
	DECLARE validated boolean;
    DECLARE pWord VARCHAR(64);
    SET pWord = (SELECT LoginPassword FROM Users WHERE UserName = UserN);
 	IF (pWord IS NULL) THEN SET validated = false;
    ELSEIF (pWord = PASS)
		THEN SET validated = true;
	ELSE
		SET validated = false;
	END IF;
    Return validated;
 END //
DELIMITER ;