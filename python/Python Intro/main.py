def flipNum(num):
    new_num = 0
    while (num > 0):
        new_num = (new_num * 10) + (num % 10)
        num //= 10
    return new_num


def flipAll(num):
    return str(num)[::-1]


def celToFer(cel):
    return (cel * 1.8) + 32


def leapYear(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def checkLength(password):
    return len(password) >= 8


def containLatinAlph(password):
    for i in password:
        if i in "abcdefghijklmnopqrstuvwxyz" or i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return True
    return False


def containSpecialChar(password):
    for i in password:
        if i in "@#%&":
            return True
    return False


def containNums(password):
    return any(char.isdigit() for char in password)


def checkPassComplex(password):
    return checkLength(password) and containNums(password) and containLatinAlph(password) and containSpecialChar(
        password)


def sumOfDiv(num):
    sum = 0
    for i in range(1, num - 1, 1):
        if num % i == 0:
            sum += i
    return sum


def isPrime(num):
    if num == 1:
        return False
    for i in range(2, num - 1, 1):
        if num % i == 0:
            return False
    return True


print(flipNum(1234))
print(flipAll(1234))
print(flipAll(1234.56))
print(celToFer(24))
print(leapYear(800))
print(containNums("asdsad"))
print(containLatinAlph("123213"))
print(containSpecialChar("1232@13"))
print(checkLength("1232@132"))
print(checkPassComplex("12345!asd"))
print(sumOfDiv(10))
print(isPrime(33))
