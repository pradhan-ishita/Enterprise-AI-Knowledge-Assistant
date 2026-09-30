import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="MyNewPassword@123",
    database="enterprise_ai"
)

print("MySQL connection successful!")

cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM employees")

result = cursor.fetchone()

print("Number of employees:", result[0])

cursor.close()
connection.close()
