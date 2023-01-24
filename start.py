import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "sma"
)

cursor = conn.cursor()

cursor.execute("show tables") 

for tb in cursor:
    print(tb)






