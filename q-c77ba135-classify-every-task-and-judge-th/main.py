statuses = "tttdirdt"

# TODO: count each status with a single for loop and if/elif/elif/else
todo_count = 0
in_progress_count = 0
review_count = 0
done_count = 0
for ch in statuses:
    if ch == 't':
        todo_count+=1
    elif ch == 'i':
        in_progress_count=+1
    elif ch == 'r':
        review_count+=1
    else:
        done_count+=1

# TODO: board_state via conditionals
total = len(statuses)
active_count = todo_count + in_progress_count + review_count

board_state = ""
if done_count == total:
    board_state = "complete"
elif done_count == 0:
    board_state = "not started"
elif done_count >= active_count:
    board_state = "mostly done"
else:
    board_state = "in progress"
# "complete" / "not started" / "mostly done" / "in progress"