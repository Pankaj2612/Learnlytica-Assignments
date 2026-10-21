# TaskFlow Assignment (Medium) — Retry and Memoize Decorators for the Sync Engine

## Memoize & Retry — Two Classic Decorators

TaskFlow has two recurring needs: skip repeat work by caching results, and automatically retry a flaky sync that sometimes fails. You'll build both as **decorators** using closures and `functools.wraps`.

A **decorator** wraps a function to add behavior. A **closure** is an inner function that remembers variables from the function that created it — that's where the cache and the retry counter live. `functools.wraps` keeps the wrapped function's name and docstring.

### Worked example
```python
memo_compute_count([(1,2),(1,2),(1,2)])   # 1
retry_result(2, 3)                         # {'result': 'synced', 'attempts': 3}
```
The same `(1,2)` is scored three times but only **computed once** (the other two come from the cache). The flaky op fails twice then succeeds on the 3rd try, so `retry` reports success after 3 attempts.

### What to build

**1. `memoize(func)`** — cache results keyed by the argument tuple; expose `wrapper.cache_clear` to empty the cache.
- Apply it to `project_score(project_id, weight)`, which returns `project_id*10 + weight` and bumps a module-level compute counter each time it really runs.
- `memo_compute_count(calls)` — `calls` is a list of `(project_id, weight)` tuples; reset the counter, clear the cache, run each pair, and return the number of **real** computations (cache hits don't count).
- `memo_value(project_id, weight)` — return the (possibly cached) score.

**2. `retry(max_attempts)`** — a decorator **factory** (a decorator that takes an argument): it retries the wrapped call up to `max_attempts` times and re-raises the last error if all attempts fail.
- `retry_result(fail_times, max_attempts)` — using a closure over a call counter, build a flaky op that raises `ValueError` for the first `fail_times` calls then returns `'synced'`. Wrap it with `retry(max_attempts)` and return `{'result': 'synced'|'failed', 'attempts': <int>}`.
- If every attempt fails (i.e. `fail_times >= max_attempts`), `retry` re-raises the last error and `retry_result` **catches** that terminal failure, returning `{'result': 'failed', 'attempts': <int>}` — so `retry_result` itself handles the all-failed case rather than letting the exception escape.

Metadata (name/docstring) must survive both decorators.

### Concepts you'll use
Decorators, decorator factories, closures, `functools.wraps`, caching, exception handling (`try`/`except`, re-raising).

<!--LL-CONTRACT-->
### How to solve this
Write your Python **directly in the code editor** on the right, then click **Run Tests**. There is a single editor — you do **not** create or name any file; just define the function(s) below.

**Define:**
- `memoize(func)`
- `project_score(project_id, weight)`
- `memo_compute_count(calls)`
- `memo_value(project_id, weight)`
- `retry(max_attempts)`
- `retry_result(fail_times, max_attempts)`

**What the grader runs** (each value is scored **separately**, so a partly-correct answer still earns marks):
- `memo_compute_count([(1,2),(1,2),(1,2)])`  →  `1`
- `retry_result(2, 3)['result']`  →  `synced`
- `retry_result(2, 3)['attempts']`  →  `3`

Return the exact value shown (a list stays a list; round numbers only if the task says so). **`return` the value — do not `print` it.**

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
def memoize(func)
def project_score(project_id, weight)
def memo_compute_count(calls)
def memo_value(project_id, weight)
def retry(max_attempts)
def retry_result(fail_times, max_attempts)
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
