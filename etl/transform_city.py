import os
import pandas as pd
import numpy as np


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
