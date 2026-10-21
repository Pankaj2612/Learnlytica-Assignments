import pandas as pd
import numpy as np
def fill_missing_status(records):
    """records: list[dict] of task rows. Return a list of each row's status
    with MISSING statuses filled as "todo".
    Missing = None, NaN, an absent "status" key, or a blank/whitespace-only string.
    """
    if not records:
        return []
    for record in records:
        status = record.get('status',None)
        if not status or  status.strip() == '' or status == np.nan:
            record['status'] = "todo" 
    df = pd.DataFrame(records)

    # TODO: ensure a "status" column exists even if some/all rows lack it
    # TODO: treat blank / whitespace-only strings as missing
    # TODO: fill missing with "todo" and return df["status"].tolist()
    return df["status"].tolist()

fill_missing_status([{'id':1,'status':'done'},{'id':2,'status':''}])