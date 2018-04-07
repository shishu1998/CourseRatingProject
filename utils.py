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

#Tests for this method
"""
print(ValidateUser('rc123','P@ssw0rd'))
print(ValidateUser('rc123','lmao'))
"""
