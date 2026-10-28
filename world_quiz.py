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


countries = []
capitals = []
for i in range(5):
    offset_num = random.randint(0,253)
    response = requests.get(
        "https://api.restcountries.com/countries/v5?",
        headers={"Authorization": f"Bearer {API_KEY}"},
        params={"limit": 1, "offset": offset_num}
    )
    country = response.json()
    name = country["data"]["objects"][0]["names"]["common"]
    capital = country["data"]["objects"][0]["capitals"][0]["name"]
    countries.append(name)
    capitals.append(capital)


score = 0
print("Welcome to the WORLD QUIZ")
print("---------------------------------------")
for i in range(5):
    print(f"{i+1}. What country's capital is {capitals[i]}?")
    answer = input("Answer: ")
    if answer.lower().strip() == countries[i].lower().strip():
        score += 1
        print("Correct!\n")
    else:
        print(f"Incorrect. The country was {countries[i]}.\n")
print(f"You answered {score}/5 correctly!")
