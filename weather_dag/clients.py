import httpx
import os

# General Client for weather requests
client = httpx.Client(base_url="https://api.openweathermap.org/data/2.5", params={
    "appId": os.getenv("OPENWEATHER_API_KEY"),
})

# Gocoding client for all Coordinates and Country operations
geoCodingClient = httpx.Client(base_url="http://api.openweathermap.org/geo/1.0", params={
    "appId": os.getenv("OPENWEATHER_API_KEY"),
})

# BulkFiles client for retrieving historical data (premium) sob :( 
bulkFilesClient = httpx.Client(base_url="https://bulk.openweathermap.org", params={
    "appId": os.getenv("OPENWEATHER_API_KEY")
})

# Air pollution client for retrieving air pollution data
airpolutionClient = httpx.Client(base_url="http://api.openweathermap.org/data/2.5/air_pollution", params={
    "appId": os.getenv("OPENWEATHER_API_KEY")
})

# Weather API client for historical weather data
weatherApiClient = httpx.Client(base_url="http://api.weatherapi.com/v1", params={
    "key": os.getenv("WEATHERAPI_KEY")
})