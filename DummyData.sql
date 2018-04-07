USE CourseMetric;

INSERT INTO UserTypes(UserType) VALUES('Student'), ('Professor');

INSERT INTO Users (UserName, LoginPassword, FullName, UserTypeID)
VALUES ('rc123', 'P@ssw0rd', 'Richie Yeung', 1), ('kp654', 'P@ssw0rd', 'Keith Phung', 1),
('lc754', 'P@ssw0rd', 'Larry Charles', 1), ('ae285', 'P@ssw0rd', 'Albert Einstein', 2);

INSERT INTO Courses VALUES ('CS-UY 3083','Database'),
('CS-UY 2214','Computer Architecture and Organization'),
('CS-UY 2413', 'Design & Analysis of Algorithms');

INSERT INTO Semester(Semester) VALUES ('Spring 2017'), ('Fall 2017'), ('Spring 2018'), ('Fall 2018');

INSERT INTO CourseSection Values
('CS-UY 2214', 'A', 1),
('CS-UY 2214', 'B', 1),
('CS-UY 2413', 'A1', 1);

INSERT INTO CourseSection(CourseID, SemesterID) Values
('CS-UY 3083', 2), ('CS-UY 3083', 3);

INSERT INTO InCourse values
('CS-UY 2214', 'A', 1, 1),
('CS-UY 2214', 'B', 1, 2),
('CS-UY 2413', 'A1', 1, 2),
('CS-UY 3083', '', 2, 3);

-- Check that things have been inserted correctly
/*
SELECT * FROM UserTypes;
SELECT * FROM Users;
SELECT * FROM Courses;
SELECT * FROM Semester ORDER BY SemesterID;
SELECT * FROM CourseSection ORDER BY SemesterID;
SELECT * FROM InCourse;
*/