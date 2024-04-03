import requests 
import json
import os
from dotenv import load_dotenv
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib



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
    
    # Create textfile content
    textfile_content = f"Duration: {duration}\nDistance: {distance}"
    textfile = "distance_duration_info.txt"  # Define your filename
    
    # Writing to a text file
    with open(textfile, 'w') as file:
        file.write(textfile_content)
    
    # Email Information

    subject = f"The contents of {textfile}"
    
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = to
    msg['Subject'] = subject
    
    # Attach the body with the msg instance
    msg.attach(MIMEText(textfile_content, 'plain'))
    
    # Open the file to be sent
    with open(textfile, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % textfile)
        
        # Attach the instance 'part' to instance 'msg'
        msg.attach(part)
    
    # Send the email
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender, password)
    text = msg.as_string()
    server.sendmail(sender, to, text)
    server.quit()
    
else:
    print("Error: ", response.status_code)