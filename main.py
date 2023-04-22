
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mk2002',
    #port='3306'
    database='pythondb'
    #database='python_video'
)

#print(mydb)

mycursor = mydb.cursor()

sql = "DROP TABLE IF EXISTS students"
mycursor.execute(sql)
mydb.commit()

"""sql = "DELETE FROM students WHERE name = 'Malli'"
mycursor.execute(sql)
mydb.commit()"""

"""sql = "SELECT * FROM students ORDER BY age DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for r in myresult:
    print(r)"""

"""mycursor.execute("SELECT * FROM students LIMIT 5 OFFSET 2")
myresult = mycursor.fetchall()
for lmt in myresult:
    print(lmt)"""


"""sql = "UPDATE students SET age = 20 WHERE name = 'Babu'"
mycursor.execute(sql)
mydb.commit()"""

#sql = "SELECT * FROM students WHERE age = 32"
"""sql = "SELECT * FROM students WHERE name LIKE 'Ma%'"
mycursor.execute(sql)
sql = "SELECT * FROM students WHERE name LIKE '%s'"
mycursor.execute(sql, ("Malli", ))
myresult = mycursor.fetchall()
for result in myresult:
    print(result)"""


#mycursor.execute("SELECT * FROM students")
#myresult = mycursor.fetchall()

"""mycursor.execute("SELECT  age  FROM students")
myresult = mycursor.fetchone()

for row in myresult:
    print(row)"""

"""sqlFormula = "INSERT INTO students(name, age) VALUES(%s, %s)"
students = [('Babu', 22),
           ('Malli', 32),
           ('Naresh', 33),
           ('Ram', 22),
           ('Laxam', 21),]
mycursor.executemany(sqlFormula, students)
mydb.commit()"""
#mycursor.execute("CREATE TABLE students(name VARCHAR(255), age INTEGER(10))")

"""mycursor.execute("SELECT * FROM students")

sts = mycursor.fetchall()

for students in sts:
    print(students)"""

#mycursor.execute("SHOW TABLES")

#mycursor.execute("SHOW DATABASES")

"""for tables in mycursor:
    print(tables)"""

"""for db in mycursor:
    print(db)"""

#mycursor.execute('CREATE DATABASE pythondb')

#mycursor.execute('SELECT * FROM user')

#users = mycursor.fetchall()

#for user in users:
    #print(user)
    #print('Username '+ user[1])
    #print('passwrod ' + user[2])