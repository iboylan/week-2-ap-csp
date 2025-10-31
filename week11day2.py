# open up the vscode from previous day
# create a new file called: week11_day1.py
# ----------------------------------------
# Day 2 Review Activity: My Personal Info Generator
# ----------------------------------------

# print(" Welcome to the Python Review Activity!")
# print("You’ll review variables, strings, numbers, and print formatting.\n")

# Step 1: Create Variables
# TODO: Replace the values below with your own info
first_name = "Izzy"
age = 15
favorite_color = "Purple"
favorite_number = 4

#  Step 2: Practice String Operations
# 1. Print your name in uppercase
print(first_name.upper())

# 2. Print how many letters are in your name
print(len(first_name))

# 3. Combine your name and favorite color into one message
print(f"{first_name}, {favorite_color}")

#  Step 3: Math Practice
# Use arithmetic operators with your favorite number
numresult = favorite_number ** 2
print(f"{favorite_number} to the power of 2: {numresult}")

#  Step 4: User Input Practice
# Ask the user two questions and combine answers
ans1 = int(input("What's your favorite number?:   "))
ans2 = int(input("What's your 2nd favorite number?:   "))
theexponenterrr = ans1 ** ans2
print(f"{ans1} to the power of {ans2} is {theexponenterrr}.")

# ⚙️ Step 5: Final Challenge (combine it all)
# Use math and strings together
month = input("What month were you born in? (name):   ")
day = int(input("What day were you born on?:   "))
daytrillion = day ** 3
print(f"You were born on {month} {day}. {day} to the power of 3 is {daytrillion}.")