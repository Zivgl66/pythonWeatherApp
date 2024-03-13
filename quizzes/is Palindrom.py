
def is_palindrome(num):
    num_len = len(str(num))
    while num_len > 2:
        if int(str(num)[:1]) != num % 10:
            return False
        num = int(str(num)[1:-1])
        num_len -= 2
    if num_len == 2 and int(str(num)[:1]) == num % 10 or num_len == 1:
        return True
    else:
        return False


def is_palindrome(num):
    return str(num) == str(num)[::-1]


print(is_palindrome(2112))
