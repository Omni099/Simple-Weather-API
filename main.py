import datetime as dt
#to take time stamps and parse them into human readable formula
import requests
import tkinter as tk
#not part of core python stack

#used to send requests to send requests to api
#specify url 

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

API_KEY = ""
CITY = "Sydney"

def Kelvin_to_Celsius_Fahrenheit(kelvin):
    #given kelvin
    celsius = kelvin - 273.15
    fahrenheit = celsius*(9/5) + 32
    return celsius, fahrenheit
    #converts units

def clear():
    text_field.delete(1.0, "end")
    text_field.insert(1.0, "")

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
#'&' used to combine paramater
#q is the city we are looking for
response = requests.get(url).json()
#in order to send requests

temp_kelvin = response['main']['temp']
#key was main #dictionary was temp

temp_celsius, temp_fahrenheit = Kelvin_to_Celsius_Fahrenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = Kelvin_to_Celsius_Fahrenheit(feels_like_kelvin)
humidity = response['main']['humidity']
wind_speed = response['wind']['speed']


description = response['weather'][0]['description']
#list of dictionaries in it

sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone']) #to get local time
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone']) #to get local time


print(f"Temperature in {CITY}: {temp_celsius:.2f} Celsius or {temp_fahrenheit:.2f} fahrenheit")
print(f"Temperature in {CITY} feels like: {feels_like_celsius:.2f} Celsius or {feels_like_fahrenheit:.2f} Fahrenheit")
print(f"Humidity in {CITY}: {humidity}%")
print(f"General weather in {CITY} is: {description}")

