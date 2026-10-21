import itertools
from itertools import islice

def paginate(items, size):
    """Lazily yield successive lists ('pages') of up to `size` items
    from the iterable `items`. If size <= 0, yield nothing.
    Hint: iter(items) + itertools.islice.
    """
    # TODO
    it = iter(items)
    while True:
        page = list(islice(it,size))
        
        if not page:
            break

        yield page
    

def find_first(events, status):
    """Return the 'id' of the first event whose 'status' matches,
    else None. Use next(<generator expression>, None).
    """
    # TODO
    
    for e in events:
        if "status" in e and e.get("status") == status:
            return e.get('id')

    return None