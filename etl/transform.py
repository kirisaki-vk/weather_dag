from datetime import datetime
import pandas as pd
from os import path
import os
import json


def transform_all_files_in(directory, callback):
    files = os.listdir(directory)
    for file in files:
        file = path.join(directory, file)
        if path.isfile(file):
            callback(file)


OUTPUT_FILES_PATH = path.abspath(os.getenv("OUTPUT_FILES_PATH"))


def map_air_pollution_frame_to_sql():
    def get_city_name(id):
        city_path = f'{OUTPUT_FILES_PATH}/city_data.json'
        dataframe = pd.read_json(city_path)
        return dataframe.loc[dataframe['id_city'] == id]['name']

    def get_weather_city_file(city):
        return f'{city}_{datetime.now().strftime("%Y-%m-%d")}.json'

    def transform_air_pollution_frame(file: str):
        obj = json.load(open(file, 'r'))
        id_city = obj['id_city']
        lis_item = ['list'][0]
        components = lis_item['components']
        weather_city_json = open(path.join(OUTPUT_FILES_PATH, get_weather_city_file(get_city_name(id_city))))
        weather_city = json.load(weather_city_json)
        df = pd.DataFrame({
            **components,
            "date": pd.to_datetime(lis_item['dt']),
            "id_city": id_city,
            "air_quality": lis_item["main"]["aqi"],
            "temp": weather_city['temp_c'],
            "weather_code": weather_city['condition']['code']
        })
        df.to_json(path.join(OUTPUT_FILES_PATH, '/transforms/air_pollution.json'), orient='records')

    air_pollution_data_dir = f'{OUTPUT_FILES_PATH}/air_pollution'
    transform_all_files_in(air_pollution_data_dir, transform_air_pollution_frame)

