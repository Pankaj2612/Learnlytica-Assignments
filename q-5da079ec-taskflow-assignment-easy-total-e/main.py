import numpy as np

def total_estimated_hours(estimates):
    # TODO: if estimates is not a list, return None
    # TODO: if any entry is None or non-numeric, return None (never NaN)
    # TODO: empty list -> 0
    # TODO: build a float NumPy array and return int(arr.sum())
    if not isinstance(estimates,list):
        return None
    if not estimates:
        return 0
    for n in estimates:
        if not isinstance(n,int):
            return None
    num = np.array(estimates)
    return int(num.sum())