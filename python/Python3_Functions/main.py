from functools import reduce

# exercise 1:
my_list = ["new", "fart", "old"]
my_list = list(filter(lambda l : l != "fart", my_list))
print(my_list)

print("-----------------------------------------------")

# exercise 2:
list_numbers = ["1", "5", "8", "2", "3", "10", "7"]
list_numbers.sort(key=lambda x: int(x))
print(list_numbers)

print("-----------------------------------------------")

# exercise 3:
list_nums = [1, 2, 3, -4, -5, -6]
sum_of_nums = reduce(lambda a, b: a+b, list_nums)
print(sum_of_nums)

print("-----------------------------------------------")

# exercise 4:
list_of_nums = [1, 2, 3, 4, 5, 6, 7, 8]
new_list_of_nums = [x**2 for x in list_of_nums if x % 2 == 0]
print(new_list_of_nums)

print("-----------------------------------------------")

# exercise 5:



