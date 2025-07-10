import sqlite3
import functools

# ✅ Copy from Task 1
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

# ✅ Step 3: Create transactional decorator
def transactional(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()  # If successful, commit
            return result
        except Exception as e:
            conn.rollback()  # If error, rollback
            print(f"[ERROR] Rolling back due to: {e}")
            raise  # Re-raise the error
    return wrapper

# ✅ Step 4: Use both decorators
@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))

# ✅ Step 5: Test it
update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
print("Email updated successfully!")
