import json
from .geocoding import get_city_coordinates
from .clients import airpolutionClient
from .utils import get_unix_time
import os

def get_air_pollution(start, end, city_name):
    """_Get the air pollution from a given city name_

    Args:
        start (_datetime_): Start date_
        end (_datetime_): End date_
        city_name (_string_): Description_

    Returns:
        _Any_: _The air pollution data in format of OpenWeather historical airpollution_
    """
    city_coordinates = get_city_coordinates(city_name)
    
    return json.loads(airpolutionClient.get("history",params={
        "lat": city_coordinates['lat'],
        "lon": city_coordinates['lon'],
        "start": get_unix_time(start),
        "end": get_unix_time(end) 
    }).read())
    
def get_current_air_pollution(country_name):
    """
    Get the current air pollution for the current date
    """
    country_coordinates = get_city_coordinates(country_name)
    
    return json.loads(airpolutionClient.request("GET", "http://api.openweathermap.org/data/2.5/air_pollution", params={
        "lat": country_coordinates['lat'],
        "lon": country_coordinates['lon'],
    }).read())
    