# TaskFlow — Error Signaling (Medium)
# A validation layer that RAISES, wrapped by a caller that CATCHES into an error dict.
#
# validate_task(payload) raises ValidationError(message, field=...) on the FIRST bad field:
#   * title: required, non-empty string (after strip)      -> field 'title'
#   * status: optional, default 'todo', in {todo,in_progress,done} -> field 'status'
#   * priority: optional, default 'medium', in {low,medium,high}   -> field 'priority'
#   * estimate_hours: optional; if present must be a real number >= 0 (bool is NOT a number)
#                                                          -> field 'estimate_hours'
#   * non-dict payload -> ValidationError('payload must be an object', field=None)
#   On success returns {'title': <stripped>, 'status': ..., 'priority': ...}
#
# submit_task(payload) calls validate_task and returns:
#   success -> {'ok': True, 'task': <validated dict>}
#   failure -> {'ok': False, 'error': {'status':422,'code':'validation_error','message':...,'field':...}}

class TaskFlowError(Exception):
    status = 500
    code = 'internal_error'

class ValidationError(TaskFlowError):
    status = 422
    code = 'validation_error'
    def __init__(self, message, field=None):
        super().__init__(message)
        self.field = field

def validate_task(payload):
    if not isinstance(payload, dict):
        raise ValidationError('payload must be an object', field=None)

    title = payload.get('title')
    if not isinstance(title, str) or not title.strip():
        raise ValidationError('title is required', field='title')

    status = payload.get('status', 'todo')
    if not isinstance(status, str) or status not in {'todo', 'in_progress', 'done'}:
        raise ValidationError('status is invalid', field='status')

    priority = payload.get('priority', 'medium')
    if not isinstance(priority, str) or priority not in {'low', 'medium', 'high'}:
        raise ValidationError('priority is invalid', field='priority')

    if 'estimate_hours' in payload:
        estimate_hours = payload['estimate_hours']
        if (
            isinstance(estimate_hours, bool)
            or not isinstance(estimate_hours, (int, float))
            or not estimate_hours >= 0
        ):
            raise ValidationError(
                'estimate_hours must be a non-negative number',
                field='estimate_hours',
            )

    return {'title': title.strip(), 'status': status, 'priority': priority}

def submit_task(payload):
    try:
        task = validate_task(payload)
    except ValidationError as exc:
        return {
            'ok': False,
            'error': {
                'status': 422,
                'code': 'validation_error',
                'message': str(exc),
                'field': exc.field,
            },
        }
    return {'ok': True, 'task': task}