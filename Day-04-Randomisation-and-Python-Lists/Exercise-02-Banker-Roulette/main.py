""" Exercise 2 - Banker Roulette"""

import random


def main():
    """ Exercise 2 - Banker Roulette"""

    # Split string method
    names_string = input("Give me everybody's names, separated by a comma. ")
    names = names_string.split(", ")
    # 🚨 Don't change the code above 👆

    # Write your code below this line 👇

    # Pick a random index number using randint()
    random_index = random.randint(0, len(names)-1)
    random_name = names[random_index]

    # Can be done in 1 step using random.choice(seq)
    #random_name = random.choice(names)
    print(f"{random_name} is going to buy the meal today!")


if __name__ == "__main__":
    main()
