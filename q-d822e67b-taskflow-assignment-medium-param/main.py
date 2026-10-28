def summarize_results(cases):
    # TODO: iterate cases, compare expected vs actual,
    # count passes and collect failing names in order
    failures = [
        case["name"]
        for case in cases
        if case["expected"] != case["actual"]
    ]
    total = len(cases)
    failed = len(failures)
    return {
        "total": total,
        "passed": total - failed,
        "failed": failed,
        "failures": failures,
    }