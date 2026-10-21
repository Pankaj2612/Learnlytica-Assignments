def format_task_label(title, status='todo'):

    # TODO: if title is empty or None, replace it with 'untitled'
    # TODO: return '[STATUS] Title' with STATUS uppercased
    if title == '' or title is None:
        title = 'untitled'
    status = status.upper()

    return f"[{status}] {title}"