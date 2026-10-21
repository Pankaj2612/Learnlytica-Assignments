def summarize_tasks(tasks, include_rate=True):
    by_status = {}

    for t in tasks:
        status = t.get('status', 'unknown')
        by_status[status] = by_status.get(status, 0) + 1

    total = len(tasks)
    result = {
        'total': total,
        'by_status': by_status
    }

    if include_rate:
        done_count = by_status.get('done', 0)

        if total == 0:
            rate = 0.0
        else:
            rate = round((done_count / total) * 100, 1)

        result['rate'] = rate

    return result