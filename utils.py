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