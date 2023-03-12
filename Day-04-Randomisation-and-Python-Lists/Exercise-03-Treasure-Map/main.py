"""Exercise 3 - Treasure Map"""


def main():
    """Exercise 3 - Treasure Map"""

    # 🚨 Don't change the code below 👇
    row1 = ["⬜️", "⬜️", "⬜️"]
    row2 = ["⬜️", "⬜️", "⬜️"]
    row3 = ["⬜️", "⬜️", "⬜️"]
    matrix = [row1, row2, row3]
    print(f"{row1}\n{row2}\n{row3}")
    position = input("Where do you want to put the treasure? ")
    # 🚨 Don't change the code above 👆

    # Write your code below this row 👇

    # column position
    col = int(position[0]) - 1
    # row position
    row = int(position[1]) - 1

    matrix[row][col] = 'X'

    # Write your code above this row 👆

    # 🚨 Don't change the code below 👇
    print(f"{row1}\n{row2}\n{row3}")


if __name__ == "__main__":
    main()
