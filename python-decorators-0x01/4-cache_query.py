import sqlite3
import functools

# ✅ Simple in-memory cache
query_cache = {}

# ✅ with_db_connection from before
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

# ✅ Step 3: Create cache_query decorator
def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        query = kwargs.get('query') or (args[0] if args else None)

        if query in query_cache:
            print("[CACHE] Returning cached result for query.")
            return query_cache[query]

        result = func(conn, *args, **kwargs)
        query_cache[query] = result
        print("[CACHE] Stored result in cache.")
        return result
    return wrapper

# ✅ Step 4: Use both decorators
@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# ✅ Step 5: Call it twice — second call should use cache
query = "SELECT * FROM users"

print("First call:")
users = fetch_users_with_cache(query=query)

print("Second call (should be cached):")
users_again = fetch_users_with_cache(query=query)
