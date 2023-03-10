# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# convert str input to int
age = int(age)

# calculate the no of years left
years_left = 90 - age

# calculate months, weeks and days left before user turns 90
months = years_left * 12
weeks = years_left * 52
days = years_left * 365

# result
print(f"You have {days} days, {weeks} weeks, and {months} months left.")
