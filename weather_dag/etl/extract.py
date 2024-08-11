from ..air_pollution import get_current_air_pollution
from ..weather import get_city_weather, get_available_condtitions
import os
from os import path
import json
import pandas as pd

def get_current_data_from_cities():
    with open(f'{os.getenv("OUTPUT_FILES_PATH")}/city_data.json', "r") as file:
        cities = json.load(file)
        
    for city in cities:
        extract_data(city)
        

def extract_data(city):
    """
    Get the air pollution and weather data for the given city
    
    It will use the path on the env `OUTPUT_FILES_PATH` to put all of the queried data
        - Weather data will be at `$OUTPUT_FILE_PATH/extract/weather`
        - Air Pollution data will be at `$OUTPUT_FILE_PATH/extract/air_pollution`
    """
    
    date_suffix_format = "%Y-%m-%d"
    
    OUTPUT_FILES_PATH = path.abspath(os.getenv("OUTPUT_FILES_PATH"))
    if not path.exists(OUTPUT_FILES_PATH):
        os.makedirs(f'{OUTPUT_FILES_PATH}', exist_ok=True)
    
    print("Downloading report for the city ", city['name']) 
    
    air_pollution_data_dir = f'{OUTPUT_FILES_PATH}/extract/air_pollution'
    weather_data_dir = f'{OUTPUT_FILES_PATH}/extract/weather'
    
    os.makedirs(air_pollution_data_dir, exist_ok=True)
    os.makedirs(weather_data_dir, exist_ok=True)
    
    with open(f'{air_pollution_data_dir}/{city['name']}.json', 'w') as file:
        data = get_current_air_pollution(city['name'])
        data['id_city'] = city['id_city'] 
        file.write(json.dumps(data, indent=4))
    
    with open(f'{weather_data_dir}/{city['name']}.json', 'w') as file:
        data = get_city_weather(city['name'])
        data['id_city'] = city['id_city']
        file.write(json.dumps(data, indent=4))
    
def extract_available_conditions():
    """
    Will get all available weather conditions and put into `$OUTPUT_FILE_PATH/weather/conditions.json`
    """
    
    output_file_path = f'{os.getenv("OUTPUT_FILES_PATH")}/weather'
    os.makedirs(output_file_path, exist_ok=True)
    
    conditions_df = pd.DataFrame(get_available_condtitions())
    conditions_df.drop(columns=['night'], inplace=True)
    conditions_df.rename(columns={
        "day":  "name",
        "code": "weather_code"
    }, inplace=True)
    
    conditions_df.to_json(path.join(output_file_path, "conditions.json"), orient='records')