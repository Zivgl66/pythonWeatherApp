from datetime import datetime
from deep_translator import GoogleTranslator


# from a given data response, extract the date and reformmat and return it to a list of week days strings.
def get_weekday(data):
    day_list= []
    for i in range(7):
        day = datetime.strptime(data['days'][i]['datetime'], '%Y-%m-%d')
        day = day.strftime('%A')
        day_list.append(day)
    return day_list
    

def validate_input(input):
    # input validation on a given input, if it's not validated, return a string of the error, else return 'OK'
    if input == '':
        return "Input cant be empty"
    for x in input:
        if x.isdigit():
            return "Input cant include Numbers!"
        if x in "!@#$%^&*()_+?/*/+-":
            return "Input cant include Special chars!"
        
    return "OK"

def translate(input):
    # return a translated string to english from a given input
    return GoogleTranslator(source='auto', target='en').translate(input)

