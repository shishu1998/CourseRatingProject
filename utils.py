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

def GetCoursesByUser(id):
    connection = DatabaseConnect()
    try:
        with connection.cursor() as cursor:
            sql = "CALL GetCoursesByUser(" + id + ");"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def GetCoursesByUsername(id):
    connection = DatabaseConnect()
    try:
        with connection.cursor() as cursor:
            sql = "CALL GetCoursesByUsername('" + id + "');"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def RegisterStudent(UName, PW, FName):
    connection = DatabaseConnect()
    try:
        with connection.cursor() as cursor:
            cursor.callproc("RegisterStudent", [UName, PW, FName, "@Success"])
            success = cursor.execute("SELECT @Success")
            return success
    finally:
        connection.commit()
        connection.close()

def AddRating(UName, CourseID, Sem, Section, Rate, Note):
    connection = DatabaseConnect()
    try:
        with connection.cursor() as cursor:
            cursor.callproc("AddRating", [UName, CourseID, Sem, Section, Rate, Note, "@Success"])
            success = cursor.execute("SELECT @Success")
            return success
    finally:
        connection.commit()
        connection.close()

#Tests for this method

#print(ValidateUser('rc123','P@ssw0rd'))
#print(ValidateUser('rc123','lmao'))
#print(GetCoursesByUser('1'))
#print(GetCoursesByUser('20'))
#print(GetCoursesByUsername('rc123'))
#print(GetCoursesByUsername('thisdoesntexist'))
#print(RegisterStudent("noob123", "pronoob", "Noob"))
#print(AddRating("rc123", "CS-UY 2413", "1", "A1", "Very Good", "GOOD CLASS!"))
