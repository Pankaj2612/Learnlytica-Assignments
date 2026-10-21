# Top Open Tasks (WHERE + ORDER BY + LIMIT)

## Top Open Tasks Ranking (SQLite)

TaskFlow wants a "top N open tasks" widget — the most important unfinished work, ranked. You'll load the tasks into an **in-memory SQLite database** and let SQL do the filtering, sorting, and limiting in one query.

### Worked example
```python
top_open_tasks(tasks_fixture(), 4, 2)
# -> [{'id': 2, 'title': 'Build API', 'priority': 5, 'estimate_hours': 8.0},
#     {'id': 4, 'title': 'Fix login bug', 'priority': 5, 'estimate_hours': 3.0}]
```
Here `min_priority=4` and `n=2`. Both returned tasks are open with priority `5`; they tie on priority, so the one with more estimated hours (`8.0`) comes first, and only the top `2` are kept.

### What to build
Write `top_open_tasks(tasks, min_priority, n)`:
- Load the task dicts into an in-memory SQLite DB, then return the top `n` tasks that are **not** `done` and have `priority >= min_priority`.
- Do it in **one** parameterised query: `WHERE status != 'done' AND priority >= ?`, then `ORDER BY priority DESC, estimate_hours DESC, id ASC` (rank by priority, break ties by hours then id), then `LIMIT ?`.
- Bind `min_priority` and `n` as parameters (`?` placeholders). If nothing qualifies (or `n` is `0`), return `[]`.
- Return a list of dicts with keys `id`, `title`, `priority`, `estimate_hours`.

### Concepts you'll use
`sqlite3` in-memory DB, multi-key `ORDER BY`, `LIMIT`, parameterised queries, result dicts.

### How to solve this
- **Define:** `top_open_tasks(tasks, min_priority, n)` and the helpers `tasks_fixture()`, `tasks_fixture2()`, `empty_tasks()`, `one_task()` exactly as in the starter — the grader calls them in its test expressions.
- **What the grader runs:**
  - `top_open_tasks(tasks_fixture(), 4, 2)` -> `[{'id': 2, 'title': 'Build API', 'priority': 5, 'estimate_hours': 8.0}, {'id': 4, 'title': 'Fix login bug', 'priority': 5, 'estimate_hours': 3.0}]`
  - `top_open_tasks(tasks_fixture(), 1, 3)` -> `[{'id': 2, 'title': 'Build API', 'priority': 5, 'estimate_hours': 8.0}, {'id': 4, 'title': 'Fix login bug', 'priority': 5, 'estimate_hours': 3.0}, {'id': 3, 'title': 'Write tests', 'priority': 4, 'estimate_hours': 6.0}]`
  - `top_open_tasks(tasks_fixture(), 6, 3)` -> `[]`

<!--LL-ATTEMPT-->
---

## How to attempt this

1. Open the assignment from your course page. Write your answer **in the code editor on the
   right** — there is no file to create and nothing to name.
2. Click **Run Tests** to grade it. The visible tests run first so you can see where you stand.
3. Read any failure carefully: it shows the **input**, what was **expected**, and what your code
   **actually returned**. That three-way comparison is usually enough to find the bug.
4. Re-run as often as you like. Each value is scored separately, so a partly-correct answer still
   earns marks — submit something rather than nothing.
5. When you are satisfied, **Submit**.

### The exact shape to define

```python
def top_open_tasks(tasks, min_priority, n)
def tasks_fixture()
def tasks_fixture2()
def empty_tasks()
def one_task()
```

> **Runtime:** your code is graded on **Python 3.9**, which may be
> older than the Python in your editor. Avoid `match` statements and `int | None` style unions
> in annotations — they run fine locally and fail on the grader. Plain `def f(x):` and
> `typing.Optional[int]` are always safe.
>
> **`return` your answer — never `print` it.** A printed value is not a returned value, and the
> grader only reads what you return.

---
Edit **main.py** in this folder. **Run Test** (in the platform) grades it.
