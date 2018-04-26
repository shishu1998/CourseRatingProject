USE CourseMetric;

INSERT INTO UserTypes(UserType) VALUES('Student'), ('Professor');

INSERT INTO Users (UserName, LoginPassword, FullName, UserTypeID)
VALUES ('rc123', sha2('P@ssw0rd',256), 'Richie Yeung', 1), ('kp654', sha2('P@ssw0rd',256), 'Keith Phung', 1),
('lc754', sha2('P@ssw0rd',256), 'Larry Charles', 1), ('ae285', sha2('P@ssw0rd',256), 'Albert Einstein', 2), 
('abc123', sha2('P@ssw0rd',256), 'Abraham Lincoln', 1), ('br123', sha2('P@ssw0rd',256), 'Bob Ross', 1);

INSERT INTO Courses VALUES ('CS-UY 3083','Database'),
('CS-UY 2214','Computer Architecture and Organization'),
('CS-UY 2413', 'Design & Analysis of Algorithms');

INSERT INTO Semester(Semester) VALUES ('Spring 2017'), ('Fall 2017'), ('Spring 2018'), ('Fall 2018');

INSERT INTO CourseSection Values
('CS-UY 2214', 'A', 1, MD5('CS-UY 2214A1')),
('CS-UY 2214', 'B', 1, MD5('CS-UY 2214B1')),
('CS-UY 2413', 'A1', 1, MD5('CS-UY 2413A11'));

INSERT INTO CourseSection(CourseID, SemesterID, CourseCode) Values
('CS-UY 3083', 2, MD5('CS-UY 30832')), ('CS-UY 3083', 3, MD5('CS-UY 30833'));

INSERT INTO InCourse values
('CS-UY 2214', 'A', 1, 1),
('CS-UY 2214', 'B', 1, 2),
('CS-UY 2413', 'A1', 1, 2),
('CS-UY 3083', '', 2, 3),
('CS-UY 3083', '', 2, 1),
('CS-UY 2214', 'A', 1, 4),
('CS-UY 2413', 'A1', 1, 4),
('CS-UY 3083', '', 2, 4),
('CS-UY 2214', 'A', 1, 5),
('CS-UY 2214', 'A', 1, 6),
('CS-UY 3083', '', 2, 5),
('CS-UY 3083', '', 2, 6);

-- Check that things have been inserted correctly
/*
SELECT * FROM UserTypes;
SELECT * FROM Users;
SELECT * FROM Courses;
SELECT * FROM Semester ORDER BY SemesterID;
SELECT * FROM CourseSection ORDER BY SemesterID;
SELECT * FROM InCourse;
*/