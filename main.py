import requests 
import json
import os
from dotenv import load_dotenv
import time
import smtplib, ssl

load_dotenv()


api_key = os.environ.get('API_KEY')
destination = os.environ.get('destination')
origin = os.environ.get('origins')

url = "https://maps.googleapis.com/maps/api/distancematrix/json"

params = {
    'destinations': {destination},
'origins': {origin}, 
    'units': 'imperial',
    'key': api_key
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    duration = data['rows'][0]['elements'][0]['duration']['text']
    distance = data['rows'][0]['elements'][0]['distance']['text']
else:
    print("Error: ", response.status_code)


password = os.environ.get('PASSWORD')
port = 
