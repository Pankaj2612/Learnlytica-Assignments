def dag_fixture():
    return [
        {'id': 'a', 'parents': []},
        {'id': 'b', 'parents': ['a']},
        {'id': 'c', 'parents': ['a']},
        {'id': 'm', 'parents': ['b', 'c']},  # merge commit
        {'id': 'd', 'parents': ['m']},
    ]

def ancestors(commits, commit_id):
    # sorted list of all transitive ancestor ids (excluding commit_id)
    commits = to_dict(commits)
    if commit_id not in commits:
        return []
    
    s =  set()
    stack = list(commits[commit_id]['parents'])

    while stack:
        curr = stack.pop()
        if curr not in s:
            s.add(curr)
            if curr in commits:
                for p in commits[curr]['parents']:
                    if p not in s:
                        stack.append(p)

    return sorted(list(s))
def is_ancestor(commits, a, b):
    # True if a is an ancestor of b
    commits = to_dict(commits)
    if a == b:
        return False

    if b not in commits:
        return False

    s = set()
    stack = list(commits[b]['parents'])
    while stack:
        curr = stack.pop()

        if curr == a:
            return True

        if curr not in s:
            s.add(curr)
            if curr in commits:
                for p in commits[curr]['parents']:
                    if p not in s:
                        stack.append(p)
    return False


def to_dict(commits:list):
    d = {}
    for i in commits:
        d[i['id']] = i
                        
    return d

print(is_ancestor(dag_fixture(),'a','d'))