import random
import string

length_input = input("Enter the length of desired password: ")

try:
    length = int(length_input)
except ValueError:
    print("Please enter a valid number.")
    exit()

if length < 8:
    print("password length must be at least 8 characters")  
    exit()  

include_upper = input("Include uppercase letters? (y/n): ") 
include_upper = include_upper.lower() == "y"

include_lower = input("Include lowercase letters? (y/n): ")
include_lower = include_lower.lower() == "y"

include_digits = input("Include numbers? (y/n): ")
include_digits = include_digits.lower() == "y"

include_symbols = input("Include symbols? (y/n): ")
include_symbols = include_symbols.lower() == "y"

character_pool = ""

if include_upper:
    character_pool += string.ascii_uppercase

if include_lower:
    character_pool += string.ascii_lowercase

if include_digits:
    character_pool += string.digits

if include_symbols:
    character_pool += string.punctuation

selected_count = sum([include_upper, include_lower, include_digits, include_symbols])

if selected_count < 2:
    print("please select at least 2 character types.")
    exit()

password = ''.join(random.choice(character_pool) for _ in range(length))
print(password)
print(len(password))

while True:
    length_input = input("Enter desired password length: ")
    print(password)

    again = input("Generate another password? (y/n): ")
    if again.lower() != "y":
        break



























