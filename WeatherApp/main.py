import requests
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import io

API_KEY = ""

def setup_window(): 
    
    root = tk.Tk()
    root.title("Weather App")
    root.configure(bg="#a3c0e0")
    root.geometry("500x500")

    entry_city = tk.Entry(root, font = "Helvetica, 18", fg="#627099", bg="#eff2fa") 
    entry_city.pack(pady=10)

    # Search button
    button = tk.Button(root, text="Search", command=lambda: get_weather(entry_city, label_results, label_icon, label_city_name), 
                       bg="#ff8e4c", fg="white", font=("Helvetica", 12), justify="left", width=7, height=1)
    button.pack(pady=10)

    #Label to show the city name
    label_city_name = tk.Label(root, text="", font=("Arial", 20, "bold"), bg="#a3c0e0", fg="#eff2fa")
    label_city_name.pack(pady=5)

    # Label to show the weather icon
    label_icon = tk.Label(root, bg="#a3c0e0")
    label_icon.pack(pady=5)

    #Label to show details (temperature, description and date)
    label_results = tk.Label(root, text="", font=("Arial", 17))
    label_results.configure(bg="#a3c0e0", fg="#eff2fa")
    label_results.pack(pady=5)

    return root

def get_weather(entry_city, label_results, label_icon, label_city_name):

    city = entry_city.get()
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

    try:
        response = requests.get(url)
    
        if response.status_code == 200:
            data = response.json()

            main = data['main']
            weather = data['weather'][0]
            country = data['sys']['country']

            temperature = main['temp']
            icon_code = weather['icon']  # Icon code for weather condition
            weather_description = weather['description']

            current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

            print_city_name = (f"{city.capitalize()}, {country}\n")
            label_city_name.config(text = print_city_name)

            # Fetch the icon image
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
            icon_response = requests.get(icon_url)
            icon_data = icon_response.content
            icon_image = Image.open(io.BytesIO(icon_data))
            icon_photo = ImageTk.PhotoImage(icon_image)
            label_icon.config(image=icon_photo)
            label_icon.image = icon_photo 

            details = (
                        f"Temperature: {temperature}°C\n"
                        f"Description: {weather_description.capitalize()}\n\n"
                        f"Data Retrieved at {current_time}")
            label_results.config(text=details)

        else:
            messagebox.showerror("Error", "City not found.") 

    except requests.exceptions.RequestException:
            messagebox.showerror("Error", "Unable to retrieve weather data. Check your internet connection.")

root = setup_window()
root.mainloop()