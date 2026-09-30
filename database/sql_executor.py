from database.mysql_connection import get_connection


def execute_query(query):

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute(query)

    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return results