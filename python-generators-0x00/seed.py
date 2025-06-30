def stream_users(connection):
    """Generator that yields one user record at a time from the database."""
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data;")
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        yield row
    cursor.close()
