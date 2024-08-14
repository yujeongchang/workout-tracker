import requests
from datetime import datetime
import os
os.environ['APP_ID'] = "e4df7ace"
APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']

WEIGHT_KG = 53
HEIGHT_CM = 163
AGE = 25

NL_FOR_EXR_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = os.environ['SHEET_ENDPOINT']

SHEETY_TOKEN = {
    "Authorization": f"Bearer {os.environ['TOKEN']}"
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exr_data = {
    "query": input("Tell me which exercised you did: "),
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=NL_FOR_EXR_ENDPOINT, json=exr_data, headers=headers)
# data = response.json()["exercises"][0]
data = response.json()["exercises"]

## time = 입력 시간 혹은 (입력 시간 - duration 시간)?
today = datetime.now()
date = today.strftime("%m/%d/%Y")
time = today.strftime("%H:%M:%S")

for exercise in data:
    duration = exercise["duration_min"]
    exercise_name = exercise["name"].title()
    calories = exercise["nf_calories"]

    add_data = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise_name,
            "duration": duration,
            "calories": calories,
        }
    }

    response = requests.post(
        url=SHEETY_ENDPOINT,
        json=add_data,
        headers=SHEETY_TOKEN)
    print(response.text)