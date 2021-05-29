import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="3305",
  user="root",
  password="root",
  database="pydb"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")

mycursor.execute(sql, val)

mydb.commit()  # required to affect changes

print(mycursor.rowcount, "record(s) affected")
