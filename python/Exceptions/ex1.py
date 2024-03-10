# define Python user-defined exceptions
class InvalidLengthException(Exception):
    # Raised when the input value is less than 8 chars long
    pass


# define Python user-defined exceptions
class InvalidLatinException(Exception):
    # Raised when the input value does not contain any latin character
    pass


# define Python user-defined exceptions
class InvalidSpecialCaseException(Exception):
    # Raised when the input value does not contain any special character
    pass


# define Python user-defined exceptions
class InvalidNumerException(Exception):
    # Raised when the input value does not contain any number
    pass


def check_length(password):
    try:
        if len(password) < 8:
            raise InvalidLengthException
    except InvalidLengthException:
        print("Exception occurred: Invalid Length of password, at least 8 characters!")
        return False
    else:
        return True


def contain_latin_alph(password):
    try:
        if not any(char.islower() for char in password) and not any(char.isupper() for char in password):
            raise InvalidLatinException
    except InvalidLatinException:
        print("Exception occurred: Invalid Password: need at least 1 latin character")
        return False
    else:
        return True


def contain_special_char(password):
    try:
        for char in password:
            if char in "@#%&":
                break
            else:
                raise InvalidSpecialCaseException
    except InvalidSpecialCaseException:
        print("Exception occurred: Invalid Password: need at least 1 special character")
        return False
    else:
        return True


def contain_nums(password):
    try:
        if not (any(char.isdigit() for char in password)):
            raise InvalidNumerException
    except InvalidNumerException:
        print("Exception occurred: Invalid Password: need at least 1 number")
        return False
    else:
        return True


def check_pass_complex(password):
    return check_length(password) and contain_nums(password) and contain_latin_alph(password) and contain_special_char(
        password)


print(f"Password check: {check_pass_complex('2132132121')}")

