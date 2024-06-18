import json
from datetime import datetime
import requests
import os


def get_weather(location):
    # with a give string of location, make an api call and return the data parsed to json of the weather info
    res = requests.get(f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?key=JYZTBA9Z5B9VPCUEWDMYLZHTC&unitGroup=metric')
    if res.status_code == 200:
        data = res.json()
        return data
    else:
        return 400


def save_query(city, weather_data):
    # Prepare the query data
    query = {
        "city": city,
        "date": datetime.now().isoformat(),
        "weather_data": weather_data
    }
    
    # Define the file path based on city
    file_path = os.path.join('data', f'{city}.json')
    
    # Check if the file exists
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            print(f"Warning: The file {file_path} is corrupted. Initializing a new file.")
            data = []
    else:
        data = []
    
    # Append the new query to the existing data
    data.append(query)
    
    # Write the updated data back to the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

    # print(f"Query saved: {query}")