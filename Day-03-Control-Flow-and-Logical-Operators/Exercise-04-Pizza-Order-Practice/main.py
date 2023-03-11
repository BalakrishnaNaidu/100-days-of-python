# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# Initialize prices

SMALL_PIZZA = 15
MEDIUM_PIZZA = 20
LARGE_PIZZA = 25

PEPPERONI_SMALL = 2
PEPPERONI_M_OR_L = 3

CHEESE = 1

# Small Pizza
if size.lower() == 's':

    if add_pepperoni.lower() == 'y':  # If Yes
        bill = SMALL_PIZZA + PEPPERONI_SMALL
    else:  # If No
        bill = SMALL_PIZZA

# Medium pizza
elif size.lower() == 'm':

    if add_pepperoni.lower() == 'y':  # If Yes
        bill = MEDIUM_PIZZA + PEPPERONI_M_OR_L
    else:  # If No
        bill = MEDIUM_PIZZA

# Large pizza
elif size.lower() == 'l':

    if add_pepperoni.lower() == 'y':  # If Yes
        bill = LARGE_PIZZA + PEPPERONI_M_OR_L
    else:  # If No
        bill = LARGE_PIZZA

if extra_cheese.lower() == 'y':
    bill += CHEESE

print(f"Your final bill is: ${bill}.")
