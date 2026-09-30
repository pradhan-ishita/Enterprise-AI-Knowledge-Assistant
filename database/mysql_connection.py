import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def get_connection():

    connection = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password=os.getenv("MYSQL_PASSWORD"),
        database="enterprise_ai"
    )

    return connection