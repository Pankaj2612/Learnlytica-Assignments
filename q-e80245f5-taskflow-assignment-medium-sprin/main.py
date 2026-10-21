import numpy as np
def estimate_summary(estimates):
    # TODO: non-list -> None
    # TODO: FILTER out None entries (unestimated tasks); non-numeric -> None
    # TODO: empty (or all-None) -> {'total':0,'mean':0.0,'std':0.0,'min':0.0,'max':0.0}
    # TODO: build float array; return total(int), mean/std/min/max rounded to 2 dp
    if not isinstance(estimates,list):
        return  {'total':0,'mean':0.0,'std':0.0, 'min':0.0,'max':0.0}
    valid_Est = [x for x in estimates if x is not None]
    if len(valid_Est) == 0:
        return  {'total':0,'mean':0.0,'std':0.0, 'min':0.0,'max':0.0}
    arr = np.array(valid_Est,dtype=float)
    return  {'total':round(np.sum(arr),2),'mean':round(np.average(arr),2),'std':round(np.std(arr),2), 'min':round(np.min(arr),2),'max':round(np.max(arr),2)}