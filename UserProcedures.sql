DROP PROCEDURE IF EXISTS GetCoursesByUser;
DROP PROCEDURE IF EXISTS GetCOursesByUserName;
DROP PROCEDURE IF EXISTS RegisterStudent;
DROP PROCEDURE IF EXISTS AddRating;

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

-- Creates a new Student with the given ID and name, returns true or false depends on if user already exists
DELIMITER //
CREATE PROCEDURE RegisterStudent(IN UName VARCHAR(20), IN PW VARCHAR(64), IN FName VARCHAR(64), OUT Success Boolean)
BEGIN
	IF UName IN (SELECT UserName FROM Users)
		THEN SET Success = false;
	ELSE
		BEGIN
			INSERT INTO Users (UserName, LoginPassword, FullName, UserTypeID) VALUES (UName, PW, FName, 1);
            SET Success = true;
		END;
    END IF;
END //
DELIMITER ;

-- Creates a new rating in the rating page
DELIMITER //
CREATE PROCEDURE AddRating(IN UserName VARCHAR(20), IN CourseCode VARCHAR(10), IN Sem INT, IN Section VARCHAR(2), IN Rate VARCHAR(10), IN Note VARCHAR(150), OUT Success Boolean)
BEGIN
	DECLARE UHash VARCHAR(64);
    SET UHash = sha2(UserName, 256);
    IF (SELECT UserHash FROM Rating WHERE UserHash = UHash AND CourseID = CourseCode AND SemesterID = Sem AND SectionName = Section) IS NULL
		THEN INSERT INTO Rating (UserHash, CourseID, SemesterID, SectionName, Rating, Notes) VALUES (UHash, CourseCode, Sem, Section, Rate, Note);
		SET Success = true;
	ELSE
		SET Success = false;
	END IF;
END //
DELIMITER ;