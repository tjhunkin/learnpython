import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="3305",
  user="root",
  password="root"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE pydb")
