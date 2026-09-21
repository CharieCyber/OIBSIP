# BMI Calculator

 A Python tool that calculates Body Mass Index and classifies it into health categories, available as both a command-line version and a GUI version with history tracking

## Features

### Beginner (CLI)

- Prompts user for weight and height via command line
- Calculates BMI using the standard formula
- Classifies result into Underweight / Normal / Overweight / Obese
- Rejects invalid input (non-numeric or negative values) with an error message

### Advanced (GUI)

- Graphical interface built with tkinter
- Colour-coded result display based on BMI category
- Saves each calculation to a SQLite database, tracked per user name
- "Show BMI Trend" button plots a user's BMI history over time using matplotlib
- Handles database errors gracefully with popup messages

## Requirements

- Python 3.x
- tkinter (comes built-in with Python — no install needed)
- sqlite3 (comes built-in with Python — no install needed)
- matplotlib (`pip install matplotlib`)

## How to Run

1. Make sure Python is installed on your system
2. Install the required library:

```bash
pip install matplotlib
```

1. Run either version from your terminal:

```bash
python bmi_cala.py        # Beginner CLI version
python bmi_calc_gui.py    # Advanced GUI version
```
