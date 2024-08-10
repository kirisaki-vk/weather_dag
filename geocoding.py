import json
from .clients import geoCodingClient

def get_city_coordinates(city):
    """
    Get city coordinates from a city name
    """
    return json.loads(
        geoCodingClient.get(
            "direct",
            params= {
                "q": city
            }
        ).read()
    )[0]

def get_city_name(lat, lon, limit = None):
    """
    Get city name from a coordinates
    """
    return json.loads(
        geoCodingClient.get(
            "reverse",
            params={
                "lat": lat,
                "lon": lon,
                "limit": limit
            }
        ).read()
    )