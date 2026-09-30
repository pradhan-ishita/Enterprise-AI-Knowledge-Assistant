from database.mysql_connection import get_connection


connection = get_connection()

print("Database connection successful!")

cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM employees")

result = cursor.fetchone()

print("Employees:", result[0])

cursor.close()
connection.close()