"""calculates the sum of all the even numbers from 1 to 100"""


def main():
    """calculates the sum of all the even numbers from 1 to 100"""
    sum_even = 0

    for num in range(1, 101):
        if num % 2 == 0:
            sum_even += num

    print(f"The sum of all the even numbers from 1 to 100 is {sum_even}.")


if __name__ == "__main__":
    main()
