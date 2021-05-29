import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="3305",
  user="root",
  password="root",
  database="pydb"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)
