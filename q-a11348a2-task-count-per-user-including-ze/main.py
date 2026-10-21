import sqlite3

def sample_users():
    return [
        {"id": 1, "name": "Ana"},
        {"id": 2, "name": "Ben"},
        {"id": 3, "name": "Cara"},
        {"id": 4, "name": "Dan"},
    ]

def sample_tasks():
    return [
        {"id": 100, "title": "Design schema", "assignee_id": 1},
        {"id": 101, "title": "Build API",     "assignee_id": 2},
        {"id": 102, "title": "Write tests",   "assignee_id": 1},
        {"id": 103, "title": "Setup CI",      "assignee_id": None},
        {"id": 104, "title": "Deploy",        "assignee_id": 3},
        {"id": 105, "title": "Docs",          "assignee_id": 2},
    ]

def no_tasks():
    return []

def alt_tasks():
    return [
        {"id": 201, "title": "A1", "assignee_id": 1},
        {"id": 202, "title": "A2", "assignee_id": 2},
        {"id": 203, "title": "A3", "assignee_id": None},
        {"id": 204, "title": "A4", "assignee_id": 1},
        {"id": 205, "title": "B1", "assignee_id": 3},
        {"id": 206, "title": "B2", "assignee_id": 2},
    ]

def task_count_per_user(users, tasks):
    # LEFT JOIN users to tasks so EVERY user appears, even one with no tasks.
    # Return a list of (user_name, task_count) tuples ordered by user name, with
    # COALESCE/COUNT giving 0 for users who have no assigned tasks.
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    cursor.execute("""
                    CREATE TABLE users (
                                id INTEGER PRIMARY KEY,
                                            name TEXT
                                                    )
                                                        """)
    cursor.execute("""
            CREATE TABLE tasks (
                    id INTEGER PRIMARY KEY,
                            title TEXT,
                            assignee_id INTEGER
                                                    )
                                                        """)
    for t in tasks:
        cursor.execute("INSERT INTO tasks VALUES (?,?,?)",(t['id'],t['title'],t['assignee_id']))

    for u in users:
        cursor.execute("INSERT INTO users VALUES (?,?)",(u['id'],u['name']))
    cursor.execute("""
        SELECT name ,COALESCE(COUNT(tasks.id),0) FROM users
        LEFT JOIN  tasks on tasks.assignee_id = users.id
        GROUP BY users.id
        ORDER BY users.name ASC 
    """)
    return cursor.fetchall()

task_count_per_user(sample_users(),sample_tasks())