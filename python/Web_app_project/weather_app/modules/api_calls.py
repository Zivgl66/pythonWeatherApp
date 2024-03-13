import requests

API_KEY = "JYZTBA9Z5B9VPCUEWDMYLZHTC"


def get_weather(location):
    # with a give string of location, make an api call and return the data parsed to json of the weather info
    res = requests.get(f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?key={API_KEY}&unitGroup=metric')
    if res.status_code == 200:
        data = res.json()
        return data
    else:
        return 400


