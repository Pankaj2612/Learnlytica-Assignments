"""TaskFlow S9 - Medium. Complete the hierarchy and the reporting function."""

class TaskFlowError(Exception):
    pass

class ValidationError(TaskFlowError):
    pass

# TODO: MissingFieldError and InvalidValueError, both subclasses of ValidationError
class MissingFieldError(ValidationError):
    pass

class InvalidValueError(ValidationError):
    pass

VALID_STATUSES = {"todo", "in_progress", "done", "blocked"}
REQUIRED_FIELDS = ("title", "status", "priority")

def validate_task(task):
    # TODO: raise MissingFieldError("missing field: <name>") for any absent required field.
    # TODO: raise InvalidValueError for: empty/whitespace title, bad status,
    #       priority not an int in 1..5 (reject booleans too). Return True if ok.
    for field in REQUIRED_FIELDS:
        if field not in task:
            raise MissingFieldError(f"missing field: {field}")
    
    title = task["title"]
    priority = task["priority"]
    if not isinstance(title,str) or not title.strip():
        raise InvalidValueError(f"invalid title")
    if task['status'] not in VALID_STATUSES:
        raise InvalidValueError(f"invalid status: {task['status']}")
    if type(priority) is not int or not (1 <= task['priority'] <= 5):
        raise InvalidValueError(f"invalid priority: {priority}")
    return True

def validate_task_report(task):
    # TODO: call validate_task inside try/except/else/finally and build a report dict:
    #   ok      -> {"valid": True,  "error_type": None,               "message": "ok"}
    #   missing -> {"valid": False, "error_type": "MissingFieldError","message": <str(exc)>}
    #   invalid -> {"valid": False, "error_type": "InvalidValueError","message": <str(exc)>}
    # In finally, add result["checked"] = True. Return the report.
    report = {}
    try:
        validate_task(task)
    except ValidationError as e:
        report = {"valid":False,"error_type":type(e).__name__,"message":str(e)}
        return report
    else:
        report = {"valid":True,"error_type":None,"message":"ok"}
        return report

    finally:
        report["checked"] = True

    return report

print(validate_task_report({'title':'','status':'done','priority':"true"}))