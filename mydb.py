import mysql.connector


myDb = mysql.connector.connect(host="localhost", user="root", password="276328", database="milton")
# print(myDb)
mycursor = myDb.cursor()

sql = "DROP TABLE person"

mycursor.execute(sql)

# mycursor.execute("Create database Milton")
# mycursor.execute("Show tables")

# mycursor.execute("Create table person(name varchar(200), age int(3))")
# mycursor.execute("Show tables")
#
# for table in mycursor:
#     print(table)
#
# sql = "INSERT INTO person (name, age) VALUES (%s, %s)"
# val = ("John", "29")
# mycursor.execute(sql, val)
# myDb.commit()
# print(mycursor.rowcount, "record inserted.")
# mycursor.execute("SELECT * from person")
# result = mycursor.fetchall()
#
# for row in result:
#     print(row)

