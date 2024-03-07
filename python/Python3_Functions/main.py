from functools import reduce

# exercise 1:
# remove a specified word from a list
my_list = ["new", "fart", "old"]
my_list = list(filter(lambda l : l != "fart", my_list))
print(my_list)

print("-----------------------------------------------")

# exercise 2:
# sort a list of strings (numbers)
list_numbers = ["1", "5", "8", "2", "3", "10", "7"]
list_numbers.sort(key=lambda x: int(x))
print(list_numbers)

print("-----------------------------------------------")

# exercise 3:
# calculate the sum of negative and positive numbers in a given list
list_nums = [1, 2, 3, -4, -5, -6]
sum_of_nums = reduce(lambda a, b: a+b, list_nums)
print(sum_of_nums)

print("-----------------------------------------------")

# exercise 4:
# construct a list from the square of each even elements of a list using comprehension 
list_of_nums = [1, 2, 3, 4, 5, 6, 7, 8]
new_list_of_nums = [x**2 for x in list_of_nums if x % 2 == 0]
print(new_list_of_nums)

print("-----------------------------------------------")

# exercise 5:
# given a dict, return a new dict with the prices 10% off
dict_products = {"Chair": 20, "Table": 50, "Counter": 100, "Lamp": 25}
dict_sale = {key: value*0.9 for (key, value) in dict_products.items()}
print("sale dict: ", dict_sale)

print("-----------------------------------------------")

# exercise 6:
# return the gematria value of a given string in hebrew
def gemetria_sum(string):
    gematria_dict = {'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9, 'י': 10,
                     'כ': 20, 'ל': 30, 'מ': 40, 'נ': 50, 'ס': 60, 'ע': 70, 'פ': 80,
                     'צ': 90, 'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400, 'ך': 500, 'ם': 600,
                     'ן': 700, 'ף': 800, 'ץ': 900}
    sum_of = 0
    for ch in string:
        sum_of += gematria_dict.get(ch)
    return sum_of


print(gemetria_sum("שלום"))

print("-----------------------------------------------")

# exercise 7:
# an implementation of the Luhn algorithm for validating a credit card number
def cred_validate(credit_card):
    list_cred = list(map(lambda x: x - 9 if(x > 9) else x, (map(lambda x: int(x) * 2, credit_card[-2::-2]))))
    return ((reduce(lambda x, y: x+y, list_cred)) + (reduce(lambda x, y: int(x) + int(y), list(credit_card)[::2]))) % 10 == 0


print(cred_validate("79927398713"))

print("-----------------------------------------------")




