import requests
import json
import time
from datetime import datetime
import pandas as pd
import numpy as np
import os

current_directory = os.getcwd()

# Changes directory to where the dataset is located
os.chdir(current_directory[:len(current_directory)-len("type-to-txt")])

df = pd.read_csv("city-coordinates.csv")  # Drops the columns that keep generating randomly
df.drop(columns="Unnamed: 0.1", inplace=True)
df.drop(columns="Unnamed: 0", inplace=True)

# Brings it back to the original directory
os.chdir("type-to-txt")
api_key = ""  # Go to openweathermap.org, sign up and get an API key.
data1 = open("Data.txt", "r+")
i = 1

while i <= 40:  # Makes the program run 40 times
    i += 1
    now = datetime.now()
    d = np.random.randint(0, 824)  # Makes the random row number to get
    get_row = df.loc[[d]]  # Gets the row based on the random number
    row = np.array(get_row)  # Makes it easier for us to access the row values

    # Accesses and defines the row values
    place = row[0][0]
    lat = row[0][1]
    lon = row[0][2]
    url = "https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s&units=imperial" % (lat, lon, api_key)
    hour = now.strftime("%I")

    if hour[0] == "0":  # Makes the twelve-hour time format correct by removing the 0
        hour = hour[1:]

    ct = now.strftime(f'%m/%d/%Y- {hour}:%M:%S %p CST')  # The time string stored in a variable

    response = requests.get(url)
    data = json.loads(response.text)

    # Accesses the values in the massive dictionary from the API and defines them to a variable

    humidity = data["main"]["humidity"]

    feel_like = data['main']["feels_like"]

    description = data["weather"][0]["description"]

    current = data['main']['temp']

    wind_speed = data['wind']['speed']

    c = f"{ct}: It is {round(current, 1)}°F outside in {place}. It feels like {round(feel_like, 1)}°F. Humidity is at {humidity}%. The wind is blowing at {wind_speed}mph. The weather description: {description.upper()} "
    data1.write(f"{c}\n")
    data1.write("\n")

    if i > 4:  # Allows the program to end without delay. really its optional
        pass
    else:
        time.sleep(30)  # Delay. You can change it to any amount of seconds you want
data1.close()
