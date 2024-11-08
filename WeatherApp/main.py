import requests
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

API_KEY = ""

def setup_window(): 
    
    root = tk.Tk()
    root.title("Weather App")
    root.geometry("500x500")

    label_city = tk.Label(root, text="Enter city: ")
    label_city.pack(pady=5)
    entry_city = tk.Entry(root) 
    entry_city.pack(pady=5)

    #Show results 
    label_results = tk.Label(root, text="", font=("Arial", 12), justify="left")
    label_results.pack(pady=20)

    # Search button
    button = tk.Button(root, text="Search", command=lambda: get_weather(entry_city, label_results), fg="black")
    button.pack()

    return root


def get_weather(entry_city, label_results):

    city = entry_city.get()
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

    try:
        response = requests.get(url)
    
        if response.status_code == 200:
            data = response.json()

            main = data['main']
            weather = data['weather'][0]

            temperature = main['temp']
            feels_like = main['feels_like']
            humidity = main['humidity']
            weather_description = weather['description']

            current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

            result_text = (f"City: {city}\n"
                           f"Temperature: {temperature}°C\n"
                           f"Feels Like: {feels_like}°C\n"
                           f"Humidity: {humidity}%\n"
                           f"Description: {weather_description.capitalize()}\n\n"
                           f"Data Retrieved at {current_time}")
            label_results.config(text = result_text)

        else:
            messagebox.showerror("Error", "City not found.") 

    except requests.exceptions.RequestException:
            messagebox.showerror("Error", "Unable to retrieve weather data. Check your internet connection.")

root = setup_window()
root.mainloop()

