import sqlite3


def tasks_by_status(tasks, status):
	conn = sqlite3.connect(':memory:')
	conn.execute('CREATE TABLE tasks (id INTEGER, title TEXT, status TEXT)')
	conn.executemany(
		'INSERT INTO tasks (id, title, status) VALUES (?, ?, ?)',
		[(task['id'], task['title'], task['status']) for task in tasks],
	)
	rows = conn.execute(
		'SELECT id, title, status FROM tasks WHERE status = ? ORDER BY id ASC',
		(status,),
	).fetchall()
	conn.close()
	return [
		{'id': task_id, 'title': title, 'status': task_status}
		for task_id, title, task_status in rows
	]