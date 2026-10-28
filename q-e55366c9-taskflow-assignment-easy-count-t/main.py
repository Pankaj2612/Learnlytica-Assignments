def count_by_status(tasks):
    # TODO: return {status: count} preserving first-seen order
    counts = {}
    for task in tasks:
        status = task["status"]
        counts[status] = counts.get(status, 0) + 1
    return counts