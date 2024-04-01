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


def send_email():
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = os.environ.get('sender_email')  # Enter your address
    receiver_email = os.environ.get('receiver_email')  # Enter receiver address
    password = os.environ.get('password')
    message = f"""\
    Subject: Distance and Time

    The distance between the two locations is {distance} and the time taken to travel is {duration}."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
