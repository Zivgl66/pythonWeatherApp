from itertools import groupby


def run_length(runner):
    counter = 0
    return_str = ''
    temp = runner[0]
    for letter in runner:
        if temp == letter:
            counter = counter + 1
        else:
            if counter == 1:
                return_str = return_str + temp
            else:
                return_str = return_str + str(counter) + temp
            temp = letter
            counter = 1
    if counter == 1:
        return_str = return_str + temp
    print(return_str)
    
run_length('WWWWWBBWWWWWBBBBWWWB')
    
    
def run_length1(runner):
    result = []
    for char, group in groupby(runner):
        group_list = list(group)
        length = len(group_list)
        if length > 1:
            result.append(f"{length}{char}")
        else:
            result.append(char)
    print(''.join(result))
    
run_length1("WWWWWBBWWWWWBBBBWWWB")
    
def run_length2(runner):
    result = ''.join(f'{print(len(list(group))) if len(list(group)) > 1 else ""}{char}' for char, group in groupby(runner))
    print(result)
    
run_length2('WWWWWBBWWWWWBBBBWWWB')
    
    