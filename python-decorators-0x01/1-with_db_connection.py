import sqlite3
import functools

# ✅ Step 3: Create the decorator
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')  # Open DB connection
        try:
            return func(conn, *args, **kwargs)  # Pass connection to the function
        finally:
            conn.close()  # Always close the connection
    return wrapper

# ✅ Step 4: Use the decorator
@with_db_connection
def get_user_by_id(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

# ✅ Step 5: Test it
user = get_user_by_id(user_id=1)
print(user)
