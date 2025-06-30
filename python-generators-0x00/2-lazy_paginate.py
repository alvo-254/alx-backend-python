seed = __import__('seed')


def paginate_users(page_size, offset):
    """Fetches one page of users with given page size and offset."""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows


def lazy_pagination(page_size):
    """Generator that lazily paginates the user_data table one page at a time."""
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page  # ✅ yield used as required
        offset += page_size  # move to the next page
