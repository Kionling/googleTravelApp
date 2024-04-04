# Google Matrix API Travel App
Automating our daily commute information enables the user to schedule and organize their life more efficiently. This application uses the Google Matrix API to obtain distance and duration information on a set route. The application then send that information via email to the user at the same time everyday. This application is useful for someone who commutes to work often and wants to know their commute conditions at a specific moment of the day, everyday. 


# Technologies 
* Python 
* Google Matrix API 
* Redmail 
* python-scheduler
* python-time
* dotenv
* requests 
* os

# Code Snippet
Redmail Gmail setup 
```
gmail.send(
    subject='Hello, World!',
    receivers=[to],
    text="duration: " + duration + " distance: " + distance
)

```
Google Matrix Query
```
arams = {
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

```


# Author
* (Daniel Jauregui)[https://kionling.herokuapp.com]

# Acknowledgements 
* Redmail
* Google Matrix API

