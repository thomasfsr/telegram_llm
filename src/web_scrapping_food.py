import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

key = os.getenv('nutrition_ix_key')
app_id = os.getenv('app_id')

url_food = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
url_train = 'https://trackapi.nutritionix.com/v2/natural/exercise'

headers = {
    'Content-Type': 'application/json',
    'x-app-id': app_id, 
    'x-app-key': key 
}

data = {
    "query": "arroz",
    # "timezone": "US/Eastern"
}

response = requests.post(url_food, headers=headers, json=data)

data = response.json()['foods'][0]
selected_data = {key: data[key] for key in [
    "food_name",
    "serving_qty",
    "serving_unit",
    "serving_weight_grams",
    "nf_calories",
    "nf_total_fat",
    "nf_saturated_fat",
    "nf_cholesterol",
    "nf_sodium",
    "nf_total_carbohydrate",
    "nf_dietary_fiber",
    "nf_sugars",
    "nf_protein",
    "nf_potassium"
]}
print(json.dumps(selected_data, indent=2))

