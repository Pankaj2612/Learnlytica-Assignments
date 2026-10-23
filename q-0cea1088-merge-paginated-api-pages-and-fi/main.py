def merge_pages(pages, status=None):
    # Merge paginated response pages into one de-duplicated, sorted list.
    # If status is given, keep only tasks with that status.
    seen = set()
    l = []
    for page in sorted(pages,key=lambda x : x.get('page',0)):

        for p in page.get('results',[]):
            task_id = p["id"]

            if task_id in seen:
                continue

            seen.add(task_id)
            if status is None or p.get("status") == status:
                l.append(p)

    return sorted(l,key=lambda t : t["id"])
def pages_fixture():
    return [
        {"page": 2, "next": False, "results": [
            {"id": 4, "status": "done"},
            {"id": 5, "status": "todo"},
        ]},
        {"page": 1, "next": True, "results": [
            {"id": 1, "status": "todo"},
            {"id": 2, "status": "done"},
            {"id": 3, "status": "todo"},
            {"id": 4, "status": "done"},
        ]},
    ]
merge_pages(pages_fixture())