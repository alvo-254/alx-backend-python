import sqlite3
import functools

# ✅ Step 3: Create the log_queries decorator
def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query') or (args[0] if args else None)
        print(f"[LOG] Executing SQL query: {query}")
        return func(*args, **kwargs)
    return wrapper

# ✅ Step 4: Use the decorator
@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# ✅ Step 5: Call the function
users = fetch_all_users(query="SELECT * FROM users")
print(users)
