
import mysql.connector  # importing datatbase
# Creating a database
# database = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password=""
# )
# db = database.cursor()
# db.execute("CREATE DATABASE python1s")

# Creating a table in database
# database = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="python1s"
# )
# db = database.cursor()
# db.execute("CREATE TABLE subject (id INT,name VARCHAR(255))")


# Authorizing or accessing thr database
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)
db = database.cursor()

# sql = "SELECT Name FROM student WHERE Percentage > 80"
# db.execute(sql)
# result = db.fetchall()
# for i in result:
#     print(i)


# commit() to change or delete or end

# Name = input("Enter your name:")
# Physics = int(input("Enter your marks in physics:"))
# Chemistry = int(input("Enter your marks in chemistry:"))
# Math = int(input("Enter your marks in math:"))
# English = int(input("Enter your marks in english:"))
# Nepali = int(input("Enter your marks in nepali:"))
# Total = Physics+Chemistry+Math+English+Nepali
# Percentage = Total/5
# Grade = input("Enter your grade:")
# sql = f'''INSERT INTO student(Name, Physics, Chemistry, Math, English,Nepali, Total, Percentage, Grade)
#  VALUES ( '{Name}', {Physics}, {Chemistry}, {Math}, {English},{Nepali}, {Total}, {Percentage}, '{Grade}')'''
# db.execute(sql)
# database.commit()

# update
# UPDATE student SET Name='Utsab' WHERE Name ='Ram'

# delete
# DELETE student WHERE name ='Ram'

# Example
# initial = input("Enter initial name")
# final = input("Enter final name")
# sql = f"UPDATE student SET Name='Anubhav' WHERE Name ='Anu"
# db.execute("UPDATE student SET Name='{final}' WHERE Name ='{initial}'")
# database.commit()

sql = f"DELETE student WHERE name ='Anu'"
db.execute("DELETE student WHERE name='Anu'")
database.commit()
