"""
A program to check if a password is valid (length, latin, number, special case) if not, throw an error
"""


class InvalidException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


def check_length(password):
    try:
        if len(password) < 8:
            raise InvalidException("Exception occurred: Invalid Length of password, at least 8 characters!")
    except InvalidException as err:
        print(err)
        return False
    else:
        return True


def contain_latin_alph(password):
    try:
        if not any(char.islower() for char in password) and not any(char.isupper() for char in password):
            raise InvalidException("Exception occurred: Invalid Password: need at least 1 latin character")
    except InvalidException as err:
        print(err)
        return False
    else:
        return True


def contain_special_char(password):
    special = "@#&%"
    try:
        for char in password:
            if special.__contains__(char):
                return True
        else:
            raise InvalidException("Exception occurred: Invalid Password: need at least 1 special character")
    except InvalidException as err:
        print(err)
        return False


def contain_nums(password):
    try:
        if not (any(char.isdigit() for char in password)):
            raise InvalidException("Exception occurred: Invalid Password: need at least 1 number")
    except InvalidException as err:
        print(err)
        return False
    else:
        return True


def check_pass_complex(password):
    return check_length(password) and contain_nums(password) and contain_latin_alph(password) and contain_special_char(
        password)


print(f"Password check: {check_pass_complex('213as%d213')}")

