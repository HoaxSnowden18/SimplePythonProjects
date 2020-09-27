from urllib.request import urlopen
import json
import datetime

API = "d651f7a4caa1d8e01f1687fc34a352a5"

userCity = input('Enter your city: ')

with urlopen(f'https://api.openweathermap.org/data/2.5/weather?q={userCity}&appid={API}') as response:
    source = response.read()

data = json.loads(source)


def kelvinToCelsius(kel):
    return "{:.2f}".format(kel - 273.15)


def showResult(data):
    country = data['sys']['country']
    cityName = data['name']
    timezone = data['timezone']
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    cloudPCT = data['clouds']['all']
    Desc = data['weather'][0]['description']
    sunrise = data['sys']['sunrise']
    sunset = data['sys']['sunset']
    windDegree = data['wind']['deg']
    windSpeed = data['wind']['speed']
    airPressure = data['main']['pressure']
    humidity = data['main']['humidity']
    feelslike = data['main']['feels_like']
    temp = data['main']['temp']
    maxTemp = data['main']['temp_max']
    minTemp = data['main']['temp_min']
    date = data["dt"]

    print(f"Weather Status in {cityName}:")
    print(f"Country: {country}")
    print(f"City Name: {cityName}")
    print(f"Date: {datetime.datetime.fromtimestamp(date).strftime('%Y-%m-%d')}")
    print(f"Timezone: {int(timezone / 3600)} hours")
    print(f"Geographic Coordinates: {latitude}, {longitude}")
    print(f"Clouds : {cloudPCT}%")
    print(f"Weather Description: {Desc.title()}")
    print(f"Sunrise: {datetime.datetime.fromtimestamp(sunrise)} ")
    print(f"Sunset: {datetime.datetime.fromtimestamp(sunset)}\n\n")

    print("Wind and Air:")
    print(f"Wind Degree: {windDegree}°")
    print(f"Wind Speed: {windSpeed}m/s")
    print(f"Air Pressure: {airPressure}hpa")
    print(f"Humidity: {humidity}%\n\n")

    print("Temperature:")
    print(f"Feels Like: {kelvinToCelsius(feelslike)}°C")
    print(f"Temperature: {kelvinToCelsius(temp)}°C")
    print(f"Max Temperature: {kelvinToCelsius(maxTemp)}°C")
    print(f"Min Temperature: {kelvinToCelsius(minTemp)}°C")


showResult(data)
