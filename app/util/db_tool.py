def unrequire(fields):
    for field in fields.items():
        if field[1].required:
            field[1].required = False
    return fields
