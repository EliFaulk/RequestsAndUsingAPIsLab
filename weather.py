import requests
import json

cities = {
    "New York":     {"latitude": 40.7128,  "longitude": -74.0060},
    "London":       {"latitude": 51.5074,  "longitude": -0.1278},
    "Tokyo":        {"latitude": 35.6762,  "longitude": 139.6503},
    "Sydney":       {"latitude": -33.8688, "longitude": 151.2093},
    "Cairo":        {"latitude": 30.0444,  "longitude": 31.2357},
    "São Paulo":    {"latitude": -23.5505, "longitude": -46.6333},
    "Mumbai":       {"latitude": 19.0760,  "longitude": 72.8777},
    "Cape Town":    {"latitude": -33.9249, "longitude": 18.4241},
    "Paris":        {"latitude": 48.8566,  "longitude": 2.3522},
    "Mexico City":  {"latitude": 19.4326,  "longitude": -99.1332},
    "Moscow":       {"latitude": 55.7558,  "longitude": 37.6173},
    "Singapore":    {"latitude": 1.3521,   "longitude": 103.8198},
    "Buenos Aires": {"latitude": -34.6037, "longitude": -58.3816},
    "Nairobi":      {"latitude": -1.2921,  "longitude": 36.8219},
    "Denver":       {"latitude": 39.7392,  "longitude": -104.9903},
}

weather_codes = {
	"0": "Clear sky",
	"1": "Mainly clear",
	"2": "Partly cloudy",
	"3": "Overcast",
	"45": "Fog",
	"48": "Depositing rime fog",
	"51": "Light drizzle",
	"53": "Moderate drizzle",
	"55": "Dense drizzle",
	"56": "Light freezing drizzle",
	"57": "Dense freezing drizzle",
	"61": "Slight rain",
	"63": "Moderate rain",
	"65": "Heavy rain",
	"66": "Light freezing rain",
	"67": "Heavy freezing rain",
	"71": "Slight snowfall",
	"73": "Moderate snowfall",
	"75": "Heavy snowfall",
	"77": "Snow grains",
	"80": "Slight rain showers",
	"81": "Moderate rain showers",
	"82": "Violent rain showers",
	"85": "Slight snow showers",
	"86": "Heavy snow showers",
	"95": "Thunderstorm",
	"96": "Thunderstorm with slight hail",
	"97": "Heavy thunderstorm",
	"99": "Thunderstorm with heavy hail"
}


# Get user input of city (for latitude and longitude) and date
while True:
    city = input("Enter a city: ")
    if city in cities:
        break;
    print("Invalid city.")
date = input("Enter a date: ")
print("------------------------------------------------")

latitude = cities[city]["latitude"]
longitude = cities[city]["longitude"]


# Get request to weather API
response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={date}&end_date={date}&daily=weather_code&daily=apparent_temperature_max&daily=apparent_temperature_min&daily=precipitation_sum&daily=wind_speed_10m_max")
forecast = response.json()
print(forecast)

print("""
conditions: {forecast["daily"]}
""")