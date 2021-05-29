import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="3305",
  user="root",
  password="root",
  database="pydb"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
