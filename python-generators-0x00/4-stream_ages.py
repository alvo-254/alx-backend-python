import mysql.connector

def stream_user_ages():
    """Generator that yields user ages one by one from the user_data table."""
    connection = mysql.connector.connect(
        host="localhost",
        user="your_mysql_username",
        password="your_mysql_password",
        database="ALX_prodev"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data;")

    for (age,) in cursor:  # loop 1
        yield age

    cursor.close()
    connection.close()


def calculate_average_age():
    """Calculates and prints the average age using the stream_user_ages generator."""
    total = 0
    count = 0

    for age in stream_user_ages():  # loop 2
        total += age
        count += 1

    average = total / count if count else 0
    print(f"Average age of users: {average:.2f}")
