class Task:
    """A single TaskFlow task with a lifecycle.

    Attributes:
        id     : the task identifier (any value)
        title  : task title; empty/None must become "Untitled"
        status : one of "todo" / "in_progress" / "done";
                 any other value must default to "todo"
    """
    ALLOWED = {"todo", "in_progress", "done"}

    def __init__(self, task_id, title, status="todo"):
        # TODO: set self.id, self.title (default "Untitled"),
        #       self.status (default "todo" if not allowed)
        self.id = task_id
        if title == '' or title is None:
            title = 'Untitled'
        self.title = title
        self.status = "todo"
        if status in self.ALLOWED:
            self.status = status

    def mark_done(self):
        # TODO: set status to "done" and return self (so calls can chain)
        self.status = "done"
        return self

    def reopen(self):
        # TODO: set status to "todo" and return self
        self.status = "todo"
        return self

    def is_done(self):
        # TODO: return True only when status == "done"
        if self.status == "done":
            return True
        return False

    def __repr__(self):
        # TODO: return  Task(id=..., title='...', status='...')
        return f"Task(id={self.id}, title='{self.title}', status='{self.status}')"