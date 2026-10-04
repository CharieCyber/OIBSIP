# Basic Weather App

A python application that fetches and displays real-time weather data for a user specified location using the OpenWeatherMap API. Available as both a command-line version and a graphical version with icons, forecasts, and unit toggling.

## Features

### Beginner (CLI)

- Prompts for a city name, with validation for empty input
- Fetches real-time weather data from the OpenWeatherMap API
- Displays current temperature in both °C and °F
- Displays humidity, weather description, and wind speed
- Handles invalid city names (404) and network errors gracefully

### Advanced (GUI)

- Graphical interface with a city input field, "Get Weather" button, and results panel
- Displays a live weather icon matching current conditions
- Hourly forecast showing the next 6 hours
- Daily forecast showing the next 5 days
- Celsius / Fahrenheit unit toggle
- Error messages shown inside the GUI, not the terminal

## Requirements

- Python 3.x
- requests (`pip install requests`)
- tkinter (comes built-in with Python — no install needed)
- Pillow (`pip install pillow` — needed for displaying weather icons in the GUI version)
- An OpenWeatherMap API key (free tier available at [openweathermap.org](https://openweathermap.org/))

## API Key Setup

This project requires a free OpenWeatherMap API key to function.

1. Sign up for a free account at [openweathermap.org](https://openweathermap.org/) and get your API key from "My API Keys" in your account dashboard
2. Copy `config_example.py` and rename the copy to `config.py`
3. Open `config.py` and replace the placeholder with your actual API key:

```python
   API_KEY = "your_actual_api_key_here"
```

1. Run the app as normal — see "How to Run" below

**Note:** `config.py` is excluded via `.gitignore` and not included in this repository, since it would contain a real API key. `config_example.py` is provided as a template showing the expected format.

## How to Run

1. Make sure Python is installed on your system
2. Install the required libraries:

```bash
pip install requests pillow
```

3.Complete the API Key Setup above before running either version

4.Run either version from your terminal:

```bash
python weather_app.py        # Beginner CLI version
python weather_app_gui.py    # Advanced GUI version
```

## Screenshots

**CLI version:**
![Weather App CLI output]("C:\Users\Dell\Documents\Internship projects\weather app\Screenshots\CLI Output.png")

**GUI version:**
![Weather App GUI result]("C:\Users\Dell\Documents\Internship projects\weather app\Screenshots\Weather App GUI Output.png")
