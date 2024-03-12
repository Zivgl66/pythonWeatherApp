"""
    This module is part of the Python3 - Data Structures Worksheet
    Exercises 1 - 8

    CR: Denis Vasilevsky
"""


# ex 1 :remove all elements except string type from a given list
def remove_str_from_list(my_list):
    for item in my_list[:]:
        if not isinstance(item, str):
            my_list.remove(item)
    # if any(not isinstance(item,str) for item in my_list[:])



# ex 2 :return a dict of how many times each letter appears in a string
def check_occurrence(stringa):
    my_dict = {}
    for elm in stringa:
        if elm in my_dict:
            my_dict[elm] = my_dict.get(elm) + 1
        else:
            my_dict[elm] = 1
    return my_dict


# ex 2 :return a dict of how many times each letter appears in a string
def check_occurrence_a(stringa):
    my_dict = {}
    for elm in stringa:
        try:
            my_dict[elm] = my_dict.get(elm) + 1
        except:
            my_dict[elm] = 1
    return my_dict


# ex 2 :return a dict of how many time each letter appears in a string
def check_occurrence_b(stringa):
    my_dict = {}
    for elm in stringa:
        my_dict[elm] = my_dict.get(elm, 0) + 1
    return my_dict


# ex 3 :given 2 lists, return a new list with the same occurring elements
def only_in_both_lists(list1, list2):
    new_list = []
    for i in (list1 if len(list1) > len(list2) else list2):
        if i in list1 and i in list2 and i not in new_list:
            new_list.append(i)
    return new_list


# ex 4 :return a unique values list from a given dict
def unique_dict(dictionary):
    return list(set(dictionary.values()))


# ex 4 :return how many times a given value appears in a given dict
def check_occurrence_dict(dictionary, val):
    count = 0
    for value in dictionary.values():
        if value == val:
            count += 1
    return count


# ex 4 :return a list from a given dict, of only its unique values
def unique(dictionary):
    unique_list = list(dictionary.values())
    for x in unique_list[:]:
        if check_occurrence_dict(dictionary, x) > 1:
            unique_list.remove(x)
    return unique_list


# ex 5 :move elements in a list to the left
def rotate_list_left(my_list):
    # first_element = my_list[0]
    # my_list = my_list[1:]
    # my_list.append(first_element)
    return my_list[1:] + my_list[:1]


# ex 6 :print and remove every other element in a list until it is empty
def remove_and_print_every_second(lis):
    count = 1
    while len(lis) > 0:
        print(lis.pop(count)) if len(lis) > count else print(lis.pop(0))
        if len(lis) > count:
            count += 1
        else:
            count -= (len(lis) - 1)


# ex 7 :convert a given dict to a list of tuples
def convert_dict_to_list_tup(dictionary):
    return [(k, v) for k, v in dictionary.items()]


# ex 8 :print the keys of the min and max values from a given dict
def get_max_and_min(dictionary):
    key_list = list(dictionary.keys())
    val_list = list(dictionary.values())
    min_val = val_list[0]
    max_val = val_list[0]
    for k, v in dictionary.items():
        if min_val > v:
            min_val = v
        if max_val < v:
            max_val = v
    position = val_list.index(min_val)
    print("Min Value: " + key_list[position])
    position = val_list.index(max_val)
    print("Max Value: " + key_list[position])


print("-----------------------------------------------------------------------------------------------------------")

my_list_lilo = [1, 3, "het", "bla", 5]
print(remove_str_from_list(my_list_lilo))
print("-----------------------------------------------------------------------------------------------------------")

string = "hello"
print(check_occurrence_b(string))
print("-----------------------------------------------------------------------------------------------------------")

print(only_in_both_lists([1, 2, 5, 6, 7, 6], [1, 2, 4, 5, 6]))
print("-----------------------------------------------------------------------------------------------------------")

print(unique({"new": 1, "newt": 1, "newer": 2}))
print("-----------------------------------------------------------------------------------------------------------")

print(rotate_list_left([1, 2, 3, 4, 5]))
print("-----------------------------------------------------------------------------------------------------------")

remove_and_print_every_second([1, 2, 3, 4, 5, 6, 7, 8])
print("-----------------------------------------------------------------------------------------------------------")

print(convert_dict_to_list_tup({'chuck': 10, 'sink': 12, 'MInk': 31}))
print("-----------------------------------------------------------------------------------------------------------")

get_max_and_min({'chuck': 10, 'sink': 12, 'MInk': 31, "FLik": 23, "Lucky": 2})
print("-----------------------------------------------------------------------------------------------------------")

