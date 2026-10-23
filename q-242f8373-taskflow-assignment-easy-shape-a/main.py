def to_task_response(task):
    """Shape a raw TaskFlow task dict into an API response dict.

    Return a dict with exactly these keys:
      - "task_id"      -> task["id"] (or None if absent)
      - "title"        -> task["title"] (empty string "" if missing/None)
      - "status"       -> task["status"] (default "todo" if missing/None)
      - "is_completed" -> True only when the (defaulted) status == "done"
    """
    # TODO: read fields safely and build the response dict
    task_id = task.get("id") if "id" in task else None
    title = task.get("title",None) or ""
    status = task.get("status",None) or "todo"
    is_completed = False
    if task.get("status") and task["status"] == "done":
      is_completed = True

    return {
        "task_id": task_id,
        "title": title,
        "status": status,
        "is_completed": is_completed,
    }