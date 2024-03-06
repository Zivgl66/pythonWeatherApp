def removeStrFromList(my_list):
    for item in my_list[:]:
        if not isinstance(item, str):
            my_list.remove(item)


def checkOccurrence(string):
    my_dict = {}
    for elm in string:
        if elm in my_dict:
            my_dict[elm] = my_dict.get(elm) + 1
        else:
            my_dict[elm] = 1
    return my_dict


def checkOccurrenceA(string):
    my_dict = {}
    for elm in string:
        try:
            my_dict[elm] = my_dict.get(elm) + 1
        except:
            my_dict[elm] = 1
    return my_dict


def checkOccurrenceB(string):
    my_dict = {}
    for elm in string:
        my_dict[elm] = my_dict.get(elm, 0) + 1
    return my_dict


def onlyInBothLists(list1, list2):
    new_list = []
    for i in (list1 if len(list1) > len(list2) else list2):
        if i in list1 and i in list2 and i not in new_list:
            new_list.append(i)
    return new_list


def uniqueDict(dictionary):
    return list(set(dictionary.values()))


def checkOccurrenceDict(dictionary, val):
    count = 0
    for value in dictionary.values():
        if value == val:
            count += 1
    return count


def unique(dictionary):
    s = list(dictionary.values())
    for x in s[:]:
        if checkOccurrenceDict(dictionary, x) > 1:
            s.remove(x)
    return s


def rotateListLeft(my_list):
    # first_element = my_list[0]
    # my_list = my_list[1:]
    # my_list.append(first_element)
    return my_list[1:] + my_list[:1]


def removeAndPrintEverySecond(lis):
    count = 1
    while (len(lis) > 0):
        print(lis.pop(count)) if len(lis) > count else print(lis.pop(0))
        if len(lis) > count:
            count += 1
        else:
            count -= (len(lis) - 1)


def convertDictToListTup(dictionary):
    return [(k, v) for k, v in dictionary.items()]


def getMaxAndMin(dictionary):
    key_list = list(dictionary.keys())
    val_list = list(dictionary.values())
    min = val_list[0]
    max = val_list[0]
    for k, v in dictionary.items():
        if min > v: min = v
        if max < v: max = v
    position = val_list.index(min)
    print("Min Value: " + key_list[position])
    position = val_list.index(max)
    print("Max Value: " + key_list[position])


my_list = [1, 3, "het", "bla", 5]
removeStrFromList(my_list)
print(my_list)
string = "hello"
print(checkOccurrenceB(string))
print(onlyInBothLists([1, 2, 5, 6, 7, 6], [1, 2, 4, 5, 6]))
print(unique({"new": 1, "newt": 1, "newr": 2}))
print(rotateListLeft([1, 2, 3, 4, 5]))
print("------------------------------------------------")
removeAndPrintEverySecond([1, 2, 3, 4, 5, 6, 7, 8])
print(convertDictToListTup({'chuck': 10, 'sink': 12, 'MInk': 31}))
getMaxAndMin({'chuck': 10, 'sink': 12, 'MInk': 31, "FLik": 23, "Lucky": 2})
