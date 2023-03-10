# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling
# to solve this.💪

# Write your code below this line 👇

# greeting
print("Welcome to the tip calculator!")

# take str input and convert to float
bill = float(input("What was the total bill?: "))

# tip percentage
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))

# calculate total bill including tip
total_bill = bill + (bill * (tip / 100))

# split the bill equally
num_people = int(input("How many people to split the bill? "))
split_bill = round(total_bill / num_people, 2)

print(f"Each person should pay {split_bill}")
