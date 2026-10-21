import sqlite3


def top_open_tasks(tasks, min_priority, n):
    """Return the top `n` NOT-done tasks with priority >= min_priority, as
    [{'id','title','priority','estimate_hours'}, ...].
    Order: priority DESC, then estimate_hours DESC, then id ASC. Use one
    parameterised query with WHERE, ORDER BY and LIMIT."""
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("""
            CREATE TABLE tasks (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            status TEXT,
            priority INTEGER,
            project_id INTEGER,
            assignee_id INTEGER,
            estimate_hours REAL
        )
                    """)
    for task in tasks:
        cursor.execute(                                                                            "INSERT INTO tasks VALUES (?,?,?,?,?,?,?)",
           (task['id'],task['title'],task['status'],int(task['priority']),int(task['project_id']),int(task['assignee_id']),float(task['estimate_hours']))
        )
    cursor.execute("""
            SELECT id,title,priority,estimate_hours FROM tasks
            WHERE status != ? AND priority >= ?
            ORDER BY priority DESC, estimate_hours DESC , id ASC
            LIMIT ?
            """,('done',min_priority,n))
    
    results = cursor.fetchall()
    conn.close()

    t_dict = []
    for t in results:
        t_dict.append({"id":t[0],"title":t[1],"priority":t[2],"estimate_hours":t[3]}) 

    return t_dict

def tasks_fixture():
    return [
        {"id": 1, "title": "Design schema", "status": "done", "priority": 3,
         "project_id": 10, "assignee_id": 100, "estimate_hours": 4.0},
        {"id": 2, "title": "Build API", "status": "in_progress", "priority": 5,
         "project_id": 10, "assignee_id": 101, "estimate_hours": 8.0},
        {"id": 3, "title": "Write tests", "status": "todo", "priority": 4,
         "project_id": 10, "assignee_id": 100, "estimate_hours": 6.0},
        {"id": 4, "title": "Fix login bug", "status": "in_progress", "priority": 5,
         "project_id": 11, "assignee_id": 102, "estimate_hours": 3.0},
        {"id": 5, "title": "Update docs", "status": "todo", "priority": 2,
         "project_id": 11, "assignee_id": 101, "estimate_hours": 2.0},
        {"id": 6, "title": "Deploy v1", "status": "done", "priority": 4,
         "project_id": 10, "assignee_id": 102, "estimate_hours": 1.5},
    ]


def tasks_fixture2():
    return [
        {"id": 1, "title": "Draft spec", "status": "todo", "priority": 5,
         "project_id": 20, "assignee_id": 200, "estimate_hours": 10.0},
        {"id": 2, "title": "Set up CI", "status": "todo", "priority": 3,
         "project_id": 20, "assignee_id": 201, "estimate_hours": 5.0},
        {"id": 3, "title": "Add linter", "status": "todo", "priority": 4,
         "project_id": 21, "assignee_id": 200, "estimate_hours": 2.5},
        {"id": 4, "title": "Review PR", "status": "review", "priority": 2,
         "project_id": 20, "assignee_id": 202, "estimate_hours": 1.0},
        {"id": 5, "title": "Security review", "status": "review", "priority": 5,
         "project_id": 21, "assignee_id": 202, "estimate_hours": 4.0},
        {"id": 6, "title": "Archive logs", "status": "done", "priority": 1,
         "project_id": 20, "assignee_id": 201, "estimate_hours": 3.0},
        {"id": 7, "title": "Wire webhook", "status": "in_progress", "priority": 4,
         "project_id": 21, "assignee_id": 200, "estimate_hours": 6.0},
    ]


def empty_tasks():
    return []


def one_task():
    return [
        {"id": 42, "title": "Kickoff", "status": "todo", "priority": 3,
         "project_id": 30, "assignee_id": 300, "estimate_hours": 2.0},
    ]