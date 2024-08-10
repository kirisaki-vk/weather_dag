from ..air_pollution import get_current_air_pollution
from ..weather import get_city_weather, get_available_condtitions
import os
from os import path
import json
from datetime import datetime

def get_current_data_from_cities(*cities):
    for city in cities:
        extract_data(city)
        

def extract_data(city):
    """
    Get the air pollution and weather data for the given city
    
    It will use the path on the env `OUTPUT_FILES_PATH` to put all of the queried data
        - Weather data will be at `$OUTPUT_FILE_PATH/weather`
        - Air Pollution data will be at `$OUTPUT_FILE_PATH/air_pollution`
    """
    
    date_suffix_format = "%Y-%m-%d"
    
    OUTPUT_FILES_PATH = path.abspath(os.getenv("OUTPUT_FILES_PATH"))
    if not path.exists(OUTPUT_FILES_PATH):
        os.makedirs(f'{OUTPUT_FILES_PATH}', exist_ok=True)
    
    print("Downloading report for the city ", city) 
    
    air_pollution_data_dir = f'{OUTPUT_FILES_PATH}/air_pollution'
    weather_data_dir = f'{OUTPUT_FILES_PATH}/weather'
    
    os.makedirs(air_pollution_data_dir, exist_ok=True)
    os.makedirs(weather_data_dir, exist_ok=True)
    
    with open(f'{air_pollution_data_dir}/{city}_{datetime.now().strftime(date_suffix_format)}.json', 'w') as file:
        file.write(json.dumps(get_current_air_pollution(city), indent=4))
    
    with open(f'{weather_data_dir}/{city}_{datetime.now().strftime(date_suffix_format)}.json', 'w') as file:
        file.write(json.dumps(get_city_weather(city), indent=4))
    
def extract_available_conditions():
    """
    Will get all available weather conditions and put into `$OUTPUT_FILE_PATH/weather/conditions.json`
    """
    
    output_file_path = f'{os.getenv("OUTPUT_FILES_PATH")}/weather'
    os.makedirs(output_file_path, exist_ok=True)
    
    with open(f'{output_file_path}/conditions.json', "w") as file:
        file.write(json.dumps(get_available_condtitions(), indent=4))