import requests 
import json
import os
from dotenv import load_dotenv
import time
from redmail import EmailSender
from redmail import gmail


load_dotenv()

api_key = os.environ.get('API_KEY')
destination = os.environ.get('destination')
origin = os.environ.get('origins')
sender = os.environ.get('from')
to = os.environ.get('to')
password = os.environ.get('PASSWORD')
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
    print(duration, distance)
else:
    print("Error: ", response.status_code)


gmail.username = sender # Your Gmail address
gmail.password = password

# And then you can send emails
gmail.send(
    subject='Hello, World!',
    receivers=[to],
    text="duration: " + duration + " distance: " + distance
)

