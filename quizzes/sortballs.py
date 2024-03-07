# quiz: 1st way:
def sort_balls_array(balls_list):
    list_green = []
    list_yellow = []
    list_red = []
    for i in balls_list:
        if i[0] == 'g':
            list_green.append(i)
        elif i[0] == 'y':
            list_yellow.append(i)
        else:
            list_red.append(i)
    return list_green + list_yellow + list_red


# 2nd way:
def sort_array(balls_array_unsorted):
    return sorted(balls_array_unsorted, key=lambda x: {'green': 1, 'yellow': 2, 'red': 3}.get(x))


balls_array = ['yellow', 'green', 'red', 'green', 'yellow', 'green', 'red', 'yellow']
print(f"first way of sorting: {sort_balls_array(balls_array)}")
print("-------------------------------------------------------")
print(f"second way of sorting: {sort_array(balls_array)}")
