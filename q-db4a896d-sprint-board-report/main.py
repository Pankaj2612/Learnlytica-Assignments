# TaskFlow sprint board — each task is a tuple: (id, title, status, assignee, hours)
tasks = [
    (1, "Design login page", "done", "Ava", 4.0),
    (2, "Write API tests", "todo", "Ben", 3.0),
    (3, "Fix payment bug", "in_progress", "Ava", 5.5),
    (4, "Deploy release", "todo", "Cara", 2.0),
    (5, "Review PR", "done", "Ben", 1.5),
]

# Start with empty containers, then fill them in ONE for loop over tasks:
task_titles = []       # TODO: append each title (t[1])
status_counts = {}     # TODO: count each status (t[2]) with if/else
unique_assignees = set()  # TODO: add each assignee (t[3])
total_hours = 0.0      # TODO: add each hours value (t[4])
for tup in tasks:
    task_titles.append(tup[1])
    i = tup[2]
    if i in status_counts:
        status_counts[i] = status_counts.get(i) + 1
    else:
        status_counts[i] = 1
    
    unique_assignees.add(tup[3])
    total_hours += tup[4]
# After the loop:
sorted_titles  = sorted(task_titles)
assignee_count = len(set)
has_ava = "Ava" in unique_assignees