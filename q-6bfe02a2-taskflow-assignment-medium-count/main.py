import sqlite3


def open_tasks_per_project(projects, tasks):
	conn = sqlite3.connect(':memory:')
	conn.execute('CREATE TABLE projects (id INTEGER, name TEXT)')
	conn.execute(
		'CREATE TABLE tasks (id INTEGER, project_id INTEGER, status TEXT)'
	)
	conn.executemany(
		'INSERT INTO projects (id, name) VALUES (?, ?)',
		[(project['id'], project['name']) for project in projects],
	)
	conn.executemany(
		'INSERT INTO tasks (id, project_id, status) VALUES (?, ?, ?)',
		[(task['id'], task['project_id'], task['status']) for task in tasks],
	)
	rows = conn.execute(
		'''
		SELECT p.id, p.name,
			   SUM(CASE WHEN t.status != ? THEN 1 ELSE 0 END) AS open_count
		FROM projects AS p
		LEFT JOIN tasks AS t ON t.project_id = p.id
		GROUP BY p.id, p.name
		ORDER BY p.id ASC
		''',
		('done',),
	).fetchall()
	conn.close()
	return [
		{'project_id': project_id, 'name': name, 'open_count': open_count}
		for project_id, name, open_count in rows
	]