Use student_management;
CREATE TABLE Students (
    id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100),
    dob DATE,
    email VARCHAR(100),
    contact VARCHAR(15)
);

CREATE TABLE Courses (
    id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100),
    credits INT
);

CREATE TABLE Enrollments (
    id varchar(10) PRIMARY KEY,
    student_id varchar(10),
    course_id varchar(10),
    enrollment_date Varchar(10),
    FOREIGN KEY (student_id) REFERENCES Student(id),
    FOREIGN KEY (course_id) REFERENCES Courses(id)
);

CREATE TABLE Grades (
    student_id varchar(10),
    enrollment_id varchar(10),
    grade VARCHAR(2),
    FOREIGN KEY (enrollment_id) REFERENCES Enrollments(id),
    FOREIGN KEY (student_id) REFERENCES Students(id)
);
CREATE TABLE Student (
    id VARCHAR(15) PRIMARY KEY,
    name VARCHAR(100),
    dob DATE,
    email VARCHAR(100),
    contact VARCHAR(15)
);

