import os
import requests
import json
import random

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

API_KEY = os.environ.get("REST_COUNTRIES_API_KEY")
headers = {
    "Authorization": f"Bearer {API_KEY}"
}

countries = {}
offset_num = random.randint(0,253)
response = requests.get(f"https://api.restcountries.com/countries/v5?limit=1&offset={offset_num}&pretty", headers=headers)
country = response.json()
print(country)


print("Welcome to the WORLD QUIZ")
print("---------------------------------------")
print("1. What country's capital is ")