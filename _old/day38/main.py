import requests
import os
from datetime import datetime

APP_ID = "001251e3"
APP_KEY = "9c1536d37660546f53e5a7daf20ffc50"

API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/e85d510898a29ca6ac9acc32538c6bb0/yo/sheet1"

QUERY = input("Enter a query: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

param = {
    "weight_kg": 80,
    "height_cm": 180,
    "age": 27,
    "query": QUERY
}

# date time and format
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# NutritionX NLP
response = requests.post(API_ENDPOINT, headers=headers, json=param)
res = response.json()

# Sheety Call & Auth.
GOOGLE_SHEET = "sheet1"
for ex in res['exercises']:
    sheety_inputs = {
        GOOGLE_SHEET: {
            "date": today_date,
            "time": now_time,
            "exercise": ex['name'].title(),
            "duration": ex['duration_min'],
            "calories": ex['nf_calories']
        }
    }
    sheety_res = requests.post(SHEETY_ENDPOINT, json=sheety_inputs)
    print(sheety_res.text)
