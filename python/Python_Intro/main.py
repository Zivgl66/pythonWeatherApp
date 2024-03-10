def countCharInStr(string, char):
    return string.count(char)

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
    return any(i.islower() for char in password) and any(i.isupper() for char in password)



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


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num - 1, 1):
        if num % i == 0:
            return False
    return True


def minimum_bills(money):
    bills = [200, 100, 50, 20, 10, 5, 2, 1]
    min_bills = 0
    min_coins = 0
    for b in bills:
        if money // b > 0:
            sum = money // b  # Checks how many bills can be entered into the amount of money.
            money %= b  # reassigns money to itself modulo the bill.
            if b <= 10:  # Checking whether the current iteration is a bill or a coin.
                min_coins += sum
            else:
                min_bills += sum
            print(f"{b} : {sum}")
    print(f"minimum number of bills: {min_bills}")
    print(f"minimum number of coins: {min_coins}")


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
print(is_prime(33))
