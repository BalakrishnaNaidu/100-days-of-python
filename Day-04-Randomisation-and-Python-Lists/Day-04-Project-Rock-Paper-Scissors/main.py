""" Rock Paper Scissors"""

import random

ROCK = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

PAPER = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

SCISSORS = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
emoji = [ROCK, PAPER, SCISSORS]


def main():
    """ Rock Paper Scissors """

    # 0 for Rock, 1 for Paper or 2 for Scissors.

    choice = [0, 1, 2]
    print("Welcome to Rock Paper Scissors!!!")

    # Start the game by asking the player
    user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper"
                           " or 2 for Scissors: "))

    if user_input in choice:
        # Randomly choose computer input
        computer_input = random.choice(choice)
        game(user_input, computer_input)

    else:
        print("Invalid input!")

        # Ask user if they want to play again?
        play_again = input("Do you want to play again? "
                           "Type 'Y|y' to play again and Type anykey to Quit: ")

        if play_again.lower() == 'y':
            main()


def game(user, computer):
    """ Predicts the outcome of the game
        * Rock wins against scissors.
        * Scissors win against paper.
        * Paper wins against rock.
    """

    name = ["Rock", "Paper", "Scissors"]

    if user == computer:
        print_output(name, user, computer)
        print("It's a Draw!")

    elif user == 0 and computer == 2:
        print_output(name, user, computer)
        print("You Win!!")

    elif user == 2 and computer == 1:
        print_output(name, user, computer)
        print("You Win!!")

    elif user == 1 and computer == 0:
        print_output(name, user, computer)
        print("You Win!!")

    else:
        print_output(name, user, computer)
        print("You Lose!!")


def print_output(lst, user_input, comp_input):
    """Prints emojis related to chosen input"""

    print(f"\nYou chose {lst[user_input]}.")
    print(emoji[user_input])
    print(f"\nComputer chose {lst[comp_input]}.")
    print(emoji[comp_input])


if __name__ == "__main__":
    main()
