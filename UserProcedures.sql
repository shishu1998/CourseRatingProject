Use CourseMetric;

DROP PROCEDURE IF EXISTS GetCoursesByUser;
DROP PROCEDURE IF EXISTS GetCoursesByUserName;
DROP PROCEDURE IF EXISTS RegisterStudent;
DROP PROCEDURE IF EXISTS AddRating;
DROP PROCEDURE IF EXISTS EnrollStudent;

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
	DECLARE PWHash VARCHAR(64);
    SET PWHash = sha2(PW, 256);
	IF UName IN (SELECT UserName FROM Users)
		THEN SET Success = false;
	ELSE
		BEGIN
			INSERT INTO Users (UserName, LoginPassword, FullName, UserTypeID) VALUES (UName, PWHash, FName, 1);
            SET Success = true;
		END;
    END IF;
END //
DELIMITER ;

-- Creates a new rating in the rating page
DELIMITER //
CREATE PROCEDURE AddRating(IN UserName VARCHAR(20), IN Course VARCHAR(10), IN Sem INT, IN Section VARCHAR(2), IN Rate VARCHAR(10), IN Note VARCHAR(150), OUT Success Boolean)
BEGIN
	DECLARE UHash VARCHAR(64);
    SET UHash = sha2(UserName, 256);
    IF (SELECT UserHash FROM Rating WHERE UserHash = UHash AND CourseID = Course AND SemesterID = Sem AND SectionName = Section) IS NULL
		THEN INSERT INTO Rating (UserHash, CourseID, SemesterID, SectionName, Rating, Notes) VALUES (UHash, Course, Sem, Section, Rate, Note);
		SET Success = true;
	ELSE
		SET Success = false;
	END IF;
END //
DELIMITER ;

-- Enrolls a student into a course by CourseCode
DELIMITER //
CREATE PROCEDURE EnrollStudent(IN UName VARCHAR(20), IN CCode VARCHAR(32), OUT Success Boolean)
BEGIN
	DECLARE StudentID int;
    DECLARE CID VARCHAR(10);
    DECLARE SName VARCHAR(2);
    DECLARE SID int;
    SET StudentID = (SELECT UserID From Users WHERE UserName=UName);
    SELECT CourseID, SectionName, SemesterID into CID, SName, SID FROM CourseSection WHERE CourseCode=CCode;
    IF(CID IS NULL)
		THEN SET Success = false;
    ELSEIF (SELECT UserID FROM InCourse WHERE UserID = StudentID AND CourseID = CID AND SemesterID = SID AND SectionName = SName) IS NULL
		THEN INSERT INTO InCourse (CourseID, SectionName, SemesterID, UserID) VALUES (CID, SName, SID, StudentID);
		SET Success = true;
	ELSE
		SET Success = false;
	END IF;
END //
DELIMITER ;