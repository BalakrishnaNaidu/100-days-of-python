# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# convert str input to float
weight_float = float(weight)
height_float = float(height)

# BMI = Weight / (Height^2)
bmi = weight_float / (height_float ** 2)

# round the result to int
bmi = int(bmi)

# print the result
print(bmi)
