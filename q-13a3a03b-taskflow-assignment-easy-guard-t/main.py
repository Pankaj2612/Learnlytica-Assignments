"""TaskFlow S9 - Easy. Fill in the TODOs. Do not use input()/print for grading."""

class TaskFlowError(Exception):
    """Base of every TaskFlow domain error."""
    pass
    

# TODO: define InvalidStatusError as a subclass of TaskFlowError
class InvalidStatusError(TaskFlowError):
    def __init__(self,msg):
        super().__init__(msg)

VALID_STATUSES = {"todo", "in_progress", "done", "blocked"}

def validate_status(status):
    # TODO: return status if it is in VALID_STATUSES,
    #       otherwise raise InvalidStatusError(f"invalid status: {status}") 
    if status not in VALID_STATUSES:
        raise InvalidStatusError(f"invalid status: {status}")
    
    return status

def safe_validate_status(status):
    # TODO: call validate_status inside try/except.
    #       Return the status on success; on InvalidStatusError return
    #       the string f"error: {the exception message}"
    try:
        return validate_status(status)
    except InvalidStatusError as e:
        return f"error: {str(e)}"