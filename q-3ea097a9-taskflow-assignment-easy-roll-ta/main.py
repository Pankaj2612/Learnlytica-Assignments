import json


def status_counts_json(tasks):
    if tasks is None:
        return "{}"
    counts = {}
    # TODO: tally each task's status into counts (missing/empty status -> 'unknown')
    # TODO: return the tally as a sorted-key JSON string
    for t in tasks:
        if  t is None or t.get('status') is None:
            counts['unknown'] = counts.get('unknown',0) + 1
        else:
            counts[t['status']] = counts.get(t['status'],0) + 1

    return json.dumps(counts,sort_keys=True)        

# tasks = [
#     {"status": "open"},
#     {"status": "done"},
#     {"status": "open"},
#     {"status": ""},
#     {},
#     None
# ]

# print(status_counts_json(tasks))