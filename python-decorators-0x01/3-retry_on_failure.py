import sqlite3
import functools
import time

# ✅ Copy your connection decorator
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

# ✅ Step 3: Create retry_on_failure
def retry_on_failure(retries=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"[Retry {attempt}] Error: {e}")
                    if attempt == retries:
                        raise  # Give up after final attempt
                    time.sleep(delay)
        return wrapper
    return decorator

# ✅ Step 4: Use both decorators
@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")  # You can force an error here to test retry
    return cursor.fetchall()

# ✅ Step 5: Test
users = fetch_users_with_retry()
print(users)
