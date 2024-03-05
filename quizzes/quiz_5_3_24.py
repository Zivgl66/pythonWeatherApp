def replace_five(num):
    str_num = str(num)
    for i in range(len(str_num)):
        if int(str_num[i]) < 5:
            return int(str_num.replace(str_num[i],"5" , 1))
        i += 1
    return num

print(replace_five(661))
