# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲

import random


def main():
    """ Heads or Tails"""

    toss = random.randint(0, 1)

    # 1 means Heads 0 means Tails
    result = "Heads" if toss == 1 else "Tails"

    print(result)


if __name__ == "__main__":
    main()
