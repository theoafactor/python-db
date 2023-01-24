import mysql.connector

_db_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="sma"
)

cursor = _db_conn.cursor()
def createUsersTable():
    cursor.execute("""
            CREATE TABLE `users`(
                `id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                `fullname` VARCHAR(300) NOT NULL,
                `email` VARCHAR(300) UNIQUE NOT NULL,
                `gender` ENUM("male", "female", "others"),
                `date_created` TIMESTAMP
            )
         """)