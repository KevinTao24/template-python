from functools import wraps

import jsonschema
from sanic.exceptions import InvalidUsage


def validate_params(schema):
    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            if not request.json:
                raise InvalidUsage("Request body must be JSON")

            try:
                jsonschema.validate(request.json, schema)
            except jsonschema.exceptions.ValidationError as e:
                raise InvalidUsage(str(e))

            return await f(request, *args, **kwargs)

        return decorated_function

    return decorator
