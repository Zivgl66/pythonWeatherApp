import string

def check_pangram(str):
    for letter in string.ascii_lowercase:
        if letter not in str.lower():
            return False
    return True

print(check_pangram("The Quick BROWN fox jumps over the la dog"))