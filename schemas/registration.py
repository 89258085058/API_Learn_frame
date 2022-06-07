# schemas/registration.py
valid_schema = {
    "type": "object",
    "properties": {
        "message": {"type": "string"},
        "uuid": {"type": "number"},
    },
    "required": ["message", "uuid"]
}
