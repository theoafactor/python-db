import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user="root", 
    password="password",
    database="sma"
)

cursor = conn.cursor()

cursor.execute("""
        CREATE TABLE `articles` (
            `id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
            `author_id` INT NOT NULL,
            `article_title` VARCHAR(500) NOT NULL,
            `article_summary` LONGTEXT,
            `article_body` LONGTEXT NOT NULL,
            `date_created` TIMESTAMP
        )
 """)

cursor.execute("SHOW TABLES")

for tb in cursor:
    print(tb)

