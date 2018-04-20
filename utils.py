import pymysql.cursors
import hashlib

#Connects to the database
def DatabaseConnect():
    return pymysql.connect(host='localhost',
                             user='root',
                             password='kappa',
                             db='CourseMetric',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def ValidateUser(username, password):
    connection = DatabaseConnect()
    try:
        with connection.cursor() as cursor:
            passwordhash = hashlib.sha256(str.encode(password)).hexdigest()
            sql = "SELECT ValidateUser('" + username + "','" + passwordhash + "') AS Valid;"
            cursor.execute(sql)
            result = cursor.fetchone()['Valid']
            return result
    finally:
        connection.close()

def GetCoursesByUsername(UName):
    connection = DatabaseConnect()
    try:
        with connection.cursor() as cursor:
            cursor.callproc("GetCoursesByUsername", [UName])
            result = list(map((lambda x: (x['CourseID'],x['SectionName'], GetSemesterName(x['SemesterID']))), cursor.fetchall()))
            return result
    finally:
        connection.close()

def GetSemesterName(semesterID):
    connection = DatabaseConnect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT Semester from Semester WHERE SemesterID =" + str(semesterID) +";"
            cursor.execute(sql)
            result = cursor.fetchone()['Semester']
            return result
    finally:
        connection.close()

def GetSemesterID(semesterName):
    connection = DatabaseConnect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT SemesterID from Semester WHERE Semester ='" + semesterName +"';"
            cursor.execute(sql)
            result = cursor.fetchone()['SemesterID']
            return result
    finally:
        connection.close()
        
def RegisterStudent(UName, PW, FName):
    connection = DatabaseConnect()
    success = 0
    try:
        with connection.cursor() as cursor:
            #FIXUP: Use cursor.callproc
            #cursor.callproc("RegisterStudent", [UName, PW, FName, "@Success"])
            sql = "CALL RegisterStudent('" + UName + "', '" + PW + "', '" + FName + "', @Success);"
            cursor.execute(sql)
            cursor.execute("SELECT @Success")
            success = cursor.fetchone()['@Success']
    finally:
        connection.commit()
        connection.close()
        return success

#FIXUP: Sem should be an int for this method to work, not string
def AddRating(UName, CourseID, Sem, Section, Rate, Note):
    connection = DatabaseConnect()
    success = 0
    try:
        with connection.cursor() as cursor:
            #FIXUP: Use cursor.callproc
            #cursor.callproc("AddRating", [UName, CourseID, Sem, Section, Rate, Note, "@Success"])
            sql = "CALL AddRating('" + UName + "', '" + CourseID + "', '" + str(Sem) + "', '" + Section + "', '" + Rate + "', '" + Note + "', @Success);"
            cursor.execute(sql)
            cursor.execute("SELECT @Success")
            success = cursor.fetchone()['@Success']
    finally:
        connection.commit()
        connection.close()
        return success

def EnrollStudent(UName, CCode):
    connection = DatabaseConnect()
    success = 0
    try:
        with connection.cursor() as cursor:
            sql = "CALL EnrollStudent('" + UName + "', '" + CCode + "', " + "@Success);"
            cursor.execute(sql)
            cursor.execute("SELECT @Success")
            success = cursor.fetchone()['@Success']
    finally:
        connection.commit()
        connection.close()
        return success

"""
print(ValidateUser('rc123','P@ssw0rd'))
print(ValidateUser('rc123','lmao'))
print(GetCoursesByUsername('rc123'))
print(GetCoursesByUsername('rc123')[0][0])
print(GetCoursesByUsername('thisdoesntexist'))
print (GetSemesterName(1))
print (GetSemesterID('Fall 2017'))
print(RegisterStudent("noob123", "pronoob", "Noob"))
print(AddRating("rc123", "CS-UY 2214", 1, "A", "Very Good", "GOOD CLASS!"))
print (EnrollStudent('rc123','125ab465cffacce0b77c7b1a08af29b3'))
"""
