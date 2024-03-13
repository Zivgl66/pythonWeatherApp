from datetime import datetime

def fer_to_cel(deg):
    return (deg - 32) // 1.8

def get_weekday(data):
    day_list= []
    for i in range(7):
        day = datetime.strptime(data['days'][i]['datetime'], '%Y-%m-%d')
        day = day.strftime('%A')
        day_list.append(day)
    return day_list
    

def validate_input(input):
    if input == '':
        return "Input cant be empty"
    for x in input:
        if x.isdigit():
            return "Input cant include Numbers!"
        if x in "!@#$%^&*()_+?/*/+-":
            return "Input cant include Special chars!"
        
    return "OK"
