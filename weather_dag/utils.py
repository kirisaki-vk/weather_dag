import math
import time
from datetime import datetime

def get_unix_time(date):
    """
    Transforms a given datetime to an unix date
    """
    return math.floor(time.mktime(date.timetuple()))


def get_datetime(unix_time):
    """
    Get the datetime from a given unix time
    """
    return datetime.fromtimestamp(unix_time)

def flatten_air_pollution(air_pollution_component):
    return {
        'air_quality': air_pollution_component['main']['aqi'],
        **air_pollution_component['components'],
        "dt": air_pollution_component['dt']
    }

def flatten_weather(weather):
    return {
        "temp": weather['day']['avgtemp_c'],
        "weather_code": weather['day']['condition']['code'],
        "dt": weather['date']
    }
