import requests
import json
from pynput.keyboard import Key, Controller
import time
from datetime import datetime
import pandas as pd
import numpy as np

df = pd.read_csv("c.csv")  # Drops the columns that keep generating randomly
df.drop(columns="Unnamed: 0.1", inplace=True)
df.drop(columns="Unnamed: 0", inplace=True)

api_key = ""  # Go to openweathermap.org, sign up and get an API key.
# data1 = open("Data.txt", "r+")
i = 1

while i <= 4:  # Makes the program run 4 times, or 4 intervals
    i += 1
    keyboard = Controller()
    now = datetime.now()  # Gets the current time
    d = np.random.randint(0, 824)  # Makes the random row number to get
    get_row = df.loc[[d]]  # Gets the row based on the random number
    row = np.array(get_row)  # Makes it easier for us to access the row values

    # Accesses and defines the row values
    place = row[0][0]
    lat = row[0][1]
    lon = row[0][2]
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=imperial" % (lat, lon, api_key)
    hour = now.strftime("%I")

    if hour[0] == "0":  # Makes the twelve hour time format correct by removing the 0
        hour = hour[1:]

    ct = now.strftime(f'%m/%d/%Y- {hour}:%M:%S %p CST')  # The time string stored in a variable

    response = requests.get(url)
    data = json.loads(response.text)

    # Accesses the values in the massive dictionary from the API and defines them to a variable
    humidity = data['current']['humidity']
    feel_like = data['current']['feels_like']
    description = data['current']['weather'][0]["description"]
    current = data['current']['temp']
    wind_speed = data['current']['wind_speed']
    # feel_like2 = int(feel_like * 1.8) + 32  # Converts the celsius to Fahrenheit, but I changed it to imperial
    # current2 = int(current * 1.8) + 32 # Converts the celsius to Fahrenheit, but I changed it to imperial
    # ---------------------------------------------------------------------------------------------------------------
    # The complete concatenated message
    c = f"{ct}: It is {round(current, 1)}°F outside in {place}. It feels like {round(feel_like, 1)}°F. Humidity is at {humidity}%. The wind is blowing at {wind_speed}mph. The weather description: {description.upper()} "
    # data1.write(c)
    # data1.write("\n")
    keyboard.type(c)  # Types the message
    keyboard.press(Key.enter)  # sends the message/types it on a newline

    if i > 4:  # Allows the program to end without delay. really its optional
        pass
    else:
        time.sleep(10)  # Delay. You can change it to any amount of seconds you want