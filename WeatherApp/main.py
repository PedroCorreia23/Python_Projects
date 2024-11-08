import requests
from datetime import datetime

API_KEY = "#"

city = "Lisbon"
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

current_time = datetime.now()
formatted_time = current_time.strftime('%d-%m-%Y %H:%M:%S')

def get_weather():

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()

        main = data['main']
        weather = data['weather'][0]

        temperature = main['temp']
        feels_like = main['feels_like']
        humidity = main['humidity']
        weather_description = weather['description']

        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Feels Like: {feels_like}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_description.capitalize()}")
        print()
        print(formatted_time)

get_weather()


