DROP DATABASE IF EXISTS CourseMetric;
CREATE DATABASE CourseMetric;

USE CourseMetric;

CREATE TABLE UserTypes (
	UserTypeID int auto_increment,
    UserType VARCHAR(20) NOT NULL,
    PRIMARY KEY(UserTypeID)
);

CREATE TABLE Users (
	UserID int auto_increment,
    UserName VARCHAR(20) NOT NULL,
    LoginPassword VARCHAR(64) NOT NULL,
    FullName VARCHAR(50),
    UserTypeID int,
    PRIMARY KEY(UserID),
    FOREIGN KEY(UserTypeID) REFERENCES UserTypes(UserTypeID)
);

CREATE TABLE Courses (
	CourseID VARCHAR(10),
    CourseName VARCHAR(30) NOT NULL,
    PRIMARY KEY(CourseID)
);

CREATE TABLE Semester(
	SemesterID int auto_increment,
	Semester VARCHAR(20) NOT NULL,
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
    Rating int CHECK(Rating BETWEEN 1 AND 10),
    Notes VARCHAR(150),
    PRIMARY KEY(RatingID),
    FOREIGN KEY (CourseID, SectionName, SemesterID) REFERENCES CourseSection(CourseID, SectionName, SemesterID)
);
