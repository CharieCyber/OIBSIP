import requests
from config import API_KEY

city = input("Enter city name: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
if not city.strip():
    print("City name cannot be empty.")
else:
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        print("Network error. Please check your internet connection.")
        exit()

    if response.status_code == 200:
        data = response.json()
        temp_c = data['main']['temp']
        temp_f = (temp_c * 9 / 5) + 32
        print(f"Temperature in {city}: {temp_c}°C ({temp_f}°F)")
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        print(f"Humidity in {city}: {humidity}%")
        print(f"Description in {city}: {description}")
        print(f"Wind Speed in {city}: {wind_speed} m/s")

    elif response.status_code == 404:
        print("City not found. Please check the spelling and try again.")
    else:
        print("Error fetching weather data.")


    