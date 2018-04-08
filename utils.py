import pymysql.cursors

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
            sql = "SELECT ValidateUser('" + username + "','" + password + "') AS Valid;"
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

def AddRating(UName, CourseID, Sem, Section, Rate, Note):
    connection = DatabaseConnect()
    success = 0
    try:
        with connection.cursor() as cursor:
            #FIXUP: Use cursor.callproc
            #cursor.callproc("AddRating", [UName, CourseID, Sem, Section, Rate, Note, "@Success"])
            sql = "CALL AddRating('" + UName + "', '" + CourseID + "', '" + Sem + "', '" + Section + "', '" + Rate + "', '" + Note + "', @Success);"
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
print(RegisterStudent("noob123", "pronoob", "Noob"))
print(AddRating("rc123", "CS-UY 2413", "1", "A1", "Very Good", "GOOD CLASS!"))
"""
