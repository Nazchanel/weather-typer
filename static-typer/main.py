import requests
import json
from pynput.keyboard import Key, Controller
import time
from datetime import datetime
import input

api_key = ""  # Go to openweathermap.org, sign up and get an API key.

# Enter your city coordinates here.
lat = input.lat
lon = input.lon
url = "https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s&units=imperial" % (lat, lon, api_key)
i = 1

# NO FILES NEEDED, unlike the other one
while i <= 825:  # Makes the program run 4 times, or 4 intervals
    i += 1
    keyboard = Controller()
    now = datetime.now()  # Gets the current time
    hour = now.strftime("%I")
    if hour[0] == "0":  # Makes the twelve-hour time format correct by removing the 0
        hour = hour[1:]
    ct = now.strftime(f'%m/%d/%Y- {hour}:%M:%S %p CST')  # The time string stored in a variable
    response = requests.get(url)
    data = json.loads(response.text)

    humidity = data["main"]["humidity"]

    print(f"{humidity}% humidity\n")

    feel_like = data['main']["feels_like"]

    print(f"{feel_like}\n")

    description = data["weather"][0]["description"]

    print(f"{description}\n")

    current = data['main']['temp']

    print(f"{current}\n")

    wind_speed = data['wind']['speed']

    print(f"{wind_speed}\n")
    # feel_like2 = int(feel_like * 1.8) + 32  # Converts the celsius to Fahrenheit, but I changed it to imperial
    # current2 = int(current * 1.8) + 32 # Converts the celsius to Fahrenheit, but I changed it to imperial
    # ---------------------------------------------------------------------------------------------------------------
    # The complete concatenated message
    c = f"{ct}: It is {round(current, 1)}°F outside in Dallas, TX. It feels like {round(feel_like, 1)}°F. Humidity is at {humidity}%. The weather description: {description.upper()}"
    keyboard.type(c)
    keyboard.press(Key.enter)  # sends the message/types it on a newline
    if i > 4:  # Allows the program to end without delay. tbh its optional
        pass
    else:
        time.sleep(1800)  # Delay. You can change it to any amount of seconds you want
