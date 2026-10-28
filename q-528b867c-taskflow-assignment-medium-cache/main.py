class TaskService:
    def __init__(self, repo, cache, clock):
        self.repo = repo      # callable(task_id) -> dict | None
        self.cache = cache    # dict used as a read cache
        self.clock = clock    # callable() -> iso timestamp

    def get_task(self, task_id):
        # TODO: check cache FIRST; on miss call repo(task_id),
        # store non-None results in cache, return None when not found.
        if task_id in self.cache:
            return self.cache[task_id]

        task = self.repo(task_id)
        if task is not None:
            self.cache[task_id] = task
        return task

    def status_of(self, task_id):
        # TODO: return the task's status, or 'unknown' when the task is missing.
        task = self.get_task(task_id)
        if task is None:
            return "unknown"
        return task.get("status") or "unknown"

    def summary(self, ids):
        # TODO: fetch each id (via get_task), skip missing ones, count by status.
        counts = {}
        for task_id in ids:
            task = self.get_task(task_id)
            if task is None:
                continue
            status = task.get("status") or "unknown"
            counts[status] = counts.get(status, 0) + 1
        return counts

    def stamp(self, task_id):
        # TODO: return the task merged with 'checked_at': clock(); None if missing.
        task = self.get_task(task_id)
        if task is None:
            return None
        return {**task, "checked_at": self.clock()}