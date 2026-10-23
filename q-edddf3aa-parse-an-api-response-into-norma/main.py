def extract_tasks(response):
    # Return a sorted list of normalised task dicts from an API response.
    
    if not isinstance(response,dict)  or response.get('status') != 'ok':
        return []
    status = ['todo','in_progress','review','done']
    r = []
    if 'data' in response:
        data = response['data']
        for d in data:
            if not 'id' in d or not d['id']:
                continue
            d['id'] = int(d['id'])
            d['title'] = d.get('title','').strip()
            stat = d.get('status','').strip().lower()
            if stat not in status:
                d['status'] = 'todo'
            
            try:
                p = int(d['priority'])
                p = max(1,min(p,5))
                d['priority'] = p 
            except:
                d['priority'] = 3
            
            r.append({'id':d['id'],'title':d['title'],'status':d['status'],'priority':d['priority']})
    else:
        return []
    return sorted(r,key=lambda x : x['id'])


def api_fixture():
    return {
        "status": "ok",
        "data": [
            {"id": 3, "title": "  Ship release  ", "status": "In_Progress", "priority": "2"},
            {"id": 1, "title": "Fix login bug", "status": "TODO", "priority": 9},
            {"id": 2, "title": "Write docs", "priority": None},
            {"id": None, "title": "orphan", "status": "done"},
        ],
    }

print(extract_tasks({'status': 'ok', 'data': [{'title': 'no id', 'status': 'done'}]}))