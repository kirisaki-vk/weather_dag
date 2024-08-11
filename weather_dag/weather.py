import json
from .clients import weatherApiClient 
from datetime import datetime

def get_city_weather(city_name):
    return json.loads(
        weatherApiClient.get(
            'current.json',
            params={
                "q": city_name
            }
        ).read()
    )['current']
    
def get_past_weather_data(city_name, date: datetime, aqi = "no"):
    return json.loads(
        weatherApiClient.get(
            'history.json',
            params={
                "q": city_name,
                "dt": date.isoformat(),
                "aqi": aqi
            }
        ).read()
    )['forecast']['forecastday'][0]
    
def get_available_condtitions():
    weather_conditions_index_url = 'https://www.weatherapi.com/docs/weather_conditions.json'
    return json.loads(
        weatherApiClient.request("GET", weather_conditions_index_url).read()
    )
