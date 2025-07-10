import sqlite3

class DatabaseConnection:
    def __enter__(self):
        self.conn = sqlite3.connect('users.db')  # Open the DB connection
        return self.conn  # Return it to the 'with' block

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()  # Always close the connection

# ✅ Use the context manager and execute the required query
with DatabaseConnection() as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")  # Required query
    results = cursor.fetchall()

    for row in results:  # Required: print results
        print(row)
