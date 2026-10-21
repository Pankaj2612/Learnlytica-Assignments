import sqlite3

def sample_tasks():
    return [
        {'title': 'Write spec', 'status': 'todo', 'priority': 5},
        {'title': 'Build API', 'status': 'in_progress', 'priority': 4},
        {'title': 'Review PR', 'status': 'todo', 'priority': 2},
        {'title': 'Ship v1', 'status': 'done', 'priority': 3},
    ]

def insert_and_fetch(rows, status):
    # Create an in-memory DB, parameterised-insert every row,
    # then return the titles for `status` ordered by id.
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE task (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            status TEXT,
            priority INTEGER
        )
    """)
  
    cursor.executemany("INSERT INTO task (title,status,priority) VALUES (:title,:status,:priority)",rows)

    cursor.execute("""SELECT title from task 
        WHERE status = ?
        ORDER BY id ASC
    """,(status,))
    # print(cursor.fetchall())
    return [x[0] for x in cursor.fetchall()]

    
print(insert_and_fetch(sample_tasks(),'todo'))