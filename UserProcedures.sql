DROP PROCEDURE IF EXISTS GetCoursesByUser;
DROP PROCEDURE IF EXISTS GetCOursesByUserName;

-- Returns the Courses that a User takes based on the UserID provided
DELIMITER //
CREATE PROCEDURE GetCoursesByUser(IN ID int)
 BEGIN
	SELECT * FROM InCourse WHERE UserID = ID;
 END //
DELIMITER ;

-- Returns the Courses that a User takes based on the Username provided
DELIMITER //
CREATE PROCEDURE GetCoursesByUsername(IN ID VARCHAR(20))
 BEGIN
	DECLARE IntID int;
	SET IntID = (SELECT UserID FROM Users WHERE UserName = ID);
    CALL GetCoursesByUser(IntID);
 END //
DELIMITER ;