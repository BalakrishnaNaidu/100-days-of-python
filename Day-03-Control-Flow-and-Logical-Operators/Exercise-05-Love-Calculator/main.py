# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# Combine names
name = name1.lower() + name2.lower()

true_count = 0
love_count = 0

for char in "true":
    true_count += name.count(char)
for char in "love":
    love_count += name.count(char)

love_scores = str(true_count) + str(love_count)

if int(love_scores) < 10 or int(love_scores) > 90:
    print(
        f"Your score is {love_scores}, you go together like coke and mentos.")

elif 40 < int(love_scores) < 50:
    print(f"Your score is {love_scores}, you are alright together.")

else:
    print(f"Your score is {love_scores}.")
