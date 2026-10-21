import sqlite3

def sample_board():
    return [
        {'title': 'A', 'status': 'review', 'priority': 5},
        {'title': 'B', 'status': 'review', 'priority': 1},
        {'title': 'C', 'status': 'todo',   'priority': 2},
        {'title': 'D', 'status': 'done',   'priority': 4},
    ]

def apply_changes(rows, min_priority):
    # Load rows, UPDATE review->done (capture rowcount),
    # then DELETE priority < min_priority (capture rowcount).
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    cursor.execute("""
                    CREATE TABLE task (
                    title TEXT,
                    status TEXT,                                   
                    priority INTEGER
                    )                                                            
        """)
    cursor.executemany("INSERT INTO task (title,status,priority) VALUES (:title,:status,:priority)",rows)

    cursor.execute("""UPDATE task
                    SET status=?
                    WHERE status==?
    """,('done','review'))
    updated = cursor.rowcount

    cursor.execute("""
            DELETE FROM task
            WHERE priority < ?
    """,(min_priority,))

    deleted = cursor.rowcount

    return {'updated':updated,'deleted':deleted}

print(apply_changes(sample_board(),3))