def handle_list_tasks(query, tasks):
    result = tasks

    if "status" in query:
        result = [task for task in result if task["status"] == query["status"]]

    if "limit" in query:
        try:
            limit = int(query["limit"])
        except ValueError:
            return {"status_code": 422, "body": {"error": "invalid limit"}}

        if limit <= 0:
            return {"status_code": 422, "body": {"error": "invalid limit"}}

        result = result[:limit]

    return {"status_code": 200, "body": result}