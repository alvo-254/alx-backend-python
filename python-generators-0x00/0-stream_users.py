import mysql.connector

def stream_users():
    """Generator that streams rows from user_data one by one as dictionaries."""
    # Connect to the ALX_prodev database
    connection = mysql.connector.connect(
        host="localhost",
        user="your_mysql_username",
        password="your_mysql_password",
        database="ALX_prodev"
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data;")

    for row in cursor:
        yield row

    cursor.close()
    connection.close()
