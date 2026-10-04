import tkinter as tk
from tkinter import messagebox
import PIL
import requests
from config import API_KEY
import io
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Weather App")
label = tk.Label(root, text="Enter city name:")
label.pack()

current_unit = "metric"

city_entry = tk.Entry(root)
city_entry.pack()

result_label = tk.Label(root, text="", justify="left")
result_label.pack()

icon_label = tk.Label(root)
icon_label.pack()

hourly_label = tk.Label(root, text="", justify="left")
hourly_label.pack()

daily_label = tk.Label(root, text="", justify="left")
daily_label.pack()

def get_weather():
    city = city_entry.get()
    if not city.strip():
        messagebox.showerror("Error", "City name cannot be empty.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={current_unit}"
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Network error. Please check your internet connection.")
        return
    
    if response.status_code == 200:
        data = response.json()
        temp = round(data['main']['temp'], 2)
        unit_symbol = "°C" if current_unit == "metric" else "°F"
        humidity = round(data['main']['humidity'], 2)
        description = data['weather'][0]['description']
        wind_speed = round(data['wind']['speed'], 2)
        icon_code = data['weather'][0]['icon']
        icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
        print(f"Icon code: {icon_code}")
        print(f"Icon URL: {icon_url}")
        icon_response = requests.get(icon_url)
        print(f"Icon response status: {icon_response.status_code}")
        image_data = icon_response.content
        image = Image.open(io.BytesIO(image_data))
        photo = ImageTk.PhotoImage(image)
        icon_label.config(image=photo)
        icon_label.image = photo
        result_text = f"Temperature in {city}: {temp}{unit_symbol}\nHumidity: {humidity}%\nDescription: {description}\nWind Speed: {wind_speed} m/s"
        result_label.config(text=result_text)

        forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
        forecast_response = requests.get(forecast_url)
        if forecast_response.status_code == 200:
            forecast_data = forecast_response.json()
            hourly_text = "Hourly Forecast:\n"
            for item in forecast_data['list'][:2]:  # Display next 5 forecasts
                time_str = item['dt_txt'].split(' ')[1][:5]  # Get time part
                temp = round(item['main']['temp'], 2)
                description = item['weather'][0]['description']
                hourly_text += f"- {time_str}, {temp}{unit_symbol}, {description}\n"
            hourly_label.config(text=hourly_text)
            daily_forecasts = {}
            for entry in forecast_data['list']:
                date = entry['dt_txt'].split(' ')[0]
                time = entry['dt_txt'].split(' ')[1]
                if time == "12:00:00":
                    daily_forecasts[date] = entry

            daily_text = "Next 5 Days:\n"
            for date, entry in daily_forecasts.items():
                temp = round(entry['main']['temp'], 1)
                description = entry['weather'][0]['description']
                daily_text += f"- {date}: {temp}{unit_symbol}, {description}\n"
            daily_label.config(text=daily_text)

    elif response.status_code == 404:
        messagebox.showerror("Error", "City not found. Please check the spelling and try again.")
        
    else:
        messagebox.showerror("Error", "Error fetching weather data.")

unit_button = tk.Button(root, text="Switch to °F")

def toggle_unit():
    global current_unit
    if current_unit == "metric":
        current_unit = "imperial"
        unit_button.config(text="Switch to °C")
    else:
        current_unit = "metric"
        unit_button.config(text="Switch to °F")
    get_weather()


weather_button = tk.Button(root, text="Get Weather", command=get_weather)
weather_button.pack()

unit_button = tk.Button(root, text="Switch to °F", command=toggle_unit)
unit_button.pack()


root.mainloop()
