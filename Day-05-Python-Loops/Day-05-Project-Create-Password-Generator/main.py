"""Password Generator Project"""

import random

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

def main():
    """Program generates a random password"""

    print("Welcome to the PyPassword Generator!")

    nr_letters = int(
        input("How many letters would you like in your password?\n"))
    nr_symbols = int(input("How many symbols would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))

    # Initialize empty password
    password = ""

    for _ in range(nr_letters):
        password += random.choice(LETTERS)

    for _ in range(nr_numbers):
        password += random.choice(NUMBERS)

    for _ in range(nr_symbols):
        password += random.choice(SYMBOLS)

    # https://stackoverflow.com/questions/2668312/shuffle-string-in-python
    # To shuffle password first convert string to list
    password = list(password)
    random.shuffle(password)
    password = "".join(password)

    # Alternate method
    # password = "".join(random.sample(password, k=len(password)))

    # print password
    print(f"\nYour Password: {password}\n")


if __name__ == "__main__":
    main()
