def validate_task_payload(payload):
    """Validate a TaskFlow task-creation payload.

    Return a dict: {"valid": <bool>, "errors": [<sorted error codes>]}.

    Rules (append the exact code shown, then sort the codes alphabetically):
      - "title_required"   : "title" missing, not a str, or blank after .strip()
      - "invalid_status"   : "status" is not one of
                             {"todo","in_progress","review","done"}
      - "invalid_priority" : "priority" key IS present but its value is not one of
                             {"low","medium","high"}
      - "invalid_estimate" : "estimate_hours" key IS present but its value is not a
                             real number >= 0 (booleans do NOT count as numbers)

    "valid" is True only when the errors list is empty.
    """
    # TODO: apply the four rules above, then sort errors
    raise NotImplementedError("Write your solution here")