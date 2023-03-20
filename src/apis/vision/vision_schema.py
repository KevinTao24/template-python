USER = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "senderId": {"type": "string"},
        "name": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "age": {"type": "integer"},
    },
    "required": ["name", "email", "age"],
    "additionalProperties": False,
}
