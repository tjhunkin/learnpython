import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="3305",
  user="root",
  password="root",
  database="pydb"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)
