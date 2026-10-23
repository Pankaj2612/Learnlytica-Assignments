STATUSES = ["todo", "in_progress", "review", "done"]


def tasks_fixture():
    return [
        {"id": 1, "title": "Design schema", "status": "done", "priority": 3, "estimate_hours": 4.0},
        {"id": 2, "title": "Build API", "status": "in_progress", "priority": 5, "estimate_hours": 8.0},
        {"id": 3, "title": "Write unit tests", "status": "todo", "priority": 2, "estimate_hours": 3.0},
        {"id": 4, "title": "Deploy to staging", "status": "todo", "priority": 4, "estimate_hours": 2.0},
        {"id": 5, "title": "Review PR", "status": "done", "priority": 1, "estimate_hours": 1.5},
    ]


def build_status_summary(tasks):
    # Return total, by_status (all 4 keys), done, completion_rate,
    # total_estimate_hours, done_estimate_hours.
    total = 0
    done = 0
    total_estimate_hours = 0
    done_estimate_hours = 0
    completion_rate = 0
    by_status = {"todo":0,"in_progress":0,"review":0,"done":0}
    for t in tasks:
        total += 1
        if t.get("status") in by_status:
            by_status[t["status"]] += 1
        total_estimate_hours += round(t.get("estimate_hours"),4)
        if 'done' == t.get('status'):
            done_estimate_hours +=  round(t.get("estimate_hours"),4)
    done = by_status.get('done')
    if total != 0:
        completion_rate = round(done/total,4)

    return {"total":total,"by_status":by_status,"done":done,"completion_rate":completion_rate,"total_estimate_hours":total_estimate_hours,"done_estimate_hours":done_estimate_hours}