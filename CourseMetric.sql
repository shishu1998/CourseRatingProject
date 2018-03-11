DROP DATABASE IF EXISTS CourseMetric;
CREATE DATABASE CourseMetric;

USE CourseMetric;

CREATE TABLE UserTypes (
	UserTypeID int auto_increment,
    UserType VARCHAR(20) NOT NULL UNIQUE,
    PRIMARY KEY(UserTypeID)
);

CREATE TABLE Users (
	UserID int auto_increment,
    UserName VARCHAR(20) NOT NULL UNIQUE,
    LoginPassword VARCHAR(64) NOT NULL,
    FullName VARCHAR(50),
    UserTypeID int,
    PRIMARY KEY(UserID),
    FOREIGN KEY(UserTypeID) REFERENCES UserTypes(UserTypeID)
);

CREATE TABLE Courses (
	CourseID VARCHAR(10),
    CourseName VARCHAR(40) NOT NULL,
    PRIMARY KEY(CourseID)
);

CREATE TABLE Semester(
	SemesterID int auto_increment,
	Semester VARCHAR(20) NOT NULL UNIQUE,
	PRIMARY KEY(SemesterID)
);

CREATE TABLE CourseSection(
	CourseID VARCHAR(10) NOT NULL,
	SectionName VARCHAR(2) DEFAULT '',
    SemesterID int NOT NULL,
    PRIMARY KEY(CourseID, SectionName, SemesterID),
	FOREIGN KEY (CourseID) REFERENCES Courses(CourseID),
	FOREIGN KEY (SemesterID) REFERENCES Semester(SemesterID)
);

CREATE TABLE InCourse(
	CourseID VARCHAR(10) NOT NULL,
	SectionName VARCHAR(2) DEFAULT '',
    SemesterID int NOT NULL,
    UserID int,
	PRIMARY KEY(CourseID, SectionName, SemesterID, UserID),
	FOREIGN KEY (CourseID, SectionName, SemesterID) REFERENCES CourseSection(CourseID, SectionName, SemesterID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

CREATE TABLE CourseRating(
	RatingID int auto_increment,
	CourseID VARCHAR(10),
    SemesterID int NOT NULL,
	SectionName VARCHAR(2),
    Rating VARCHAR(10) CHECK(Rating IN ('Very Good', 'Good', 'Average', 'Bad', 'Very Bad')),
    Notes VARCHAR(150) DEFAULT '',
    PRIMARY KEY(RatingID),
    FOREIGN KEY (CourseID, SectionName, SemesterID) REFERENCES CourseSection(CourseID, SectionName, SemesterID)
);

CREATE VIEW Rating AS 
	SELECT CourseID, SemesterID, SectionName, Rating, Notes
    FROM CourseRating
    WHERE Rating IN ('Very Good', 'Good', 'Average', 'Bad', 'Very Bad') WITH CHECK OPTION;
