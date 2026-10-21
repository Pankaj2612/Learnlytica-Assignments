import pandas as pd


def status_counts(records):
    # `records` is a list of task dicts. Do NOT read any file.
    # 1. Build a DataFrame: df = pd.DataFrame(records)
    # 2. Count the 'status' column (value_counts) and return a plain dict
    #    {status: int_count}. Return {} when there are no records.
    if not records:
        return {}
    df = pd.DataFrame(records)
    if 'status' not in df.columns:
        return {}
    c = df['status'].value_counts()
   
    res = {}
    for v in c.keys():
        res[v] = int(c.get(v))
    return res
    
r = status_counts([{'status':'in progress'}])
print(r)
