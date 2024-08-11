import os
import pandas as pd
import numpy as np
from glob import glob
import json
from ..utils import get_datetime

def gen_city_list():
    DATA_OUTPUT_PATH = os.getenv("OUTPUT_FILES_PATH")
    
    DEMOGRAPHIC_DATA = pd.read_csv(os.getenv("DEMOGRAPHIC_DATA_PATH"))
    GEOGRAPHIC_DATA = pd.read_csv(os.getenv("GEOGRAPHIC_DATA_PATH"))
    
    GEOGRAPHIC_DATA = GEOGRAPHIC_DATA.merge(DEMOGRAPHIC_DATA, on='Location', how='inner')
    GEOGRAPHIC_DATA.insert(0, 'id_city', range(len(GEOGRAPHIC_DATA)))
    
    GEOGRAPHIC_DATA.rename(columns={
        "Location": 'name',
        "Population": 'population',
        "Density (people/km²)": 'population_density',
        "Urbanization (%)": 'urbanization',
        "Average Income (USD)": 'average_income',
        "Education Level (% with Bachelor's or higher)": 'education_level',
        "Altitude (m)": 'altitude',
        "Proximity to Industry (km)": 'proximity_to_industry'
    }, inplace=True)
    
    GEOGRAPHIC_DATA.to_json(f'{DATA_OUTPUT_PATH}/city_data.json', indent=4, orient='records')



def transform_data():
    data = []
    
    output_file = open(f'{os.getenv("OUTPUT_FILES_PATH")}/transform.json', 'w')
    os.makedirs(f'{os.getenv("OUTPUT_FILES_PATH")}', exist_ok=True)
    
    pollution_data_paths = glob(f'{os.getenv("OUTPUT_FILES_PATH")}/extract/air_pollution/*.json')
    for pollution_data_path in pollution_data_paths:
        pollution_data = json.loads(open(pollution_data_path, 'r').read())
        weather_data = _get_weather_data(pollution_data['id_city'])
        data.append({
            **pollution_data['list'][0]['components'],
            "air_quality": pollution_data['list'][0]['main']['aqi'],
            "dt": get_datetime(pollution_data['list'][0]['dt']).strftime("%Y-%m-%d"),
            "id_city": pollution_data['id_city'],
            "temp": weather_data['temp_c'],
            "weather_code": weather_data['condition']['code']
        })
    
    output_file.write(json.dumps(data, indent=4))

def _get_weather_data(city_id):
    cities = pd.read_json(f'{os.getenv("OUTPUT_FILES_PATH")}/city_data.json')
    city_name = cities.loc[cities['id_city'] == city_id].iloc[0]['name']
    return json.load(open(f'{os.getenv("OUTPUT_FILES_PATH")}/extract/weather/{city_name}.json', 'r'))