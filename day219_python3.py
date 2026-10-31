allowed_roles = {"student", "teacher", "admin"}

def validate_role(role):
    if role not in allowed_roles:
        raise ValueError("Invalid role")
    return role

try:
    print(validate_role("student"))
    print(validate_role("guest"))
except ValueError as error:
    print(error)
