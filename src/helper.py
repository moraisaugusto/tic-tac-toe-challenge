from functools import wraps

import flask
from werkzeug.exceptions import BadRequest


def is_json_request(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not flask.request.is_json:
            raise BadRequest(
                "Invalid request, must be a JSON request. Please, try again"
            )
        return f(*args, **kwargs)

    return wrapper
