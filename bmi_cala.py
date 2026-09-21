
input_weight = input("Enter your weight in kg: ")
input_height = input("Enter your height in meters: ")

try:
    weight = float(input_weight)
    height = float(input_height)
except ValueError:
    print("Invalid input for both weight and height. Please enter a numeric value.") 
    exit()
if weight <= 0 or height <= 0:
    print("Weight and height must be positive values. Please enter valid numbers.")
    exit()

bmi = weight / (height ** 2) 
if bmi < 18.5:
    category = "underweight"
elif bmi <= 24.9:
    category = "normal weight"
elif bmi <= 29.9:
    category = "overweight"
else:
    category = "obese"

print(f"Your BMI is: {round(bmi, 2)} and you are classified as {category}.")

