statuses = "tttdirdt"
total_tasks = len(statuses)
# TODO: total_hours via a WHILE loop (index i from 0):
#   +1 for each 'd', +3 for every other task
i = 0
total_hours = 0
while i < total_tasks:
    if statuses[i] == 'd':
        total_hours+=1
    else:
        total_hours+=3
    i+=1

# TODO: first_done_index — start at -1, for idx in range(total_tasks),
#   at first 'd' store idx and break
first_done_index = 0
for i in range(-1,total_tasks):
    if statuses[i] == 'd':
        first_done_index = i
        break

# TODO: progress_bar — string accumulator: '#' for done, '.' otherwise
progress_bar = ""
for i in range(0,total_tasks):
    if statuses[i] == 'd':
        progress_bar += '.'
    else:
        progress_bar += '#'

# TODO: headline — f-string "First done at index <first_done_index>, <total_hours>h total"
headline=f"First done at index {first_done_index} , {total_hours}h total"
