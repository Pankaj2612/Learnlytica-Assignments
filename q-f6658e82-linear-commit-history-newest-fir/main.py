def commits_fixture():
    return [
        {'id': 'a1', 'parent': None, 'message': 'init TaskFlow repo'},
        {'id': 'b2', 'parent': 'a1', 'message': 'add Task model'},
        {'id': 'c3', 'parent': 'b2', 'message': 'add status field'},
        {'id': 'd4', 'parent': 'c3', 'message': 'add priority field'},
    ]

def history_messages(commits, head_id):
    # walk parent pointers from head_id, collecting messages newest-first
    commits = to_dict(commits)
    log = []
    while True:
        if head_id not in commits:
            return []

        log.append(commits[head_id]['message'])
        if commits[head_id]['parent'] is None:
            break
        head_id = commits[head_id]['parent']
    
    return log

def to_dict(commits:list):
    d = {}
    for i in commits:
        d[i['id']] = i
    
    return d
        
# print(history_messages(commits_fixture(),'c3'))