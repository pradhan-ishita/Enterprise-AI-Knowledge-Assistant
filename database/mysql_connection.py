import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def get_connection():

    host = os.getenv("MYSQL_HOST") or os.getenv("MYSQLHOST")
    port = os.getenv("MYSQL_PORT") or os.getenv("MYSQLPORT") or "3306"
    user = os.getenv("MYSQL_USER") or os.getenv("MYSQLUSER")
    password = os.getenv("MYSQL_PASSWORD") or os.getenv("MYSQLPASSWORD")
    database = os.getenv("MYSQL_DATABASE") or os.getenv("MYSQLDATABASE")

    connection = mysql.connector.connect(
        host=host,
        port=int(port),
        user=user,
        password=password,
        database=database
    )

    return connection