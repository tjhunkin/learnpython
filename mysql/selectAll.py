import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="3305",
  user="root",
  password="root",
  database="pydb"
)

mycursor = mydb.cursor()

sql = "SELECT id,name,address FROM customers"
sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"
sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

# avoid sql injection
sql = "SELECT * FROM customers WHERE address = %s ORDER BY name DESC"
adr = ("Yellow Garden 2", )

# SELECT * FROM customers LIMIT 5
# SELECT * FROM customers LIMIT 5 OFFSET 2

mycursor.execute(sql, adr)

# mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
    print(type(x))
