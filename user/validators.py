def phone_validator(value):
    if not len(value) == 13:
        raise ValueError("There is an error in the phone number, enter the correct phone number, for example: +998882640011")
    else:
        return True
