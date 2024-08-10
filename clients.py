import httpx
import os

# General Client for weather requests
client = httpx.Client(base_url=os.getenv("API_BASE_URL"), params={
    "appId": os.getenv("OPENWEATHER_API_KEY"),
})

# Gocoding client for all Coordinates and Country operations
geoCodingClient = httpx.Client(base_url=os.getenv("GEOCODING_BASE_URL"), params={
    "appId": os.getenv("OPENWEATHER_API_KEY"),
})

# BulkFiles client for retrieving historical data (premium) sob :( 
bulkFilesClient = httpx.Client(base_url=os.getenv("BULK_API_URL"), params={
    "appId": os.getenv("OPENWEATHER_API_KEY")
})

# Air pollution client for retrieving air pollution data
airpolutionClient = httpx.Client(base_url=os.getenv("AIRPOLLUTION_API_URL"), params={
    "appId": os.getenv("OPENWEATHER_API_KEY")
})

# Weather API client for historical weather data
weatherApiClient = httpx.Client(base_url=os.getenv("WEATHERAPI_URL"), params={
    "key": os.getenv("WEATHERAPI_KEY")
})